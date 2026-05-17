# Dr. Devesh Chandra Binwal Academic Website

This is a simple static website designed for GitHub Pages. It does not require Hugo, Jekyll, npm, or any build step.

## Website Structure

- `index.html` - homepage
- `research.html` - research areas
- `publications.html` - publication cards and DOI links
- `expertise.html` - skills and methods
- `awards.html` - awards, fellowships, presentations, and service
- `gallery.html` - academic photo gallery
- `cv.html` - CV download page
- `contact.html` - email and profile links
- `assets/site.css` - shared design styles
- `assets/images/` - website images
- `assets/docs/` - CV and document downloads
- `CNAME` - custom domain configuration for `deveshbinwal.com`

## GitHub Pages Setup

In the GitHub repository, go to:

Settings -> Pages -> Build and deployment

Use:

- Source: Deploy from a branch
- Branch: `main`
- Folder: `/root`

The `CNAME` file is already prepared for `deveshbinwal.com`. After publishing through GitHub Pages, configure the domain DNS records at your domain provider according to GitHub Pages instructions.

## Updating Content

Most edits can be made directly in the matching `.html` file. For example:

- Edit research text in `research.html`
- Add publications in `publications.html`
- Replace or add photos in `assets/images/`
- Replace the CV in `assets/docs/`
- Update emails and profile links in `contact.html`

See `CONTENT_UPDATE_GUIDE.md` for non-coder instructions.
