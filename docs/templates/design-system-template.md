---
# ─────────────────────────────────────────────────────────────
# DESIGN TOKENS (machine-readable)
# Fill every <PLACEHOLDER>. Delete optional blocks you don't use.
# Component props reference other tokens with {group.key} syntax,
# e.g. "{colors.primary}", "{rounded.pill}", "{spacing.md}".
# ─────────────────────────────────────────────────────────────
version: alpha
name: <Brand-name Analysis>
description: "<One rich paragraph describing the design language: the dominant surface/ink relationship, the single accent color and where it's allowed to appear, the display typeface and its tracking, button shapes, and the overall mood (e.g. dense/technical, warm/editorial, stark/developer).>"

colors:
  # Brand & accent
  primary: "#000000"
  on-primary: "#ffffff"
  primary-hover: "#000000"
  primary-focus: "#000000"
  # Text (ink) ramp: strong → faint
  ink: "#000000"
  ink-muted: "#000000"
  ink-subtle: "#000000"
  ink-tertiary: "#000000"
  # Surfaces: base canvas → elevated panels
  canvas: "#ffffff"
  surface-1: "#ffffff"
  surface-2: "#ffffff"
  surface-3: "#ffffff"
  # Hairlines / borders
  hairline: "#ebebeb"
  hairline-strong: "#d4d4d4"
  # Semantic
  semantic-success: "#000000"
  semantic-error: "#000000"
  semantic-warning: "#000000"
  # ── Optional blocks (delete if unused) ──
  # borders:            # if the brand distinguishes several border tones
  # brand-gradient-start: "#000000"
  # brand-gradient-end:   "#000000"
  # category-accent-a:  "#000000"   # e.g. per-sport / per-collection chips

typography:
  # Each role: fontFamily, fontSize, fontWeight, lineHeight, letterSpacing
  display-xl:
    fontFamily: <Font, fallback, sans-serif>
    fontSize: 48px
    fontWeight: 600
    lineHeight: 48px
    letterSpacing: -2.4px
  display-lg:
    fontFamily: <Font, fallback, sans-serif>
    fontSize: 32px
    fontWeight: 600
    lineHeight: 40px
    letterSpacing: -1.28px
  display-md:
    fontFamily: <Font, fallback, sans-serif>
    fontSize: 24px
    fontWeight: 600
    lineHeight: 32px
    letterSpacing: -0.6px
  headline:
    fontFamily: <Font, fallback, sans-serif>
    fontSize: 20px
    fontWeight: 600
    lineHeight: 28px
    letterSpacing: -0.4px
  card-title:
    fontFamily: <Font, fallback, sans-serif>
    fontSize: 18px
    fontWeight: 600
    lineHeight: 24px
    letterSpacing: -0.2px
  subhead:
    fontFamily: <Font, fallback, sans-serif>
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px
    letterSpacing: 0px
  body-lg:
    fontFamily: <Font, fallback, sans-serif>
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px
    letterSpacing: 0px
  body:
    fontFamily: <Font, fallback, sans-serif>
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
    letterSpacing: 0px
  body-sm:
    fontFamily: <Font, fallback, sans-serif>
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 0px
  caption:
    fontFamily: <Font, fallback, sans-serif>
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
    letterSpacing: 0px
  button:
    fontFamily: <Font, fallback, sans-serif>
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: 0px
  eyebrow:
    fontFamily: <Font, fallback, sans-serif>
    fontSize: 12px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: 1px
  mono:
    fontFamily: <Mono, ui-monospace, monospace>
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

components:
  # Reference tokens with {group.key}. Add brand-specific "signature" components at the end.
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "{spacing.sm} {spacing.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-strong}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "{spacing.sm} {spacing.md}"
  button-tertiary:
    backgroundColor: "transparent"
    textColor: "{colors.ink-muted}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "{spacing.xs} {spacing.sm}"
  card:
    backgroundColor: "{colors.surface-1}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  feature-card:
    backgroundColor: "{colors.surface-2}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
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
    height: 64px
    padding: "{spacing.sm} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  # signature-component-name:
  #   <props unique to this brand — the one or two components that define its look>

assets:
  # Canonical brand asset URLs (CDN or brand-portal links, not temporary uploads).
  logos:
    primary: "<https://…/logo.svg>"        # default lockup
    mark: "<https://…/icon.svg>"           # symbol / favicon only
    wordmark: "<https://…/wordmark.svg>"   # type-only lockup
    inverse: "<https://…/logo-white.svg>"  # for dark surfaces
  images:
    - name: hero
      url: "<https://…/hero.jpg>"
      alt: "<description>"
    - name: og-image
      url: "<https://…/og.png>"
      alt: "<social share preview>"
  videos:
    - name: hero-loop
      url: "<https://…/hero.mp4>"
      poster: "<https://…/hero-poster.jpg>"
  # ── Optional blocks (delete if unused) ──
  # icons:
  #   - name: <name>
  #     url: "<https://…/icon.svg>"
  # fonts:
  #   - name: <font-name>
  #     url: "<https://…/font.woff2>"
---

## Overview

<2–4 sentences: what kind of surface this is (marketing site / product UI / docs), the
core visual thesis, and the one thing a designer must get right to make it feel on-brand.>

## Colors

### Brand & Accent
<Where the accent is allowed to appear, and — just as important — where it is not.>

### Surface
<The canvas → elevated-panel progression; when each surface level is used.>

### Text
<The ink ramp from strongest to faintest and what each tone is for.>

### Semantic
<Success / error / warning usage.>

<!-- Optional: ### Borders · ### Brand Gradient · ### Category Accents -->

## Typography

### Font Family
<Primary display face, body face, mono face, and their intended roles.>

### Hierarchy
<How the roles above map to real page elements (hero, section title, body, eyebrow…).>

### Principles
<Tracking, weight, and case conventions that make the type feel right.>

### Note on Font Substitutes
<Fallback stack and how close the substitute should get if the brand font is unavailable.>

## Layout

### Spacing System
<The spacing scale in practice; base unit and rhythm.>

### Grid & Container
<Max content width, column count, gutters.>

### Whitespace Philosophy
<Dense vs. airy; how much room sections breathe.>

<!-- Variant B places responsiveness here instead of a top-level section:
### Responsive Strategy
#### Breakpoints
#### Touch Targets
#### Collapsing Strategy
#### Image Behavior
-->

## Elevation & Depth
<Shadow usage (or deliberate flatness); how layering is signaled.>

### Decorative Depth
<Any gradients, glows, blurs, or texture — and how sparingly they're used.>

## Shapes

### Border Radius Scale
<Which radii apply to which elements; the overall roundness personality.>

### Photography & Illustration Geometry
<Crop ratios, framing, corner treatment of imagery.>

## Assets

Registry of brand asset URLs (defined in the `assets:` front-matter). Keep links
canonical and permanent, not one-off uploads.

### Logos
<Which lockup goes where: primary vs. mark-only vs. wordmark vs. inverse on dark
surfaces. Minimum size and clear-space rules.>

### Images
<Hero art, OG/social previews, illustration sources. Note licensing and required crops.>

### Videos
<Background loops, product demos. Autoplay / muted / poster conventions and static fallback.>

## Components

### Buttons
<Variants, states (default/hover/pressed/focus/disabled), sizing.>

### Cards & Containers
<Panel styles, borders, padding, when each card type is used.>

### Inputs & Forms
<Field styling, focus treatment, labels, validation.>

### Navigation
<Top nav, mobile nav, footer navigation behavior.>

### Signature Components
<The 1–3 components that most define this brand's identity.>

## Do's and Don'ts

### Do
- <Concrete rule that keeps output on-brand.>
- <…>

### Don't
- <Concrete anti-pattern to avoid.>
- <…>

<!-- ── Variant A adds the following top-level sections; delete for Variant B ── -->

## Responsive Behavior

### Breakpoints
<Named breakpoints and layout intent at each.>

### Touch Targets
<Minimum sizes and spacing for touch.>

### Collapsing Strategy
<What stacks, hides, or reflows as width shrinks.>

### Image Behavior
<How imagery scales, crops, or swaps across sizes.>

## Iteration Guide
<How to extend this system: adding a token, a component, or a new page type
without breaking the language.>

## Known Gaps
<What this analysis does not yet cover; unresolved questions.>
