# Security Policy

This repository contains the public static portfolio website for `deveshbinwal.com`.

## API Keys And Secrets

API keys, tokens, private keys, webhook URLs, passwords, service credentials, and other secrets must never be committed to this repository or placed in browser-visible code. That includes HTML, CSS, JavaScript, JSON, YAML, generated assets, public build output, and GitHub Pages files.

Private API keys must only be used from server-side environment variables in a trusted backend or serverless provider. This site is currently static, so private API keys cannot be safely used directly by the front end.

Use `.env.example` for placeholder names only. Real values belong in local `.env` files, GitHub Actions secrets, or the deployment provider's secret/environment-variable store.

## If A Key Is Exposed

If any real key or token is committed or appears in Git history:

1. Revoke or rotate the key immediately in the provider dashboard.
2. Remove the key from the current repository state.
3. Review Git history exposure and deployment logs.
4. Replace the secret only through server-side environment variables.

Do not print full secret values in terminal output, reports, issues, pull requests, or logs. Report only the file path, line number when available, secret type, and a masked value.

## Static GitHub Pages Limitation

GitHub Pages serves static front-end files. Any key placed in front-end code is public to visitors. Private API calls require a backend/serverless provider such as Netlify Functions, Cloudflare Workers, Vercel Functions, Supabase Edge Functions, or another trusted server-side environment.

Do not fake security by hiding private keys in JavaScript, build files, comments, minified assets, or public config files.

## Rate Limiting Policy

Every backend/serverless API route added in the future must have rate limiting. Expensive AI or paid API routes should default to approximately 10 requests per minute per IP unless intentionally changed.

Routes must return `429 Too Many Requests` when the limit is exceeded. Rate-limit values should be configurable through environment variables where practical.

## Request Protection And Input Validation

Every future API route or form endpoint must:

- Validate and sanitize all user input.
- Reject empty, oversized, malformed, or suspicious requests.
- Enforce request body size limits.
- Use request timeouts for upstream calls.
- Block dangerous URL schemes such as `javascript:`.
- Avoid exposing stack traces, local file paths, raw provider errors, or secret-related errors to the browser.
- Log only safe metadata such as timestamp, endpoint, status code, and limited error labels.

If a database is added later, use parameterized queries or trusted database libraries to prevent SQL or NoSQL injection.

## CORS And Headers

Private API routes must not use unrestricted CORS. Production origins should be limited to `https://deveshbinwal.com` and approved local development origins.

Security headers should be configured in the active hosting layer where possible, including:

- `Content-Security-Policy`
- `X-Content-Type-Options`
- `Referrer-Policy`
- `Permissions-Policy`
- `X-Frame-Options` or CSP `frame-ancestors`

## Dependency Audits

Run dependency audits before deployment when package files are present. For this project, use:

```sh
pnpm audit --prod
```

Do not add unnecessary, outdated, vulnerable, or unmaintained packages for small fixes.
