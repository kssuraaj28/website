from dataclasses import dataclass

from data_model import Bold, BulletList, ExternalUrl, Link, Section, WebText


@dataclass(frozen=True)
class Publication:
    name: str
    venue_date: str
    authors: tuple[str, ...]  # TODO: Link?
    links: tuple[Link, ...]


def to_text(pub: Publication) -> WebText:
    authlist = ', '.join(pub.authors)

    linktext = tuple(y for x in pub.links for y in (x, ' ')) # What in the slop
    return WebText(( '[', pub.venue_date , '] ', *linktext,
                    Bold(pub.name), ' - ', authlist))


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
                          "Samira Khan"),
                          (Link('[conference]', ExternalUrl('https://www.usenix.org/conference/usenixsecurity23/presentation/liu-sihang')),),
                         )

cr2 = Publication("CR²: Chain Replication Revisited",
                  "In submission",
                  ("Suraaj Kanniwadi",
                   "Yacqub Mohamed",
                   "Fred B. Schneider",
                   "Robbert van Renesse"),
                  ()
                  )

typeconf = Publication("Type Confusion Security",
                       "In submission",
                       ("Silei Ren",
                        "Hanxi Chen",
                        "Suraaj Kanniwadi",
                        "Andrew Myers"),
                  (Link('[arxiv]', ExternalUrl('https://arxiv.org/abs/2611.20298')),),
                       )

nmif = Publication("Demystifying Information Flow Downgrading using the Real–Ideal Paradigm",
                   "In submission",
                   ("Suraaj Kanniwadi", "Andrew Myers"),
                   (
                      Link('[arxiv]', ExternalUrl('https://arxiv.org/abs/2611.05695')),
                      Link('[rocq]', ExternalUrl('https://github.com/kssuraaj28/demystify-ifc-rocq')),
                    ),
                   )

pubs = [optane_sec, cr2, typeconf, nmif]
pubs.reverse()

# TODO: A-exam
# TODO: Writings and Publications
this_section = Section("Papers",
                       (BulletList(tuple(to_text(p) for p in pubs)), ))
