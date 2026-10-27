from data_model import Section, Text, Link


para1 = [
"I am presently a computer science graduate student at ", Link("Cornell university", "https://www.cs.cornell.edu/"), '. ',
"My research interests lie broadly in systems (real broad, I know!). "
"Problems relating to formal specifications, security, extensibility and programmability appeal to me in particular. ",  
"I am fortunate to be advised by ", Link("Andrew Myers", "https://www.cs.cornell.edu/andru"), " and ",
Link("Robbert van Renesse","https://www.cs.cornell.edu/rvr"), " to pursue my interests. ",
"I also enjoy working with ", Link("Fred Schneider", "https://www.cs.cornell.edu/fbs/"), " on building fault-tolerant distributed systems.",
]

para2 = [
"Before making the questionable decision to become a grad student, I had a blast as an undergrad at ", Link("IIT Roorkee","https://www.iitr.ac.in/"), ", where I was awarded the ",
Link("director's gold medal","https://iitr.ac.in/SCSP/Awards/Convocation%20Award.html"), '. ',
"On the internet, my accounts usually have a character from the ",
Link("greatest show ever", "https://www.youtube.com/watch?v=iAR7Aj_p3Ck"), '.',
]


this_section = Section("About me", [Text(para1), Text(para2)])
#this_section = Section("About me", [Text([f"Line {i}"]) for i in range(100)])
