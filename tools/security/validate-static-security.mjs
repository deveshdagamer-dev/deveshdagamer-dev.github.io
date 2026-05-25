import { readdir, readFile } from "node:fs/promises";
import path from "node:path";

const ROOT = process.cwd();
const SITE = "https://deveshbinwal.com";
const PUBLIC_PAGES = [
  "",
  "research.html",
  "publications.html",
  "highlights.html",
  "gallery.html",
  "news.html",
  "contact.html",
];

const IGNORED_DIRS = new Set([".git", "node_modules", "public", ".cache", ".netlify"]);
const IGNORED_PATH_PARTS = [
  ["resources", "_gen"],
];
const TEXT_EXTENSIONS = new Set([
  ".css",
  ".html",
  ".js",
  ".json",
  ".md",
  ".mjs",
  ".toml",
  ".txt",
  ".xml",
  ".yaml",
  ".yml",
]);

const SECRET_PATTERNS = [
  ["private-key-block", /-----BEGIN (?:RSA |DSA |EC |OPENSSH |)?PRIVATE KEY-----/],
  ["aws-access-key", /\bAKIA[0-9A-Z]{16}\b/],
  ["github-token", /\b(?:ghp|gho|ghu|ghs|ghr|github_pat)_[A-Za-z0-9_]{20,}\b/],
  ["openai-style-key", /\bsk-[A-Za-z0-9]{20,}\b/],
  ["slack-token", /\bxox[baprs]-[A-Za-z0-9-]{20,}\b/],
  ["google-api-key", /\bAIza[0-9A-Za-z_-]{35}\b/],
  [
    "assigned-secret-like-value",
    /\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*["']?(?!replace|placeholder|example|dummy|test|none|null|false|true|not_|your_|\$\{|secrets\.|GITHUB_TOKEN\b)[A-Za-z0-9_./+=-]{16,}/i,
  ],
];

const issues = [];

function rel(file) {
  return path.relative(ROOT, file).replaceAll(path.sep, "/");
}

function addIssue(message) {
  issues.push(message);
}

function isIgnoredPath(fileOrDir) {
  const relativeParts = path.relative(ROOT, fileOrDir).split(path.sep).filter(Boolean);
  if (relativeParts.some((part) => IGNORED_DIRS.has(part))) return true;

  return IGNORED_PATH_PARTS.some((ignoredParts) =>
    ignoredParts.every((part, index) => relativeParts[index] === part) ||
    relativeParts.some((part, index) => ignoredParts.every((ignoredPart, offset) => relativeParts[index + offset] === ignoredPart)),
  );
}

async function walk(dir) {
  if (isIgnoredPath(dir)) return [];

  const entries = await readdir(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const entryPath = path.join(dir, entry.name);
    if (isIgnoredPath(entryPath)) continue;

    if (entry.isDirectory()) {
      files.push(...await walk(entryPath));
    } else {
      files.push(entryPath);
    }
  }
  return files;
}

async function readText(file) {
  const ext = path.extname(file).toLowerCase();
  if (!TEXT_EXTENSIONS.has(ext) && path.basename(file) !== "_headers" && !path.basename(file).startsWith(".env")) {
    return null;
  }
  return readFile(file, "utf8");
}

function extractAttr(tag, attr) {
  const match = tag.match(new RegExp(`${attr}\\s*=\\s*["']([^"']*)["']`, "i"));
  return match ? match[1] : "";
}

function checkSitemap(files) {
  const sitemapFiles = files.filter((file) => path.basename(file).toLowerCase() === "sitemap.xml");
  if (sitemapFiles.length !== 1) {
    addIssue(`Expected exactly one sitemap.xml, found ${sitemapFiles.length}: ${sitemapFiles.map(rel).join(", ")}`);
  }
}

async function checkSitemapContents() {
  const sitemapPath = path.join(ROOT, "sitemap.xml");
  const text = await readFile(sitemapPath, "utf8");
  const urls = [...text.matchAll(/<loc>([^<]+)<\/loc>/g)].map((match) => match[1]);
  const expected = PUBLIC_PAGES.map((page) => `${SITE}/${page}`);
  const extra = urls.filter((url) => !expected.includes(url));
  const missing = expected.filter((url) => !urls.includes(url));

  if (extra.length) addIssue(`sitemap.xml contains non-public URLs: ${extra.join(", ")}`);
  if (missing.length) addIssue(`sitemap.xml is missing public URLs: ${missing.join(", ")}`);
  if (urls.some((url) => /\/(tools|docs|reports|\.github|content|data|layouts|scripts)\//i.test(url))) {
    addIssue("sitemap.xml contains an internal tooling path.");
  }
}

async function checkPublicPages() {
  for (const page of PUBLIC_PAGES) {
    const file = path.join(ROOT, page || "index.html");
    const html = await readFile(file, "utf8");
    if (!/<link\b[^>]*rel\s*=\s*["']canonical["'][^>]*>/i.test(html)) {
      addIssue(`${page || "index.html"} is missing a canonical tag.`);
    }

    const navBlocks = [...html.matchAll(/<nav\b[\s\S]*?<\/nav>/gi)].map((match) => match[0]);
    for (const nav of navBlocks) {
      if (/href\s*=\s*["'](?:\.\/)?(?:tools|docs|reports|\.github|content|data|layouts|scripts)\//i.test(nav)) {
        addIssue(`${page || "index.html"} has public navigation linking to an internal path.`);
      }
      const hrefs = [...nav.matchAll(/href\s*=\s*["']([^"']+)["']/gi)].map((match) => match[1]);
      for (const href of hrefs) {
        if (/^(https?:|mailto:|tel:|#)/i.test(href)) continue;
        const cleanHref = href.split("#")[0].split("?")[0];
        if (!cleanHref || cleanHref === "/") continue;
        const target = path.join(ROOT, cleanHref);
        const targetExists = PUBLIC_PAGES.some((publicPage) => target === path.join(ROOT, publicPage || "index.html"));
        if (!targetExists) addIssue(`${page || "index.html"} navigation links to missing public page: ${href}`);
      }
    }
  }
}

async function checkInternalNoindex(files) {
  const internalHtmlFiles = files.filter((file) => /[\\/]tools[\\/]dashboard[\\/].+\.html$/i.test(file));
  for (const file of internalHtmlFiles) {
    const html = await readFile(file, "utf8");
    if (!/<meta\b[^>]*name\s*=\s*["']robots["'][^>]*content\s*=\s*["'][^"']*noindex[^"']*nofollow[^"']*["'][^>]*>/i.test(html)) {
      addIssue(`${rel(file)} is internal HTML without meta robots noindex,nofollow.`);
    }
  }
}

async function checkBlankTargets(files) {
  for (const file of files) {
    const text = await readText(file);
    if (!text) continue;
    const anchors = text.match(/<a\b[^>]*target\s*=\s*["']_blank["'][^>]*>/gi) || [];
    for (const tag of anchors) {
      const relValue = extractAttr(tag, "rel").toLowerCase();
      if (!relValue.split(/\s+/).includes("noopener") || !relValue.split(/\s+/).includes("noreferrer")) {
        addIssue(`${rel(file)} has target="_blank" without rel="noopener noreferrer".`);
      }
    }
  }
}

async function checkHttpAssetUrls(files) {
  for (const file of files) {
    const text = await readText(file);
    if (!text) continue;
    const assetTags = text.match(/<(?:script|img|source|video|audio|link)\b[^>]*(?:src|href|poster)\s*=\s*["'][^"']+["'][^>]*>/gi) || [];
    for (const tag of assetTags) {
      const url = extractAttr(tag, "src") || extractAttr(tag, "href") || extractAttr(tag, "poster");
      if (/^http:\/\//i.test(url) || /^\/\//.test(url)) {
        addIssue(`${rel(file)} contains a non-HTTPS or protocol-relative asset URL; use HTTPS explicitly.`);
      }
    }
  }
}

async function checkSecrets(files) {
  for (const file of files) {
    const text = await readText(file);
    if (!text) continue;
    const lines = text.split(/\r?\n/);
    lines.forEach((line, index) => {
      for (const [label, pattern] of SECRET_PATTERNS) {
        pattern.lastIndex = 0;
        if (pattern.test(line)) {
          addIssue(`${rel(file)}:${index + 1} matches ${label}; value redacted.`);
        }
      }
    });
  }
}

async function checkRequiredStaticFiles() {
  const required = [
    "robots.txt",
    "sitemap.xml",
    ".well-known/security.txt",
    "SECURITY.md",
    "docs/SECURITY_CHECKLIST.md",
    "_headers",
    ".github/workflows/gitleaks.yml",
  ];

  const files = await walk(ROOT);
  const fileSet = new Set(files.map(rel));
  for (const requiredFile of required) {
    if (!fileSet.has(requiredFile)) addIssue(`Missing required security file: ${requiredFile}`);
  }

  const robots = await readFile(path.join(ROOT, "robots.txt"), "utf8");
  if (!robots.includes("Sitemap: https://deveshbinwal.com/sitemap.xml")) {
    addIssue("robots.txt does not point to https://deveshbinwal.com/sitemap.xml");
  }
}

async function main() {
  const files = await walk(ROOT);
  checkSitemap(files);
  await checkSitemapContents();
  await checkRequiredStaticFiles();
  await checkPublicPages();
  await checkInternalNoindex(files);
  await checkBlankTargets(files);
  await checkHttpAssetUrls(files);
  await checkSecrets(files);

  if (issues.length) {
    console.error("Static security validation failed:");
    for (const issue of issues) console.error(`- ${issue}`);
    process.exitCode = 1;
    return;
  }

  console.log("Static security validation passed.");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
