# news-image-20261120: a single image summing up the world news of
# Friday 20 November 2026. The finished image ships in this repo as
# entry.png; this program places a copy of it at /output/entry.png.
# Python 3.13, standard library only, no network access. Deterministic:
# every run writes the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output, so a local run looks like this:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

IMAGE_NAME = "entry.png"


def output_directory():
    """Where the image goes: /output, or MAKEFUN_OUTPUT_DIR locally."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    here = Path(__file__).resolve().parent
    target = output_directory()
    target.mkdir(parents=True, exist_ok=True)
    # Same file name the judge expects, same bytes every run.
    shutil.copyfile(here / IMAGE_NAME, target / IMAGE_NAME)


if __name__ == "__main__":
    main()
