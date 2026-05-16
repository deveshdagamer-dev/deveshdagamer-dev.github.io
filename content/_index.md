---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2022-10-24
type: landing

sections:
  - block: resume-biography-3
    content:
      username: me
      text: |-
        My doctoral research expanded the family of magnetic halide double perovskites by introducing
        Mo(III) (4d³, t₂g³) as the trivalent B-site cation. Although closed-shell ions such as Bi(III),
        Sb(III) and In(III) dominate the literature on lead-free perovskites, open-shell transition-metal
        analogues remain relatively under-explored. I have contributed five first-author publications in
        Chemical Science (HOT Article and Pick of the Week), Chemistry of Materials, Chemical
        Communications and ACS Applied Energy Materials, together with a manuscript on layered Mo(III)
        perovskites currently under review at Angewandte Chemie International Edition.

        In parallel, I retain an interest in low-dimensional materials for hydrogen evolution. My early
        work on phase-engineered MoS₂, MoSe₂, WS₂ and Mo₂C nanosheets yielded one cover article in
        ACS Applied Energy Materials and underpins several co-authored studies on 3R-polytype TMDs.

        I served as a Visiting PhD Student in the group of Prof. Ajayan Vinu at the University of
        Newcastle, Australia (2025), and have presented at the Gordon Research Conference on
        Unconventional Semiconductors (USA, 2024) and the International Workshop on Advanced Materials
        (UAE, 2023). I am a peer reviewer for ACS Applied Energy Materials.
      button:
        text: Download CV
        url: uploads/CV_Dr_Devesh_Chandra_Binwal.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle

  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2

  - block: collection
    content:
      title: Recent Publications
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation

  - block: collection
    id: talks
    content:
      title: Conferences & Talks
      filters:
        folders:
          - events
    design:
      view: card

  - block: markdown
    content:
      title: 'Technical Skills'
      subtitle: ''
      text: |-
        **Crystal Growth and Synthesis:** Sealed-tube, solvothermal, hydrothermal, Schlenk line techniques; growth of single crystals of air-sensitive halide materials

        **Structural Characterization:** SCXRD, PXRD, XPS, SEM, TEM, UV-Vis, Raman, DSC, SQUID magnetometry

        **Applications:** Photocatalysis, electrocatalysis (HER), evaluation of magnetic and optical functionalities

        **Software:** Olex2, APEX4, WinGX, Mercury, VESTA, GSAS-II, Origin, Fityk, MS Office
    design:
      columns: '1'

  - block: markdown
    content:
      title: 'Teaching & Service'
      subtitle: ''
      text: |-
        - Teaching Assistant, Recent Trends in Inorganic and Nano Materials, JNCASR (2021–2022)
        - Peer Reviewer, ACS Applied Energy Materials (2026)
        - Volunteer: National Science Day (2025); International Conference on Recent Advances in Materials RAM-90 (2023); JNCASR International Winter School (2023–2024)
    design:
      columns: '1'

  - block: markdown
    content:
      title: 'Training & Workshops'
      subtitle: ''
      text: |-
        - Rigaku School for Practical Crystallography (January 2022)
        - STUTI-DST Workshop on X-ray Crystallography, VIT (August 2022)
        - Workshop on Neutron Scattering and Muon Spectroscopy (February 2024)
        - Crash course on Next-Generation Solar Cells (March–April 2022)
    design:
      columns: '1'
---
