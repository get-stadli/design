# Stadli Design System v25

This folder is the maintainable, split version of the current Stadli design-system specification. Start with the machine-readable spec, then update the smallest topic file that matches the change you are making.

## Sections

1. [Machine-readable spec](00-machine-readable-spec.md)
   - [Canonical JSON tokens](tokens.json) — consumed by generated CSS in the HTML examples.
2. [Overview & Foundations](01-overview-foundations.md)
3. [Layout, Shapes & Depth](02-layout-shapes-depth.md)
4. [Components & Brand Assets](03-components-brand-assets.md)
5. [Data Visualization](04-data-visualization.md)
6. [Motion & Responsive Behavior](05-motion-responsive-behavior.md)
7. [Guidelines, Iteration, Gaps & References](06-guidelines-iteration-gaps.md)

## Maintenance

- Keep v25 changes inside this folder while v25 is current.
- Keep the split near eight Markdown files total, including this README, so each file remains substantial without fragmenting the spec too much.
- If a future v26 is promoted, move this folder to `../../archive/versions/v25/` and create a new current folder.
