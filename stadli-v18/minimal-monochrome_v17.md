---
version: alpha
name: "Minimal Monochrome"
description: "A high-contrast design language where design exist to tell the story — made to build whatever the story needs, as long as it stays in sync with the chrome and the rest of the page. The story comes first, always. The chrome — navigation, buttons, text, and canvas — stays strictly black, white, and gray, and chrome is also the resting state of every block: a plain surface with a hairline border is a finished block, not an unstyled one. Color is bold where it appears but rare. Imagery is always raw: full strength, no filter, no scrim. Inter is used for every text role, buttons are pill-shaped, cards are flat with hairline borders, and the mood is quiet and technical in the frame, loud and saturated at the few moments that earn it."

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
  semantic-success: "#15803d"
  semantic-error: "#b91c1c"
  semantic-warning: "#b45309"

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
  surface-1: "#111111"
  surface-2: "#171717"
  surface-3: "#1e1e1e"
  hairline: "#262626"
  hairline-strong: "#404040"
  semantic-success: "#4ade80"
  semantic-error: "#f87171"
  semantic-warning: "#fbbf24"

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
  container: 1440px
  wide: full-bleed.
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
    - name: banner
      url: "https://placehold.co/1920x720/f0f0f0/737373?text=Viewport-bleed+image"
      alt: "Full viewport-width banner image"
---


## Overview

A marketing/product surface with a split personality: monochrome chrome, earned-color content. The core visual thesis is that all color comes from content, and that color — like color on a chart mark — must be earned by a claim. Chrome is the resting state of every block. Across a whole document expect a mix of photography, color, and chrome; on any single viewport, expect mostly chrome with one loud moment.

## Colors

### Brand & Accent

TBD 

### Color Computation

TBD 

### Surface

Canvas and chrome surfaces stay strictly neutral — pure white and barely-there grays — so they read as a quiet frame around the full-color content blocks. Surface tone differentiates cards and panels without shadow; saturated color never appears on the base canvas or chrome.

### Text

Ink ramps from pure black through muted and subtle grays to a near-invisible tertiary gray. Text is always neutral. 

### Semantic

TBD 

## Typography

### Font Family

Inter is the only typeface in the system, used for every text role. There is no secondary display face and no monospace face — even code, numeric readouts, and tabular figures set in Inter (use its tabular-figures feature for alignment, never a monospaced font).

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

Content sits in a centered 1440px container on a 12-column grid with 32px gutters and a 898px `narrow` variant for long-form reading. The grid is a positioning tool.

**Viewport bleed.** The container constrains text and chrome — never content blocks. Any full-bleed content block, image or flat color, may break out of the container and run edge-to-edge of the viewport: a hero photograph, a section-scale image, a storytelling band marking a chapter. The 1558px `wide` variant remains for blocks that should feel large but still framed; full viewport width is for blocks that should feel like the page itself changed material.

### Whitespace Philosophy

Airy and unhurried — whitespace is the primary tool for separating sections in the absence of color or heavy borders. When in doubt between two spacing tokens, choose the larger one; density is never the goal in this system.

## Elevation & Depth

The system is deliberately flat. No drop shadows; layering is signaled only by subtle surface-color shifts and hairline borders.

### Decorative Depth

None. No gradients, or glows — this is the hard rule that keeps color reading as solid blocks. A content color is only ever a flat fill, never a gradient or a semi-transparent tint. Blur can be used if needed.

## Shapes

### Border Radius Scale

Buttons and badges use fully pilled corners; cards use large (12–16px) radii; inputs use medium (8px) radii. Nothing is sharp-cornered except hairline dividers.

### Photography & Illustration Geometry

Cinematic, documentary, storytelling. Photography is always presented raw: flat, at full strength, in its own color, with no gradient overlay, tint, duotone, filter, or house treatment of any kind. The system's style lives in how images are framed and cropped, never in what is done to their pixels. When a full-bleed image needs overlaid text, the text rides over a very subtle seamless chrome semi-opacity overlay or subtle blur. Imagery and color read as one family, so surrounding blocks can be filled with colors if that fits the story.

## Components

### Buttons

Primary (solid black), secondary (outlined), and tertiary (text-only) variants, all pill-shaped except tertiary — always rendered in the monochrome chrome palette, never in a content color. Hover darkens fill slightly; focus uses a solid black ring; disabled drops opacity.

### Cards & Containers

Flat surfaces with hairline borders and generous 32px padding — and this chrome state is the default and the norm: most cards on any page are surface-1 or surface-2 with a hairline, full stop. A card may be filled edge-to-edge with one flat, full-strength color pulled from its content only when it carries a narrative moment that earns the fill (see Signature Components), counted against the per-viewport block budget — and never when it contains a chart, in which case it stays chrome and the color enters only through the data marks. When a card is filled, its border and any chrome inside stay neutral. Feature cards use a slightly larger radius and a faint surface-2 tint to differentiate standard cards. Scrollbars are chrome: styled as thin hairline pills — an 8px hairline-strong thumb with a pill radius on a transparent track, no arrows or buttons — darkening to ink-subtle on hover.

### Inputs & Forms

Fields are white with a hairline-strong border, switching to solid black on focus. Labels use caption typography in ink-muted. Inputs are chrome and never take a content color.

### Navigation

The top nav is pure chrome. Sometime overlay. Links are button typography in ink-muted, darkening to ink on hover and sitting at full ink when active — state is carried by weight and tone, never by color or underline decoration. 

### Signature Components

Components exist to tell the story — build whatever the story needs, as long as it stays in sync with the chrome and the rest of the page. The story comes first, always.

The story comes first. The chrome stays silent so the few loud moments can actually be heard.


Two rules keep the forms coherent:

- **Shared bloodline.** Any color block sharing a viewport with an image pulls its hue from that image by the standard extraction, so a viewport mixing a photo and color tiles still reads as one palette. Color blocks are derived from the imagery on screen, never hand-picked against it.
- **Legibility stays chrome.** 

## Brand Assets

### Logo

The logo is provided as inline SVG below and must be used **verbatim** — copy this exact markup into the page; never redraw, retrace, approximate, or substitute it with text, a placeholder, or a generated mark. It is a chrome element: it renders only in ink (black on light surfaces, near-white on dark), never in a content color, never with gradients, tints, shadows, or effects — the same laws that govern all chrome.

The canonical markup uses `fill="currentColor"`, so it inherits the correct ink automatically from its parent (`color: var(--ink)` on light chrome, the dark-mode ink on dark chrome, and pure `#fff` or `#000` when it sits on a chrome panel over imagery). One markup, every surface:

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1375 405" role="img" aria-label="Logo" fill="currentColor"><g><path d="M1051.69,394.57h-54.65l-2.02-2.02v-33.06c-42.56,49.75-117.24,53.96-170.74,18.93-78.29-51.26-81.53-180.87-9.37-238.84,49.67-39.91,129.04-42.78,173.35,6.71l1.36-141.69h61.4l.67,389.98ZM893.51,170.95c-87.55,10.51-90.94,159.71,6.53,169.48,117.59,11.79,121.12-184.81-6.53-169.48Z"/><path d="M679.26,356.79c-42.34,48.71-111.23,58.07-166.88,25.87-89.21-51.62-91.14-196.86-4.39-251.79,46.28-29.3,111.66-29.62,155.09,5.28l16.18,16.88v-37.78h56.68v279.33h-56.68v-37.78ZM585.92,169.55c-101.03,2.6-103.13,162.67-4.47,171.03,117.35,9.94,120.05-174,4.47-171.03Z"/><path d="M204.27,194.86c-10.91-35.78-68.12-38.63-96.73-27.23-25.2,10.04-27.56,30.88-.79,41.76,49.3,20.02,153.48,18.37,160.77,87.52,5.15,48.85-27.44,82.07-72.42,93.22-72.52,17.97-169.96-6.31-181.1-91.36h60.72c5.34,28.33,32.46,39.88,58.72,41.81,19.34,1.43,66.25,1.8,71.57-22.84,4.2-19.43-14.07-24.71-28.79-29.38-60.82-19.3-170.98-21.31-146.2-115.93,22.64-86.43,198.37-88.08,229.59,2.85.89,2.58,6.66,19.59,2.01,19.59h-57.35Z"/><path d="M351.35,24.84v90.41h86.36v59.37h-86.36l1.3,128.92c.82,14.68,10.18,28.78,25.33,31.34,7.14,1.21,21.35,1.42,29.31,1.73,11,.42,22.12-.42,33.12-.06v58.02h-65.45c-42.34,0-83.34-40.72-84.32-83.01l-1.33-244.19c.29-2.95,2.91-4.23,4.93-5.87,11.48-9.31,39.68-28.28,52.67-35.05,1.51-.79,2.36-2.11,4.44-1.63Z"/><rect x="1094.87" y="4.6" width="63.42" height="391.33"/><rect x="1200.13" y="115.25" width="60.72" height="280.68"/><path d="M1225.47,3.63c46.2-4.43,58.77,59.87,17.22,73.89-55.1,18.6-70.9-68.74-17.22-73.89Z"/></g><path d="M1328.45,398.23c-4.33,0-8.38-.78-12.15-2.35s-7.06-3.76-9.88-6.59c-2.82-2.82-5.02-6.1-6.59-9.84-1.57-3.73-2.35-7.77-2.35-12.1s.78-8.38,2.35-12.15c1.57-3.76,3.76-7.06,6.59-9.88,2.82-2.82,6.12-5.02,9.88-6.59,3.76-1.57,7.81-2.35,12.15-2.35s8.37.78,12.1,2.35c3.73,1.57,7.01,3.76,9.84,6.59,2.82,2.82,5.02,6.12,6.59,9.88s2.35,7.81,2.35,12.15-.78,8.37-2.35,12.1c-1.57,3.74-3.76,7.01-6.59,9.84-2.82,2.82-6.1,5.02-9.84,6.59-3.74,1.57-7.77,2.35-12.1,2.35ZM1328.45,392.16c4.73,0,8.92-1.05,12.57-3.17,3.65-2.11,6.51-5.05,8.6-8.81,2.08-3.76,3.12-8.04,3.12-12.83s-1.06-9.15-3.17-12.92c-2.11-3.76-4.99-6.7-8.64-8.81-3.65-2.11-7.81-3.17-12.49-3.17s-8.85,1.06-12.53,3.17c-3.68,2.11-6.57,5.05-8.68,8.81-2.11,3.76-3.17,8.07-3.17,12.92s1.05,9.07,3.17,12.83c2.11,3.76,5,6.7,8.68,8.81,3.68,2.11,7.85,3.17,12.53,3.17ZM1328.36,384.29c-3.14,0-5.9-.71-8.3-2.14-2.4-1.42-4.26-3.41-5.6-5.94-1.34-2.54-2.01-5.49-2.01-8.85s.67-6.31,2.01-8.85c1.34-2.54,3.19-4.52,5.56-5.94,2.37-1.42,5.12-2.14,8.25-2.14,2.74,0,5.35.73,7.83,2.18s4.35,3.41,5.6,5.86l1.11,2.22-5.73,2.22-1.11-1.8c-.74-1.31-1.83-2.38-3.25-3.21-1.43-.83-2.91-1.24-4.45-1.24-2.79,0-5.06.98-6.8,2.95-1.74,1.97-2.61,4.55-2.61,7.74s.88,5.7,2.65,7.7c1.77,2,4.05,2.99,6.84,2.99,1.54,0,3.04-.48,4.49-1.45,1.45-.97,2.61-2.19,3.46-3.68l.77-1.54,5.99,2.14-1.03,2.05c-1.31,2.62-3.22,4.73-5.73,6.33-2.51,1.6-5.16,2.39-7.96,2.39Z"/></svg>
```

**Sizing.** The viewBox is 1375×405 (aspect ratio ≈ 3.4:1). Scale by height only — 24–28px tall in the top nav, up to 36px in the footer — with width auto; logos never stretch, crop, or rotate. Maintain clear space of at least the logo's height on all sides.

**Fixed-color fallbacks.** If `currentColor` is unavailable in a given context, use `fill="#111"` on light surfaces and `fill="#fff"` on dark surfaces — never any other value.

## Data Visualization

### Color Scope

A chart is not a special case — it is a block, and it obeys a one-block-one-color law. A chart may carry one hue, extracted from its own content the same way any block is. The hue is spent only on the marks that encode a value — bars, line, points, filled area. Everything structural stays chrome: the plot background is canvas or surface, gridlines are hairline, axis ticks and labels are ink-muted. Color lives strictly on the geometry that carries data and leaks nowhere else — the same discipline that keeps content color out of the nav.

**Directional status is the one licensed exception to the chrome law:** a metric's delta or status may print in `semantic-success` (up/good), `semantic-warning` (caution), or `semantic-error` (down/bad) — applied only to the figure, its sign or arrow glyph, or a small inline dot, never to the card, surface, badge, or container, which stay chrome. This is a whisper of hue on the number itself, the same "hue on the marks, the vessel stays chrome" logic that governs charts.

### The Chart Container

Dataviz cards are never colored. A chart's card, panel, or section stays chrome (canvas, surface-1, or surface-2 with a hairline border), and the hue enters only through the marks inside the plot. In a chart, the data is the content, so the data takes the color; the vessel never does. A colored card behind a chart would make the container compete with the marks it exists to frame — the one place in the system where the full-bleed pattern and legibility pull in opposite directions, resolved in legibility's favor.

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

TBD

## Responsive Behavior

### Breakpoints

TBD

### Touch Targets

TBD

### Collapsing Strategy

Multi-column grids stack to one column, nav links collapse to a menu, and side-by-side media and text reflow to stacked. The primary CTA never hides. On mobile, section breaks may step down the spacing scale (e.g. 144px → 96px).

### Image Behavior

Images scale fluidly within their rounded frames, keeping their crop ratio; heroes may switch to a tighter crop on mobile. Viewport-bleed blocks remain edge-to-edge at every breakpoint — they never fall back into the container on small screens. Logos never stretch.

## Iteration Guide

To extend this system, keep all chrome tokens within the black/white/gray ramp — usage of color is chosen per instance from the content, not tokenized — and reuse the 8px spacing scale for any new component. 

## Known Gaps

TBD

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