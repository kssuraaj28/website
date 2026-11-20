from dataclasses import dataclass
from datetime import date
from data_model import Section, WebText

# Title, Location, Date, Slides
# XXX @ Usenix secuity 2023 (??/??/??) [slides]

@dataclass(frozen=True)
class TalkContent:
    title: str
    when: date
    day: str
    month: str
    year: int

# Usenix
# Advanced systems
# Hyperprops
# PLDG
# Syslunch
# Syslunch
# A-exam
# PLDG
# AI4AI

this_section = Section(
    "Talks",
    (WebText(("Brown fox or something",)),)) # This syntax is terrible
