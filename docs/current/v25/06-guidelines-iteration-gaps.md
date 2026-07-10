## Do's and Don'ts

### Do

- Let chrome be the resting state. A plain surface with a hairline border is a *finished* block — ship it without color. Most blocks on most viewports are chrome.
- Spend the one loud moment deliberately. One earned-color block or one full-strength image per viewport carries the section; make it count.
- Extract, never pick. Every content hue comes off the imagery or content on screen by the standard extraction and rotations — harmony is arithmetic.
- Print the number. Key figures sit large and direct on or beside the marks; name series at the mark. No legends, no lookup.
- Keep imagery raw. Full strength, real color, no filter, tint, duotone, or scrim; the style is in the crop and the frame, not the pixels.
- Let whitespace do the separating. When choosing between two spacing tokens, take the larger.
- Compose asymmetrically by default; reach for symmetry only when the content itself is symmetric. Anchor to the leading edge, let a cluster's silhouette stay ragged, and let a block overlap a neighbor's frame when the story layers.
- Keep legibility chrome. Type over color or photo resolves to black or white; add a subtle chrome scrim if contrast fails.
- Count a story rail as one moment. A mixed rail of photo, color, stat, and chart cards spends a single block-budget slot; the hue budget still applies inside it.
- Reach for texture before a second hue. Hatching and dashed fills distinguish projected from actual in one color; pattern is free, hue is budgeted.
- Treat screenshots and generative art as imagery. Their internal gradients are pixels, not block styling — raw, full strength, one loud moment.
- Design both canvases at once. A block is finished only when it holds on `#ffffff` *and* `#0a0a0a`; build on paired tokens, re-resolve earned color per canvas, and check both renders before shipping.

### Don't

- Don't color the chrome. Nav, buttons, inputs, badges, borders, focus rings, and chart containers stay neutral — always. A saturated CTA belongs to another system.
- Don't hand-pick an accent or hardcode a brand hue. If there's nothing to extract from, stay chrome.
- Don't treat photography. No gradient overlay, tint, duotone, filter, or house wash on an image.
- Don't gradient a content block. Content color is a flat fill; the only soft gradient allowed is a full-viewport ambient background carrying no content.
- Don't build a rainbow chart or a legend. One hue for the claim, the rest to the ink ramp; label in place.
- Don't exceed the budgets. At most three hues and one loud block per viewport; if a chart needs more hues, the claim is too diffuse — split it.
- Don't back a word with a color chip. A highlighted word in a headline sitting on a flat colored rectangle is a colored badge by another name — emphasis in this system is weight and italic, never a hue behind type.
- Don't use an icon where a word belongs. Functional chrome glyphs only; never an icon as a label or a chart legend.
- Don't add shadows or glows for depth. Layering is surface tone and hairlines only.
- Don't square up a layout out of habit. Centering a lone block, equalizing column widths, or snapping a cluster's edges to shared rows are claims of balance that must be earned by the content — unearned symmetry is the layout equivalent of an unearned hue.
- Don't ship light-only. Never hardcode a hex where a chrome token exists (a literal `#000` ink dies on the dark canvas), never reuse a light-mode swatch on `#0a0a0a`, and never "fix" dark mode by treating imagery — re-resolve color per canvas and re-crop instead.
- Don't mirror the examples as a kit. Reuse chrome primitives verbatim, but build story components to fit the content in front of you, and pull a named composite like the rail only when the content already has its shape. The catalog is inspiration spent once, not a checklist to instantiate.

## Iteration Guide

To extend this system, keep all chrome tokens within the black/white/gray ramp — usage of color is chosen per instance from the content, not tokenized — and reuse the 8px spacing scale for any new component. Any new component or token is defined on both canvases at once: give chrome values a `colors` and a `colors-dark` entry, and make sure any earned color it carries is re-resolved per canvas (Color Computation → Canvas-aware extraction) rather than hardcoded. A component that only has a light-mode design is not finished.

## Known Gaps

- **Dark-canvas floor calibration.** Canvas-aware extraction and the canvas-contrast floor are now specified as *behavior* (re-weight lightness per canvas; earned color must clear a minimum contrast against the active canvas), but the exact numeric targets — the perceived-loudness curve per hue band on `#0a0a0a`, the contrast-floor value, and how they interact with the chart-mark chroma floor at the hardest hues (deep blue, violet) — are not pinned to numbers, so implementers could still differ at the edges. Ties to the reference-implementation gap below.
- **Extraction reference implementation.** Color Computation defines the intended *result* (anchor hue → cusp-relative L/C per canvas → rotations → floors), but there is no reference algorithm, library, or fixed rotation direction/step documented, so two implementers could disagree at the edges.
- **Ambient-background exception** is deliberately narrow (full-viewport, content-free — it may not carry even a logo lockup) and untested at scale; revisit if it begins leaking onto content surfaces.
- **Annotation vocabulary.** In-place callouts over imagery and ink-drawn editorial marks (circles, arrows) were considered and deferred; if they recur in practice, they need a dedicated type role and scrim rules before use.
## Inspirations

- The Economist
- Shopify
- Stripe
- Spotify Wrapped

## Keywords
- Data-driven visuals
- Editorial hierarchy
- Vibrant accents
- Modern tech
- Startup neo-corporate
- Vibrant utilitarian
