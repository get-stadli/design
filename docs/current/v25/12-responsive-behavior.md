## Responsive Behavior

### Breakpoints

Anchored to the layout tokens (`container: 1440`, `narrow: 898`):

- `mobile`: < 640px — single column; section spacing steps down (144px → 96px).
- `tablet`: 640–1024px — up to two columns; side-by-side media/text may still pair or begin to stack.
- `desktop`: 1024–1440px — full 12-column grid inside the centered container.
- `wide`: > 1440px — the container stays centered at 1440; only the `wide` (1558px) variant and full-bleed blocks extend past it.

Viewport-bleed blocks are edge-to-edge at every breakpoint and never fall back into the container.

### Touch Targets

Minimum interactive size is 44×44px. Pill buttons meet this through vertical padding rather than a fixed height; icon-only chrome affordances (menu, search, close, chevron) sit in a 44×44px hit area even when the glyph itself is smaller. Collapsed nav rows are at least 44px tall with full-row tap targets. Adjacent targets keep at least `spacing.sm` (8px) between them.

### Collapsing Strategy

Multi-column grids stack to one column, nav links collapse to a menu, and side-by-side media and text reflow to stacked. The primary CTA never hides. On mobile, section breaks may step down the spacing scale (e.g. 144px → 96px).

### Image Behavior

Images scale fluidly within their rounded frames, keeping their crop ratio; heroes may switch to a tighter crop on mobile. Viewport-bleed blocks remain edge-to-edge at every breakpoint — they never fall back into the container on small screens. Logos never stretch.
