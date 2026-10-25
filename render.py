"""Turns the data model into HTML. This is the only file that touches htpy."""
from htpy import a, body, head, html, li, meta, nav, p, strong, title, ul
from htpy import main as mainhtml

from data_model import Bold, Heading, Link, List, SectionComponent, SectionContent, Text, TextPart


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


def render_page(page: SectionContent):
    # The <title> is the first heading's text.
    page_title = next((c.text for c in page.components if isinstance(c, Heading)), "Untitled")
    return html(lang="en")[
        head[
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1"),
            title[page_title],
        ],
        body[
            nav[a(href="/")["Home"], " · ", a(href="/about/")["About"]],
            mainhtml[(render_component(c) for c in page.components)],
        ],
    ]
