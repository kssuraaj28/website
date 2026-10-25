"""Turns the data model into HTML. This is the only file that touches htpy."""
# It is very weird that you can do from htpy import asfas

from htpy import a, body as htmlbody, h2, head as htmlhead, html, li, meta, nav, p, section, strong, title, ul
from htpy import main as mainhtml

from data_model import Bold, Link, List, MainPage, Section, SectionComponent, Text, TextPart


def dict_to_css_style(props: dict[str, str]) -> str:
    """{"margin": "0", "display": "grid"} -> "margin: 0; display: grid;" """
    return " ".join(f"{name}: {value};" for name, value in props.items())


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
        case Text(parts):
            return p[(render_part(x) for x in parts)]
        case List(items):
            return ul[(li[(render_part(x) for x in item.parts)] for item in items)]


def render_section(sec: Section):
    return section[
        h2[sec.title],
        (render_component(c) for c in sec.content),
    ]


BODY_FONT = 'sans-serif'

def render_homepage(page: MainPage, site_title: str):
    head = htmlhead[
        meta(charset="utf-8"),
        meta(name="viewport", content="width=device-width, initial-scale=1"),
        title[site_title],
    ]

    body_style = dict_to_css_style({
        "margin": "0",
        "font-family": BODY_FONT,
        "display": "grid",
        "grid-template-columns": "300px 1fr",
    })

    sidebar_style = dict_to_css_style({
        "position": "sticky",
        "top": "0",
        "height": "100vh",
        "padding": "16px",
    })

    sidebar = nav(style=sidebar_style)[
        p["Sidebar placeholder"],
    ]

    body = htmlbody(style=body_style)[
        sidebar,
        mainhtml[(render_section(s) for s in page.sections)],
    ]

    return html(lang="en")[head, body]
