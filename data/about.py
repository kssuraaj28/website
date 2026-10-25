from data_model import Section, Text
from data_model import Link


text = [
"I am presently a computer science graduate student at ", Link("Cornell university", "https://www.cs.cornell.edu/"), '. ',
"My research interests lie broadly in the areas of Systems (real broad, I know!). "
"Problems relating to formal specifications, security, extensibility and programmability appeal to me in particular. ",  
"I am fortunate to be advised by ", Link("Andrew Myers", "https://www.cs.cornell.edu/andru"), " and ",
Link("Robbert van Renesse","https://www.cs.cornell.edu/rvr"), " to pursue my interests. ",
"I also enjoy working with ", Link("Fred Schneider", "https://www.cs.cornell.edu/fbs/"), " on Fault-tolerant distributed systems."]


this_section = Section("About me", [Text(text)], id="about") 
#this_section = Section("About me", [Text([f"Line {i}"]) for i in range(100)])
