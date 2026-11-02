#The document vocabulary. Pages are built only from these types.
from dataclasses import dataclass
from urllib.parse import urlsplit

@dataclass(frozen=True)
class Bold:
    text: str


@dataclass(frozen=True)
class ExternalUrl:
    url: str

   # dataclasses run __post_init__ right after init
    def __post_init__(self):
        parts = urlsplit(self.url)
        if parts.scheme not in ("http", "https") or not parts.hostname:
            raise ValueError(
                f"Link url must be a full http(s) URL, got {self.url!r}")

@dataclass(frozen=True)
class Link:
    text: str
    target: ExternalUrl

TextPart = str | Bold | Link

@dataclass(frozen=True)
class Text:
    parts: tuple[TextPart, ...] # A tuple of any length

@dataclass(frozen=True)
class BulletList:
    items: tuple[Text, ...]

SectionComponent = Text | BulletList

@dataclass(frozen=True)
class Section:
    title: str
    content: tuple[SectionComponent, ...]

@dataclass(frozen=True)
class MainPage:
    sections: tuple[Section, ...]
