#!/usr/bin/env -S uv run
import shutil
from pathlib import Path

from data_model import MainPage
from render_homepage import render_homepage

# TODO: Script relative?
OUT = Path("_dist")


# Each module in data/ defines this_section. Listed in display order.
from data import about, teaching, talks, research, pubs, software, fun, blog
SECTIONS = tuple(m.this_section for m in [
                 about, research, teaching,  software])


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir()
    path = OUT / "index.html"
    # TODO: This should be
    SITE_TITLE = "Suraaj's webpage"
    path.write_text(
        str(render_homepage(MainPage(SECTIONS), SITE_TITLE)), encoding='utf-8')
    print(f"/ -> {path}")


if __name__ == "__main__":
    main()
