#!/usr/bin/env python3
"""Cutest-picture entry: copy the bundled kitten picture to the output.

The picture is a photorealistic close-up of a tiny fluffy orange tabby
kitten, already chosen and stored as entry.png beside this file. The
program does one deterministic thing: copy those exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png), so both grading
runs write identical output.
"""
import os
import shutil

SRC_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guarantee the deterministic-bytes requirement: the output must be
    # byte-identical to the bundled picture, so fail loudly instead of
    # silently leaving a partial file if the copy is ever interrupted.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("entry.png copy incomplete")


if __name__ == "__main__":
    main()
