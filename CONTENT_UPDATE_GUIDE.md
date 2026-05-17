# Content Update Guide for Dr. Devesh Chandra Binwal

This website is intentionally simple. You only need to edit normal text inside HTML files.

## Replace or Update the CV

1. Put the new CV file inside `assets/docs/`.
2. Use a simple file name, for example `CV-Devesh-Chandra-Binwal.pdf`.
3. Open `index.html` and `cv.html`.
4. Search for `assets/docs/CV-Devesh-Chandra-Binwal.docx`.
5. Replace it with the new file path.

If you add a PDF later, update the button text from `Download CV (Word)` to `Download CV (PDF)`.

## Add a New Publication

1. Open `publications.html`.
2. Copy one existing publication card.
3. Paste it in the correct section.
4. Update the title, authors, journal, year, highlight sentence, and DOI link.

For DOI links, use this format:

`https://doi.org/YOUR-DOI-HERE`

If a DOI is not available yet, write:

`Add DOI link here`

## Update Research Text

1. Open `research.html`.
2. Find the research section you want to change.
3. Edit only the paragraph text between `<p>` and `</p>`.
4. Keep the text concise. One short paragraph per research area is usually enough.

## Add or Replace Gallery Images

1. Put the image inside `assets/images/`.
2. Use a descriptive file name, for example `grc-poster-2024.jpg`.
3. Open `gallery.html`.
4. Replace the image path in `src="..."`.
5. Update the caption inside `<figcaption>`.

## Update Contact Links

Open `contact.html` and edit:

- Email addresses
- Google Scholar link
- ORCID link
- ResearchGate link
- LinkedIn link

## Design Notes

The main design file is `assets/site.css`. You usually do not need to edit it. If you want a color or spacing change, ask someone comfortable with CSS or use Codex to make the change.
