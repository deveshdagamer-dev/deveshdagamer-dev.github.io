# External Services

This file documents scripts, widgets, forms, and externally loaded services used
by the static site.

| Service | Where Used | Necessary | Loads JavaScript | API Key Needed | Privacy/Security Notes |
| --- | --- | --- | --- | --- | --- |
| GoatCounter | Public HTML pages with `data-goatcounter="https://dcbinwal.goatcounter.com/count"` and `https://gc.zgo.at/count.js` | Optional privacy-friendly analytics | Yes | No frontend API key | Third-party analytics script. Keep it HTTPS-only. Review privacy settings in GoatCounter. Do not add secret tokens to frontend code. |
| `mailto:` contact form | `contact.html` | Yes, for static contact workflow | No | No | Frontend validation helps usability only. Real spam control requires a form provider, Cloudflare, or backend if this is converted from `mailto:` later. Never expose email-service API keys in JavaScript. |
| Public academic profile links | Contact/footer/profile links to Google Scholar, ORCID, ResearchGate, LinkedIn, DOI/publisher pages | Yes, for academic credibility | No, normal outbound links only | No | Keep `target="_blank"` links paired with `rel="noopener noreferrer"`. These are public links, not embedded widgets. |

No iframes were found in the current HTML/JS scan.
