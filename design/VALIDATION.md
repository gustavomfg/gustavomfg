# Verification record

Checked on 2026-10-02 against the published `redesign/orbital-observatory` branch in `gustavomfg/gustavomfg`.

## Rendering

- GitHub Markdown API preserved `picture`, responsive media sources, reduced-motion media queries, native headings, links and alternative text.
- Local preview used current GitHub stylesheets. Independent visual review disposition: **ship**, no material findings in desktop, mobile and light-theme captures.
- Actual GitHub branch rendering was then inspected in Chromium at 1440px desktop and 390px mobile viewports, with dark and light themes.
- All four selected images loaded in each inspected layout. The actual README content widths were 838px desktop and 324px mobile; neither had horizontal overflow.
- Desktop and mobile selected their intended image variants. `prefers-reduced-motion: reduce` selected static PNGs on the live GitHub page; ordinary preference selected the corresponding GIFs.
- Native Projects and Contact navigation reached the correct headings on the live page. Project links resolve to existing repositories; the portfolio returned HTTP 200. LinkedIn and email match the supplied resumes; account login flows and email delivery were not exercised.

## Asset checks

- Ten relative image references resolve to repository files, all displayed images have meaningful alt text, and the README includes no page scripts or custom style attributes.
- Selected desktop image set: **90,863 bytes**. Selected mobile set: **76,520 bytes**. These figures exclude GitHub's own page resources and include only the four images normally selected for that layout.
- The two GIFs loop for exactly **12 seconds**. The encoder merges identical frames into 44 desktop and 42 mobile stored frames, retaining the authored 48 × 250ms duration.
- Shared palettes and delta encoding avoid palette flicker. Only the small orbital moon moves; there are no blinking stars or automatic text transitions.
- Static variants, source image, generation/edit prompts, authored asset builder, fonts and font licenses are retained. Font files and high-resolution source are build inputs, not resources fetched by the README.
- Final diff whitespace check passed.

## Content and limits

Project copy was checked against the two supplied resumes and the canonical READMEs at https://github.com/gustavomfg/nocturne-studio and https://github.com/gustavomfg/sysmon. Java/TypeScript remain primary, Rust is labeled as project use, and Python remains in learning. The explicit NVIDIA GPU condition follows SysMon's README.

GitHub owns native text, spacing, link styling and page background. A Profile README cannot force dark mode. Visual headings and the language panel contain rasterized text; alt descriptions provide their textual equivalent, while project descriptions, education and contact links remain native text. This is not a full screen-reader audit or an exhaustive test of every GitHub client.

No merge into main and no force push were performed. The base main commit at verification was `087740f3757a74901e5d1c32c602331042ecc068`.
