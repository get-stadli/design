## Overview

A marketing/product surface with a split personality: monochrome chrome, earned-color content. The core visual thesis is that all color comes from content, and that color — like color on a chart mark — must be earned by a claim. Chrome is the resting state of every block. Across a whole document expect a mix of photography, color, and chrome; on any single viewport, expect mostly chrome with one loud moment.

## Colors

### Both Canvases Are One Deliverable

The system ships on two canvases at once — light (`canvas` `#ffffff`) and dark (`canvas` `#0a0a0a`) — and they are a single deliverable, not a base design with a dark recolor bolted on afterward. Like Reduced Motion, the dark canvas is a first-class state: either canvas must be a complete, correct, finished surface on its own, and a block is not "done" until it has been resolved and checked on both.

- **Chrome resolves automatically.** Every chrome value is a paired token — `colors` and `colors-dark` carry the full ramp (primary, ink, canvas, surfaces, hairlines) and the semantic triad in both modes. A block built strictly on tokens is already correct on both canvases with no extra work. This is why a literal hex where a chrome token exists is a light-mode-only bug: a hardcoded `#000` ink is invisible on `#0a0a0a`. Never hardcode a value the ramp already names.
- **Legibility is contrast-driven, so it crosses modes for free.** *Legibility stays chrome* already resolves type over color or imagery to pure black *or* white by contrast, and the logo inherits ink through `currentColor`; both are correct on either canvas by construction.
- **Earned color must be re-resolved per canvas — it is not free.** Extraction is run against the *active* canvas, because a single anchor hue does not yield the same swatch on `#ffffff` and on `#0a0a0a`. This is the one place dark mode takes real work; it is specified in Color Computation → Canvas-aware extraction.
- **Verify both renders.** A viewport ships only after both modes are checked: contrast holds, the one loud moment still reads as *loud* on dark (a saturated block is objectively louder on black — it must not tip into glare), imagery holds against the dark canvas per Photography & Illustration Geometry, and no chrome literal leaked through.

### Brand & Accent

There is no brand accent color. The only colors the brand owns outright are the chrome ramp — the blacks, whites, and grays in `colors`/`colors-dark` — plus the fixed semantic triad. Every other color on the page is *earned and extracted*, never assigned: an accent is whatever hue the on-screen content yields for that viewport, pulled by the extraction in Color Computation and spent under the per-viewport budget. This is deliberate. A fixed accent would make color a decoration the brand applies to content; here color is a property the content lends to the frame. Two documents in this system can look nothing alike at the level of hue and still be unmistakably the same system, because what they share is the chrome and the discipline, not a swatch.

Consequence for tooling: nothing hardcodes a "brand" hue for buttons, links, badges, focus rings, or charts — those are chrome. If a value must be resolved with no content to extract from, it stays neutral, never a guessed accent.

### Color Computation

Every content color is computed, not chosen. This is the machinery the rest of the document refers to as "the standard extraction" and "the standard rotations."

**Extraction.** For any block that shares a viewport with an image, take the image's dominant vibrant hue as the viewport's *anchor*. Convert to OKLCH and discard the source's lightness and chroma — keep only the hue angle. Re-render that hue at its own *cusp-relative* lightness and chroma: the most saturated, correctly-weighted version of that hue the display gamut allows, so each hue arrives at the weight it should carry rather than one borrowed from the photo. A yellow anchor therefore lands as a bright, light yellow; a blue anchor as a deep, saturated blue — no hue is ever forced to another hue's lightness. When a viewport has no image, the anchor is extracted from the most prominent content color already on screen; if there is none, the block stays chrome.

**Canvas-aware extraction.** The *hue angle* is a property of the content and is identical in both modes — extraction never rotates the wheel to suit the canvas, so a block's identity holds across light and dark. But the cusp-relative *lightness* is resolved against the **active canvas**, because "correctly weighted" means *correctly weighted for the surface it sits on*, and the same swatch cannot be right on both `#ffffff` and `#0a0a0a`. On the light canvas the hue takes the cusp-relative weight it always has. On the dark canvas the resolver targets equivalent *perceived* presence against `#0a0a0a` rather than reusing the light swatch: a hue that reads light on white (yellow) is pulled back from full brightness so it lands as *present, not glaring*, and a hue that reads deep on white (blue, violet) is lifted in lightness so it clears the canvas instead of sinking into it. Chroma stays at the cusp where the gamut allows; only lightness is re-weighted per canvas. The result is one anchor hue, two rendered swatches — the light one and its dark-canvas sibling — bound to the same role. This runs identically for the anchor and for every rotation below.

**Chart-mark floor.** Marks that encode data carry a minimum chroma floor so a hue never desaturates into something that reads as gray on a plot. The floor applies only to data geometry; chrome is unaffected.

**Canvas-contrast floor.** Every earned color — a filled block, a chart mark, a filled rail card — must clear a minimum lightness contrast against the *active* canvas so it still reads as a loud moment rather than dissolving into the surface. This is the dark-canvas failure mode a chroma floor alone does not catch: a hue can be legally saturated yet sit too close to `#0a0a0a` in lightness to register. When a hue cannot meet both its cusp-relative chroma and the canvas-contrast floor at once on a given canvas, contrast wins — lightness is adjusted until the floor is met, exactly as the chart-mark floor protects chroma. Semantic hues are exempt: they are already tokenized per mode (`colors` / `colors-dark`) so their contrast is pre-guaranteed on either canvas.

**Rotations.** Additional hues are never hand-picked — they are derived from the anchor by fixed moves on the OKLCH hue wheel, each then re-rendered at its own cusp-relative lightness and chroma *for the active canvas* (per Canvas-aware extraction). Two moves are sanctioned: analogous (±30–40°) when the story is variation within one family, and complementary (180°) when the story is opposition. Harmony is arithmetic, not taste. The rotation is computed once on the shared hue angle; each mode then renders it against its own canvas.

**Budgets.** Two budgets, both measured per viewport (what is visible at once), never per document:

- *Hue budget* — at most three hues on a viewport: one anchor plus derived siblings. Viewport Palette governs how the palette drifts across a long, scrolling document.
- *Block budget* — at most one loud, earned-color moment per viewport: one filled color block or one full-strength image carrying the section. Everything else on that viewport is chrome. This is the "mostly chrome, one loud moment" rule made countable, and it is the budget the Cards and Signature Components sections refer to. Loudness is canvas-relative: a saturated fill reads louder on `#0a0a0a` than on `#ffffff`, so the budget is re-checked on the dark render — one loud moment must still be exactly one, not one that has tipped into glare.

Roles are document-wide even though budgets are per viewport: once a hue is bound to a role — protagonist, counterpoint, supporting note — it keeps that meaning everywhere it reappears (see Viewport Palette).

### Surface

Canvas and chrome surfaces stay strictly neutral — near-white and barely-there grays on the light canvas, near-black and barely-there dark grays on the dark canvas — so they read as a quiet frame around the full-color content blocks on either mode. Surface tone differentiates cards and panels without shadow; saturated color never appears on the base canvas or chrome, in light mode or dark.

### Text

Ink ramps from pure black through muted and subtle grays to a near-invisible tertiary gray. Text is always neutral. 

### Semantic

The semantic triad — `semantic-success`, `semantic-warning`, `semantic-error` — is the single exception to extraction. It is fixed, not derived, precisely because its meaning must be stable: up/good, caution, down/bad have to read the same regardless of what imagery happens to be on screen. For that reason semantic hues are exempt from the extraction and rotation rules and do not count against the viewport hue budget.

Scope is strict and matches Data Visualization → Color Scope: a semantic color prints only on the figure itself, its sign or arrow glyph, or a small inline dot — never on a card, surface, badge, border, or container, which stay chrome. It is a whisper of hue on a number, not a state applied to a vessel. A `+12.4%` delta prints its digits and its arrow in success green on an otherwise chrome card; the card does not turn green.

One functional exception: an invalid form field may print `semantic-error` on its border and its helper text (see Inputs & Forms → States). This is a state a control reports, not a decoration a vessel wears — the field's background stays canvas, the label stays chrome, and no other border in the system ever takes a semantic or content color.

Light and dark modes carry their own semantic values (already tokenized) so contrast holds on either canvas.

## Typography

### Font Family

Inter is the only typeface in the system, used for every text role. There is no secondary display face and no monospace face — even code, numeric readouts, and tabular figures set in Inter (use its tabular-figures feature for alignment, never a monospaced font).

### Hierarchy

Display sizes map to hero and section headers, headline/card-title to component titles, body sizes to paragraph copy, and caption/eyebrow to metadata and labels.

### Principles

Larger sizes carry tighter (negative) letter-spacing for density; body and smaller sizes sit at 0 tracking for readability. Weight (400–600) does the work that a second typeface normally would.

600 is the working ceiling and the default for every display role; a single hero headline — the one loud typographic moment on a viewport — may go heavier (up to 700) when the story calls for it, but body and UI text never exceed 500. Italic is available for display and headline roles as editorial emphasis (a stressed word, a stance), never for body or UI copy; like weight, it is a tool of the one loud moment, not a texture spread across the page.

### Note on Font Substitutes

If Inter is unavailable, fall back to the system sans-serif stack (-apple-system, "Segoe UI", sans-serif). Preserve weight and size exactly; do not substitute a serif or display face.
