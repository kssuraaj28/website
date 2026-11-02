#!/usr/bin/env -S uv run
import shutil
from pathlib import Path

from data_model import MainPage
from render_homepage import render_homepage

OUT = Path("dist")
SITE_TITLE = "Suraaj's webpage"

# Each module in data/ defines this_section. Listed in display order.
from data import about, teaching, talks, research, pubs, software, fun, blog
SECTIONS = [m.this_section for m in [about, research, pubs, teaching, talks, software]]


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir()
    path = OUT / "index.html"
    path.write_text(str(render_homepage(MainPage(SECTIONS), SITE_TITLE)))
    print(f"/ -> {path}")


if __name__ == "__main__":
    main()
