---
version: alpha
name: "Minimal Monochrome"
description: "A high-contrast design language with a split personality: the chrome — navigation, buttons, text, and canvas — stays strictly black, white, and gray, while every card, image, and section carries one full-bleed content block — either its own real photograph or one big, flat, full-strength color extracted from that image (the photo, the brand, the event) — with imagery earned by literal content and flat color doing structural and mood work. Color is bold and everywhere, but always as solid blocks — never gradients, tints, or UI decoration. Inter is used for every text role, buttons are pill-shaped, cards are flat with hairline borders, and the mood is quiet and technical in the frame, loud and saturated in the content."

colors:
  primary: "#000000"
  on-primary: "#ffffff"
  primary-hover: "#1a1a1a"
  primary-focus: "#000000"
  ink: "#000000"
  ink-muted: "#4d4d4d"
  ink-subtle: "#808080"
  ink-tertiary: "#b3b3b3"
  canvas: "#ffffff"
  surface-1: "#ffffff"
  surface-2: "#f7f7f7"
  surface-3: "#f0f0f0"
  hairline: "#ebebeb"
  hairline-strong: "#d4d4d4"
  semantic-success: "#000000"
  semantic-error: "#000000"
  semantic-warning: "#000000"

color-computation:
  space: "oklch"
  cusp-lift: 0.75            # fraction of the way from white (L=1) down to the hue's cusp lightness
  chroma-ratio: 0.85         # fraction of the hue's cusp chroma
  chart-mark-lightness-max: 0.85   # lightness ceiling for hues used as chart marks on light canvas
  gamut: "srgb"

colors-dark:
  primary: "#f5f5f5"
  on-primary: "#0a0a0a"
  primary-hover: "#e1e1e1"
  primary-focus: "#d1d1d1"
  ink: "#f5f5f5"
  ink-muted: "#cfcfcf"
  ink-subtle: "#a8a8a8"
  ink-tertiary: "#828282"
  canvas: "#0a0a0a"
  surface-1: "#0a0a0a"
  surface-2: "#0a0a0a"
  surface-3: "#0a0a0a"
  hairline: "#333333"
  hairline-strong: "#4d4d4d"
  semantic-success: "#d25656"
  semantic-error: "#d25656"
  semantic-warning: "#d25656"

typography:
  display-xl:
    fontFamily: Inter, sans-serif
    fontSize: 64px
    fontWeight: 600
    lineHeight: 68px
    letterSpacing: -2.56px
  display-lg:
    fontFamily: Inter, sans-serif
    fontSize: 40px
    fontWeight: 600
    lineHeight: 48px
    letterSpacing: -1.2px
  display-md:
    fontFamily: Inter, sans-serif
    fontSize: 32px
    fontWeight: 600
    lineHeight: 40px
    letterSpacing: -0.96px
  headline:
    fontFamily: Inter, sans-serif
    fontSize: 24px
    fontWeight: 600
    lineHeight: 32px
    letterSpacing: -0.48px
  card-title:
    fontFamily: Inter, sans-serif
    fontSize: 20px
    fontWeight: 600
    lineHeight: 28px
    letterSpacing: -0.4px
  subhead:
    fontFamily: Inter, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px
    letterSpacing: 0px
  body-lg:
    fontFamily: Inter, sans-serif
    fontSize: 20px
    fontWeight: 400
    lineHeight: 32px
    letterSpacing: 0px
  body:
    fontFamily: Inter, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
    letterSpacing: 0px
  body-sm:
    fontFamily: Inter, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 0px
  caption:
    fontFamily: Inter, sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
    letterSpacing: 0px
  button:
    fontFamily: Inter, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: 0px
  eyebrow:
    fontFamily: Inter, sans-serif
    fontSize: 12px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: 1px
  mono:
    fontFamily: Inter, ui-monospace, monospace
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 0px

rounded:
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 24px
  pill: 999px
  full: 50%

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 56px
  xxl: 96px
  section: 144px

layout:
  container: 1320px
  wide: 1558px
  narrow: 898px
  gutter: 32px
  columns: 12

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "10px 18px"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-strong}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "10px 18px"
  button-tertiary:
    backgroundColor: "transparent"
    textColor: "{colors.ink-muted}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "10px 18px"
  card:
    backgroundColor: "{colors.surface-1}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  feature-card:
    backgroundColor: "{colors.surface-2}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-strong}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.primary-focus}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: "{spacing.xxs} {spacing.sm}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    height: "64px"
    padding: "{spacing.sm} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  scrollbar:
    width: "8px"
    thumbColor: "{colors.hairline-strong}"
    thumbColorHover: "{colors.ink-subtle}"
    trackColor: "transparent"
    rounded: "{rounded.pill}"

assets:
  logos:
    primary: "https://placehold.co/220x60/ededed/737373?text=Logo"
    mark: "https://placehold.co/64x64/ededed/737373?text=Icon"
    wordmark: "https://placehold.co/220x56/ededed/737373?text=Wordmark"
    inverse: "https://placehold.co/220x60/1a1a1a/ededed?text=Logo+(inverse)"
  images:
    - name: hero
      url: "https://placehold.co/1200x600/f5f5f5/737373?text=Hero+image"
      alt: "Hero image"
    - name: feature
      url: "https://placehold.co/800x450/ededed/737373?text=Feature+image"
      alt: "Feature image"
---


## Overview

A marketing/product surface with a split personality: monochrome chrome, full-color content. The core visual thesis is that all color comes from content — each card, image, and section is filled edge-to-edge either by its own photograph or by one big flat block of full-strength color extracted from that image, the choice governed by intent — while the surrounding UI stays black, white, and gray. Two things to get right: the boundary (never let color leak into the chrome, and never dilute it into gradients or tints) and the split within content (show a real image when the literal subject carries the message; use a flat color block when the block is doing structural or mood work).

## Colors

### Brand & Accent

Every card, image, and section is a full-bleed content block, filled edge-to-edge either by its own photograph or by one big, flat, full-strength color extracted from that photograph (the photo, the brand, the event) — the choice governed by intent (see Signature Components). Whichever way a block is filled, its single characteristic hue is extracted the same way, so a color block and the image beside it read as siblings drawn from the same source. Color is bold and everywhere — but always as solid blocks, never as gradients, tints, or UI decoration. The chrome around the blocks — nav, buttons, text, canvas — stays strictly black, white, and gray. There is no fixed brand accent: the block color is chosen per instance from the content it frames. To pick it, extract the most dominant saturated hue from the block's own image — ignoring near-blacks, whites, and grays — then derive its lightness and chroma **cusp-relatively** in OKLCH (see Color Computation below). The hue itself passes through untouched, so a teal and a slightly greener teal produce two genuinely different blocks. What is fixed is not a lightness value but a *position relative to each hue's own gamut*: every hue is rendered at the same fraction of the maximum energy the sRGB gamut allows it, so a yellow carries the same force as a violet by being a bright, vivid yellow — never a darkened olive. Deriving lightness and chroma per hue (rather than locking one global value or snapping to presets) is what keeps every block reading as a sibling while letting each hue sit where it is actually beautiful. Every block therefore matches its content exactly while the palette stays controlled.

### Color Computation

Block colors are computed, never picked, by one deterministic rule. The sRGB gamut is lopsided in OKLCH: every hue has a **cusp** — the lightness at which it reaches its maximum chroma — and that cusp sits at very different heights (blue ≈ 0.45 L, red ≈ 0.63 L, yellow ≈ 0.97 L). A single locked lightness therefore strands most hues far from their cusp and strands yellow the farthest, which is how mud happens. Instead, for an extracted hue `h`:

1. Find the cusp of the sRGB gamut at hue `h` in OKLCH — the point `(L_cusp, C_cusp)` of maximum chroma. Use a color library's gamut math (culori, color.js) or a short binary search; the analytic approximation from the OKLCH gamut-clipping literature is equally acceptable.
2. Set lightness a fixed fraction of the way from white down to the cusp: `L = 1 − cusp-lift × (1 − L_cusp)`, with `cusp-lift = 0.75`.
3. Set chroma as a fixed fraction of what the hue can carry at full strength: `C = chroma-ratio × C_cusp`, with `chroma-ratio = 0.85`.
4. Clamp the result to the sRGB gamut by reducing chroma only (never shifting hue or lightness).

The two constants `cusp-lift` and `chroma-ratio` are the system's only color tunables; changing them retunes every block on every page at once. The output varies in lightness by design — yellows land light, blues land deep — and that variation is correct: it is what equal *perceptual* force looks like once the gamut is respected.

**Chart-mark floor.** When a computed color is used as a chart mark on a light canvas (a line, a point, a thin bar edge), apply a lightness ceiling of `chart-mark-lightness-max = 0.85` — `L = min(L, 0.85)` — reducing chroma as needed to stay in gamut. Large filled blocks can afford a near-white yellow; a hairline-thin line cannot. Full-bleed color blocks never apply the floor.

### Surface

Canvas and chrome surfaces stay strictly neutral — pure white and barely-there grays — so they read as a quiet frame around the full-color content blocks. Surface tone differentiates cards and panels without shadow; saturated color never appears on the base canvas or chrome.

### Text

Ink ramps from pure black through muted and subtle grays to a near-invisible tertiary gray. Text is always neutral — never tinted to match a color block. On a color block, text flips automatically between black and white by computing the block's luminance and switching at a fixed contrast threshold — never to a hue. Because block lightness now varies by hue by design — cusp-relative yellows come out light, blues come out deep — this flip must be computed per block rather than pre-verified by hand: expect black text on yellow and chartreuse blocks, white text on blue and violet ones, both produced by the same threshold.

### Semantic

Success, error, and warning states are all rendered in black — differentiated by copy and placement, not color (and not icons, which the system does not use), to preserve the monochrome chrome.

## Typography

### Font Family

Inter is the only typeface in the system, used for display, body, and mono roles alike. There is no secondary display face.

### Hierarchy

Display sizes map to hero and section headers, headline/card-title to component titles, body sizes to paragraph copy, and caption/eyebrow to metadata and labels.

### Principles

Larger sizes carry tighter (negative) letter-spacing for density; body and smaller sizes sit at 0 tracking for readability. Weight (400–600) does the work that a second typeface normally would.

### Note on Font Substitutes

If Inter is unavailable, fall back to the system sans-serif stack (-apple-system, "Segoe UI", sans-serif). Preserve weight and size exactly; do not substitute a serif or display face.

## Layout

### Spacing System

An 8px base rhythm (with a 4px half-step) governs all spacing. Micro tokens (2–16px) handle component-internal padding and stay tight; from `lg` upward the scale stretches deliberately — 32px card padding, 56/96px block gaps, and 144px section breaks — so macro whitespace clearly outweighs micro whitespace and layouts read airy rather than dense.

### Grid & Container

Content sits in a single centered column with generous side gutters (32px); no complex multi-column grid is used at this stage.

### Whitespace Philosophy

Airy and unhurried — whitespace is the primary tool for separating sections in the absence of color or heavy borders. When in doubt between two spacing tokens, choose the larger one; density is never the goal in this system.

## Elevation & Depth

The system is deliberately flat. No drop shadows; layering is signaled only by subtle surface-color shifts and hairline borders.

### Decorative Depth

None. No gradients, glows, blurs, or texture anywhere — this is the hard rule that keeps color reading as solid blocks. A content color is only ever a flat fill, never a gradient or a semi-transparent tint.

## Shapes

### Border Radius Scale

Buttons and badges use fully pilled corners; cards use large (12–16px) radii; inputs use medium (8px) radii. Nothing is sharp-cornered except hairline dividers.

### Photography & Illustration Geometry

Images are cropped to simple rectangular ratios with no rounding beyond the standard card radius. A photograph may fill a content block edge-to-edge as a full-bleed image (see Signature Components) — presented flat, at full strength, with no gradient overlay, tint, or duotone, since the same solid-fill law that governs color blocks governs imagery. When a full-bleed image needs overlaid text, the text rides a solid chrome panel or bar (black or white), or sits below the image — never on a gradient or semi-transparent scrim. Every image also yields the single extracted hue that its neighboring color blocks inherit, so imagery and color read as one family. No illustration style is defined yet.

## Components

### Buttons

Primary (solid black), secondary (outlined), and tertiary (text-only) variants, all pill-shaped except tertiary — always rendered in the monochrome chrome palette, never in a content color. Hover darkens fill slightly; focus uses a solid black ring; disabled drops opacity.

### Cards & Containers

Flat surfaces with hairline borders and generous 32px padding. A card may be filled edge-to-edge with one flat, full-strength color pulled from its content — unless it contains a chart, in which case it stays chrome and the color enters only through the data marks; when it is, its border and any chrome inside stay neutral. Feature cards use a slightly larger radius and a faint surface-2 tint to differentiate standard cards. Scrollbars are chrome: styled as thin hairline pills — an 8px hairline-strong thumb with a pill radius on a transparent track, no arrows or buttons — darkening to ink-subtle on hover.

### Inputs & Forms

Fields are white with a hairline-strong border, switching to solid black on focus. Labels use caption typography in ink-muted. Inputs are chrome and never take a content color.

### Navigation


### Signature Components

Components exist to tell the story — build whatever the story needs, as long as it stays in sync with the chrome and the rest of the page. The story comes first, always.

The signature pattern is the full-bleed content block: content pushed edge-to-edge, loud and saturated, held in a quiet monochrome frame. Nothing is contained for containment's sake — imagery and color want to spill, stretch, and fill. A block is either a photograph at full strength or one flat, unapologetic color drawn from that world; both are treated as material, not decoration. Let the image lead whenever there's something real to show, and let color carry the energy everywhere else. Use components to tell a story — whatever the story needs, invent it, bend it, build it — as long as it stays in sync with the chrome and the rest of the page. The story comes first. The chrome stays silent so the content can be loud.


Two rules keep the forms coherent:

- **Shared bloodline.** Any color block sharing a viewport with an image pulls its hue from that image by the standard extraction, so a viewport mixing a photo and color tiles still reads as one palette. Color blocks are derived from the imagery on screen, never hand-picked against it.
- **Legibility stays chrome.** Text over an image sits on a solid black or white chrome panel or bar, or below the image — never on a gradient or semi-transparent scrim, which the no-gradients / no-tints law forbids. The frame around and over imagery is chrome, exactly like the frame around a color block.

## Data Visualization

### Color Scope

A chart is not a special case — it is a block, and it obeys the one-block-one-color law. A chart may carry one hue, extracted from its own content the same way any block is, rendered at its cusp-relative lightness and chroma in OKLCH with the chart-mark lightness floor applied (see Color Computation). That hue is spent only on the marks that encode a value — bars, line, points, filled area. Everything structural stays chrome: the plot background is canvas or surface, gridlines are hairline, axis ticks and labels are ink-muted. Color lives strictly on the geometry that carries data and leaks nowhere else — the same discipline that keeps content color out of the nav.

### The Chart Container

Dataviz cards are never colored. The full-bleed color block — a card filled edge-to-edge with its content color — does not apply to charts: a chart's card, panel, or section stays chrome (canvas, surface-1, or surface-2 with a hairline border), and the hue enters only through the marks inside the plot. In a chart, the data is the content, so the data takes the color; the vessel never does. A colored card behind a chart would make the container compete with the marks it exists to frame — the one place in the system where the full-bleed pattern and legibility pull in opposite directions, resolved in legibility's favor.

### Gray by Default

Gray is the resting state of data. An all-gray chart — ink marks on a neutral plot — is a complete chart, not an unfinished one; ink-weight, size, and a large printed value do the structural work. Color must be earned by a claim: hue appears only when the chart has something to say — a single point to emphasize (a peak, a problem, a winner, a "this one") or, per Multiple Series, a comparison between named categories that is itself the claim. No claim, no color. This is why a page of charts never drifts toward a rainbow: most marks were never candidates for color at all.

### Direct Labeling

Values are printed, not looked up. Key figures sit directly on or beside the marks at display or headline sizes; series are named by direct labels at the mark, and annotations point at the moment they describe. There are no legends — a legend is a lookup table, and the system labels everything with text in place, the same rule that bans icons.

### Multiple Series

There is no category palette, but color may encode category when the comparison *is* the claim. The default remains emphasis: one hue marks the single series that carries the message — the focus, the latest, the total, the "you are here" — and every other series drops into the ink ramp (ink-muted → ink-subtle → ink-tertiary), separated by weight and direct labels rather than hue. A five-line chart is one saturated line and four gray ones, not five hues competing.

The exception is the chart whose entire point is the contest between named categories — East vs. West, this vs. that, the parts of a whole — where no series is background because the comparison itself is the claim. There, two or three hues may each encode a named category, but only hues the system would have produced anyway: derived from the viewport's anchor by the standard rotations, each then rendered at its own cusp-relative lightness and chroma (with the chart-mark floor), counted against the same three-hue viewport budget, and bound to their roles document-wide like any other character. Each series is direct-labeled in its own hue at the mark — the label is the legend, so the no-legend rule holds. Everything that is not party to the claim still falls to the ink ramp; categorical color is a license for the contestants, never for the crowd. If a chart needs more hues than the budget allows, the claim is too diffuse — split the chart or collapse the categories, don't grow the palette.

### Sequential Scales

Ordered or quantitative encodings — a heatmap, a choropleth, a magnitude scale — may step the single hue through lightness only: fixed hue, varying lightness, never a second hue. The ramp is anchored at the hue's cusp-relative color and runs toward near-white on the light end (and, if the data demands more range, toward a darker step of the same hue on the deep end), so a yellow ramp lives in the light half of the scale where yellow is vivid instead of forcing it down into olive. This is the one place a ramp is legitimate, because here the gradient *is* the data rather than decoration. One exception: a diverging scale — data that splits around a meaningful midpoint, above vs. below average — may run the anchor hue on one side and its complement on the other, meeting at a neutral center. That is not a second color entering the system; it is the anchor and its computed opponent telling an opposition story. Anything beyond one hue and its complement turns the ramp into a rainbow, which the system does not permit.

### Viewport Palette

The color budget is measured per viewport — what is visible at once — not per chart and not per document. A viewport carries at most three hues: one anchor, extracted from its content like any block, plus extra hues derived from it, never hand-picked. Extra hues come by fixed rotation on the OKLCH hue wheel, each then rendered at its own cusp-relative lightness and chroma, so harmony is arithmetic rather than taste: the rotation moves hue alone, and the gamut supplies each hue's correct weight. A rotation that lands in the yellow band therefore produces a bright, light yellow — a legitimate sibling — never an olive, because no hue is ever forced to another hue's lightness. Two relationships are sanctioned — analogous (±30–40°) when the story is variation within one family, and complementary (180°) when the story is opposition; one opponent, never a third party.

A long, scrolling surface may therefore hold more than three hues in total, but adjacent viewports must share blood: each new viewport's palette is derived by continuing the same rotation from a hue already on screen, so scrolling reads as one palette slowly turning through the wheel — analogous drift of ±30–40° per viewport — never as a palette swap. The drift is a storytelling device: sections feel different while provably belonging to one family. A hard 180° flip is permitted once per document, and only at a genuine narrative turn — results to problems, before to after — because a complement is a plot twist, not a transition.

Roles are document-wide even though budgets are not. Every hue is a character bound to a named role — the protagonist (the focus, the "you are here"), the counterpoint (the comparison, the opposing force), at most one supporting note per viewport — and once bound, it keeps that meaning on every viewport it reappears in; no other hue may take over that role downpage. New viewports may introduce new characters, never re-cast old ones. A color that changes meaning between charts is worse than a rainbow. Gray remains the resting state of everything that is not a character, and a viewport of all-gray charts with one large printed number per panel is a finished viewport.

## Do's and Don'ts

### Do

- Fill each card, image, and section as a full-bleed content block — either its own real photograph or one flat, full-strength color extracted from that image — choosing between them by intent: imagery when the literal subject is the message, flat color when the block does structural or mood work.
- When a viewport mixes imagery and color blocks, derive the color blocks' hue from the images on screen, so the whole viewport reads as one palette.
- Set text over imagery on a solid black or white chrome panel (or below the image), never on a gradient or translucent scrim.
- Compute every block and mark color cusp-relatively: extract the hue, derive lightness and chroma from that hue's sRGB cusp using the `cusp-lift` and `chroma-ratio` constants, and apply the chart-mark lightness floor when the color is a mark rather than a block.
- Keep all chrome — nav, buttons, text, canvas — strictly black, white, and gray.
- Style scrollbars as thin hairline pills.
- Use weight, size, and spacing (not color) to structure the chrome.
- In charts, default to gray and print values directly on the marks; spend hue only on what carries the claim — the one emphasized point, or the named categories when the comparison itself is the claim — and keep the plot background, gridlines, and axes chrome.
- Err toward the larger spacing token; macro whitespace should always dominate micro whitespace.

### Don't

- Don't use icons anywhere — no icon sets, inline glyphs, or pictograms; label everything with text instead.
- Don't use gradients, tints, or semi-transparent color — content blocks are solid fills only.
- Don't overlay a full-bleed image with a gradient scrim, tint, or duotone to force text legibility — use a solid chrome panel instead; the no-gradients / no-tints law applies to imagery exactly as it applies to color blocks.
- Don't reach for a real photograph when a flat color block would do — imagery is earned by literal content, not a default; an unearned photo is the noise the color-block system exists to avoid.
- Don't lock one global lightness or chroma across hues, and don't hand-adjust an individual block to compensate — the yellow band turning to olive is the symptom of the first, and per-instance taste is the disease the system exists to prevent. Both are solved by the cusp-relative rule; if a computed color looks wrong, retune `cusp-lift` or `chroma-ratio` for the whole document, never one block.
- Don't exceed the viewport's color budget — one anchor hue, at most three visible at once, all derived by analogous or complementary rotation; this cap holds even when hues encode categories in a comparison chart. On scroll, drift the palette, never swap it, and never re-cast a hue's role downpage. Never use legends — in categorical charts, the direct label in the series' own hue is the legend.
- Don't fill a dataviz card, panel, or section with a content color — chart containers are always chrome; the hue lives only on the marks.
- Don't let a content color leak into the nav, buttons, or text.
- Don't add shadows or decorative texture.

## Responsive Behavior

### Breakpoints

Three intents: mobile (<640px, single column), tablet (640–1024px, two columns), desktop (>1024px, the full 12-column grid at the 1120px container).

### Touch Targets

Interactive targets are at least 44×44px, with a minimum of 8px spacing between adjacent controls.

### Collapsing Strategy

Multi-column grids stack to one column, nav links collapse to a menu, and side-by-side media and text reflow to stacked. The primary CTA never hides. On mobile, section breaks may step down the spacing scale (e.g. 144px → 96px).

### Image Behavior

Images scale fluidly within their rounded frames, keeping their crop ratio; heroes may switch to a tighter crop on mobile. Logos never stretch.

## Iteration Guide

To extend this system, keep all chrome tokens within the black/white/gray ramp — content-block color is chosen per instance from the content, not tokenized — and reuse the 8px spacing scale for any new component. The only color tunables are the three constants in `color-computation` (`cusp-lift`, `chroma-ratio`, `chart-mark-lightness-max`); retuning them re-renders every block and mark document-wide, which is the only sanctioned way to adjust how color feels. Revisit the split (monochrome chrome vs. full-color content blocks) before introducing any new colored surface.

## Known Gaps

No dark-mode surface set is defined (note that the cusp-relative constants are tuned for light canvas; a dark theme would need its own `cusp-lift`, likely lower). Full-bleed photography is now specified, but no illustration style is — illustration would need its own geometry plus the same solid-fill and chrome-legibility rules before it enters the system. Iconography is intentionally omitted — the system uses no icons at all. Responsive breakpoints and touch-target rules are not yet defined. Cusp computation assumes a color library with OKLCH gamut math (culori, color.js) or an equivalent implementation of the analytic cusp approximation.
