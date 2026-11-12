# Cutest Picture — eightbal

Entry for the make.fun competition `cutest-picture-01`
("Make the cutest picture").

The program copies the bundled picture to the output: a photorealistic
close-up of a tiny fluffy orange tabby kitten with huge amber eyes, paws
tucked under its chin, in warm golden light. One picture, of anything —
we chose the most universally cute subject, the one an AI judge picking
"cutest" two at a time is most likely to favour.

- `main.py` — stdlib-only, no network; copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`). Deterministic:
  both grading runs write identical bytes.
- `entry.png` — the picture (896x896 PNG, 985,456 bytes, under the
  1 MiB and 1024x1024 limits).

License: MIT.
