## Iteration Guide

To extend this system, keep all chrome tokens within the black/white/gray ramp — usage of color is chosen per instance from the content, not tokenized — and reuse the 8px spacing scale for any new component. Any new component or token is defined on both canvases at once: give chrome values a `colors` and a `colors-dark` entry, and make sure any earned color it carries is re-resolved per canvas (Color Computation → Canvas-aware extraction) rather than hardcoded. A component that only has a light-mode design is not finished.
