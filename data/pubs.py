from dataclasses import dataclass

from data_model import Bold, BulletList, Section, WebText


@dataclass(frozen=True)
class Publication:
    name: str
    venue_date: str
    authors: tuple[str, ...]  # TODO: Link?


def to_text(pub: Publication) -> WebText:
    authlist = ', '.join(pub.authors)
    return WebText(( '[', pub.venue_date , '] ', Bold(pub.name), ' - ', authlist))


# TODO s
# Have a _me_
# Author affliation
# Talk # Paper # Slides
optane_sec = Publication("Side-Channel Attacks on Optane Persistent Memory",
                         "USENIX Security '23",
                         ("Sihang Liu",
                          "Suraaj Kanniwadi",
                          "Martin Schwarzl",
                          "Andreas Kogler",
                          "Daniel Gruss",
                          "Samira Khan"))

cr2 = Publication("CR²: Chain Replication Revisited",
                  "In submission",
                  ("Suraaj Kanniwadi",
                   "Yacqub Mohamed",
                   "Fred B. Schneider",
                   "Robbert van Renesse"))

typeconf = Publication("Type Confusion Security",
                       "In submission",
                       ("Silei Ren",
                        "Suraaj Kanniwadi",
                        "Hanxi Chen",
                        "Andrew Myers"))

nmif = Publication("Demystifying Information Flow Downgrading using the Real–Ideal Paradigm",
                   "In submission",
                   ("Suraaj Kanniwadi", "Andrew Myers"))

pubs = [optane_sec, cr2, typeconf, nmif]
pubs.reverse()

# TODO: A-exam
# TODO: Writings and Publications
this_section = Section("Papers",
                       (BulletList(tuple(to_text(p) for p in pubs)), ))
