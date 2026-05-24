# Agent Instructions

This repository contains the academic portfolio website of Dr. Devesh Chandra Binwal at https://www.deveshbinwal.com.

## Site Priorities

- Preserve a clean, professional academic appearance.
- The primary target experience is desktop and laptop use, while maintaining strong mobile responsiveness.
- Homepage and profile text should remain justified by default unless a specific layout exception is needed.
- Avoid unnecessary redesigns, visual churn, or broad rewrites.
- Do not change visible website design, text, layout, CSS, JavaScript, images, animations, videos, or research/publication content unless the user explicitly asks for that change.

## Audit And Maintenance Rules

- Audit systems must never directly overwrite visible website content without review.
- Audit scripts and reports should be additive and should not deploy the website.
- Future audits should evaluate SEO, accessibility, performance, security headers, metadata, structured data opportunities, sitemap integrity, and UX issues.
- Treat audit findings as recommendations until reviewed by the site owner.
- Keep GitHub Pages deployment behavior intact.

## Security and Production Safety Rules

This is a public production portfolio website for `deveshbinwal.com`. Treat all code changes as production-facing.

### General Change Rules

- Do not change visual design, layout, animations, content, gallery, images, videos, research text, or styling unless the task explicitly asks for it.
- Desktop and laptop layout is the primary target, while keeping the website fully responsive on mobile and tablet.
- Keep homepage and profile text justified by default unless a specific layout element looks worse with full justification.
- Make small, targeted changes only.
- Always explain what files were changed and why.
- Do not introduce unnecessary dependencies.
- Do not remove existing working features unless required for security.

### API Key And Secret Safety

- Never place API keys, tokens, private keys, webhook URLs, passwords, or service credentials in front-end code.
- No secret should appear in HTML, CSS, JavaScript, JSON, public assets, build files, or browser-visible files.
- Private API keys must only be read from server-side environment variables.
- Never print full secret values in terminal output or final reports. If a secret is discovered, report only the file path, line number, and masked value.
- If a secret appears in Git history, treat it as compromised and clearly state that it must be rotated immediately.
- Add or maintain `.gitignore` rules for `.env`, `.env.local`, `.env.production`, `.env.*`, logs, cache files, and private config files.
- Use `.env.example` only with placeholder values. Never include real keys.

### API And Backend Safety

- Front-end code must not call paid or private third-party APIs directly using secret keys.
- Browser code should call only this site's own secure backend or serverless endpoint.
- Backend or serverless routes must read secrets only from environment variables.
- Every API route must have rate limiting.
- Expensive routes, especially AI or API routes, should use strict rate limits such as 10 requests per minute per IP unless the task specifies otherwise.
- API routes must return `429 Too Many Requests` when rate limits are exceeded.
- API routes must have request body size limits and timeouts.
- Do not expose internal stack traces, file paths, raw third-party errors, or secret-related errors to the browser.

### Input Validation

- Never trust user input.
- Validate and sanitize all input from forms, search boxes, AI prompt boxes, dashboard fields, URL inputs, contact forms, and future upload features.
- Reject empty, oversized, malformed, or suspicious requests.
- Block dangerous URL schemes such as `javascript:`.
- Protect against XSS and injection-style attacks.
- If a database is added in the future, protect against SQL or NoSQL injection using parameterized queries or trusted libraries.

### CORS And Security Headers

- Do not use unrestricted CORS for private API routes.
- Production API routes should allow only `https://deveshbinwal.com` and approved local development origins.
- Add or verify security headers where applicable:
  - `Content-Security-Policy`
  - `X-Content-Type-Options`
  - `Referrer-Policy`
  - `Permissions-Policy`
  - `X-Frame-Options` or `frame-ancestors`

### File Upload Safety

- If file upload exists or is added later, enforce:
  - file size limit
  - allowed file types only
  - executable file blocking
  - randomized file names
  - storage outside public root when private
  - no direct public access to sensitive uploads
  - encryption for sensitive stored files when applicable
- If no file upload feature exists, report that file-upload risk is not currently applicable.

### Authentication

- Do not build a custom authentication or password system from scratch unless explicitly required.
- Prefer tested providers such as Firebase Auth, Supabase Auth, Clerk, Auth0, Google OAuth, or GitHub OAuth.

### Dependency Safety

- Review every added dependency.
- Avoid old, unmaintained, unnecessary, or suspicious packages.
- Run dependency audits when package files exist.
- Remove unused packages when safe.
- Do not add many packages for a small fix.

### Logging Safety

- Logs must not contain API keys, tokens, passwords, full request bodies, or sensitive data.
- Use safe logs only, such as timestamp, endpoint, status code, and limited error labels.

### Security Task Final Report

Before finishing any security-related task, report:

- What was checked.
- Whether any exposed secret was found, with values masked.
- Whether Git history was checked.
- Whether rate limiting exists.
- Whether user input validation exists.
- Whether CORS is restricted.
- Whether security headers exist.
- Whether dependency audit was run.
- What files were changed.
- Whether any manual action is required from the user.
