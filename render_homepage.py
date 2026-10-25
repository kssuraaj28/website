"""Turns the data model into HTML. This is the only file that touches htpy."""
# It is very weird that you can do from htpy import asfas

import htpy as h

from data_model import Bold, Link, List, MainPage, Section, SectionComponent, Text, TextPart


def dict_to_css_style(props: dict[str, str]) -> str:
    """{"margin": "0", "display": "grid"} -> "margin: 0; display: grid;" """
    return " ".join(f"{name}: {value};" for name, value in props.items())


def render_part(part: TextPart):
    match part:
        case str(txt):
            return txt
        case Bold(text):
            return h.strong[text]
        case Link(text, url):
            return h.a(href=url)[text]


def render_component(component: SectionComponent):
    match component:
        case Text(parts):
            return h.p[(render_part(x) for x in parts)]
        case List(items):
            return h.ul[(h.li[(render_part(x) for x in item.parts)] for item in items)]


def render_section(sec: Section):
    return h.section[
        h.h2[sec.title],
        (render_component(c) for c in sec.content),
    ]


BODY_FONT = 'sans-serif'


def render_homepage(page: MainPage, site_title: str):
    head = h.head[
        h.meta(charset="utf-8"),
        h.meta(name="viewport", content="width=device-width, initial-scale=1"),
        h.title[site_title],
    ]

    body_style = dict_to_css_style({
        "margin": "0", #Browsers make the body margin 8px. Override
        # No border
        "border": "10px solid",
        "border-color": "green",
        "height": "10vh",
        "font-family": BODY_FONT,
        "display": "grid",
        "grid-template-columns": "25% 1fr", # 25% and the rest
        "background-color": "lightblue",
        "color": "blue",  # Color of text
    })

    sidebar_style = dict_to_css_style({
        # "position": "sticky",
        # "top": "0",
        "height": "100vh",
        # "padding": "16px",
        "border": "10px solid",
        "border-color": "purple",
    })

    main_style = dict_to_css_style({
        "background-color" : "beige",
        "border": "10px solid",
        "border-color": "red",
    })

    sidebar = h.nav(style=sidebar_style)[
        h.p["Sidebar placeholder"],
    ]

    body = h.body(style=body_style)[
        sidebar,
        h.main(style=main_style)[(render_section(s) for s in page.sections)],
    ]

    return h.html(lang="en")[head, body]
