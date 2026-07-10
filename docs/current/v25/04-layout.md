## Layout

### Spacing System

An 8px base rhythm (with a 4px half-step) governs all spacing. Micro tokens (2–16px) handle component-internal padding and stay tight; from `lg` upward the scale stretches deliberately — 32px card padding, 56/96px block gaps, and 144px section breaks — so macro whitespace clearly outweighs micro whitespace and layouts read airy rather than dense.

### Grid & Container

Content sits in a centered 1440px container on a 12-column grid with 32px gutters and a 898px `narrow` variant for long-form reading. The grid is a positioning tool.

**Viewport bleed.** The container constrains text and chrome — never content blocks. Any full-bleed content block, image or flat color, may break out of the container and run edge-to-edge of the viewport: a hero photograph, a section-scale image, a storytelling band marking a chapter. The 1558px `wide` variant remains for blocks that should feel large but still framed; full viewport width is for blocks that should feel like the page itself changed material.

### Composition

**The grid is a ruler, not a cage.** The 12-column grid positions blocks; it does not entitle them to fill rows or share edges. Asymmetry is the system's resting composition: blocks anchor to the container's leading edge and take only the width their content earns — a block at half-width with the rest of the line left empty is a finished statement, not an incomplete one. Trailing whitespace is active material, doing the same work color and imagery do elsewhere. When a layout can resolve as either a squared-up arrangement or an offset one, prefer the offset: alignment must be earned by a relationship between blocks, never applied out of habit. Like color, symmetry is spent, not defaulted to — a centered, mirrored composition is a loud claim of balance and must be justified by content that is itself balanced.

**Clusters are silhouettes, not tables.** When several blocks travel together — stats, cards, mixed media — they form one composed shape, and the shape may be irregular: columns of unequal width, staggered starting heights, edges that deliberately refuse to meet. Internal misalignment inside a cluster is a design tool of equal rank with spacing and scale, because a ragged silhouette holds the eye the way a uniform grid cannot. The cluster spends one block-budget slot as a whole; discipline lives in the hue and type budgets inside it, not in forcing its outline to be rectangular. The offsets themselves stay on the spacing scale — a stagger is a deliberate step of `lg` or more, never a few stray pixels that read as error.

### Whitespace Philosophy

Airy and unhurried — whitespace is the primary tool for separating sections in the absence of color or heavy borders. When in doubt between two spacing tokens, choose the larger one; density is never the goal in this system. Whitespace is also directional: it may pool on one side of a viewport — the empty half of an asymmetric composition — rather than distribute evenly around blocks, and that pooling is a compositional act, not leftover space waiting to be filled.
