"""The document vocabulary. Pages are built only from these types."""
from dataclasses import dataclass
from urllib.parse import urlsplit

@dataclass(frozen=True)
class Bold:
    text: str


@dataclass(frozen=True)
class Link:
    text: str
    url: str  # external only, for now

   # dataclasses run __post_init__ right after init
    def __post_init__(self):
      parts = urlsplit(self.url)
      if parts.scheme not in ("http", "https") or not parts.hostname:
          raise ValueError(f"Link url must be a full http(s) URL, got {self.url!r}")

TextPart = str | Bold | Link

@dataclass(frozen=True)
class Heading:
    text: str

@dataclass(frozen=True)
class Text:
    parts: list[TextPart]

@dataclass(frozen=True)
class List:
    items: list[Text]

SectionComponent = Text | List

@dataclass(frozen=True)
class SectionContent:
    components: list[SectionComponent]
