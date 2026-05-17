# Content Update Guide for Dr. Devesh Chandra Binwal

This website is a simple static GitHub Pages site. The visible pages are controlled by the root HTML files and the `assets` folder.

## Main files

- `index.html` - homepage and CV download button
- `research.html` - research areas
- `publications.html` - complete publication list
- `expertise.html` - technical expertise
- `awards.html` - academic highlights, conferences, visits, recognition, and service
- `gallery.html` - carousel and gallery images
- `contact.html` - email, website, contact form, and academic profile links
- `assets/site.css` - colors, spacing, layout, gallery, and mobile styling
- `CNAME` - custom domain for GitHub Pages

## Update publications

1. Open `publications.html`.
2. Find the year where the new paper belongs.
3. Copy one existing `<article class="card pub-card"> ... </article>` block.
4. Paste it in the correct reverse-chronological position.
5. Replace the title, authors, journal details, short highlight, DOI link, publisher link, and Google Scholar link.
6. Bold the name using `<strong>D. C. Binwal</strong>` or the exact author-name form used in the paper.
7. Use chemical subscripts such as `MoS<sub>2</sub>` and `Cl<sub>6</sub>`.

If a DOI or PDF is not available, leave that button out until it is ready.

## Update gallery images and captions

1. Put the new image in `assets/images/`.
2. Use a simple file name, for example `grc-poster-2024.jpg`.
3. Open `gallery.html`.
4. Replace the image path in `src="assets/images/..."`.
5. Update the caption inside `<figcaption>`.

The top carousel is the first image group inside `<div class="gallery-carousel">`. Use only images that look good in a wide carousel. Put portrait images or close-cropped images in the lower gallery grid.

Keep captions short and factual, for example:

- `Poster presentation at the Gordon Research Conference, Boston, 2024.`
- `Research presentation at the University of Newcastle, Australia, 2025.`
- `After the PhD defense, with lab members.`

## Update the CV

1. Put the new CV file in `assets/docs/`.
2. Use a clear file name, for example `CV-Devesh-Chandra-Binwal.pdf`.
3. Open `index.html`.
4. Search for `assets/docs/CV-Devesh-Chandra-Binwal.docx`.
5. Replace it with the new file name.
6. If the file changes from Word to PDF, change the button text if needed.

The CV is intentionally linked from the homepage only.

## Update contact links

Open `contact.html` and update:

- email address
- website/domain
- Google Scholar
- ORCID
- ResearchGate
- LinkedIn

The contact form currently uses a safe `mailto:` fallback for GitHub Pages. To use Formspree, Getform, or another form service later, replace the form `action` URL with the service endpoint.

## Update research text

Open `research.html` and edit the text inside paragraph tags:

`<p>Research text goes here.</p>`

Keep each research area concise. One short paragraph plus key methods is usually enough.

## Update icons

Profile icons are stored in `assets/icons/`.

Replace icon files with the same names if you want to update them:

- `google-scholar.png`
- `orcid.png`
- `researchgate.png`
- `linkedin.png`
- `email.png`

Keep icon images small and square so they do not distort in buttons.
