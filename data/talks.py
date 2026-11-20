from dataclasses import dataclass
from datetime import date
from data_model import Bold, BulletList, Section, WebText

# Title, Location, Date, Slides
# XXX @ Usenix secuity 2023 (??/??/??) [slides]

@dataclass(frozen=True)
class TalkContent:
    title: str
    place: str
    when: date
    slides_pdf: str

def to_text(talk: TalkContent) -> WebText:
    date = talk.when.strftime("%d %b %Y")
    return WebText(
            ( date,': ', 
             Bold(talk.title), 
             ' [', talk.place ,']', 
             #' [slides]',
             ))

talks =  [
  TalkContent("Paxos made Simple", "CS 6410 @ Cornell", date(2022, 9, 27), 'paxos-6410'),
  TalkContent("Hyperproperties", "CS 6156 @ Cornell", date(2023, 2, 16), 'hyperprop-6156'),
  TalkContent("Side-Channel Attacks on Optane Persistent Memory", "USENIX Security '23", date(2023, 8, 11), 'optane-23'),
  TalkContent("Secure Synthesis of Distributed Cryptographic Applications", "PLDG @ Cornell", date(2024, 2, 28), 'viaduct-pldg'),
  TalkContent("Verifying Hardware Security Modules with Information-Preserving Refinement", "Systems Lunch @ Cornell", date(2024, 9, 13), 'knox-syslunch'),
  TalkContent("An Algebraic Theory of Systems", "Systems Lunch @ Cornell", date(2025, 2, 7), 'algth-syslunch'),
  TalkContent("The Real–Ideal Paradigm for Systems", "A Exam @ Cornell", date(2025, 4, 16), 'aexam'),
  TalkContent("Demystifying Information Flow Downgrading using the Real–Ideal Paradigm", "PLDG @ Cornell", date(2026, 8, 26), 'nmif-pldg'),
  TalkContent("Why security? What security? How security?", "AI4AI Fall Retreat @ Cornell Tech.", date(2026, 10, 27), 'ai4ai'),
  ]


talks.reverse()

this_section = Section("Talks", 
                       (BulletList(tuple(to_text(p) for p in talks)),))
