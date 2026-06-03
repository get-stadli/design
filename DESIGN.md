---
name: Stadli
description: Monochrome editorial sports-franchise platform. Near-black canvas, white Helvetica display at weight 500 with tight negative tracking. A strict split — admin chrome stays monochrome, atmospheric marketing surfaces are where saturated Spectrum color and house gradients live. The heat comes from full-color fan photography and one oversized manifesto per page, never from accent color on UI. Meaning is carried by type, tabular numerals, and photography — not iconography. The product is monochrome on purpose so that people are what's in color when they show up.

colors:
  # Surface
  canvas: "#010101"
  surface: "#080808"
  surface-elevated: "#1a1a1a"
  hairline: "#161616"
  hairline-strong: "#303030"
  # Text
  ink: "#ffffff"
  body: "#e8e8e8"
  muted: "#929292"
  muted-soft: "#6a6a6a"
  # Spectrum — gated to atmospheric surfaces only. Each carries an assigned meaning (see "The spectrum, by meaning"); never a default, never on chrome.
  spec-red: "#fe0000"
  spec-orange: "#fe5619"
  spec-lime: "#ecfc3b"
  spec-green: "#44d62b"
  spec-teal: "#00d4a8"
  spec-cyan: "#00b0d8"
  spec-blue: "#0140f0"
  spec-violet: "#7b2ff7"
  spec-magenta: "#d633ff"
  spec-rose: "#f6166e"
  # House gradients — use by name, never compose new ones. All three sit at equal weight; pick by context (mood, contrast, what the section is saying), never as a default.
  grad-stadium: "linear-gradient(135deg, #d633ff, #7b2ff7)"   # Matchnight, primetime, fans-on-their-feet
  grad-pitch:   "linear-gradient(135deg, #ecfc3b, #00d4a8)"   # Daylight, training, growth, ops moments
  grad-tribune: "linear-gradient(135deg, #fe5619, #f6166e)"   # Crowd warmth, season-ticket nostalgia

typography:
  fontFamily: "Helvetica Neue, Helvetica Now, Inter, sans-serif"
  mono: "JetBrains Mono, ui-monospace, monospace"
  # All display weight capped at 500. Negative tracking scales with size. tabular-nums on every metric.
  manifesto: "clamp(48px, 9vw, 104px) / 1.02 / weight 500 / tracking ~-3.5%"
  display:   "clamp(46px, 7vw, 92px)  / 1.05 / weight 500 / tracking ~-3%"
  heading:   "clamp(32px, 4vw, 56px)  / 1.10 / weight 500 / tracking ~-2%"
  title:     "21px / 1.3 / weight 600"
  body:      "17px / 1.55 / weight 400"
  label:     "13px / 1.3 / weight 700 / uppercase / tracking +1px"
  file-path: "12px JetBrains Mono / weight 400"

rounded:
  sm: 6px      # buttons, inputs
  lg: 8px      # cards
  xl: 12px     # mockup frames
  pill: 9999px # badges, tooltip pills only

spacing:
  scale: "4 / 8 / 12 / 16 / 24 / 32 / 48"
  section: "152px desktop, 96px mobile (top + bottom on every product section)"
---

# Stadli Design

## Essence

Near-pure black canvas, white display type in Helvetica Neue at weight 500, negative tracking scaled to size. The product is monochrome on purpose so that *people are what's in color when they show up* — fans, players, staff, shot full-bleed in documentary color and anchored by a film-grain overlay.

Hierarchy comes from size, whitespace, and tabular numerals. Not color. Not shadows. Not weight beyond 500. Not icons.

Surface language is French (Québec). Dark is the marketing canvas; light theme exists for product parity only.

## Five principles

1. **Monochrome chrome, vivid signal.** Admin chrome — buttons, inputs, cards, navbars, anything inside a mockup frame — stays strictly black/white/gray. Spectrum color is reserved for atmospheric surfaces and data viz. Color carries meaning, never decoration.
2. **Editorial confidence over UI noise.** Cards are flat. Borders are quiet. No drop shadows. No icons. Depth comes from surface contrast (`canvas` → `surface` → `surface-elevated`) and gradient saturation against black, and meaning comes from type and number — not glyphs bolted onto the interface.
3. **Mockups are first-class storytelling.** Every product mockup is a container-query-driven frame, paired with a human moment in the same section — inset photo, photographic strip, or sidebar fan card. Never a screenshot floating alone.
4. **Atmosphere is product.** Between product sections the page breathes through fan photography, color-blocked editorial breaks, and exactly one oversized manifesto per page. Atmosphere is the rhythm device that prevents the page from reading as "tech."
5. **Motion is reveal, not decoration.** Scroll-revealed content fades with a blur-and-rise. AI-related surfaces shimmer subtly (see "AI surfaces"). Everything respects `prefers-reduced-motion`.

## No icons

Stadli is a type-and-photography system. The interface earns its meaning the editorial way — through word, weight, size, tabular number, and the human face in the photograph — not through iconography. Avoid icons as far as the work allows: no nav glyphs, no button icons, no feature-grid pictograms, no decorative line-art, no logo-mark stand-ins for words. Where a convention seems to demand an icon, spell it out in a label or let layout and number do the work instead. Status is no exception — see the dot pill under "The spectrum, by meaning" for the type-first way to show state.

The single permitted exception is the directional arrow `→` that closes a CTA. It is typography, set in the brand family, not an icon — it reads as punctuation, not ornament. Nothing else qualifies for the exception.

## The split — the brand's spine

The line between monochrome chrome and atmospheric color is non-negotiable. Spectrum and the three house gradients are gated by **surface**, not by element type.

No Spectrum color or gradient is more important than another. Every color choice is semantic — picked for what the moment is saying (mood, contrast, content), never assigned as a default. The same atmosphere section can run on any of the three gradients depending on context.

**Allowed:** atmosphere breaks, fan-voice sections, manifesto sections, charts and data viz, narrative pills and tags, hero accent words.

**Forbidden:** buttons, inputs, cards, navbars, hover states, icons of any kind, anything inside a mockup frame.

If you reach for a `spec-*` color on a button or a card, the brand is drifting. The same is true the moment you reach for an icon.

## The spectrum, by meaning

"Pick by context" is the rule, but context needs a vocabulary. Every `spec-*` color carries an assigned meaning, and the meaning it activates depends on the surface it lands on. This is what makes "every color choice is semantic" operable rather than aspirational: the figure-skater's choice of which color, like the choice of which gradient, is a reading of what the moment is saying.

These meanings live **only on the surfaces "The split" already allows** — data viz, narrative pills and tags, atmosphere and marketing. Assigning a meaning never licenses a color onto chrome. If a surface spans contexts and you're unsure, the stricter reading wins: treat it as chrome and stay monochrome.

| Spectrum | Hex | On data viz | On narrative pills & status dots | On atmosphere & marketing |
|---|---|---|---|---|
| **Red** | `#fe0000` | Negative delta · churn · revenue loss · decline | Error · cancelled · blocked | Urgency · scarcity · countdown · limited-time |
| **Orange** | `#fe5619` | At-risk metric · caution threshold · near-miss | Warning · approaching a limit · draft | Energy · hype · the warm call-to-action |
| **Lime** | `#ecfc3b` | Spike · trending anomaly · breakout metric | New · just-updated · highlight | Disruption · freshness · novelty |
| **Green** | `#44d62b` | Positive growth · target met · goal achieved | Success · confirmed · on-sale · complete | Momentum · wins · the go-signal |
| **Teal** | `#00d4a8` | Benchmark · baseline reference · comparison anchor | Active · selected · toggled-on | Innovation · trust · forward-looking |
| **Cyan** | `#00b0d8` | Volume series · engagement · secondary KPI | Informational · hint · guidance | Openness · clarity · the inviting moment |
| **Blue** | `#0140f0` | Primary KPI series · headline metric · lead indicator | Neutral primary · in-progress | Authority · confidence · reliability |
| **Violet** | `#7b2ff7` | Forecast · projection · modeled estimate | Premium · gated · pro | Exclusivity · vision · the premium tier |
| **Magenta** | `#d633ff` | Outlier · anomaly flag · unusual pattern | Notification · unread · system alert | Boldness · the standout · differentiation |
| **Rose** | `#f6166e` | Fan sentiment · engagement score · NPS positive | Favourite · loyalty · saved | Passion · fandom · emotion · connection |

The three house gradients keep the meanings already noted in their tokens — `grad-stadium` for matchnight and primetime, `grad-pitch` for daylight and ops, `grad-tribune` for crowd warmth and season-ticket nostalgia. As with the single colors, no gradient is a default; pick the one whose meaning matches the section.

### One spectrum color per element

A chart series, a narrative tag, a status dot, or a color block carries **one** spec color — never two. A card built on `spec-magenta` does not also reach for `spec-green`; an insight tagged "forecast" in violet does not also wear a second hue. If a composition needs to say two things, it needs two elements, each monochrome around its single color, with canvas or surface as the neutral between them. One color, one meaning, one element.

### The dot pill — status without a glyph

Where a lesser system reaches for a colored icon or a fully-saturated badge to show state, Stadli isolates the meaning to a single small dot and leaves everything else monochrome. The dot carries the one spec (or semantic) color; the text beside it stays white or `body`, the border stays a quiet hairline. This is the type-first, icon-free way to show status — the editorial answer to a status glyph, and the construction principle behind the "narrative pills and tags" surface.

- The **dot is the only colored element.** Pill background and border stay monochrome; the text never takes a spec color.
- Pill text is set in neutral body or title case — **not** the all-caps `label` style — and **never wraps.** The dot signals; the word names.
- **One color per pill**, per the rule above. A pill says one thing.

## AI surfaces

AI-touched surfaces get one consistent, quiet signal — never a robot icon, never a sparkle glyph. The no-icons rule holds here too: the signal is motion and a word, not a picture.

- **The AI badge.** A single shimmering badge marks anything AI-generated — a slow, low-contrast sheen travelling across an otherwise monochrome pill, paired with a word (`IA`, `Généré par IA`). The shimmer is the only animation the badge carries, and it is the system's consistent tell that a surface is machine-made. Same badge everywhere; the consistency is the point.
- **Insight cards.** AI narrative output lives in insight cards — short, editorial cards that read like a sentence and are tagged with a narrative pill (the dot pill above). This is the home for the "narrative pills and tags" surface: the tag's dot carries the one spec color — `spec-violet` for a forecast, `spec-rose` for fan sentiment, `spec-magenta` for an outlier — while the card itself stays monochrome.
- **Shimmer skeletons.** While AI content loads, show a skeleton that matches the *shape* of the final content — the same line count, the same rough widths — filled with a monochrome shimmer rather than a spinner. The skeleton sits inside the same card or grid as the real content, so nothing shifts when it resolves.

All three resolve to a static resting state under `prefers-reduced-motion`: the badge sheen freezes, the skeleton holds without animation.

## Type

One family, scaled. Helvetica Neue (Inter is the open-source fallback that ships in production) covers display, body, nav, and buttons. JetBrains Mono appears in exactly one place: the file-path label under product mockups.

- **Display weight caps at 500.** Visual heaviness comes from size and tight tracking, not stroke. Sub-titles step to 600 only at ≤21px.
- **Negative tracking scales with size.** ~-3% at display ≥56px, -1% to -2% at 32–50px, 0 on body. The compression is the brand voice — without it, headlines lose their editorial feel.
- **Tabular numerals are mandatory** on every metric, dashboard, KPI tile, and table. Number is the brand's substitute for the icon — where a lesser system would set a pictogram, Stadli sets a figure.

## Photography & mockups

Photography carries the warmth the chrome refuses to.

**The image is never colored.** No duotone, no black-and-white, no grayscale, no color tints, no gradient overlays, no semi-transparent color washes. Photography ships full-color and untouched. The one thing applied is a fine film-grain texture (~6% opacity, no color) — that's what anchors imagery to the editorial tone and stops it reading as stock.

**Documentary color** is the treatment direction: slightly desaturated, film-not-Instagram. Used everywhere photography appears — hero, atmosphere breaks, fan portraits, testimonials, product-pairing strips.

**Color combines with photography through solid blocks, never overlays.** When a composition needs both color and an image, the color sits in a solid panel — canvas, surface, or Spectrum — containing copy or content, layered on top. The block carries the color; the image stays clean. Examples: a canvas card with a quote sitting over a fan photo; a magenta panel with display type anchored to the corner of a stadium image; a manifesto bar resting across the lower third of a hero shot.

**Subject hierarchy:** faces (mid-emotion, not posed) → crowds → stadium architecture → operational moments.

**Forbidden imagery** (markers of B2B SaaS): laptops/screens showing the product, conference-room team meetings, handshakes, smiling-businessperson stock headshots, drone-from-outside establishing shots, empty seats in marketing, posed "diverse team" group shots, lens flares, competitor branded apparel.

**Mockup pairing rule:** every product mockup ships with a human moment in the same section. The mockup proves the software exists; the photo proves who it is for.

## Layout & rhythm

- Max content width 1280px. Atmosphere sections are full-bleed and override this cap.
- Section padding 152px desktop / 96px mobile, top and bottom on every product section. Generous on purpose.
- The dark canvas *is* the whitespace. Long stretches of black are the brand's breathing room.
- The page reads like a magazine cut into bands: black product band → full-bleed gradient atmosphere → back to black.
- Surface lift marks hierarchy: `canvas` → `surface` → `surface-elevated`. Not opacity changes on white type.

## Voice & naming

- Surface language is **French (Québec).** UI labels, marketing copy, CTAs. Documentation is English.
- **Title case** for English titles, headings, buttons, and labels (e.g. "Save Changes", "New Event"). Sentence case is not required on chrome. French copy follows French convention (sentence case) — French does not title-case.
- **FR-CA number format:** thin-space thousands, comma decimal, currency mark after the figure with one space (`142 850,00 $`).
- CTAs end with a directional arrow `→`. This arrow is type, not an icon, and is the only glyph the system permits.
- **File-path labels** (e.g. `stadli/app/.../component.tsx`) sit above or below every product mockup in JetBrains Mono. Brand voice — signals real software, real engineering. Never apply to atmosphere, fan voice, manifesto, or photography.

## Don't

- Don't put Spectrum color on admin chrome. Gating is by surface, not element type.
- Don't push display weight past 500. Hierarchy is size and tracking, not stroke.
- Don't add drop shadows. Cards are flat by contract; depth is built from surface contrast.
- Don't reach for icons. The interface communicates through type, tabular numerals, and photography — not glyphs, pictograms, or line-art. The directional arrow `→` on CTAs is the only permitted mark, and it is typography, not an icon.
- Don't layer two spectrum colors on one element. One spec color per atomic element — a tag, a series, a dot, a block — paired with neutral or canvas around it. Two meanings need two elements.
- Don't color a status pill's text or background. The dot carries the one color; the text stays monochrome and never goes all-caps `label` style.
- Don't treat a spectrum color as decoration once it's assigned a meaning — a green dot means success, not "a green dot." If the meaning doesn't fit the moment, pick the color whose meaning does.
- Don't mark AI surfaces with an icon. The signal is the shimmer plus a word, never a sparkle or robot glyph.
- Don't compose new gradients. The three house gradients are exhaustive.
- Don't ship a mockup floating alone — pair it with a human moment.
- Don't run more than three product sections without an atmosphere break.
- Don't ship more than one manifesto section per page.
- Don't tint, color, or overlay images — no duotone, B&W, grayscale, color washes, or gradient overlays. Only the colorless grain texture touches the image. For color + photo compositions, layer a solid color block on top instead.
- Don't treat any gradient or Spectrum color as a default — pick by context.
- Don't run photography without the grain overlay. Stock-photo look is the failure mode.

## Accessibility

- Every shimmer, reveal, parallax, and rotating-word transition is disabled under `prefers-reduced-motion: reduce`, with final states forced to their resting values. This includes the AI badge sheen and the shimmer skeleton, which freeze to static.
- Focus rings: white at 12% alpha on dark, black at 12% on light. No Spectrum on focus rings inside admin chrome.
- Atmosphere sections using gradients must verify white-text contrast at AAA — the orange end of `grad-tribune` and the lime end of `grad-pitch` are the most likely to fail. Darken the affected stop, place type over the darker side of the gradient, or pick whichever gradient gives this content the contrast it needs.
- Because the system avoids icons, never lean on a glyph to convey state or action — label it in words so meaning survives without visual decoding. A status dot always travels with its word; the dot is never the only carrier of meaning.
- Every photograph carries descriptive alt text.
