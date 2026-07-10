# Design.md — Editorial Monochrome

> Distilled from **DICE · Nike · Cosmos · Savee · Are.na · Runway · Krea · OpenAI**.
> One rule above all the others: **the pictures are the only color. Everything you build is monochrome.**

## Essence

An editorial system, not a dashboard. Big confident type, wide margins of quiet, and full-color imagery doing all the talking. The chrome — type, buttons, lines, fields — never takes a hue. It reads the same in ink-on-paper (light) and white-on-near-black (dark); the register is editorial, and the brand has a point of view.

## Principles

1. **Imagery is the only color.** If a color isn't coming from a photograph or a video, it doesn't appear.
2. **Chrome is monochrome — including buttons.** No accent, no colored state, no exception.
3. **Type carries the brand.** Hierarchy is size and tracking, never weight beyond 600, never a hue.
4. **Whitespace is structure.** Air is the layout. Crowding is the failure mode.
5. **One mark only: the arrow `→`.** No icons, no icon font.
6. **Editorial voice.** Curate, have an opinion, name things the way the room would.

## Color

Two canvases, one rule: chrome is grayscale; color enters only through media. There is **no accent token** — that absence is the system.

**Dark (primary)**

| token | hex | role |
|---|---|---|
| `--canvas` | `#0A0A0A` | page background / the quiet |
| `--surface` | `#141414` | raised panels |
| `--hairline` | `#242424` | dividers, borders |
| `--ink` | `#FFFFFF` | headlines, primary button fill |
| `--body` | `#E6E6E6` | body copy |
| `--muted` | `#8A8A8A` | captions, secondary |
| `--faint` | `#5A5A5A` | the annotation register |

**Light (parity)**

| token | hex |
|---|---|
| `--canvas` | `#FAFAF8` |
| `--surface` | `#FFFFFF` |
| `--hairline` | `#E6E4DE` |
| `--ink` | `#0A0A0A` |
| `--body` | `#232323` |
| `--muted` | `#6E6E6E` |
| `--faint` | `#9B9B9B` |

## Typography

One family — a grotesque (Inter, or an editorial neo-grotesk). No second face.

| step | size · line · tracking · weight | use |
|---|---|---|
| display | `clamp(48px, 6vw, 96px)` · 1.0 · -0.03em · 500 | hero lines, the loud moment |
| heading | `clamp(30px, 4vw, 56px)` · 1.08 · -0.02em · 500 | section + feature titles |
| title | `22px` · 1.3 · -0.01em · 600 | sub-headlines |
| body | `17–18px` · 1.55 · 0 · 400 | running text |
| caption | `13px` · 1.4 · 0 · 500 `--muted` | the editorial / annotation voice |
| label | `12px` · 1.3 · 0.08em · 600 uppercase | eyebrows only, a few words |

- The size jump *is* the hierarchy. If two levels look interchangeable, restore the jump — don't add weight.
- **Tabular numerals on every figure.** The number is the icon.
- **Type is never colored.** Emphasis is ink weight or italic, never a hue.

## Layout & space

- Content caps ~1280–1440px, centered, with an edge inset that never collapses to zero.
- Generous vertical rhythm — ~120–160px between bands on desktop, ~80px on mobile.
- The page reads as bands: **editorial text block → full-bleed media → back to quiet.** One idea per band, one scroll-stop.
- Image grids may be the entire composition (Cosmos / Savee); the chrome disappears around them.
- Top-left carries the lead.

## Imagery — the color source

- **Full-bleed, full-color, never tinted, toned, duotoned, or overlaid.** The photo or video is the brand's voice; leave it alone.
- Every image earns a quiet caption in the editorial register — who / what / where, tabular where numeric.
- A section without imagery is text-and-air, never a colored block standing in for one.

## Chrome — buttons, fields, lines

- **Buttons are 100% monochrome.**
  - *Primary:* solid `--ink` fill, opposite-tone label.
  - *Secondary:* `--hairline` outline, ink label.
  - *Ghost:* label + `→` only.
- Inputs: hairline border, ink text, monochrome focus ring. No colored validation states — pair a word with the change instead.
- Depth is surface contrast and hairlines. **No drop shadows, no gradients, no halos, no glow.**
- Radii: small (6–8px) or square.

## Motion

- Restrained and slow. Scroll reveals fade-and-rise. Hover is a quiet tone shift, never a color.
- **Media may move** (autoplay loops, Runway/Krea-style); the chrome stays still.

## Voice

- Editorial and human — name things the way the building would, not the database.
- Captions read like a knowledgeable friend, not a UI string.

## Don't

- Don't color the chrome — no accent buttons, links, tags, or states.
- Don't color type, ever — not a word, not a glyph, not a number.
- Don't tint or overlay images; their untouched color is the only color.
- Don't add icons; the arrow `→` is the only mark.
- Don't add a second typeface, or push weight past 600.
- Don't use shadows, gradients, or glows — use surface and hairline.
- Don't fill a missing image with a colored block; use type and air.
- Don't crowd. If a band argues two things, split it.

---

### Lineage

| Source | What it contributes |
|---|---|
| **DICE · Resident Advisor** | fan/scene voice, imagery as energy, monochrome chrome over a ticketing product |
| **Nike** | full-bleed photography, back-row type, monochrome UI |
| **Cosmos · Savee** | image grids, chrome that vanishes |
| **Are.na** | editorial restraint, text-forward calm |
| **Runway · Krea** | dark, media-as-hero |
| **OpenAI** | light, airy, editorial confidence |
