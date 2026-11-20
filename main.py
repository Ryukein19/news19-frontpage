#!/usr/bin/env python3
"""Copy the front-page image to the output directory.

Reads entry.png beside this file and writes it to the output dir
(MAKEFUN_OUTPUT_DIR or /output) as entry.png.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Validate the output: must be a PNG and under 1 MiB.
    with open(dst, "rb") as f:
        header = f.read(8)
    if header != b"\x89PNG\r\n\x1a\n":
        print("error: output is not a PNG", file=sys.stderr)
        return 1
    size = os.path.getsize(dst)
    if size > 1024 * 1024:
        print("error: output over 1 MiB (%d bytes)" % size, file=sys.stderr)
        return 1
    print("wrote", dst, "(%d bytes)" % size)
    return 0


if __name__ == "__main__":
    sys.exit(main())
