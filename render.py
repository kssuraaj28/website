"""Turns the data model into HTML. This is the only file that touches htpy."""
from htpy import a, body, h2, head, html, li, meta, p, section, strong, title, ul
from htpy import main as mainhtml

from data_model import Bold, Link, List, MainPage, Section, SectionComponent, Text, TextPart

def render_part(part: TextPart):
    match part:
        case str(txt):
            return txt
        case Bold(text):
            return strong[text]
        case Link(text, url):
            return a(href=url)[text]


def render_component(component: SectionComponent):
    match component:
        # case Heading(text):
        #     return h1[text]
        case Text(parts):
            return p[(render_part(x) for x in parts)]
        case List(items):
            return ul[(li[(render_part(x) for x in item.parts)] for item in items)]


def render_section(sec: Section):
    return section[
        h2[sec.title],
        (render_component(c) for c in sec.content),
    ]



def render_page(page: MainPage):
    # The <title> is the first heading's text.
    page_title = "Suraaj's webpage"
    return html(lang="en")[
        head[
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1"),
            title[page_title],
        ],
        body[
            mainhtml[(render_section(s) for s in page.sections)],
        ],
    ]
