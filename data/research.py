from dataclasses import dataclass

from data import useful_links
from data_model import Bold, ExternalUrl, Link, Section, Text, TextPart


@dataclass(frozen=True)
class ResearchTopic:
    heading: str
    body: Text
    collabs: tuple[Link, ...]


def to_text(topic: ResearchTopic) -> tuple[Text, ...]:
    heading = Text((Bold(topic.heading),))

    ending : list[TextPart] = ["Joint work with ", ]

    match topic.collabs:
        case ():
            ending = []
        case (a,):
            ending.append(a)

        case (a, b):
            ending.extend((a, ' and ', b, '.'))

        case (a, b, c):
            ending.extend((a, ', ', b, ', and ', c, '.'))

        case _:  # TODO: Implement this.
            raise RuntimeError("Unimplemented")

    return (heading, topic.body, Text(tuple(ending)))


nmif = ResearchTopic(
    "Real–ideal semantic foundations for language-based security",
    Text((
        "Existing security properties such as noninterference are too simplistic; "
        "they cannot capture the security requirements of practical systems, "
        "which often have intertwined confidentiality and integrity requirements. "
        "Our insight is to adapt the ",
        Link('real–ideal paradigm',
             ExternalUrl('https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/GMW87/GMW87.pdf')),
        " from cryptography to give simple and expressive security specifications for computer systems. "
        "This has been quite successful. "
        "Using this paradigm, we have been able to provide "
        "simple semantic definitions of important—but less understood—"
        "security properties (such as nonmalleable information flow, robust declassification, and confused deputy attack security). "
        "In fact, we show that even syntactic type soundness theorems for information-flow type systems are presented best as "
        "real–ideal statements.",)),
    (useful_links.andru, useful_links.silei, useful_links.hanxi))

aispec = ResearchTopic(
    "Enforcing auditable specifications for AI prompts",

    Text((
        "Using AI is exhilarating. Its lack of guarantees is also terrifying. "
        # "it's not fun when the production database gets deleted"
        "The right interaction model with AI must be to combine LLM prompting "
        "with techniques from programming languages and formal methods. "
        "We are designing simple, easily auditable, refinable, and enforceable specification languages "
        "to constrain AI execution to give users functionality and security guarantees. "
        "Moreover, AI can itself generate such specifications, lifting significant user burden; "
        "a user only needs to audit the generated specification. "
        "Additionally, AI's remarkable ability to write formal proofs can even automate specification refinement! "
        "Such an interaction model is an important step in a future where we use our AI superpowers more responsibly. "
        "Because, with great power comes great responsibility. ",)),

    (useful_links.andru, useful_links.alexandra, useful_links.guyamir))

cr2 = ResearchTopic(
    "Self-managing chain replication",
    Text((
        "The original chain replication protocol has been in use in many companies and research projects. "
        "One downside of chain replication is that it cannot stand on its own and requires a configuration service. "
        "It turns out that this is not fundamental: a chain replicated service can reconfigure itself, for example after a failure. "
        "The new protocol also addresses certain inefficiencies in the original protocol, such as latency increasing with chain length. ",)), (useful_links.rvr, useful_links.fbs, useful_links.yacqub))

intro = Text(('We can only build secure and trustworthy systems if we know what secure and trustworthy means. '
              'In a nutshell, my research is about finding and enforcing the right specifications for computer systems. '
              "I'm currently working on the following projects:",
              ))

this_section = Section(
    "Research", (intro, *to_text(nmif), *to_text(aispec), *to_text(cr2)))
# Same as (intro,) + to_text(nmif) + to_text(aispec) + to_text(cr2))
