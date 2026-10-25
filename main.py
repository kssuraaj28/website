#!/usr/bin/env -S uv run
"""Build the static site into dist/. Every page is a Page built from the vocabulary in data_model.py."""
import shutil
from pathlib import Path

from data_model import MainPage
from render import render_page

OUT = Path("dist")

# Each module in data/ defines this_section. Listed in display order.
from data import about, teaching
SECTIONS = [m.this_section for m in [about, teaching]]

def main():
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir()
    path = OUT / "index.html"
    path.write_text(str(render_page(MainPage(SECTIONS))))
    print(f"/ -> {path}")


if __name__ == "__main__":
    main()
