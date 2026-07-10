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

## Elevation & Depth

The system is deliberately flat. No drop shadows; layering is signaled only by subtle surface-color shifts and hairline borders.

**Blocks may trespass.** An element may overlap the edge of a neighboring frame or reach past it into whitespace — a pill breaking a photo's border, a card crossing a section seam. A boundary crossed on purpose reads as composition, not error; the overlapping element is layered by tone and hairline exactly as any surface is, never by a shadow announcing its height. Flatness governs *how* layers are drawn, not *whether* they may occur.

### Decorative Depth

None on content. No gradients or glows on any content block — this is the hard rule that keeps color reading as solid blocks. A content color is only ever a flat fill, never a gradient or a semi-transparent tint. Blur can be used if needed. One narrow exception: a full-viewport *ambient background* — canvas behaving like material, carrying no content and no text-bearing block — may use a soft gradient of a single extracted hue (or chrome). This is the page changing its lighting, not a block being decorated; it never applies to a card, tile, chart, or any surface that holds content. Everything that carries meaning stays a flat fill.

## Shapes

### Border Radius Scale

Buttons and badges use fully pilled corners; cards use large (12–16px) radii; inputs use medium (8px) radii. Nothing is sharp-cornered except hairline dividers.

### Photography & Illustration Geometry

Cinematic, documentary, storytelling. Photography is always presented raw: flat, at full strength, in its own color, with no gradient overlay, tint, duotone, filter, or house treatment of any kind. The system's style lives in how images are framed and cropped, never in what is done to their pixels. When a full-bleed image needs overlaid text, the text rides over a very subtle seamless chrome semi-opacity overlay or subtle blur. Imagery and color read as one family, so surrounding blocks can be filled with colors if that fits the story.

**Rendered graphics are imagery.** Imagery is not only photography: product screenshots, UI collages, device mockups, and generative or data art all count as images and follow the same laws — presented raw, at full strength, never filtered or washed. Because they are imagery, their *internal* gradients and textures are pixels, not block styling; a generative panel of gradient bars is a picture the same way a photograph of a sunset is. The flat-fill rule is untouched: it governs blocks the *system* paints (cards, tiles, bands), never the pixels inside a piece of imagery. A rendered-graphic panel is still a full-strength image for budgeting purposes — it spends the viewport's one loud moment, and any block sharing its viewport extracts from it like any other image. Chrome UI cards may float over such a panel exactly as text rides over a photograph, on the same legibility rules.

**Imagery on the dark canvas.** Photography stays raw on both canvases — the no-filter, no-tint, no-duotone, no-scrim law is absolute in either mode, because treating the pixels to "fit" dark mode is exactly the house wash the system forbids. What changes on `#0a0a0a` is only the *seam* between image and canvas, which is a chrome concern, not an image treatment:

- **The edge, not the pixels.** A raw image dropped straight onto `#0a0a0a` can read as a bright rectangle floating in a void. The frame handles this the chrome way: the image keeps its hairline (`hairline` / `hairline-strong` in dark tokens) so the boundary is defined by chrome, never by a gradient fade or a vignette painted onto the photo.
- **Minimum-luminance check, resolved by crop.** A predominantly dark image can sink into the dark canvas until its own edge disappears. This is resolved by crop and framing — choosing a frame with enough of its own tonal range, or seating it in a `surface-1`/`surface-2` card so a chrome step separates it from canvas — never by lightening or washing the pixels. If an image cannot clear the canvas without treatment, it is the wrong crop, not a candidate for a filter.
- **Overlaid text uses the same chrome scrim, re-toned per canvas.** The subtle seamless chrome semi-opacity overlay (or blur) behind text on a full-bleed image is chrome, so it flips with the mode: a light scrim under dark type on light chrome, a dark scrim under light type on dark chrome, chosen by the same contrast test as *Legibility stays chrome*. The scrim is still seamless and still chrome-neutral — never a tinted or gradient overlay.
- **Extraction is unaffected.** Because the pixels are never treated, the anchor hue pulled from an image is identical in both modes (per Canvas-aware extraction); only the rendered swatch's lightness differs by canvas. Image and extracted block therefore still read as one bloodline on dark exactly as on light.
