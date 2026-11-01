from dataclasses import dataclass

from data import useful_links
from data_model import Bold, Section, SectionComponent, Text


@dataclass(frozen=True)
class ResearchTopic:
    topic: str
    name: str
    role: str
    sem: str
    year: int

    def __post_init__(self):
        possible_sem = ('Fall', 'Spring', 'Summer', 'Winter')
        # TODO: Vet course numbers?
        if self.sem not in possible_sem:
            raise ValueError(f"sem must be in {possible_sem}. Get {self.sem}")


nmif = [
    Text([Bold("Real–ideal semantic foundations for language based security ")]),

    Text([
        "Existing security properties such as noninterference are too simplistic; "
        "they cannot capture the security requirements of practical systems, "
        "which often have intertwined confidentiality and integrity requirements. "
        "Our insight is to adapt the ", useful_links.realideal,
        " from cryptography to give simple and expressive security specifications for computer systems. "
        "This has been quite successful. "
        "Using this paradigm, we have been able to provide "
        "simple semantic definitions of important---but less understood---"
        "security properties (such as nonmalleable information flow, robust declassification, and confused deputy attacks). "
        "In fact, we show that even syntactic type soundness theorems for information-flow type systems are presented best as "
        "real--ideal statements."]),

    Text(["Joint work with ",
          useful_links.andru, ', ',
          useful_links.silei, ', and ',
          useful_links.hanxi, '.'])

]

# TODO: Eventually, textwtopic in data model?
aispec = [
    Text([Bold("Enforcing auditable specifications for AI prompts")]),

    Text([
        "Using AI is exhilarating. Its lack of guarantees is also terrifying. "
        # "it's not fun when the production database gets deleted"
        "We believe that the right interaction model is to combine LLM prompting "
        "with techniques from programming languages and formal methods. "
        "We are designing simple, easily auditable, refinable, and enforceable specification languages "
        "to constrain AI execution to give users functionality and security guarantees. "
        "AI can itself generate such specifications, lifting significant user burden; "
        "a user only needs to audit the generated specification. "
        "Moreover, AI's remarkable ability to write formal proofs can even automate specification refinement! "
        "Such an interaction model is an important step in a future where we use our AI superpowers more responsibly. "
        "Because, with great power comes great responsibility. ",]),

    Text(["Joint work with ",
          useful_links.guyamir, ', ',
          useful_links.andru, ', and ',
          useful_links.alexandra, '.']),
]

cr2 = [
    Text([Bold("Self-managing chain replication")]),

    Text([
        "The original chain replication protocol has been in use in many companies and research projects."
        "One downside of chain replication is that it it cannot stand on its own and requires a configuration service. "
        "It turns out that this is not fundamental: a chain replicated service can reconfigure itself, for example after a failure. "
        "The new protocol also addresses certain inefficiencies in the original protocol, such as latency increasing with chain length. ",]),

    Text(["Joint work with ",
          useful_links.yacqub, ', ',
          useful_links.fbs, ', and ',
          useful_links.rvr, '.']),
]

# The typechecker almost killed me. TODO
# Change types to Sequence or something
intro: list[SectionComponent] = [
    Text(['We can only build secure and trustworthy systems if we know what secure and trustworthy means. '
          'In a nutshell, my research is about finding and enforcing the right specifications for computer systems. ']),

    Text(["I'm currently working on the following projects:"]),
]

this_section = Section("Research", intro + nmif + aispec + cr2)
