# Stadli — Design System (minimal)

Operating platform for sports franchises. **Monochrome on purpose, so that people are what's in color when they show up.**

**How to build:** paste **§Tokens** verbatim → obey the **§7 Laws** → compose **§Components** (they enforce the laws for you) → match a **§Recipe**. When two surfaces seem to conflict, the more monochrome reading wins.

| Building… | Go to |
|---|---|
| anything | §7 Laws, §Tokens |
| a dashboard / product page | §Layout, §Components, Recipe A |
| a chart or KPI | §Components (Chart, Kpi), Recipe D |
| a marketing / hero section | §Surfaces, §Components (bands), Recipe C |
| the sellout / big-night screen | §Surfaces (the Moment), Recipe B |
| copy, labels, errors | §Voice |

---

## The idea (read once — this is the taste)

Color never lives inside type or chrome. It rises out of the black as **light** (dot/stripe texture) or appears as **data** (charts, dot matrices) where every point maps to a real person or number. Chrome stays monochrome so the people, the photographs, and the one important number are what carry color.

The system runs at **two volumes, never confused**: the work is *calm* (dashboards, lists, numbers) and the Moment is *loud* (the match, the gate, the sellout). Loud is rare, so loud lands.

---

## The 7 Laws (the only rules)

1. **Monochrome chrome.** Buttons, inputs, cards, nav, tables, hovers are always monochrome. Color is gated to atmosphere, data, and dots — **never chrome, and never inside type** (not a word, glyph, or number, ever; emphasis is ink weight or `<em>`).
2. **Color is scarce and earned.** At most **one colored thing per screen** — one chart story-series *or* one dot field. It marks an **outcome, a direction, or the one story** — never a resting state, never decoration. Pending/in-flight/routine = the monochrome ink dot. A two-way comparison is white-vs-gray; the hue is the single story.
3. **One typeface (Inter), no icons.** Hierarchy is size, tracking, whitespace, and the tabular number. Display weight caps at **500**. The only mark is the CTA arrow `→`, read as punctuation.
4. **Flat.** No gradients, halos, or drop shadows. Depth is surface contrast + hairlines. Color-as-light is dot/stripe texture, not glow.
5. **Two volumes.** Calm is the default everywhere; the Moment is loud, monochrome, and **once per view, maximum**.
6. **People are required.** Photography is recurring and load-bearing, not optional. Every product section ships with its paired human moment; full-color, untouched, film-grain on top.
7. **Speak the building, not the machine.** Plain, specific, warm. Name things the way the stands would.

---

## §Tokens — paste verbatim (single source of truth)

```css
:root {
  /* surfaces (dark = default) */
  --canvas:#010101; --surface:#080808; --surface-2:#1a1a1a;
  --hairline:#161616; --hairline-2:#303030; --focus-line:#454545;
  --focus-ring:rgba(255,255,255,.12);

  /* text — hierarchy is weight/value, never color */
  --ink:#fff; --body:#e8e8e8; --muted:#929292; --muted-soft:#6a6a6a;

  /* raw palette — for ATMOSPHERE only (pick by feel; never on chrome/type) */
  --red:#ff4b3e; --orange:#ff9d2e; --lime:#f2e23a;
  --green:#22c55e; --azure:#3f86f2; --purple:#b85cf2; --rose:#ff5c9e;

  /* semantic — the ONLY colors allowed on data + status dots (fixed meaning) */
  --ok:var(--green); --bad:var(--red); --warn:var(--orange); --info:var(--azure);

  /* type */
  --font:"Inter",system-ui,-apple-system,sans-serif; /* no second face, no mono face */
  --w-display:500; --w-title:600; --w-body:400; --w-label:700;
  --t-display:clamp(44px,5.6vw,72px); --t-heading:clamp(34px,4.5vw,62px);
  --t-title:22px; --t-body:17px; --t-small:14px; --t-label:12px; --t-meta:11px;

  /* spacing / radii */
  --s1:4px; --s2:8px; --s3:12px; --s4:16px; --s5:24px; --s6:32px;
  --s7:48px; --s8:64px; --s9:96px; --s10:152px;
  --r-sm:6px; --r-lg:8px; --r-xl:12px; --r-pill:9999px; --touch:44px;

  /* layout */
  --edge:clamp(20px,5vw,64px); --container:1440px;
  --bleed-inset:clamp(24px,6vw,120px); --gutter:clamp(24px,3vw,48px);
  --cap:1280px; /* where display TYPE stops scaling — not a width */

  /* motion — all slow timing derives from --beat */
  --ease:cubic-bezier(.22,1,.36,1); --ease-io:cubic-bezier(.65,0,.35,1);
  --fast:140ms; --dur:240ms; --slow:600ms; --beat:2200ms;
}

[data-theme="light"]{ /* product parity ONLY — no atmosphere, grain, or Moment in light */
  --canvas:#f2f2f1; --surface:#fafafa; --surface-2:#fff;
  --hairline:#e6e6e6; --hairline-2:#d0d0d0;
  --ink:#0a0a0a; --body:#232323; --muted:#6d6d6d; --muted-soft:#9b9b9b;
  --focus-ring:rgba(0,0,0,.12);
}

body{ background:var(--canvas); color:var(--body);
  font:var(--w-body) var(--t-body)/1.55 var(--font); font-variant-numeric:tabular-nums; }
```

---

## §Type

| Step | Size / line-height / tracking | Weight | Use |
|---|---|---|---|
| display | `--t-display` / 1.05 / -.03em | 500 | manifesto, hero, the Moment |
| heading | `--t-heading` / 1.10 / -.02em | 500 | section + chart titles |
| title | `--t-title` / 1.3 / -.01em | 600 | sub-headlines |
| body | `--t-body` / 1.55 / 0 | 400 | copy |
| small | `--t-small` | 400 | secondary |
| label | `--t-label` / .083em **CAPS** | 700 | eyebrows (a few words) |
| meta | `--t-meta`, `--muted-soft`, tabular | 400 | the annotation register |

- Heaviness = size + tight tracking, never stroke (cap 500). If two levels look alike, restore the size jump.
- **Tabular numerals everywhere** on metrics/tables — the number is the brand's icon.
- **Meta = the forensic voice:** file-paths, `updated 12s ago`, `n = 18,442 · source: ticketing`, `SEC 104 · R12 · S07`. It annotates, never titles; never on the manifesto or inside a quote.

---

## §Color

- **Chrome + type:** none. (Law 1.)
- **Data + status dots:** only `--ok / --bad / --warn / --info`, exception-first. (Law 2.) Pending = ink dot. Deltas are directional (`--ok` up, `--bad` down, `--warn` at-risk; flat = ink). One affirmative-green carve-out: a *live measured* "Operational" health row.
- **Atmosphere + marketing:** any raw hue (`--red`…`--rose`), picked by feel, expressive — it can't touch chrome anyway. One hue per field.
- **Where a chart needs forecast or a second emphasis, use form, not a 5th color:** forecast = a **dashed** line, an outlier = one **highlighted point**, lead vs. supporting = stroke weight.

---

## §Layout — three tiers, nested centered containers (no grid template, no line names)

```css
.wide  { width:100%; max-width:var(--container); margin-inline:auto; padding-inline:var(--edge); }
.full  { width:100%; }                              /* edge-to-edge; put a .wide inside for text */
.bleed { width:100%; max-width:calc(var(--container) + 2*var(--bleed-inset));
         margin-inline:auto; padding-inline:var(--edge); } /* display/heading TYPE only */

.cols       { display:grid; grid-template-columns:repeat(12,1fr); gap:var(--gutter); }
.cols>.lead { grid-column:span 8; }
.cols>.side { grid-column:span 4; }
@media (max-width:900px){ .cols>.lead,.cols>.side{ grid-column:1/-1; } .bleed{ max-width:var(--container); } }
```

- **`wide`** = the default (dashboards, prose, forms, tables). **`full`** = immersion (hero, photo, atmosphere, the Moment); its text re-wraps in a `.wide`. **`bleed`** = a headline opting a fixed amount wider; never body, chrome, or meta.
- `.wide` and `.bleed` are both centered and share `--edge`, so they line up automatically — nothing to keep in sync.
- **Rhythm:** read the page like a magazine cut into bands — black product band → full-bleed photo/atmosphere → black. One idea per band. 5–9 widgets per product view. Never 3+ product sections without a photo/atmosphere break. One manifesto per page.

---

## §Surfaces — texture, photography, the Moment

**Texture, two families, never mixed.** Color rises out of black; never a flat fill, and the optical center stays ≥⅓ near-black so the words sit on dark.
- `.atmo-dots` · `.atmo-stripes` · `.atmo-matrix` — **carry color (light).** One hue per field; value = density/opacity steps. Render as `inset:0; z-index:0` inside a `position:relative` near-black box, `.grain` on top.
- `.pat-dots` · `.pat-lines` · `.pat-type` — **always monochrome** calm texture. Never take a hue.

**Photography (Law 6).** Required and recurring — a marketing page runs ≥3 full-bleed photo bands; a product page shows a face every ~2 screens. Faces (mid-emotion, not posed) → crowds → architecture → operational. The only treatment is a fine colorless **film grain (~6%)** — no duotone, tint, grayscale, or overlay. For color + photo, layer a solid block on top; copy on it stays monochrome. **Forbidden:** laptops-showing-product, conference rooms, handshakes, stock headshots, drone shots, empty seats, posed "diverse team," lens flares.

**The Moment** = the earned roar, once per view. Full-bleed, a ground darker than the page (`#070809`), back-row display scale on `.bleed`, generous air. **Monochrome** — force is scale + dark + air, never a hue. A `.pat-*` may carry the dark. Voice distilled: *"A full house is a city saying yes."*

---

## §Components (correct-by-construction — composing these inherits the laws)

Exposed at `window.StadliDesignSystem`. The point of using them is that the wrong thing is *impossible*: a pill can't colorize its label, a card can't grow a shadow, a chart can't run two story-colors.

**Core**
- `Button` — monochrome action; CTA states value + `→`. `variant: primary|secondary|ghost` · `size` · `arrow` · `full` · `disabled`.
- `Input` — forgiving field; error never colors the border or label. `label · value · onChange · required` (the word, not `*`) · `error` (red dot on the message line) · `hint`.
- `Card` — flat container, hairline + surface lift only. `surface: canvas|surface|elevated` · `padding` · `border`.

**Data** (color = `--ok/--bad/--warn/--info` only, on the dot)
- `StatusPill` — colored dot + mono text. `tone: pending|positive|negative|attention|info` (`pending` = ink dot) · `variant: dot|pill`.
- `Kpi` — figure + directional delta + cite (a number never travels alone). `value · delta · deltaDir: up|down|risk|flat · cite`.
- `Table` — mono; no zebra, no colored row; status lives in a dot cell. `columns · rows`.
- `Chart` — chart-as-poster: heading-size title that **states the insight**, one story series (rest mono), bars from zero, cite required. `series · story · title · cite`.
- `DotMatrix` — every dot = one real unit; one hue. `count · columns · hue · cite` (**required**).
- `Moment` — the loud register; monochrome, full-bleed, one per view. `eyebrow · line · image|texture · cite`.

**Feedback**
- `AiBadge` — shimmer pill + a word, never an icon. `children?` (default "Generated by AI").
- `Toast` — severity dot on a bar; one at a time (exempt from scarcity). `severity: confirmed|error|warning · action`.

**Marketing bands** (`MarketingBands`) — text always monochrome; color lands on a dot, an `.atmo-*` field, or a block. `SectionManifesto · StatBand · DotMatrixBand · PeopleBand · QuoteBand · DissolvePortrait · CollageStrip`.

---

## §Recipes (copy the shape)

**A — product band** (calm, `.wide`)
```jsx
<section className="wide">
  <p className="meta">stadli/app/(admin)/ticketing/dashboard.tsx · synced 9:04 PM</p>
  <div className="cols">
    <Kpi className="side" value="$142,850" delta="+12.1%" deltaDir="up" cite="vs last wk" />
    <Kpi className="side" value="18,442"   delta="−3.0%"  deltaDir="down" cite="n = 3,204" />
    <Kpi className="side" value="91%"       delta="flat"   deltaDir="flat" cite="house full" />
    <Table className="lead" columns={cols} rows={rows} />
  </div>
</section>
```

**B — the Moment** (loud, one per view)
```jsx
<Moment className="full" eyebrow="SECTION 104 · SOLD OUT"
  line="A full house is a city saying yes." cite="41 minutes to sellout" />
```

**C — manifesto beside a photo** (marketing, full-bleed)
```jsx
<section className="full">
  <SectionManifesto image="https://stadli.com/assets/photography/crowd.png" alt="…"
    eyebrow="THE TEAM BEHIND THE TEAM">
    The fans feel the roar; <em>we build the room it happens in.</em>
  </SectionManifesto>
</section>
```

**D — chart as poster** (one story series)
```jsx
<section className="wide">
  <Chart title="The 2026 season passes 2025 by spring"
    series={[{name:"2026", story:true}, {name:"2025"} /* mono */]}
    cite="source: ticketing · 2026 season" />
</section>
```

---

## §Voice

| Machine | Building |
|---|---|
| Inactive account | A regular who stopped coming |
| Churn risk | We'd like to know why they left |
| Run campaign | Call the crowd in |
| Occupancy 91% | The house is nearly full |
| Engagement score | How often they show up |
| Empty state | The doors aren't open yet |

- Plain, specific, active. **Specific beats superlative** — "Sold out in 41 minutes," not "ultra-fast."
- More "you" than "we." **Front-load** the key word. CTAs state value (`View tickets →`), never "Submit."
- Errors say what + how to fix, never apologize: "The email needs an @." Required is a word, not `*`.
- **Trust:** real names + real counts only; a metric shown twice must match; cancelling is as easy as buying. A colored dot that means nothing teaches people to ignore every dot.

---

## §Don't (lint before shipping)

- [ ] Color on chrome or inside type (incl. one "colored word," a number, the Moment).
- [ ] More than one colored field per screen; both series of a comparison colored.
- [ ] A colored pending/resting state (that's the ink dot).
- [ ] Display weight past 500; a 4th width tier; `wide/bleed` for body or chrome.
- [ ] Gradients, halos, shadows, icons (the CTA `→` is the only mark), a 2nd typeface.
- [ ] Tint/duotone/overlay on a photo; photography missing; a mockup without its paired face.
- [ ] A data dot with no citation; a 5th chart color (use dashed/weight/point); dual y-axis or truncated bar baseline.
- [ ] Atmosphere in the light theme; fake scarcity or dark patterns.

---

## §Assets — hosted URLs

Use directly in `image`/`src`. Grain still applies; §Surfaces photo rules hold.

`…/photography/` + `crowd.png` · `crowd-dancer.jpg` · `crowd-reach.png` · `217.png` · `arena-courtside.png` · `atmosphere-section-217.png` · `eye.png` · `eye-closeup.png` · `foam-finger.png` · `jersey-mesh.png` · `seats-blue.png` · `stadium-tunnel.png` · `stage-performers.jpg` — all under `https://stadli.com/assets/`. Logo: `https://stadli.com/assets/logo.svg`.

---

**In one line:** monochrome by contract; *people are what's in color when they show up.* Two volumes, never confused — the work is calm, the Moment is loud and earned. Type, the tabular number, the dot, and the human face carry every meaning; color is light, rationed to atmosphere.
