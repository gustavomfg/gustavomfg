# Maintaining the orbital profile

Run these commands from the repository root:

```sh
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/build_assets.py
```

The build uses pinned Pillow 12.3.0, the fonts under `design/fonts/`, and `design/source/planet.png`. It writes ten responsive assets under `assets/`: animated and static desktop/mobile heroes, language panels and two project heading pairs. Keep README asset links relative (`./assets/...`) so they work on the review branch and when the repository is moved. Asset coordinates, typography and animation are authored in `scripts/build_assets.py`; `DESIGN.md` documents the extracted system.

## Sources and licenses

The planet was created and edited with OpenAI image generation on 2026-10-02. The prompts and provenance are retained in `design/source/PROMPTS.md`; the generated source is `design/source/planet.png`. Do not mislabel it as hand-drawn artwork or an application screenshot. The builder authors the scene, moon, orbit, stars, typography, archive and processor geometry.

Space Grotesk and Silkscreen came from the Google Fonts repository. Retain `design/fonts/OFL-SpaceGrotesk.txt` and `design/fonts/OFL-Silkscreen.txt` with their respective font files. Those font licenses do not establish a license for the entire profile or generated artwork. Content truth comes from Gustavo's resumes and the canonical Nocturne Studio and SysMon READMEs, linked in `README.md`.

## GitHub and responsive behavior

GitHub controls native text CSS, font stack, document width, spacing, background and link states. Custom page CSS and JavaScript are not available in this README. Artwork typography is rasterized and scales with image width; native paragraphs remain selectable.

The mobile breakpoint is a viewport width of 760px. Hero source priority is reduced motion plus mobile PNG, reduced motion desktop PNG, mobile GIF, then desktop GIF fallback. Other image pairs use mobile PNG sources and desktop PNG fallbacks. Preserve this ordering and meaningful alt text. Reduced-motion behavior depends on GitHub preserving `picture`/`source` media attributes and the viewer supporting them. Do not claim that the GIF itself pauses; a different static asset is selected.

## Review and publishing

The finish review reported “ship” with no material findings on desktop 1440px, mobile 390px and light-theme local captures. GitHub Markdown API sanitization was checked by the implementation workflow. Those screenshots simulate the README; they do not establish live branch rendering or change the default branch. After asset or copy edits, inspect desktop/mobile, light/dark, image links and reduced-motion source behavior on GitHub.

Publish only through the separately authorized review branch. Do not merge into main or force-push main. This documentation does not itself publish anything.
