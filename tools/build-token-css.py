#!/usr/bin/env python3
"""Build the CSS custom-property bridge consumed by the HTML examples."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = ROOT / "docs/current/v25/tokens.json"
OUT = ROOT / "apps/current/stadli.tokens.css"

spec = json.loads(TOKENS.read_text())
tokens = spec["tokens"]
lines: list[str] = [
    "/* Stadli v25 design tokens. Generated from ../../docs/current/v25/tokens.json. */"
]


def emit_theme(selector: str, theme: str) -> None:
    lines.append(f"{selector} {{")
    for name, value in tokens["color"][theme].items():
        lines.append(f"  --color-{name}: {value};")
    for name in tokens["color"][theme]:
        lines.append(f"  --{name}: var(--color-{name});")
    lines.append("}")


emit_theme(':root, :root[data-theme="light"]', "light")
emit_theme(':root[data-theme="dark"], html.dark', "dark")

lines.append(":root {")
for name, value in tokens["radius"].items():
    lines.append(f"  --radius-{name}: {value};")
for name, value in tokens["spacing"].items():
    lines.append(f"  --space-{name}: {value};")
for name in tokens["radius"]:
    lines.append(f"  --r-{name}: var(--radius-{name});")
for name in tokens["spacing"]:
    lines.append(f"  --sp-{name}: var(--space-{name});")
for name, value in tokens["motion"]["duration"].items():
    lines.append(f"  --duration-{name}: {value};")
for name in tokens["motion"]["duration"]:
    lines.append(f"  --d-{name}: var(--duration-{name});")
for name, value in tokens["motion"]["easing"].items():
    lines.append(f"  --ease-{name}: {value};")
lines.extend([
    '  --font-sans: Inter, -apple-system, "Segoe UI", sans-serif;',
    f'  --reveal-blur: {tokens["motion"]["reveal"]["blur"]};',
    "}",
])

OUT.write_text("\n".join(lines) + "\n")
