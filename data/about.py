from data import useful_links
from data_model import Link, Section, Text


para = Text([
    "I am presently a computer science graduate student at ", useful_links.cornell, '. ',
    "My research interests lie broadly in systems (real broad, I know!). "
    "Problems relating to formal specifications, security, extensibility and programmability appeal to me in particular. ",
    "I am fortunate to be advised by ", useful_links.andru, " and ",
    useful_links.rvr, " to pursue my interests. ",
    "Before making the questionable decision to become a grad student, I had a blast as an undergrad at ", useful_links.iitr, ", where I was awarded the ", Link(
        "director's gold medal", "https://iitr.ac.in/SCSP/Awards/Convocation%20Award.html"), '. ',
    "On the internet, my accounts usually have a character from the ",
    Link("greatest show ever", "https://www.youtube.com/watch?v=iAR7Aj_p3Ck"), '.'
])


this_section = Section("About me", [para])
# this_section = Section("About me", [Text([f"Line {i}"]) for i in range(100)])
