---
version: alpha
name: "Minimal Monochrome"
description: "A high-contrast design language with a split personality: the chrome — navigation, buttons, text, and canvas — stays strictly black, white, and gray, while every card, image, and section carries one big, flat, full-strength color pulled from its own content (the photo, the brand, the event). Color is bold and everywhere, but always as solid blocks — never gradients, tints, or UI decoration. Inter is used for every text role, buttons are pill-shaped, cards are flat with hairline borders, and the mood is quiet and technical in the frame, loud and saturated in the content."

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

colors-dark:
  primary: "#f5f5f5"
  on-primary: "#0a0a0a"
  primary-hover: "#e1e1e1"
  primary-focus: "#d1d1d1"
  ink: "#f5f5f5"
  ink-muted: "#cfcfcf"
  ink-subtle: "#a8a8a8"
  ink-tertiary: "#828282"
  canvas: "#141414"
  surface-1: "#141414"
  surface-2: "#141414"
  surface-3: "#141414"
  hairline: "#333333"
  hairline-strong: "#4d4d4d"
  semantic-success: "#d25656"
  semantic-error: "#d25656"
  semantic-warning: "#d25656"

typography:
  display-xl:
    fontFamily: Inter, sans-serif
    fontSize: 48px
    fontWeight: 600
    lineHeight: 48px
    letterSpacing: -2.4px
  display-lg:
    fontFamily: Inter, sans-serif
    fontSize: 32px
    fontWeight: 600
    lineHeight: 40px
    letterSpacing: -1.28px
  display-md:
    fontFamily: Inter, sans-serif
    fontSize: 24px
    fontWeight: 600
    lineHeight: 32px
    letterSpacing: -0.6px
  headline:
    fontFamily: Inter, sans-serif
    fontSize: 20px
    fontWeight: 600
    lineHeight: 28px
    letterSpacing: -0.4px
  card-title:
    fontFamily: Inter, sans-serif
    fontSize: 18px
    fontWeight: 600
    lineHeight: 24px
    letterSpacing: -0.2px
  subhead:
    fontFamily: Inter, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px
    letterSpacing: 0px
  body-lg:
    fontFamily: Inter, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px
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
    fontSize: 13px
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
  lg: 24px
  xl: 40px
  xxl: 64px
  section: 96px

layout:
  container: 1320px
  wide: 1558px
  narrow: 898px
  gutter: 24px
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

A marketing/product surface with a split personality: monochrome chrome, full-color content. The core visual thesis is that color comes entirely from content — each card, image, and section takes one big flat block of full-strength color drawn from what it contains — while the surrounding UI stays black, white, and gray. The one thing to get right is the boundary: never let color leak into the chrome, and never dilute it into gradients or tints.

## Colors

### Brand & Accent

Every card, image, and section takes one big, flat, full-strength color pulled from its own content (the photo, the brand, the event). Color is bold and everywhere — but always as solid blocks, never as gradients, tints, or UI decoration. The chrome around the blocks — nav, buttons, text, canvas — stays strictly black, white, and gray. There is no fixed brand accent: the block color is chosen per instance from the content it frames. To pick it, extract the most dominant saturated hue from the block's own image — ignoring near-blacks, whites, and grays — then snap that hue to the nearest of eight preset, brand-safe tones (blue, magenta, orange, green, violet, red, teal, yellow) held at a fixed saturation and lightness. Every block therefore matches its content while the palette stays controlled.

### Surface

Canvas and chrome surfaces stay strictly neutral — pure white and barely-there grays — so they read as a quiet frame around the full-color content blocks. Surface tone differentiates cards and panels without shadow; saturated color never appears on the base canvas or chrome.

### Text

Ink ramps from pure black through muted and subtle grays to a near-invisible tertiary gray. Text is always neutral — never tinted to match a color block. On a dark block it may flip to white for legibility, but never to a hue.

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

An 8px base rhythm (with a 4px half-step) governs all spacing, from tight component padding up to 96px section breaks.

### Grid & Container

Content sits in a single centered column with generous side gutters; no complex multi-column grid is used at this stage.

### Whitespace Philosophy

Airy and unhurried — whitespace is the primary tool for separating sections in the absence of color or heavy borders.

## Elevation & Depth

The system is deliberately flat. No drop shadows; layering is signaled only by subtle surface-color shifts and hairline borders.

### Decorative Depth

None. No gradients, glows, blurs, or texture anywhere — this is the hard rule that keeps color reading as solid blocks. A content color is only ever a flat fill, never a gradient or a semi-transparent tint.

## Shapes

### Border Radius Scale

Buttons and badges use fully pilled corners; cards use large (12–16px) radii; inputs use medium (8px) radii. Nothing is sharp-cornered except hairline dividers.

### Photography & Illustration Geometry

Images are cropped to simple rectangular ratios with no rounding beyond the standard card radius; no illustration style is defined yet.

## Components

### Buttons

Primary (solid black), secondary (outlined), and tertiary (text-only) variants, all pill-shaped except tertiary — always rendered in the monochrome chrome palette, never in a content color. Hover darkens fill slightly; focus uses a solid black ring; disabled drops opacity.

### Cards & Containers

Flat surfaces with hairline borders and generous padding. A card may be filled edge-to-edge with one flat, full-strength color pulled from its content; when it is, its border and any chrome inside stay neutral. Feature cards use a slightly larger radius and a faint surface-2 tint to differentiate standard cards.

### Inputs & Forms

Fields are white with a hairline-strong border, switching to solid black on focus. Labels use caption typography in ink-muted. Inputs are chrome and never take a content color.

### Navigation

A simple top nav on a white background with a hairline bottom border; footer uses surface-1 with muted body-sm text. Navigation is chrome, so it stays strictly black/white/gray — content color blocks never bleed into the nav or footer.

### Signature Components

The signature pattern is the full-bleed color block: a card, image, or section filled edge-to-edge with a single flat, content-derived color, framed entirely by monochrome chrome.

## Do's and Don'ts

### Do

- Give each card, image, and section one flat, full-strength color pulled from its own content.
- Keep all chrome — nav, buttons, text, canvas — strictly black, white, and gray.
- Use weight, size, and spacing (not color) to structure the chrome.

### Don't

- Don't use icons anywhere — no icon sets, inline glyphs, or pictograms; label everything with text instead.
- Don't use gradients, tints, or semi-transparent color — content blocks are solid fills only.
- Don't let a content color leak into the nav, buttons, or text.
- Don't add shadows or decorative texture.

## Responsive Behavior

### Breakpoints

Three intents: mobile (<640px, single column), tablet (640–1024px, two columns), desktop (>1024px, the full 12-column grid at the 1120px container).

### Touch Targets

Interactive targets are at least 44×44px, with a minimum of 8px spacing between adjacent controls.

### Collapsing Strategy

Multi-column grids stack to one column, nav links collapse to a menu, and side-by-side media and text reflow to stacked. The primary CTA never hides.

### Image Behavior

Images scale fluidly within their rounded frames, keeping their crop ratio; heroes may switch to a tighter crop on mobile. Logos never stretch.

## Iteration Guide

To extend this system, keep all chrome tokens within the black/white/gray ramp — content-block color is chosen per instance from the content, not tokenized — and reuse the 8px spacing scale for any new component. Revisit the split (monochrome chrome vs. full-color content blocks) before introducing any new colored surface.

## Known Gaps

No dark-mode surface set is defined. No illustration style is specified; iconography is intentionally omitted — the system uses no icons at all. Responsive breakpoints and touch-target rules are not yet defined.
