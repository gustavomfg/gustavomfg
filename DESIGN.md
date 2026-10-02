---
name: Orbital observatory
description: Gustavo Maquias — a restrained pixel-art software identity
colors:
  background: "#100f1d"
  ink: "#f2edff"
  muted: "#bfb1d6"
  line: "#342849"
  violet: "#aa80ee"
  lilac: "#d9bcff"
  mint: "#9ccec9"
typography:
  hero:
    fontFamily: "Space Grotesk"
    fontSize: "91px"
    fontWeight: 650
  hero-mobile:
    fontFamily: "Space Grotesk"
    fontSize: "74px"
    fontWeight: 650
  project:
    fontFamily: "Space Grotesk"
    fontSize: "62px"
    fontWeight: 650
  project-mobile:
    fontFamily: "Space Grotesk"
    fontSize: "45px"
    fontWeight: 650
  caption:
    fontFamily: "Space Grotesk"
    fontSize: "25px"
    fontWeight: 450
  caption-mobile:
    fontFamily: "Space Grotesk"
    fontSize: "26px"
    fontWeight: 450
  terminal:
    fontFamily: "Silkscreen"
    fontSize: "19px"
    fontWeight: 400
  languages-primary:
    fontFamily: "Space Grotesk"
    fontSize: "66px"
    fontWeight: 650
  languages-secondary:
    fontFamily: "Space Grotesk"
    fontSize: "30px"
    fontWeight: 650
  languages-secondary-mobile:
    fontFamily: "Space Grotesk"
    fontSize: "33px"
    fontWeight: 650
components:
  artwork-surface:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
---
# Design System: Orbital observatory

## Overview

**Creative North Star: "Orbital observatory"**

A calm, spacious identity built from violet pixel geometry and crisp authored typography. The signature world combines coarse astronomical sprites, sparse stars and diagram-like orbital motion. Native GitHub paragraphs and links carry readable project evidence around the artwork.

Dark image surfaces hold a consistent atmosphere across GitHub themes. Distinct archive and processor silhouettes give each project its own identity within the same limited visual language.

**Key Characteristics:**

- Coarse pixel geometry with nearest-neighbor scaling.
- Violet and lavender, with restrained mint for telemetry.
- One moving moon; readable native text and links.

## Colors

The palette is plum-dark, lavender-lit and deliberately restrained. The normative colors above apply to authored artwork, not GitHub's surrounding document.

### Primary

- **Violet:** the language separator and core identity accent.
- **Lilac:** terminal line and secondary language names.

### Secondary

- **Cool mint:** the SysMon signal trace, reserved for its telemetry identity.

### Neutral

- **Orbital background:** all artwork canvases.
- **Pale ink:** main names and primary language lettering.
- **Dusty lavender:** captions and explanatory labels.
- **Plum line:** dotted orbit and language dividers.

The sprite's twelve colors are quantized from `design/source/planet.png`; they are image-derived, not a hand-authored global scale. Other illustration colors are local to their geometry in `scripts/build_assets.py`.

## Typography

**Display Font:** Space Grotesk, bundled variable font; no runtime fallback is used by the asset builder.
**Body Font:** GitHub's native font stack, controlled by the host.
**Label/Mono Font:** Silkscreen, bundled regular font, used only for the terminal line.

Space Grotesk uses weight 650 for bold and 450 otherwise. Sizes in the frontmatter are source-image pixels; the browser scales the entire image. These are not CSS text sizes. Pillow uses a top-left text anchor, with separately positioned lines rather than a CSS line-height or tracking token.

The desktop language panel uses 66px primary names, 52px separator, 24px primary caption, 30px secondary names and 26px usage labels. Mobile uses Java at 54px, TypeScript at 48px, the separator at 40px, the primary caption at 25px, secondary names at 33px and usage labels at 26px. Desktop hero name origins are independently placed at y=122 and y=216; mobile at y=50 and y=128. The drawing API uses top-left anchors, so these y values are placement origins, not typographic baselines.

## Layout

Images fill 100% of the available README width. GitHub determines the container, native paragraph spacing, heading treatment and link states. The implementation has no page-level CSS spacing scale.

| Asset | Desktop source | Mobile source |
| --- | --- | --- |
| Hero | 1200 × 500 | 640 × 720 |
| Languages | 1200 × 236 | 640 × 350 |
| Each project | 1200 × 300 | 640 × 390 |

`picture` switches to mobile sources at viewport widths ≤760px. The hero stacks identity above the planet on mobile. Project titles sit above their emblems on mobile and beside them on desktop. Image composition uses explicit coordinates in the builder, not a reusable padding scale: desktop text origins generally start at x=60–68, mobile at x=38–46.

## Elevation & Depth

There are no authored CSS shadows. Depth comes from flat tonal layers, overlap, the ringed planet and the moon passing behind and in front of it. The Nocturne archive has three staggered layers; the SysMon processor uses nested flat rectangles. GitHub owns surrounding surface treatment.

## Shapes

The planet is reduced to a 96 × 64 sprite, quantized to twelve colors without dithering, with alpha threshold 210. It is enlarged sixfold to 576 × 384. Project emblems start at 120 × 84 and enlarge threefold to 360 × 252. Stars and orbit positions use a four-pixel grid. Image canvases are rectangular; no authored rounded-corner token exists.

## Components

### Orbital hero

Large two-line identity with a terminal label and ringed planet. The sole animated object is the moon: 48 frames at 250ms each make a 12-second infinite loop. The orbit is rotated −0.32 radians. Desktop radii are 240 × 104 around (897,243); mobile radii are 228 × 78 around (320,506). The moon switches drawing order at the sine sign change. A shared 128-color GIF palette, no dithering and disposal mode 1 keep frames consistent. Static PNGs use frame zero.

### Language panel

Explicit typographic priority for Java and TypeScript; Rust is “Em projetos” and Python “Em aprendizado.” A two-pixel divider separates groups: vertical on desktop, horizontal on mobile. No scores or percentages.

### Project heading artwork

Nocturne uses an archive with a crescent; SysMon uses a processor and a mint pulse. Each project image is inside a native repository link and an h3. A four-pixel top tracking strip is plum (#5e437d) for Nocturne and slate (#536c78) for SysMon. The project descriptions and technology lines remain native text.

### Native navigation and contact

Centered introductory links use middle-dot separators. Project links also appear as native text after each description. GitHub supplies hover, focus, selection and responsive wrapping; this repository does not define interactive CSS states or custom buttons, inputs or cards.

## Do's and Don'ts

### Do:

- **Do** keep artwork on its authored pixel grid and use nearest-neighbor enlargement.
- **Do** provide native descriptions, meaningful image alt text and real project links.
- **Do** pair each animated hero with its static reduced-motion image.
- **Do** preserve the explicit Java/TypeScript, Rust and Python hierarchy.

### Don't:

- **Don't** introduce badge walls, generic statistics widgets or proficiency percentages.
- **Don't** imply that symbolic project illustrations are application screenshots or measured telemetry.
- **Don't** rely on custom CSS, JavaScript or custom fonts for native GitHub text.
