#!/usr/bin/env -S uv run

import argparse

from data_model import Image, LocalAsset, MainPage, WebText
from paths import SanitizedPath
from construct_site import construct_site


# Each module in data/ defines this_section. Listed in display order.


def parse_base(arg: str) -> SanitizedPath:
    # "/" -> ()
    # "website" -> ("website",)
    # "website/a" -> ("website", "a")
    stripped = arg.strip("/")
    return SanitizedPath(tuple(stripped.split("/")) if stripped else ())


def main():
    parser = argparse.ArgumentParser()
    # argparse turns a ValueError from parse_base into a usage error.
    parser.add_argument("--base", type=parse_base, default=SanitizedPath(()),
                        help='where the site is hosted, e.g. "website" (default: the domain root)')
    base: SanitizedPath = parser.parse_args().base

    from data import about, teaching, talks, research, pubs, software, fun, blog
    sections = tuple(m.this_section for m in [
                     about, research, teaching,  software])
    side = (
        WebText(("Suraaj Kanniwadi",)),
        WebText(("Ph.D. Candidate",)),
        WebText(("Department of Computer Science",)),
        WebText(("Cornell University",)),
    )

    # TODO: Can we have coercion? This is a little painful
    img = Image(LocalAsset(SanitizedPath(("photo.jpg",))),
                "Photo of Suraaj")  # I wanted to write 'handsome man'

    construct_site(base, MainPage("Suraaj's Webpage", img, side, sections))


if __name__ == "__main__":
    main()
