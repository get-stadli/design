# Machine-readable spec

This file contains the v25 machine-readable design-system metadata and tokens.

---
version: alpha-25
name: "Stadli"
description: "A high-contrast design language where design exist to tell the story — made to build whatever the story needs, as long as it stays in sync with the chrome and the rest of the page. The story comes first, always. The chrome — navigation, buttons, text, and canvas — stays strictly black, white, and gray, and chrome is also the resting state of every block: a plain surface with a hairline border is a finished block, not an unstyled one. Color is bold where it appears but rare. Imagery is always raw: full strength, no filter, no scrim. Inter is used for every text role, buttons are pill-shaped, cards are flat with hairline borders, composition is asymmetric by default — blocks anchor to the leading edge, clusters keep ragged silhouettes, whitespace pools deliberately — and the mood is quiet and technical in the frame, loud and saturated at the few moments that earn it. Every surface is designed on both canvases at once — light (#ffffff) and dark (#0a0a0a) are one deliverable, never a recolor applied later."
about-stadli: "Stadli is an all-in-one event intelligence platform helping sports teams and live-event organizers sell more tickets, know their fans, and build fuller venues. From ticketing, CRM, email, ecommerce, surveys, analytics, and AI tools, Stadli gives teams one fan-first system to grow revenue without losing ownership of their audience or data."

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

motion:
  duration:
    instant: 160ms     # focus rings, press states — feels immediate
    fast: 320ms        # hover tone shifts, small chrome transitions
    base: 560ms        # default state changes, toggles, small expand/collapse
    slow: 1400ms       # content entrances and reveals
    deliberate: 1600ms # the one earned loud moment — count-up, chart draw, hero reveal
  easing:
    standard: cubic-bezier(0.16, 1, 0.3, 1)   # cinematic ease-out — quick lead, long graceful settle
    exit: cubic-bezier(0.7, 0, 0.84, 0)       # elements leaving — accelerates away
    in-out: cubic-bezier(0.65, 0, 0.35, 1)    # reorders and moves — smooth symmetric
    linear: linear                            # continuous loops only (loading pulse)
  stagger:
    opening: 220ms     # first gap in a cascade — deliberate, per-item
    floor: 110ms       # successive gaps ease toward this so long sequences don't drag
    cap: 6             # stop staggering after this many items
  reveal:
    blur: 6px          # entrances clear from a 6px blur to sharp, alongside the rise
  trigger:
    activation-line: 65%   # a reveal fires when the block's top crosses this line from the top of the viewport, then rises and un-blurs into reading position
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
  stat-card:
    backgroundColor: "{colors.surface-1}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.eyebrow}"
    figureTypography: "{typography.display-lg}"
    captionTypography: "{typography.body-sm}"
  metric-header:
    backgroundColor: "{colors.surface-1}"
    borderColor: "{colors.hairline}"
    dividerColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    cellPadding: "{spacing.md} {spacing.lg}"
    labelTypography: "{typography.eyebrow}"
    valueTypography: "{typography.display-md}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.semantic-error}"
    helperTextColor: "{colors.semantic-error}"
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
  rail-handle:
    thumbHeight: "8px"
    thumbMinWidth: "40px"
    thumbColor: "{colors.hairline-strong}"
    thumbColorActive: "{colors.ink-subtle}"     # hover and while dragging — tone only
    trackColor: "transparent"                    # no track chrome; the thumb stands alone
    rounded: "{rounded.pill}"
    hitBand: "20px"                              # invisible grab band centered on the 8px thumb
    idleHideDelay: "1100ms"                      # fades out this long after the last interaction
    decay: 0.92                                  # per-frame velocity falloff for the release glide

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
