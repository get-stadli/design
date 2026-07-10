## Components

### Buttons

Primary (solid black), secondary (outlined), and tertiary (text-only) variants, all pill-shaped except tertiary — always rendered in the monochrome chrome palette, never in a content color. Hover darkens fill slightly; focus uses a solid black ring; disabled drops opacity. Even where a reference shows a saturated CTA, buttons in this system stay chrome; the loud moment is spent on a block or an image, never on a control.

### Cards & Containers

Flat surfaces with hairline borders and generous 32px padding — and this chrome state is the default and the norm: most cards on any page are surface-1 or surface-2 with a hairline, full stop. A card may be filled edge-to-edge with one flat, full-strength color pulled from its content only when it carries a narrative moment that earns the fill (see Signature Components), counted against the per-viewport block budget — and never when it contains a chart, in which case it stays chrome and the color enters only through the data marks. When a card is filled, its border and any chrome inside stay neutral.

**A filled block may host media.** A filled block is not required to be an empty slab of color: it may frame imagery in a rounded media frame and carry chrome sub-cards (a stat pill, a small white UI card) floating over or beside that imagery. The fill itself stays a single flat color, all text and sub-cards resolve to chrome per Legibility stays chrome, and the entire assembly — fill, photo, overlays — counts as *one* loud moment against the block budget, not several. The hosted image is raw as always, and the block's hue is extracted from it by the standard extraction (or is a sanctioned rotation of the viewport's anchor). Feature cards use a slightly larger radius and a faint surface-2 tint to differentiate standard cards. Scroll affordances are chrome. The native scrollbar is suppressed in favor of the `rail-handle`: an 8px `hairline-strong` pill on a transparent track — no track chrome, no arrows, no buttons — that darkens to `ink-subtle` on hover or while dragging (tone only, never a color). It is self-effacing, appearing while the reader is hovering, scrolling, or has the handle focused, and fading out after `idleHideDelay` so nothing sits in the frame when it is not in use. The whole strip is grab-to-pan (press anywhere and drag; the cursor reads grab → grabbing), the pill itself is draggable, and the handle carries a real `scrollbar` role with arrow / Page / Home / End keys and a 20px invisible hit band around the 8px visual. This governs any horizontally scrolling region; the story rail is its primary home.

### Stat Cards & Metric Rows

"Print the number" as components, not a habit. Both are pure chrome — black figures on neutral surfaces with hairline structure — so they cost nothing against any budget and can repeat freely across a viewport.

- **Stat card** (`stat-card`): an eyebrow label in ink-subtle, one large figure at display size (tabular figures on), and a one-line body-sm caption in ink-muted. The figure is the content; nothing else in the card competes with it.
- **Metric header row** (`metric-header`): two to five stat cells in a single hairline-bordered strip, separated by hairline dividers — label above, value below, an optional delta beneath. Cells stack to a single column on mobile with dividers rotating to horizontal.

The only color either component ever carries is the licensed semantic whisper: a delta's digits and arrow in `semantic-success` / `semantic-warning` / `semantic-error`, per Colors → Semantic. The card, the value, and every border stay chrome.

### Inputs & Forms

Fields are white with a hairline-strong border, switching to solid black on focus. Labels use caption typography in ink-muted. Inputs are chrome and never take a content color.

**States.** Error is the one licensed departure from chrome on a control: an invalid field prints `semantic-error` on its border and its helper text (`text-input-error`), while the background stays canvas and the label stays chrome — the extension of semantic scope defined in Colors → Semantic, and the only border in the system that ever leaves the neutral ramp. Success needs no color: a field that validates simply returns to its resting chrome state (an optional confirmation may print its text in `semantic-success`, text only). Helper text explains what to do next in one plain sentence — errors never apologize and are never vague. Loading is chrome in motion: skeleton bars pulse between surface-2 and surface-3 — an opacity/tone pulse, never a traveling shimmer gradient, which the no-gradient rule forbids. Empty states are an invitation to act: a body-sm line in ink-muted naming the first action, with an optional chrome button — no illustration, no icon standing in for the words.

### Navigation

The top nav is pure chrome. Sometime overlay. Links are button typography in ink-muted, darkening to ink on hover and sitting at full ink when active — state is carried by weight and tone, never by color or underline decoration. 

### Iconography

The system does not use icons *as labels* — an icon in the place where a word belongs. A feature is named in text, a chart series is named at the mark, a status is spelled out; this is why there are no legends and no icon-captioned feature grids. What the system does permit is *functional chrome affordances*: the small set of glyphs that operate the interface rather than describe content — menu (hamburger), search, close, chevron/disclosure, carousel arrows, external-link, play/pause. These are chrome — rendered in ink, monochrome, no content color, sized to the touch-target minimum, and never decorative. The test is simple: if a glyph is carrying meaning that a word should carry, it's barred; if it's a control the user operates, it's chrome and allowed.

### Signature Components

Components exist to tell the story — build whatever the story needs, as long as it stays in sync with the chrome and the rest of the page. The story comes first, always.

The story comes first. The chrome stays silent so the few loud moments can actually be heard.

**Two classes of component — chrome you reuse, story you invent.** The components in this document are not one library. *Chrome primitives* — button, input, nav, footer, badge, focus ring, the `rail-handle` — are the interface's fixed vocabulary: reuse them verbatim, because a control that drifts between pages is a bug, and consistency is the whole job of chrome. *Story components* — the story rail, stat and metric cards, sparkline cards, filled blocks — are worked examples, not inventory. They show how the tokens and the color and motion laws combine to carry a claim; copy the *reasoning*, then build the component this content actually needs, even if it appears nowhere here. Instantiating the rail, the metric header, and the stat card *because the spec named them* is the most common way to misread this system. The examples are evidence of the laws, spent once as inspiration — never a checklist to work through.


**The story rail.** The system's named composite: a horizontal strip of mixed cards — raw photo cards, one or two flat filled color cards, chrome stat cards, chrome sparkline cards — sharing one height and one gap, dragged or overhanging the container edge (rails are content blocks, so they may bleed past the container per Layout → Viewport bleed). The rail is moved by grab-to-pan — the reader presses anywhere on the strip and drags, and on release it decelerates and stops with no elastic edge-bounce (see Motion → Rail glide) — with the self-effacing `rail-handle` as the visible affordance and keyboard path. The rail is counted as **one** composite loud moment against the block budget: the strip carries the section together, so it occupies a single slot no matter how many cards it holds. The hue budget is *not* relaxed inside it — filled cards in a rail draw on the viewport's anchor and its sanctioned rotations (in practice: at most two filled cards, anchor plus one sibling), photo cards stay raw, and every other card is chrome. Text and controls on filled or photo cards resolve to chrome per Legibility stays chrome. A rail that is mostly chrome and photography with one saturated card is the intended reading; a rail of wall-to-wall color is a palette swap wearing a costume.

Reach for the rail only when the content is genuinely a row of peer items with more than fit on screen, so the horizontal overflow is real and traversing it is the point. A rail of three cards that already fit is a grid in costume; a rail chosen to "add energy" is decoration. Most sections are not rails — it is one worked example of the laws, not a default layout.

Two rules keep the forms coherent:

- **Shared bloodline.** Any color block sharing a viewport with an image pulls its hue from that image by the standard extraction, so a viewport mixing a photo and color tiles still reads as one palette. Color blocks are derived from the imagery on screen, never hand-picked against it.
- **Legibility stays chrome.** Text, labels, and functional marks sitting on a colored block or a photograph resolve to chrome ink — pure black or pure white, whichever carries contrast — never to a content hue. If neither reads cleanly, add the subtle seamless chrome scrim or blur from Photography & Illustration Geometry rather than tinting the type. Type is chrome even when everything behind it is loud.
