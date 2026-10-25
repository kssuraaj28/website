#!/usr/bin/env -S uv run
"""Build the static site into dist/. Every page is a Page built from the vocabulary in data_model.py."""
from data import about, teaching
import shutil
from pathlib import Path

from data_model import MainPage
from render_homepage import render_homepage

OUT = Path("dist")
SITE_TITLE = "Suraaj's webpage"

# Each module in data/ defines this_section. Listed in display order.
SECTIONS = [m.this_section for m in [about, teaching]]


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir()
    path = OUT / "index.html"
    path.write_text(str(render_homepage(MainPage(SECTIONS), SITE_TITLE)))
    print(f"/ -> {path}")


if __name__ == "__main__":
    main()
