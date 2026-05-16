---
title: 'Gallery'
date: 2022-10-24
type: landing

sections:
  - block: markdown
    content:
      title: 'Gallery'
      subtitle: ''
      text: |-
        <style>
        .gallery-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 1rem;
          width: 100%;
        }
        .gallery-grid figure {
          margin: 0;
          text-align: center;
        }
        .gallery-grid img {
          width: 100%;
          height: 220px;
          object-fit: cover;
          border-radius: 8px;
          display: block;
        }
        .gallery-grid figcaption {
          font-size: 0.82rem;
          margin-top: 0.4rem;
          color: #555;
          text-align: center;
        }
        @media (max-width: 768px) {
          .gallery-grid { grid-template-columns: 1fr 1fr; }
        }
        @media (max-width: 480px) {
          .gallery-grid { grid-template-columns: 1fr; }
        }
        </style>
        <div class="gallery-grid">
          <figure>
            <img src="/uploads/gallery-1.jpg" alt="With Prof. C.N.R. Rao, JNCASR">
            <figcaption>With Prof. C.N.R. Rao, JNCASR</figcaption>
          </figure>
          <figure>
            <img src="/uploads/gallery-2.jpg" alt="Poster Presentation, GRC USA 2024">
            <figcaption>Poster Presentation, GRC USA 2024</figcaption>
          </figure>
          <figure>
            <img src="/uploads/gallery-3.jpg" alt="Oral Talk, University of Newcastle 2025">
            <figcaption>Oral Talk, University of Newcastle 2025</figcaption>
          </figure>
          <figure>
            <img src="/uploads/gallery-4.jpg" alt="Group Photo, JNCASR–Rice University Workshop 2023">
            <figcaption>Group Photo, JNCASR–Rice University Workshop 2023</figcaption>
          </figure>
          <figure>
            <img src="/uploads/gallery-5.jpg" alt="IWAM Poster, UAE 2023">
            <figcaption>IWAM Poster, UAE 2023</figcaption>
          </figure>
        </div>
    design:
      columns: '1'
---
