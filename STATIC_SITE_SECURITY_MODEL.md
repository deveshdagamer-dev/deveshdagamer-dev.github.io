# Static Site Security Model

This repository publishes the static academic portfolio website for
`deveshbinwal.com`.

## Current Production Scope

- No login.
- No payments.
- No user accounts.
- No private user dashboard.
- No database.
- No server-side API routes.

Because of that current scope, authentication, password reset, password hashing,
session expiry, session storage, authorization ownership checks, and IDOR
protections are not applicable at present.

## Current Real Risks

- Exposed secrets in repository files, generated assets, GitHub Actions, or Git
  history.
- Unsafe or unnecessary third-party scripts.
- Internal diagnostic tools being indexed or publicly linked.
- Contact-form spam if a third-party form provider is added later.
- Weak DNS, HTTPS, or CDN configuration.
- Future additions that accidentally introduce browser-visible API keys, unsafe
  input handling, unrestricted CORS, or unprotected backend endpoints.

## Operating Rule

Keep security controls static-site appropriate. Do not add login, password,
session, database, payment, or fake backend code unless the website actually
adds those production features later.
