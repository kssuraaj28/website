from dataclasses import dataclass
from datetime import date
from data_model import Bold, BulletList, ExternalUrl, Link, LinkTarget, LocalAsset, Section, TextPart, WebText
from paths import SanitizedPath

@dataclass(frozen=True)
class TalkContent:
    title: str
    place: str
    when: date
    slides: LinkTarget | None

def to_text(talk: TalkContent) -> WebText:
    date = talk.when.strftime("%d %b %Y")

    s: TextPart = ''
    if isinstance(talk.slides, LinkTarget):
        s = Link(' [slides]', talk.slides) 

    return WebText(
            ( date,': ', 
             Bold(talk.title), 
             ' [', talk.place ,']', 
             s,
             ))

def local_slides(inp: str) -> LocalAsset:
    path = SanitizedPath(('talk-slides', f'{inp}.pdf'))
    return LocalAsset(path)

talks =  [
  TalkContent("Paxos made Simple", 
              "Cornell CS 6410", 
              date(2022, 9, 27), 
              local_slides('paxos-cs6410')),

  TalkContent("Hyperproperties", 
              "Cornell CS 6156", 
              date(2023, 2, 16), 
              local_slides('hyperprop-6156')),

  TalkContent("Side-Channel Attacks on Optane Persistent Memory", 
              "USENIX Security '23", 
              date(2023, 8, 11),
              ExternalUrl('https://www.usenix.org/system/files/sec23_slides_liu-sihang.pdf')),

  TalkContent("Secure Synthesis of Distributed Cryptographic Applications", 
              "Cornell PLDG", 
              date(2024, 2, 28), 
              local_slides('viaduct-pldg')),

  TalkContent("Verifying Hardware Security Modules with Information-Preserving Refinement", 
              "Systems Lunch @ Cornell", 
              date(2024, 9, 13), 
              local_slides('knox-syslunch')),

  TalkContent("An Algebraic Theory of Systems", 
              "Cornell Systems Lunch", 
              date(2025, 2, 7), 
              local_slides('algth-syslunch')),

  TalkContent("The Real–Ideal Paradigm for Systems", 
              "Cornell A-Exam", 
              date(2025, 4, 16), 
              local_slides('a-exam')),

  TalkContent("Demystifying Information Flow Downgrading using the Real–Ideal Paradigm", 
              "PLDG @ Cornell", 
              date(2026, 8, 26), 
              local_slides('nmif-pldg')),

  TalkContent("Why security? What security? How security?", 
              "Cornell Tech. AI4AI Fall Retreat", 
              date(2026, 10, 27), 
              local_slides('ai4ai-security')),
  ]


talks.reverse()

this_section = Section("Talks", 
                       (BulletList(tuple(to_text(p) for p in talks)),))
