# Stadli Design System

This repository is organized as a design-system workspace. The current source of truth is **Stadli Design System v25**.

## Start here

- **Current design system:** [`docs/current/v25/README.md`](docs/current/v25/README.md)
- **Current demos/prototypes:** [`apps/current/`](apps/current/)
- **Current brand assets:** [`assets/logos/v25/`](assets/logos/v25/)

## Repository map

```text
docs/
  current/              Current maintained design-system spec.
  archive/versions/     Historical versioned design-system markdown files.
  archive/experiments/  Older explorations, variants, and one-off studies.
  brand/                Voice, manifesto, inspiration, and copywriting guidance.
  prompts/              Design and implementation prompts.
  templates/            Reusable design-system document templates.
apps/
  current/              Prototypes and HTML demos aligned to the current system.
  prototypes/           Older standalone prototypes and design-system tools.
assets/
  logos/v25/            Logo exports for the current v25 system.
  references/           Reference imagery and inspiration assets.
```

## Maintenance rules

1. Treat `docs/current/v25/README.md` as the canonical design-system document until a newer version is promoted.
2. When promoting a future version, move the prior current file into `docs/archive/versions/`, add the new spec under `docs/current/`, and update this README.
3. Keep historical markdown files in `docs/archive/versions/` even when they are superseded.
4. Put experiments in `docs/archive/experiments/` unless they are promoted to a versioned system.
5. Avoid root-level design files; new docs should land in the category folders above.

## Duplicate cleanup

The previous root-level `DESIGN.md` was an exact duplicate of `v10.md`. The duplicate was removed and the retained copy now lives at `docs/archive/versions/v10.md`.
