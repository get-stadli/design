# Stadli — Design System

**Version:** v12 · EN · namespace `StadliDesignSystem`

> **We are the team behind the team.** The fans feel the roar; we build the room it happens in. A full house is a city saying yes — Stadli is the quiet work that gets it to say yes again.

Stadli is the operating platform for sports franchises — ticketing, season tickets, fan engagement, and the night of the match. The product is monochrome **on purpose**, so that *people are what's in color when they show up.* This is a standalone specification: every token, rule, and component API is inlined here.

---

## 1 · Manifesto — the thesis

We don't design for the dashboard. We design for **the night** — and for the people who spend all week making sure it happens: the person who turns an empty bowl into a full one, who turns a name on a list into a face they know by sight.

Near-black canvas, white Inter display at weight 500, negative tracking scaled to size. Hierarchy comes from **size, whitespace, and the tabular numeral** — never color, never shadow, never weight beyond 500, never an icon, and never colored type.

When color does appear it behaves as **light** — rising out of the black like floodlights seen from the street, carried by dot and stripe fields built on the circle, never flat fills and never inside the letterforms. And when data appears it can become **points** — matrices of dots where every dot maps to a real person or a real number.

So we keep **two volumes, and never confuse them.** The work is calm; the moment is loud. Loud is not the default; loud is what we **earn** by being calm everywhere else. We speak the language of the building, never the language of the machine.

---

## 2 · The two volumes — calm and loud

Every surface belongs to one register. They are designed apart on purpose.

| | **Calm — the command center** | **Loud — the Moment** |
|---|---|---|
| Where | Tuesday-afternoon work: lists, planning, numbers, dashboards | The match, the gate, the seat filling, the sellout |
| Feel | Composed, in control; energy held and coiled | Everything held back, landing at once |
| Type | Measured; hierarchy by size and tracking | Back-row scale — readable from the cheap seats |
| Color | Monochrome; a data hue only where a person's eyes are needed | **The light** comes on — one azure accent |
| Motion | Restrained, slow | The lean into kickoff; the light snapping on |
| Frequency | The default, almost everywhere | **Once per view, maximum** |

The rule that makes it work is the same shape as "one story hue per viewport": **scarcity.** Loud is rare, so loud lands. If a screen has two Moments, it has none — cut one.

The two volumes are an axis of *intensity*; **the split** (next) is an axis of *surface*. They align — chrome is always calm — but they are not the same line: a quiet editorial photo break is atmosphere yet still calm. The Moment is the single loudest surface the system owns.

---

## 3 · The split — the brand's spine

The line between **monochrome chrome** and **atmospheric color** is non-negotiable. Spectrum color is gated by **surface**, not by element type.

**Allowed:** atmosphere and marketing breaks, fan-voice sections, the manifesto, charts and data viz, dot matrices, narrative pills and tags, photo-naming meta.

**Forbidden:** buttons, inputs, cards, navbars, hover states, error borders, icons of any kind, anything inside a mockup frame.

If you reach for a `spec-*` color on a button or a card, the brand is drifting. The same is true the moment a spec color lands on a headline or a line of text. **Type is never colorized, on any surface, with no exceptions — not a headline, not a line of body, not a single word, not a single glyph, not a number, not even in the Moment.** There is no "one colored word." Color lives in the texture behind the type, the block beneath it, the dot beside it, the data series, or the matrix — never inside the letterforms. Emphasis on a word is always **ink weight or `<em>` lifting to ink**, never a hue.

---

## 4 · Principles

**Volume**
1. **Two volumes, never confused.** The work whispers; the Moment roars.
2. **Loud is earned.** One loud Moment per view, at most. If everything shouts, nothing does.

**One world**
3. **One light.** Azure (`--spec-azure`) is reserved as the emotional accent — the light snapping on in the dark. In the command center azure still does its KPI data job; as the light it appears once, in the Moment, and means *this is the thing.* The light is a **keyline, a dot, or a texture field beside or behind the words — never the words themselves.** Even here, type stays white.
4. **One lean.** A single forward tilt — type and entering motion lean *in*, the way a crowd tilts when something's about to happen. Motion has direction; it always travels the same way.
5. **One beat.** A single slow tempo (`--beat`) runs under the pulse, the shimmer, the ignite, and the clock — so the whole thing feels authored, not assembled.

**Language**
6. **Speak the building, not the machine.** A person isn't a record; they're someone who's had the same seat for thirty years. Name things the way the stands would.

**Craft (the invariants)**
7. **Monochrome chrome, vivid signal.** Text and buttons are always monochrome; color is gated to atmosphere and data.
8. **Color only carries meaning** — a data semantic, the direction of a movement, the one story, or the light. Never decoration.
9. **Exception-first on product.** Color marks the outcome, the movement, or the call for attention — never the expected resting state.
10. **No gradients, no halos, no drop shadows.** Color-as-light is dot and stripe texture, not glow. Depth is surface contrast and hairlines.
11. **One typeface (Inter), no second face, no icons.** The only permitted mark is the CTA arrow `→`, read as punctuation.
12. **Earn the un-obvious.** Push past the first easy answer — the easy answer is the one every other building already has.

---

## 5 · Color tokens

Depth is built from **surface contrast**, divided by hairlines — never opacity changes on white type. Text hierarchy is **ink weight**, not color.

### Surfaces (dark — the default canvas)

| Token | Hex | Role |
|---|---|---|
| `--canvas` | `#010101` | Page background; the whitespace |
| `--surface` | `#080808` | Raised surface, cards, panels |
| `--surface-elevated` | `#1a1a1a` | Highest surface |
| `--hairline` | `#161616` | Quiet divider, default border |
| `--hairline-strong` | `#303030` | Loud divider |
| `--focus-line` | `#454545` | Input focus border (monochrome) |

### Text

| Token | Hex | Role |
|---|---|---|
| `--ink` | `#ffffff` | Headlines, keywords, primary button fill |
| `--body` | `#e8e8e8` | Body copy |
| `--muted` | `#929292` | Context, secondary |
| `--muted-soft` | `#6a6a6a` | Faint text, the annotation register |

### The Spectrum — seven hues, meaning-gated

Allowed on atmosphere, data viz, dots, narrative tags, and photo-naming meta. **Forbidden** on chrome. Each hue carries a fixed meaning; pick by what the moment is saying, never as a default. The set was consolidated for color-blind safety — seven hues at distinct luminances with deliberate spacing, broadcast-saturated on a raised lightness floor so each reads against `#010101`.

| Token | Hex | Meaning |
|---|---|---|
| `--spec-red` | `#ff4b3e` | negative · error · decline · downward delta |
| `--spec-orange` | `#ff9d2e` | at-risk · warning · needs intervention |
| `--spec-lime` | `#f2e23a` | spike · new · breakout · just-updated |
| `--spec-green` | `#22c55e` | positive · success · growth · benchmark · active |
| `--spec-azure` | `#3f86f2` | KPI series (headline + secondary) — **and the light** |
| `--spec-purple` | `#b85cf2` | forecast · outlier · notification · premium |
| `--spec-rose` | `#ff5c9e` | fan sentiment · loyalty · favourite |

**The light.** `--spec-azure` is the one emotional hue. In the command center azure does its KPI data job; in the **Moment** it appears once — a word, a number, or a line that *snaps on* — and nothing else takes color. Same hue, two duties; the surface tells them apart.

### Status-dot fills (picked by meaning, not default)

| Token | Resolves to | Use |
|---|---|---|
| `--dot-pending` | `--muted` | in-flight / routine category |
| `--dot-positive` | `--spec-green` | success outcome |
| `--dot-negative` | `--spec-red` | failure outcome |
| `--dot-attention` | `--spec-orange` | at-risk |

The lone carve-out for color on a resting state: a live health / uptime monitor, where a measured "Operational" pass may wear green.

### Focus ring

`--focus-ring: rgba(255,255,255,.12)` (white 12% on dark; black 12% on light).

### Light theme — product parity only

A chrome theme, never a brand surface. No atmosphere textures, manifesto, dot matrices, or grain in light. Spectrum survives only in data viz + status dots; on light, `lime` / `green` / `azure` dots gain a 1px ring. Set via `[data-theme="light"]`.

| Token | Hex |
|---|---|
| `--canvas` | `#f2f2f1` |
| `--surface` | `#fafafa` |
| `--surface-elevated` | `#ffffff` |
| `--hairline` | `#e6e6e6` |
| `--hairline-strong` | `#d0d0d0` |
| `--ink` | `#0a0a0a` |
| `--body` | `#232323` |
| `--muted` | `#6d6d6d` |
| `--muted-soft` | `#9b9b9b` |
| `--focus-ring` | `rgba(0,0,0,.12)` |

---

## 6 · The spectrum, by meaning

"Pick by context" is the rule, but context needs a vocabulary. Every `spec-*` color carries an assigned meaning, and the meaning it activates depends on the surface it lands on. These meanings live **only on the surfaces the split allows** — assigning a meaning never licenses a color onto chrome or onto type. If a surface spans contexts and you're unsure, the stricter reading wins: treat it as chrome and stay monochrome.

| Spectrum | On data viz | On narrative pills & status dots | On atmosphere & marketing |
|---|---|---|---|
| **Red** | negative delta · churn · loss · decline | error · cancelled · blocked · the downward delta | urgency · scarcity · countdown |
| **Orange** | at-risk metric · caution threshold · near-miss | warning · approaching a limit · draft | energy · hype · the warm CTA |
| **Lime** | spike · trending anomaly · breakout | new · just-updated · highlight | disruption · freshness · novelty |
| **Green** | growth · target met **and** benchmark · baseline | success · resolved · the upward delta **and** active · toggled-on | momentum · wins · the go-signal |
| **Azure** | KPI series — headline **and** secondary alike | informational · hint · guidance | authority · confidence · clarity — **and the light** |
| **Purple** | forecast · projection **and** outlier · anomaly | notification · unread **and** premium · gated | exclusivity · vision · the standout |
| **Rose** | fan sentiment · engagement score · NPS | favourite · loyalty · saved | passion · fandom · connection |

**Where two merged meanings must coexist, form and word separate them — never a second hue.** Green: the color goes to the outcome; a benchmark drops to a monochrome `muted` reference line. Azure: one hue for every KPI series; lead vs. supporting is stroke weight and position. Purple: a forecast is a **dashed** line, an outlier is a **single highlighted point** — same hue, different form.

### Exception-first — the color budget

The table says what each color means; this rule says **when a color may speak at all.** On product surfaces a spec color marks an outcome, a movement, or a call for attention — never a moment still in flight. Pending, in-progress, and routine category states carry the **monochrome ink dot**.

- **States are resolved or pending.** A state that resolved successfully — "Confirmed," "Completed," "Refunded" when that was the goal — wears `spec-green`; a failed or cancelled one — "Cancelled," "Declined" — wears `spec-red`. Everything in flight — "Processing," "Payment pending" — and pure category labels carry the ink dot. `spec-orange` is reserved for the state that cannot resolve without the operator's intervention.
- **Health monitors are the one affirmative-green carve-out.** A component whose job is to report whether a system is *up right now* may color its healthy rows `spec-green`, because there "Operational" is a live measured pass, not an idle label. The test: is the positive state being *measured* now, or is it only the thing's default category? Only the measured pass earns green.
- **Deltas are directional.** A delta is inherently a signal: `spec-green` for growth, `spec-red` for decline, `spec-orange` for the at-risk threshold. A flat or exactly-as-forecast delta may go ink.
- **One story hue per viewport.** At most one large colored field — a chart's story series *or* a dot matrix — per screen. When two stories share a viewport, one goes monochrome; white-versus-gray carries the comparison on black.
- **Budget arithmetic.** A healthy product view shows one story hue plus only the alert dots that are real. More than three hues visible at once means something is decoration wearing a meaning.
- **Atmosphere and toasts are exempt.** Marketing keeps its full expressive range; a toast is itself an event, so its severity dot keeps its color.

---

## 7 · Color as light — atmosphere textures

The signature. Stadli never fills a surface with color; it lets color **rise out of the black.** Halos and flat or diagonal gradient fills are retired. Color-as-light renders as **dot and stripe fields built on the circle** — over a near-black container, with the film grain on top (light through film, not glass). Use as an absolutely-positioned layer (`inset:0; z-index:0`) inside a `position:relative` near-black container; put `.grain` over it. One color-story per screen.

| Class | Texture |
|---|---|
| `.atmo-dots` | halftone — circular dot trame |
| `.atmo-stripes` | LED — fine vertical light bars |
| `.atmo-matrix` | dot-matrix board — circular LED pixels |

- **The optical center stays near-black.** A texture illuminates the canvas; it never saturates it edge to edge. If less than a third of the surface still reads near-black, the light has become a fill — pull it back.
- **Type sits on the dark zone.** White display type rests where the surface is still black; contrast is structural, not corrective. The light is colored; the words are not.
- **One color per field**, per the one-color-per-element rule. Value is encoded in opacity or density steps of that single hue, never a second hue.
- A surface that needs one solid color is a **block**, not a texture — blocks stay flat and saturated, and any copy on them stays monochrome.

### The dot — the colored atom

The dot is Stadli's only colored atom, and it scales: the **status dot** (8px) → the **dot matrix** (a data chart, every dot cited) → the **atmosphere dot/stripe field** (the light). The closest thing to "iconography" the brand owns is the dot.

---

## 8 · Monochrome patterns

Texture without color. Where the `.atmo-*` fields carry the light, the `.pat-*` patterns are the **calm** texture — always monochrome, flat, hard-edged, never colored, never inside a surface card. Rendered raw on the page background; tintable via `--pat-ink` but kept neutral.

| Class | Pattern | Use |
|---|---|---|
| `.pat-dots` | Dot grid | Crowd & seat fields |
| `.pat-lines` | Blueprint grid | Maps & data structure |
| `.pat-type` | Repeating "STADLI" type field | Typographic atmosphere — print-style repeating wordmark |

`.pat-type` is the print-style repeating-wordmark field, used as quiet typographic atmosphere. It stays **strictly monochrome** — the colored dot/stripe fields are the place color lives; the type field never takes a hue.

---

## 9 · The dot matrix — data as points

The dot matrix scales the colored atom into data art: fields of dots where **every dot maps to a real quantity** — a crowd one-dot-per-fan, a season of attendance as columns, a section map where density is occupancy.

- **Every dot is data.** A dot field is a chart, not a texture. It ships with an annotation-register line citing what a dot is and how many (`18,442 points · 1 point = 1 person · source: ticketing`). If the dots don't map to anything, delete them.
- **One color per field.** Value is encoded in density, size, or opacity steps of one hue — never a second.
- **Dots read as dots.** Keep the resolution coarse enough that points are visible at arm's length; if it blurs into a gradient it has stopped being data.
- **Dots scale by area, not radius** — perceived area tracks the quantity.
- This is the brand's literal thesis rendered: *people are what's in color* — and here every point of color is a person.

---

## 10 · The annotation register — the forensic voice

The system's second voice. Where display type carries emotion, a quiet data line carries **evidence** — the layer that signals real software, real data. With one typeface across the system, the register is set apart not by a different font but by treatment: 11–12px Inter, `--muted-soft`, a hair of positive tracking, tabular numerals.

- **File-path** — `stadli/app/(admin)/ticketing/dashboard.tsx` — above or below every product mockup.
- **Timestamp** — `updated 12s ago`, `synced · 9:04 PM` — on live data surfaces.
- **Data citation** — `n = 18,442 · source: ticketing · 2026 season` — under every chart and matrix.
- **Coordinates** — `SEC 104 · R12 · S07`, `GATE B` — on tickets, seat maps, venue surfaces.
- **Version & meta** — `v12 · EN` — on system surfaces.

The register annotates; it never titles. One line per element. It belongs to product and data surfaces — never the manifesto, never an atmosphere headline, never inside a fan quote. The forensic voice and the emotional voice don't speak from the same line.

---

## 11 · Typography

**One family, scaled — Inter** covers display, body, nav, buttons, and the annotation register alike (Helvetica Neue is an acceptable metrics-compatible fallback). There is no second face: the register is set apart by size, color, tracking, and tabular figures, not by a different font. Loads weights 400 / 500 / 600 / 700.

```
--font-sans: "Inter", system-ui, -apple-system, sans-serif;
--font-mono: var(--font-sans);   /* alias — Inter, NOT a mono face */
```

### Scale, line-height, tracking

| Step | Size | Line-height | Tracking | Use |
|---|---|---|---|---|
| display | `clamp(44px, 5.6vw, 72px)` | 1.05 | -0.03em | The manifesto, hero headlines, the Moment |
| heading | `clamp(34px, 4.5vw, 62px)` | 1.10 | -0.02em | Section titles, chart titles |
| title | 22px | 1.3 | -0.01em | Sub-headlines (weight 600) |
| body | 17px | 1.55 | 0 | Body copy |
| body-sm | 14px | — | — | Secondary |
| label | 12px | 1.3 | 0.083em | All-caps eyebrows (weight 700) |
| annotation | 11px | 1.4 | 0.01em | The register (`--muted-soft`, tabular) |

### Weights

| Token | Value | Use |
|---|---|---|
| `--weight-display` | 500 | Display ceiling — never heavier |
| `--weight-title` | 600 | Titles, ≤22px |
| `--weight-body` | 400 | Body |
| `--weight-label` | 700 | All-caps labels |

- **Display weight caps at 500.** Heaviness comes from size and tight tracking, not stroke. Negative tracking scales with size (~-3% at display, 0 at body) — the compression is the brand voice.
- **The scale jumps deliberately.** If two adjacent levels look interchangeable, the scale has been flattened — restore the jump rather than adding weight. Display stays the largest type on the page, capped at 72px regardless of viewport.
- **Tabular numerals are mandatory** on every metric, KPI, and table (`.tnum`). The number is the brand's substitute for the icon.
- **Back-row scale.** The Moment uses display type larger than anywhere else — the number you can read from the back row. It is the one place type is allowed to get loud.
- **One lean.** Moment type and entering motion carry a subtle forward tilt — the crowd leaning into kickoff. Keep it slight; it's a posture, not an effect.
- **All-caps is an eyebrow, not a sentence.** The `label` style stays a few words long.
- **Type is never colorized**, dark or light, on any surface, with no exceptions. A spec color never fills a letterform — not a headline, not a line of body, not a single word, not a single glyph, not a number, not even in the Moment. Word-level emphasis is **ink weight or `<em>` lifting to ink**, never a hue.

---

## 12 · Spacing, radii, breakpoints

**Scale:** 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 152 px (`--space-1`…`--space-10`).

| Token | Value | Use |
|---|---|---|
| `--section-y` | 152px | Section top + bottom (desktop) |
| `--section-y-mobile` | 96px | Section rhythm (mobile) |
| `--radius-sm` | 6px | Buttons, inputs |
| `--radius-lg` | 8px | Cards |
| `--radius-xl` | 12px | Mockup frames |
| `--radius-pill` | 9999px | Badges, tooltip pills only |
| `--touch-min` | 44px | Hit-target floor (everywhere) |

**Breakpoints:** `--bp-compact: 560px` · `--bp-mobile: 760px` · `--bp-collapse: 900px` · `--bp-cap: 1280px`. CTAs stack full-width at ≤560px.

---

## 13 · Layout — one track set, two width tiers

Width is not one global rule; it's *which columns a band spans* on a single track set. The twelve columns are declared **once** on the page grid — fluid, growing with the viewport, capped at `--container` (1440) by the track sizing — and every tier is a span on them. Any multi-column band inherits the same twelve through `subgrid`, so columns are never redeclared and every tier aligns to one set of edges.

| Token | Value | Notes |
|---|---|---|
| `--columns` | 12 | The track count |
| `--gutter` | `clamp(24px, 3vw, 48px)` | One fluid value — column gap **and** edge inset |
| `--container` | `1440px` | Track-sizing cap on the twelve (not a `max-width` wall) |
| `--cap` | `1280px` | Where display *type* stops scaling — not a width |

```css
.page {
  display: grid;
  grid-template-columns:
    [full-start] minmax(0, 1fr)
    [wide-start] repeat(12, minmax(0, calc((var(--container) - 11 * var(--gutter)) / 12))) [wide-end]
    minmax(0, 1fr) [full-end];
  column-gap: var(--gutter);
}

.page > *         { grid-column: wide; }   /* container — the default tier      */
.page > .full     { grid-column: full; }   /* atmosphere — bleeds to the glass  */

/* a multi-column band inherits the SAME twelve — never redeclared */
.cols { grid-column: wide; display: grid; grid-template-columns: subgrid; column-gap: var(--gutter); }
.cols > .lead { grid-column: span 8; }
.cols > .side { grid-column: span 4; }
```

**The two tiers.**
- **Full-bleed — immersion.** `grid-column: full`, edge to edge. Hero, photography, atmosphere textures, the manifesto, dot-matrix art, **the Moment**. The black runs to the glass. Type inside a full band still rests in the `wide` span: the texture bleeds, the words do not.
- **Container — dense product.** `grid-column: wide`, the inner twelve. Dashboards, tables, KPI grids, settings, prose, forms, legal, empty states. Fluid up to 1440, then the outer columns grow and center the twelve.

**Governance.** Atmosphere, hero, photography, manifesto, dot-matrix, the Moment → **full**. Everything else — dashboards, tables, KPI grids, chrome, prose, forms, legal, empty states → **wide**. Width follows what the band *is*, never a guess.

**Immersion is opt-in; containment is the safe default.** A product band defaults to `wide`; a band goes `full` deliberately. Two ceilings, two jobs: type caps at `--cap` (1280), content at `--container` (1440). Never add a third content width.

### Rhythm

- The page reads like a magazine cut into bands: black product band → full-bleed atmosphere → back to black. The black between bands is the punctuation.
- The dark canvas *is* the whitespace. Surface lift marks hierarchy (`canvas` → `surface` → `surface-elevated`), never opacity on white type.
- **Top-left carries the lead.** The eye lands top-left first; importance decays along the reading path.
- **One idea per band** — one scroll-stop. If a section argues two things, it's two sections.
- **Product views hold 5–9 widgets.** Past nine, split into tabs or pages.
- Don't run more than three product sections without an atmosphere break, and ship at most one manifesto per page.

---

## 14 · Data viz — the chart is a poster

A Stadli chart is an editorial composition, not a widget. It earns a heading-size title, generous space, and an annotation-register citation — a magazine treating a chart as artwork with a caption.

- **One story series.** The story series takes the spec color whose meaning matches it; comparison and context series stay monochrome (`muted` / `muted-soft`). Prefer one colored series; never exceed three spec colors in a chart.
- **Monochrome comparison is first-class.** Two series read perfectly as `ink` vs. `muted-soft` on black — contrast does the work color was doing.
- **Hairline structure.** Gridlines and axes in `hairline` / `hairline-strong` only. No zebra striping, no filled plot backgrounds, no border boxes.
- **Flat color in data.** Series colors are flat — no gradients on bars or areas. Area fills under a line sit at ≤10% alpha, or not at all.
- **The title states the insight.** A chart answers a question and its title is the answer — "The 2026 season passes 2025 by spring," not "Tickets sold by month." The title is monochrome heading type, never colored to match the series.
- **A number alone means nothing.** Every KPI ships with context — target, prior period, or benchmark — carried by the delta line and its directional dot.
- **Honest by construction.** Bars start at zero; a non-zero line baseline is declared in the citation. Never dual y-axes. Aspect ratios stay honest. Actuals are solid; forecasts and objectives are dashed (and purple).
- **Every chart carries a citation**, sorts by value not alphabet, and rounds to meaning (`4.2M`, never `4,218,377.18`). Tooltips are chrome: `surface-elevated` card, hairline border, monochrome text, series identified by its dot + word.
- No 3D, no donut-with-icon centers, no rounded bar caps beyond `sm`, no sparkline confetti. One chart, one statement.

### Zones — structure, not color

A product view is organized into zones — Revenue, Engagement, Reliability, Growth. A zone is a **structural and editorial** device, never a coloring one: it governs where a widget lives and which widgets share a consistency contract, but it does not hand out a hue. A Revenue card and a Growth card look identical in chrome. What a zone *does* carry is **consistency** — within a zone a given data meaning always resolves to the same hue, so an operator learns the mapping once. Zone scopes consistency, meaning picks the color, exception-first rations it.

---

## 15 · The Moment — the loud register

A formal surface type: the earned roar. Used for the night, not the work. **Once per view, maximum.**

- **When:** the match, the gate, the seat filling, the sellout, a season-defining number.
- **Form:** full-bleed, a ground darker than the page (`#070809`), back-row display scale, generous air. Atmosphere texture may carry the dark; the words stay white.
- **The light:** exactly one azure accent that *snaps on* (draws in over `--beat`) — a keyline, a dot, or a texture field rising beside or behind the type. **It is never a colored word or number; the letterforms stay white even in the Moment.** Emphasis on a word is ink weight, never a hue. Nothing else takes color.
- **The line:** a single azure keyline that draws in left-to-right — the lean, the beat made visible. This is the Moment's light made type-adjacent: it sits under or beside the words, never on them.
- **Voice:** the building, at its most distilled — "A full house is a city saying yes."

If a screen has two Moments, it has none. Cut one.

---

## 16 · Motion — reveal, not decoration

Two motion systems, one rhythm. **Chrome micro-motion** is fast and quiet; **the one beat** is the slow brand pulse.

| Token | Value | Use |
|---|---|---|
| `--ease-out` | `cubic-bezier(0.22, 1, 0.36, 1)` | Reveals, entrances |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | State transitions |
| `--dur-fast` | 140ms | Hover, press |
| `--dur` | 240ms | Standard transition |
| `--dur-slow` | 600ms | Scroll reveal |
| `--beat` | 2200ms | **One beat** — the Moment's ignite, the AI shimmer, the pulse, the clock |

- **One beat.** The slow durations — the light snapping on, the keyline drawing in, the AI sheen, a countdown — all derive from `--beat`, so atmosphere feels authored, not assembled.
- **One lean.** Entrances lean *in*; directional effects (ignite, draw) always travel the same way, like a crowd wave.
- **Calm vs. loud.** The command center moves slowly and little; the Moment is where motion is allowed to land.
- **Reveal.** Scroll content fades with a blur-and-rise (`@keyframes stadli-reveal`), gated behind `.js` via `IntersectionObserver`.
- **Interaction states.** Hover is quiet — primary lightens slightly, secondary/ghost gain a faint surface wash, rows lift one surface step; never a colored hover. Press is a 1px downward nudge, no color change.
- **`prefers-reduced-motion: reduce` disables all of it** — every sheen, reveal, parallax, ignite, and countdown freezes to its resting state.

---

## 17 · AI surfaces

AI-touched surfaces get one consistent, quiet signal — never a robot icon, never a sparkle. The no-icons rule holds: the signal is motion and a word.

- **The AI badge** — a slow, low-contrast monochrome sheen across an otherwise monochrome pill, paired with a word ("AI," "Generated by AI"). Same badge everywhere; the consistency is the point.
- **Insight cards** — short editorial sentences tagged with a narrative dot pill, exception-first: routine output carries the ink dot; `spec-purple` marks the detected outlier, `spec-red` the metric in decline — on the dot only. The card and its copy stay monochrome.
- **Shimmer skeletons** — shape-matched monochrome shimmer instead of a spinner, inside the same card so nothing shifts on resolve.

All three freeze to a static resting state under `prefers-reduced-motion`.

---

## 18 · Photography & mockups

Photography carries the warmth the chrome refuses to.

- **The image is never colored.** No duotone, black-and-white, grayscale, tint, or overlay. Photography ships full-color and untouched; the one thing applied is a fine colorless **film grain** (~6% opacity) — what anchors imagery to the editorial tone and stops it reading as stock.
- **Documentary color** is the treatment direction — slightly desaturated, film-not-Instagram. One treatment everywhere; it's identity glue.
- **Color combines with photography through solid blocks, never overlays.** When a composition needs both, the color sits in a solid panel layered on top; the block carries the color, the image stays clean, the copy on the block stays monochrome. Name people in **Inter set on the image** — large given name + mono meta, never a colored block of text.
- **Subject hierarchy:** faces (mid-emotion, not posed) → crowds → architecture → operational moments. **Real faces beat stock faces.** Faces direct gaze — compose so the subject's eyes point into the copy, number, or CTA.
- **Forbidden imagery** (markers of B2B SaaS): laptops showing the product, conference-room meetings, handshakes, smiling-stock headshots, drone establishing shots, empty seats in marketing, posed "diverse team" shots, lens flares, competitor apparel.
- **Mockup pairing rule:** every product mockup ships with a human moment in the same section. The mockup proves the software exists; the photo proves who it's for.

---

## 19 · Component reference

React components, exposed at `window.StadliDesignSystem` via the compiled bundle. Props below are the public API.

### Core

**`Button`** — Monochrome action control. CTAs state value and close with an arrow ("View tickets →"), never mechanics. Never a spectrum color.
- `variant?: 'primary' | 'secondary' | 'ghost'` — solid / lifted / hairlined
- `size?: 'sm' | 'md' | 'lg'`, `arrow?: boolean`, `disabled?`, `full?`, `type?`, `onClick?`, `style?`

**`Input`** — Forgiving text field. Errors say what happened and how to fix it. Message wired via `aria-describedby`.
- `label?`, `value?`, `onChange?`, `placeholder?`, `type?`, `id?`, `disabled?`, `style?`
- `required?: boolean` — marks the field "required" in words, never an asterisk
- `error?: string | null` — renders a red dot on the message line; **border stays monochrome**
- `hint?: string | null`

**`Card`** — Flat container. No drop shadows — depth is surface contrast + a quiet hairline.
- `surface?: 'canvas' | 'surface' | 'elevated'`, `padding?`, `border?`, `as?`, `style?`

### Data

**`StatusPill`** — The signature status construction: one colored dot, monochrome text. Color marks an outcome, never the expected resting state.
- `tone?: 'pending' | 'positive' | 'negative' | 'attention' | 'new' | 'info' | 'notice' | 'fan'` — `'pending'` = monochrome ink dot
- `variant?: 'dot' | 'pill'` — `'dot'` (bare dot + word) or `'pill'` (rounded hairline container for dense chrome)

**`KpiTile`** — A KPI never travels alone: figure + directional delta + citation. The delta dot is the only color.
- `label`, `value` (formatted), `delta?`, `deltaDir?: 'up' | 'down' | 'risk' | 'flat'` (`'flat'` stays ink), `cite?`

**`DataTable`** — Monochrome table: label-style header, hairline dividers, no zebra, row-hover lift. Status belongs in a dot-pill cell, never a colored row.
- `columns: { key, label, align?, mono?, strong? }[]`, `rows: Array<Record<string, ReactNode> & { id? }>`

**`DotMatrix`** — Data-as-points chart; every point of color is a person. One hue per field; always cited.
- `count?`, `columns?`, `dotSize?`, `gap?`, `hue?`, `fill?: number | null`, `cite: string` (**required**)

**`Moment`** — The loud register (§15). Full-bleed, darker ground, back-row scale, one azure accent — a keyline, dot, or texture field — that ignites over `--beat`. The type stays white. One per view.
- `eyebrow?`, `line` (the distilled statement, monochrome), `accent?: ReactNode` (the azure keyline/field beside the type — never a colored word or number), `image?`, `texture?`, `cite?`

### Feedback

**`AiBadge`** — The consistent tell that a surface is AI-generated: a shimmering monochrome pill + a word.
- `children?: ReactNode` — defaults to "Generated by AI"; `style?`

**`Toast`** — Transient feedback bar from the dot-pill. One at a time; confirmations auto-dismiss, errors persist. Polite live region.
- `severity?: 'confirmed' | 'error' | 'warning'` (dot stays colored), `action?`, `onAction?`, `style?`

### Marketing bands

Section-scale, photo-forward compositions in the `MarketingBands` barrel. Text is always monochrome — color lands on a dot, an atmosphere texture, or a block, never on a word. Emphasis is ink weight (muted context → ink keyword).

- **`SectionManifesto`** — Display-scale type on black beside a full-height photo. `{ eyebrow?, image, alt?, meta?, children }` — emphasize one word with `<em>`; it lifts to ink, never color.
- **`StatBand`** — A giant tabular figure on a full-bleed photo. `{ eyebrow?, figure, suffix?, caption?, image, alt? }`.
- **`DotMatrixBand`** — A one-dot-per-unit matrix over a photo. `{ eyebrow?, image, alt?, columns?, rows?, hotRate?, hue?, cite?, children }`.
- **`PeopleBand`** — "The people" band: heading + mono index + named portraits. `{ heading, index?, people: { image, alt?, name, role? }[] }`.
- **`QuoteBand`** — A testimonial over a photo, closed by a colophon meta bar. `{ image, alt?, children, by?, logo?, colophon? }`.
- **`DissolvePortrait`** — A portrait whose corner dissolves into spectrum dots. `{ image, alt?, name, role?, ghost?, tone? }`.
- **`CollageStrip`** — A staggered row mixing photos and atmosphere-texture panels. `{ items: { image?, alt?, panel?, texture?, h1?, h2?, label?, sub? }[] }`.

---

## 20 · Chrome, extended

### The interaction contract

- **Buttons look like buttons.** Monochrome never means ambiguous — primary solid, secondary lifted, ghost hairlined. Affordance beats minimalism.
- **Inline links carry a subtle underline** in the surrounding text's own monochrome ink (`text-decoration-thickness: 1px; text-underline-offset: ~3px`, muted alpha). The underline is the signal; the color never changes, and a link is never tinted a spec color. Standalone CTAs are the exception — they close with `→` and aren't underlined.
- **Prevent errors before messaging them.** Constrain, disable, and format as the user types. Inputs are forgiving, then normalize on display.
- **Prefer undo over confirm.** Confirmation dialogs are reserved for destructive, irreversible actions.
- **Status is always visible.** Respond under 400ms; past one second, show a shape-matched skeleton, never a spinner.
- **Every action has an exit** — undo, cancel, back. The operator is never trapped.

### Data tables

- Header row on `surface-elevated`, cells in `label` style. Rows separated by `hairline` — no zebra, no outer box heavier than `hairline`.
- Numeric columns right-aligned, tabular, NA format. Text left-aligned. Row height ≥48px.
- Status lives in a dot-pill column — gray means in flight, color means something happened. Row hover lifts to `surface`; selection to `surface-elevated`. Never a colored row.

### Empty states

An empty screen is an invitation to act, set in type: a `heading`-scale line (≤32px), one body sentence saying what will appear, one primary CTA closing with `→`, optionally one annotation line of fact. No illustration, no icon, no spectrum color — the canvas is already the whitespace. ("The doors aren't open yet.")

### Errors, validation & toasts

- **Voice:** say what happened and how to fix it. Errors never apologize and are never vague — "The email needs an @," not "Oops, something went wrong."
- **Inline field errors:** a `spec-red` dot + the sentence in body at 14px below the field. **The input border stays monochrome** (may darken to `--focus-line`, never turns red). Wire with `aria-describedby`.
- **Required fields** are marked in words — "required" in `muted`, never an asterisk.
- **Toasts:** the pill scaled to a bar — `surface-elevated`, hairline border, dot carrying severity, text in body, optional action closing with `→`. One at a time; confirmations auto-dismiss, errors persist. Exempt from exception-first.

### Light theme

Light exists for product parity only — a bright admin in a sunlit box office. Lift still reads as lift; hairlines and text invert. **No atmosphere in light** — no textures, manifesto, dot-matrix art, or grain. Spectrum survives only in data viz + status dots, exception-first exactly as in dark, with the ink dot inverting to near-black and `lime` / `green` / `azure` dots gaining a 1px ring. Film grain never appears in light.

---

## 21 · Voice — the language of the building

We name things the way the people in the stands would. A person is not a record; a quiet account is a regular who stopped coming, and we'd like to know why.

| Machine | Building |
|---|---|
| Inactive account | A regular who stopped coming |
| Churn risk | We'd like to know why they left |
| User record / profile | Someone who's had 14F for thirty years |
| Run campaign | Call the crowd in |
| Occupancy 91% | The house is nearly full |
| Sell-through / conversion | Seats finding people |
| Engagement score | How often they show up |
| Empty state | The doors aren't open yet |

- **Speak the building, not the machine.** Plain, specific, active. Name the thing the way it's lived in the building.
- **Specific beats superlative.** "Sold out in 41 minutes" beats "ultra-fast" — the tabular numeral is the brand's form of proof.
- **More "you" than "we."** The copy talks about the fan and the operator, not about Stadli.
- **Front-load every line.** People scan the first two words of a sentence, a bullet, a button. The key word goes first.
- **CTAs state value, not mechanics.** "View tickets →," "Create a promotion →" — never "Submit," never "Click here."
- **Clarity beats cleverness.** Write at the level of the bleachers, even for the boardroom. Warm, never clever for its own sake.
- **Microcopy is the brand at its most intimate** — error messages, empty states, and button labels get the same care as the manifesto.
- **Casing & numbers.** Title Case for English titles, headings, buttons, and labels. NA number format: comma thousands, period decimal, currency mark before the figure (`$142,850.00`). Round to meaning (`4.2M`); a percentage travels with its base (`+12.1% · n = 3,204`). Documentation is English.

---

## 22 · Trust

Trust is built in drops and lost in buckets. Stadli's honesty devices — tabular numerals, the annotation register, real names — are trust mechanics, not decoration.

- **Proof is specific.** A testimonial carries a full name, a face, and a real outcome. Anonymous praise reads as decoration.
- **Numbers move and reconcile.** "Join 12,480 fans" beats "thousands of fans," the figure is live, and a metric shown twice matches exactly — or every other number becomes suspect.
- **Scarcity is real or absent.** "48 seats left in section 104" must be true to the seat. A fake countdown destroys trust permanently.
- **No dark patterns.** No confirm-shaming, no hidden costs, no forced continuity. Cancelling is as easy as buying — the exit is the last brand impression and the seed of the return.
- **Color that cries wolf is a dark pattern too.** Exception-first is a trust mechanic: when a colored dot always means something real, operators learn to act on it. A dot whose color carries no information teaches them to ignore every dot.

---

## 23 · Accessibility & responsive

- Target **4.5:1** body contrast on every surface; display type on atmosphere targets AAA (the dark zone makes contrast structural). Visible keyboard focus; 44px touch targets.
- **Color is never the only signal** — a status dot always travels with its word; chart series are direct-labeled (monochrome) or paired with a dot + word; the key takeaway is stated in copy so the data survives without the picture.
- Inline errors wired with `aria-describedby`; toasts announce via a polite live region. Chart tooltips have a touch and keyboard equivalent — hover is never the only path to a value.
- On light surfaces, `lime` / `green` / `azure` dots carry a 1px `hairline-strong` ring. Every photograph carries descriptive alt text.
- **One track set, fluid at every width.** Contained bands span the inner twelve and center past 1440; full-bleed bands never stop. At `collapse` (900) multi-column `subgrid` children drop to `grid-column: 1 / -1` and stack; the mockup-plus-photo pairing survives stacking. At `compact` (560) KPI grids go 4 → 2 → 1, CTAs stack full-width, tables scroll horizontally with a hint.
- **Mobile-first, not mobile-shrunk.** For most fans the phone *is* the brand. Atmosphere textures stay anchored to the bottom edge on mobile; the dark zone above remains the type area. The manifesto never wraps past three lines — shorten the words before shrinking the type.
- The no-icons rule does not pause on small screens: the nav collapses to a single text button ("Menu →"), never a hamburger.

---

## 24 · Don't

- Don't put spectrum color on chrome. Gating is by surface, not element type.
- Don't colorize type — display, headlines, and body stay monochrome on every surface, with no exceptions. Not a single word, not a single glyph, not a number, not even the Moment's accent. Color rises in the texture behind the type, sits in a block beneath it, marks data beside it, or fills the dot next to it — never a letterform. Word-level emphasis is ink weight or `<em>` to ink, never a hue.
- Don't drop an inline link's underline or tint it a spec color.
- Don't color the pending state. In-flight and routine labels carry the ink dot; a spec color means outcome, direction, attention, or the one story.
- Don't run two colored stories in one viewport, or color both series of a two-series comparison. White-versus-gray is the comparison; the hue is the single story.
- Don't push display weight past 500. Hierarchy is size and tracking.
- Don't add drop shadows, gradients, or halos. Cards are flat; color-as-light is dot and stripe texture, not glow.
- Don't reach for icons. The arrow `→` on a CTA is the only permitted mark, and it's typography.
- Don't add a second typeface. One family — Inter — with no mono face.
- Don't let an atmosphere texture saturate its frame — keep a third of it near-black.
- Don't scatter dots as texture in a data context. Every data dot maps to a real quantity and ships with its citation.
- Don't color a `.pat-type` field or any monochrome pattern — those stay strictly neutral; color lives in the `.atmo-*` fields.
- Don't tint, tone, duotone, or overlay images. Only the colorless grain touches a photograph. For color + photo, layer a solid block on top.
- Don't run photography without the grain overlay — stock-photo look is the failure mode, and don't ship a mockup floating alone.
- Don't plot dual y-axes, truncate a bar baseline, or stretch an aspect ratio.
- Don't ship a carousel hero, or run more than one Moment per view, or more than three product sections without an atmosphere break.
- Don't add a third content width — type caps at 1280, content at 1440.
- Don't redeclare the columns — the twelve tracks are defined once; multi-column bands inherit them through `subgrid`.
- Don't ship atmosphere in the light theme — light is product parity only.
- Don't mark AI surfaces with an icon — the signal is the shimmer plus a word.
- Don't fake scarcity or use dark patterns. Real counts, real deadlines, and an exit as easy as the entrance.

---

## 25 · Files & assets

```
stadli-design-system/
├─ index.html      # Self-contained build (imagery embedded as optimized base64)
├─ design.md       # This document
├─ styles.css      # Global entry — @imports fonts → colors → typography → spacing → effects → base
└─ images/         # Source photography (full resolution)
   ├─ crowd.png            ├─ jersey-mesh.png
   ├─ section-217.png      ├─ eye.png
   ├─ foam-finger.png      └─ stadium-tunnel.png
```

`index.html` renders on its own — the photographs are embedded. The `images/` folder holds the originals for production, where you'd reference real `<img>` files instead of data URIs. Styles link the global `styles.css` to inherit all tokens and fonts; components read from `window.StadliDesignSystem` after the compiled bundle loads. Default canvas is `--canvas` (`#010101`), `--body` text, Inter at 17px with tabular numerals on; set `[data-theme="light"]` for the chrome-only light theme.

### Hosted asset URLs

Live, reference-able URLs for the photography and logo above — use these directly in `image`/`src` props instead of base64 or local paths.

**Photography**

| File | URL |
|---|---|
| 217 | `https://stadli.com/assets/photography/217.png` |
| Arena, courtside | `https://stadli.com/assets/photography/arena-courtside.png` |
| Atmosphere, section 217 | `https://stadli.com/assets/photography/atmosphere-section-217.png` |
| Crowd, dancer | `https://stadli.com/assets/photography/crowd-dancer.jpg` |
| Crowd, reach | `https://stadli.com/assets/photography/crowd-reach.png` |
| Crowd | `https://stadli.com/assets/photography/crowd.png` |
| Eye, closeup | `https://stadli.com/assets/photography/eye-closeup.png` |
| Eye | `https://stadli.com/assets/photography/eye.png` |
| Foam finger | `https://stadli.com/assets/photography/foam-finger.png` |
| Jersey mesh | `https://stadli.com/assets/photography/jersey-mesh.png` |
| Seats, blue | `https://stadli.com/assets/photography/seats-blue.png` |
| Stadium tunnel | `https://stadli.com/assets/photography/stadium-tunnel.png` |
| Stage, performers | `https://stadli.com/assets/photography/stage-performers.jpg` |

**Logo**

| File | URL |
|---|---|
| Wordmark | `https://stadli.com/assets/logo.svg` |

Same rules apply as to local imagery: the colorless film grain still goes on top, no duotone/tint/overlay, and forbidden-imagery rules (§18) still hold.

### The brand in one line

Monochrome by contract; **people are what's in color when they show up.** Two volumes, never confused — the work is calm, the Moment is loud, and loud is earned. Type, the tabular number, the dot, and the human face carry every meaning; color is light, rationed to atmosphere, and the light is azure.
