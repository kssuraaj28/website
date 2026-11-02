#!/usr/bin/env -S uv run
from data import about, teaching, talks, research, pubs, software, fun, blog
import argparse
import shutil
from pathlib import Path

from data_model import MainPage
from paths import SitePath
from render_homepage import render_homepage



# Each module in data/ defines this_section. Listed in display order.
SECTIONS = tuple(m.this_section for m in [
                 about, research, teaching,  software])


def parse_base(arg: str) -> SitePath:
    # "/" -> ()
    # "website" -> ("website",)
    # "website/a" -> ("website", "a")
    stripped = arg.strip("/")
    return SitePath(tuple(stripped.split("/")) if stripped else ())


# TODO: Script relative?
OUT = Path("_dist")
def clean_dist():
    # Start from an empty output directory, so that no stale files get deployed.
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir()


def install_dist(base: SitePath, index_html: str) -> Path:
    # The site goes under OUT/<base>, mirroring where it is hosted.
    site_root = OUT.joinpath(*base.content)
    site_root.mkdir(parents=True, exist_ok=True)
    path = site_root / "index.html"
    path.write_text(index_html, encoding='utf-8')
    return path


def main():
    parser = argparse.ArgumentParser()
    # argparse turns a ValueError from parse_base into a usage error.
    parser.add_argument("--base", type=parse_base, default=SitePath(()),
                        help='where the site is hosted, e.g. "website" (default: the domain root)')
    base: SitePath = parser.parse_args().base
    print(f"base: {base}")

    clean_dist()
    # TODO: This should be
    SITE_TITLE = "Suraaj's webpage"
    path = install_dist(base, str(render_homepage(MainPage(SECTIONS), SITE_TITLE)))
    print(f"/ -> {path}")


if __name__ == "__main__":
    main()
