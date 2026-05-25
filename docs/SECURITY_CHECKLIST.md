# Security Checklist

This checklist is for the static public academic portfolio at `deveshbinwal.com`.

## Deployment

- Keep GitHub Pages HTTPS enabled.
- Keep DNS records correctly pointed at the approved GitHub Pages target.
- Keep `sitemap.xml`, `robots.txt`, and `.well-known/security.txt` deployed with the public site.
- If any API key, token, password, webhook URL, or private key was ever committed, revoke or rotate it in the provider dashboard. Deleting it from the current file is not enough.

## Static Site Scope

- Authentication is not applicable while the site has no login, user accounts, payments, private dashboards for users, or database.
- IDOR checks are not applicable while there is no user-specific data layer, profile ownership model, API, or database.
- Do not add fake backend, session, password, or database logic for this static portfolio.

## Cloudflare-Ready Controls

- Cloudflare can be added later for WAF, bot protection, rate limiting, response headers, and caching.
- After DNS migration, enable the Cloudflare proxy for the production hostname.
- Enable basic bot protection.
- Add rate limiting for suspicious repeated requests.
- Rate limiting is mainly useful if there are forms, APIs, login, generation tools, or repeated suspicious requests.
- Do not rate-limit verified search crawlers aggressively because it can affect SEO.
- Protect internal dashboard and tool paths such as `/tools/`, `/reports/`, and `/docs/`.
- Cache static assets aggressively while keeping HTML cache behavior conservative.

## Contact And Forms

- The current contact form is static and uses `mailto:`.
- Frontend validation should remain in place for name length, email format, message length, and script-like input.
- If a third-party form service is added later, real spam filtering and rate limiting must be configured in that service or through Cloudflare.

## Headers

- `_headers` contains safe static-hosting headers, but GitHub Pages may not apply it directly.
- Netlify headers are also configured in `netlify.toml`.
- A strict Content-Security-Policy is staged rather than forced in `_headers` because overly strict CSP can break current images, videos, fonts, profile links, analytics, or scripts. Test CSP in report-only mode before enforcing it through a CDN or alternate host.

## Secret Scanning

- GitHub Actions runs Gitleaks on `push` and `pull_request`.
- Check that GitHub secret scanning and push protection are enabled where available in the repository Security settings. GitHub secret scanning scans Git history for hardcoded credentials and alerts when secrets are detected.
- Before pushing locally, run:

```sh
npx gitleaks detect --source . --redact --verbose
```

- If `npx` is unavailable, install or download Gitleaks from the official project and run the equivalent `gitleaks detect --source . --redact --verbose` command.
- If a real API key was ever committed, deleting it is not enough. Revoke or rotate it immediately with the provider.

## GitHub Repository Hygiene

- Confirm GitHub Pages HTTPS is enforced.
- Check the repository Security tab regularly.
- Enable secret scanning and push protection where available.
- Enable Dependabot alerts because package files exist.
- Consider branch protection if multiple people edit the repository.
- Never commit private PDFs, passports, certificates, unpublished manuscript files, API keys, credentials, or local config files.
