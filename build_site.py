#!/usr/bin/env -S uv run
from data import about, teaching, talks, research, pubs, software, fun, blog
import argparse

from data_model import MainPage
from dist import clean_dist, install_dist
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

def main():
    parser = argparse.ArgumentParser()
    # argparse turns a ValueError from parse_base into a usage error.
    parser.add_argument("--base", type=parse_base, default=SitePath(()),
                        help='where the site is hosted, e.g. "website" (default: the domain root)')
    base: SitePath = parser.parse_args().base

    clean_dist()
    # TODO: This should not be hardcoded
    SITE_TITLE = "Suraaj's webpage"
    install_dist(base, str(render_homepage(MainPage(SECTIONS), SITE_TITLE)))


if __name__ == "__main__":
    main()
