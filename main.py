"""news-image-20261119 entry: a one-day world-news front page.

The image is a newspaper front page drawn in code (HTML + CSS) and rendered
to entry.png: a 1024x1024 summary of Thursday 19 November 2026's world news
-- the first Trump-Xi-Putin three-way summit in Shenzhen, the ICJ's finding
that Myanmar committed genocide against the Rohingya, COP31's draft dropping
fossil fuels, Anthropic's record IPO, the GTA VI launch, and 16 more stories
from every continent, each attributed to its source.

This program is the entrypoint the grader runs. It copies the finished image
to the output directory as entry.png, the name the task requires. It runs
with no network and only the standard library.
"""

import os
import shutil
from pathlib import Path

# The finished front page, beside this file in the repository.
IMAGE = Path(__file__).resolve().parent / "entry.png"

# The grader sets MAKEFUN_OUTPUT_DIR outside its container; /output inside.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(IMAGE, target)
    # The gate reads the file as a whole image: confirm it is a PNG of
    # at most 1 MiB before we hand it over.
    data = target.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("entry.png is not a PNG")
    if len(data) > 1_048_576:
        raise ValueError("entry.png is over the 1 MiB limit")


if __name__ == "__main__":
    main()
