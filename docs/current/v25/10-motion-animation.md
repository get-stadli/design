## Motion & Animation

Motion is chrome. It obeys the same discipline as everything else in the frame: quiet by default, loud only when a claim earns it. The system is flat, so motion never fakes depth — no parallax, no lift, no shadow blooming under a hover, no card floating toward the viewer. Movement lives in the plane: **tone, opacity, and small in-plane travel**, the same vocabulary the loading skeleton already uses when it pulses between `surface-2` and `surface-3` instead of running a shimmer gradient. That pulse is the whole language in miniature — if a motion can't be built from tone and opacity and a short honest move, it doesn't belong here.

Two hard rules fall straight out of the rest of the system and are worth stating first, because they rule out most of what makes a design feel generated:

- **Motion never introduces or shifts a hue.** Hover darkens tone within chrome; it never fades in a color, and it never shifts the one earned hue. This is the kinetic form of *no color-shifting hovers*.
- **Motion never simulates depth.** No parallax, no z-translation, no shadow or glow appearing on interaction. Layering stays surface tone and hairlines, in motion as at rest (see Elevation & Depth).

### The Motion Budget

Color has a per-viewport budget of one loud moment; motion has the same. Micro-motion — tone shifts on hover and press, the fade-rise of content into view, the loading pulse — is free, like chrome: it may repeat anywhere. But **orchestrated** motion — a figure counting up, a chart drawing its marks, a staged hero reveal — is budgeted to **at most one loud moment per viewport**, earned by a claim exactly the way color is. No claim, no motion. A viewport where everything animates is the motion equivalent of a rainbow chart: the eye has nowhere to land because everything is competing.

### Tokens

Motion is tokenized like spacing and type — a handful of named steps in the `motion` block of the frontmatter, no ad-hoc values. Durations grow on roughly a 1.6× rhythm (`instant` 160ms → `fast` 320ms → `base` 560ms → `slow` 1400ms → `deliberate` 1600ms), so macro motion outweighs micro the same way the spacing scale stretches at the top. Easing is fixed to four curves: `standard` (a long cinematic ease-out — a quick lead into a slow, graceful settle — and the default), `exit` for anything leaving (accelerates away), `in-out` for reorders and in-place moves (smooth, symmetric), and `linear` for continuous loops only. Stagger (`opening` 220ms easing toward a `floor` of 110ms, `cap` at 6 items), the reveal `blur` of 6px, and the scroll `activation-line` at 65% are tokenized alongside them.

**No spring, no overshoot, no bounce, no elastic.** The mood is technical and editorial — engineered curves that arrive and stop. An overshoot is the motion equivalent of a saturated CTA: it belongs to a different, louder system.

### Named Motions

Each pattern is bound to components that already exist, so motion never invents behavior the system doesn't already sanction.

**Tone shift** (`fast` · `standard`). Hover and press are carried by tone within chrome, never a lift or a color. Nav links darken toward ink; buttons darken their fill; table rows tint to `surface-2`. Press adds an `instant` scale nudge (≈0.97), nothing more. This is *state by weight and tone* made kinetic.

**Fade-rise** (`slow` · `standard`). The workhorse content entrance: opacity 0→1 with an upward travel of **no more than `spacing.sm` (8px)** and a **6px blur clearing to sharp** — a soft focus-in that reads as the block settling, not a filter effect. A scroll-triggered reveal does not fire when the block first peeks into view; it waits until the block reaches **reading position** — its top crossing the activation line at ~65% of the viewport — so motion begins in front of a reader who has arrived, not behind one still scrolling toward it. The first viewport is the exception: its content (typically a staged hero) plays **on load**, not on scroll — a reader who is already at the top must still see it appear rather than find it pre-settled. Elsewhere, anything already inside the activation zone when the page loads also animates in immediately; the trigger gates on position, never on the act of scrolling. The cap is the point — a longer travel reads as parallax, which flatness forbids. Blocks and cards enter with fade-rise as they reach the viewport; sub-elements inside a block do not each animate, the block arrives as one piece.

**Staggered rail** (`slow` · `50ms` step, capped). When several cards enter together — a story rail, a metric row — they fade-rise on an accelerating cascade (a ~220ms opening gap easing toward a ~110ms floor) so the strip assembles in one rhythm, like the shared height and gap. The stagger is capped (`stagger.cap`) so a long rail never crawls. The hue and block budgets are unchanged inside a rail; only the timing is added.

**Rail glide** (direct, then decelerate to a stop). The motion of dragging a rail. While the pointer is down the strip tracks it 1:1 — no easing, no lag; a drag is a direct manipulation, not an animation. On release, the drag's velocity carries the strip into a short deceleration that loses a fixed fraction of its speed each frame (`rail-handle.decay`) and simply stops — no coasting past, and a **hard clamp at both edges**, never an elastic pull-back or bounce. This is the one motion driven by input velocity rather than a duration token, but it obeys the same law as the rest: it arrives and stops. Like hover and press it is chrome interaction, not an orchestrated moment, so it is **not** counted against the motion budget. Under reduced motion the glide is dropped entirely — the strip stops the instant the pointer lifts.

**Tone pulse** (`~2000ms` · `in-out` · loop). The system's one continuous motion, already specified for loading: skeleton bars pulse between `surface-2` and `surface-3` — opacity and tone only, **never a traveling shimmer gradient**, which the no-gradient rule bars. It is the only motion permitted to loop, because it reports an ongoing state rather than a transition.

**Count-up** (`deliberate` · ease-out) — *a loud moment.* "Print the number" made kinetic: a figure counts from a baseline to its **true value** and lands exactly on it — no jitter, no fake precision — with **tabular figures** locked so digits never reflow. Use it only when the number's arrival is the claim (a stat card carrying a section), and it spends the viewport's one loud motion. A semantic delta may whisper in after the count settles, hue on the number alone.

**Mark draw** (`deliberate` · ease-out) — *a loud moment.* A chart that has earned its hue draws it in: the line strokes left-to-right, the area fills beneath, bars grow from the axis. Motion obeys the color law — the **emphasized mark lands last and lands hardest** (the final point scales in, the one saturated bar arrives after the gray ones). Gray comparison marks simply fade; they were never candidates for attention. Structural chrome (axes, gridlines, ticks) does not animate. One drawn chart is the viewport's loud moment.

**Focus ring** (`instant`). Focus is a state, so the solid ink ring appears crisply and near-instantly — **never an animated glow or pulse**, since glows are banned for depth. On/off, no travel.

### Reduced Motion

`prefers-reduced-motion: reduce` collapses everything: reveals and staggers become instant (or a plain ≤`fast` opacity fade), the count-up jumps to its final value, the chart appears fully drawn, the rail glide is dropped so the strip stops the instant the pointer lifts, and the loading pulse falls to a static tone. This is not a degraded experience — it is the system's own restraint taken to completion, and it must always be a finished, correct surface.

### Do

- Keep chrome motion to tone and opacity — hover darkens, it never colors or lifts.
- Spend the one loud motion deliberately: a count-up *or* a chart draw *or* a staged reveal per viewport, not all three.
- Cap the fade-rise travel at 8px; let the block arrive as one piece, not a cascade of parts.
- Let the emphasized mark or the claim arrive last — motion follows the color law.
- Respect reduced motion as a first-class state, not an afterthought.

### Don't

- Don't fake depth: no parallax, no float-on-hover, no shadow or glow appearing on interaction.
- Don't shift a hue in motion — no color-fading hovers, no accent sliding in.
- Don't use spring, bounce, overshoot, or elastic easing; arrivals are decisive, not playful.
- Don't run a traveling shimmer over a skeleton; loading is a tone pulse, per Inputs & Forms.
- Don't animate structural chrome (axes, gridlines, borders, ticks) or let more than one orchestrated motion run per viewport.
