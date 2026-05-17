# Content Update Guide for Dr. Devesh Chandra Binwal

This website is a simple GitHub Pages site. The visible website is controlled by the root `.html` files and the `assets` folder.

## Main Files

- `index.html` - homepage
- `research.html` - research page
- `publications.html` - publication cards
- `expertise.html` - technical expertise
- `awards.html` - academic highlights, conferences, awards, visits, and service
- `gallery.html` - carousel and gallery images
- `cv.html` - CV download page
- `contact.html` - email and academic profile links
- `assets/site.css` - visual design

## Update Publications

1. Open `publications.html`.
2. Copy one existing `<article class="card pub-card"> ... </article>` block for a first-author paper.
3. Copy one existing `<article class="card"> ... </article>` block for a collaborative paper.
4. Replace the title, authors, journal, year, short significance line, DOI link, and publisher link.
5. Use `<sub>2</sub>` for chemical subscripts, for example `MoS<sub>2</sub>`.

If a DOI is not available yet, leave the DOI button out until it is known.

## Update Gallery Images

1. Put the new image in `assets/images/`.
2. Use a simple descriptive file name, for example `grc-poster-2024.jpg`.
3. Open `gallery.html`.
4. Find the image path in `src="assets/images/..."`.
5. Replace the image path and update the caption inside `<figcaption>`.

The top carousel uses the first group of images inside `<div class="gallery-carousel">`. The lower sections are grouped as conferences, scientific discussions, visits, and milestones.

## Update Captions

Keep captions short, factual, and academic. Good examples:

- `Poster presentation at the Gordon Research Conference, Boston, 2024.`
- `Research presentation at the University of Newcastle during my visiting PhD stay.`
- `After the PhD defense, with lab members.`

## Update the CV

1. Put the new CV file in `assets/docs/`.
2. Use a clear name, for example `CV-Devesh-Chandra-Binwal.pdf`.
3. Open `index.html` and `cv.html`.
4. Search for `assets/docs/CV-Devesh-Chandra-Binwal.docx`.
5. Replace it with the new file name.

If you switch to PDF, also change the button text from `Download CV (Word)` to `Download CV (PDF)`.

## Update Contact Links

Open `contact.html` and update:

- email addresses
- Google Scholar
- ORCID
- ResearchGate
- LinkedIn
- website/domain text

## Update Research Text

Open `research.html` and edit only the text inside paragraph tags:

`<p>Research text goes here.</p>`

Keep each research area concise. One short paragraph plus key methods is usually enough.

## Design Changes

Most design choices are in `assets/site.css`. Change this file only if you are comfortable editing CSS, or ask Codex to make the design change.
