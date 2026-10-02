# Planet source and provenance

Mode: OpenAI built-in image generation tool, followed by one built-in image edit. Generated for Gustavo Maquias on 2026-10-02. `planet.png` retains the second generated image with unchanged pixels and embedded prompt metadata. It is build input only and is not loaded by the profile.

## Generation prompt

Create a single production pixel-art sprite: a sophisticated violet ringed planet, isolated on a truly transparent background. This is a small game-style pixel sprite for a professional software developer's orbital observatory identity. STRICT deliberate 96 by 64 logical pixel aesthetic, large visible square pixel clusters, a limited palette of 8 purple shades plus pale lavender, completely flat hard pixel edges, NO anti-aliasing, NO blur, NO glow, NO gradients, NO photographic or painterly texture, NO fine noise. Broad designed horizontal surface bands, a few deliberate dither clusters on the shadow boundary. Planet sphere about 40 logical pixels across; sweeping diagonal rings span about 80 logical pixels; rings correctly behind upper hemisphere and in front of lower hemisphere. Light at upper left, deep plum shadow bottom right. A premium 1990s pixel-art astronomical sprite, calm, elegant and iconic. Center the sprite with generous transparent margin. No stars, scenery, text, logos, frame, border, UI, satellites or additional objects. Export one single sprite only, not a sheet. Pixels must be intentionally big and clean.

## Edit prompt

Edit this planet sprite. Remove ALL the purple glow and soft halos around and inside the ring openings. Outside the hard pixel outline must be fully transparent. Preserve the ringed planet silhouette and composition, but simplify the surface to about eight flat purple colors in chunky clean 3-6 pixel clusters, without blurry outlines or microtexture. Redraw clean crisp low resolution pixel art with fully opaque colors inside the shape. No semi-transparent purple haze anywhere. The ring holes must be empty transparent cutouts. It should look hand-pixeled on a 96x64 pixel canvas and enlarged using nearest neighbor. No background, no lighting bloom, no gradients.

## Production

The build converts the source to a 96×64 logical sprite, a 12-color palette and binary alpha for GIF compatibility. Nearest-neighbor scaling preserves the grid. The scene, orbital motion, lettering, knowledge archive and processor signal are authored in `scripts/build_assets.py`. Project visuals are symbolic graphics, not application screenshots or measured telemetry.

Space Grotesk and Silkscreen were obtained from the Google Fonts repository, with their OFL licenses retained in `design/fonts/`.
