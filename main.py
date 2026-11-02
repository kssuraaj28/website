#!/usr/bin/env -S uv run
from data import about, teaching, talks, research, pubs, software, fun, blog
import shutil
from pathlib import Path

from data_model import MainPage
from render_homepage import render_homepage

OUT = Path("dist")
SITE_TITLE = "Suraaj's webpage"

# Each module in data/ defines this_section. Listed in display order.
SECTIONS = tuple(m.this_section for m in [
                 about, research, teaching,  software])


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir()
    path = OUT / "index.html"
    path.write_text(
        str(render_homepage(MainPage(SECTIONS), SITE_TITLE)), encoding='utf-8')
    print(f"/ -> {path}")


if __name__ == "__main__":
    main()
