# Dr. Devesh Chandra Binwal Academic Website

This is a simple static website designed for GitHub Pages. It does not require Hugo, Jekyll, npm, or any build step.

## Website Structure

- `index.html` - homepage
- `research.html` - research areas
- `publications.html` - publication cards and DOI links
- `expertise.html` - skills and methods
- `awards.html` - academic highlights, conferences, awards, visits, and service
- `gallery.html` - academic photo gallery
- `contact.html` - email and profile links
- `assets/site.css` - shared design styles
- `assets/images/` - website images
- `assets/icons/` - profile and contact icons
- `assets/docs/` - CV and document downloads
- `CNAME` - custom domain for GitHub Pages

## GitHub Pages Setup

This repository deploys through the included GitHub Actions workflow:

- `.github/workflows/deploy.yml`

The workflow publishes the root HTML files, `assets/site.css`, images, icons, documents, `.nojekyll`, and `CNAME`. The public website is `https://deveshbinwal.com`.

## Updating Content

Most edits can be made directly in the matching `.html` file. For example:

- Edit research text in `research.html`
- Add publications in `publications.html`
- Replace or add photos and captions in `gallery.html` and `assets/images/`
- Replace `assets/docs/CV_Dr. Devesh Chandra Binwal.pdf` when updating the CV
- Update emails and profile links in `contact.html`

See `CONTENT_UPDATE_GUIDE.md` for non-coder instructions.
