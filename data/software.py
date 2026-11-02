from data_model import ExternalUrl, Link, Section, Text


text = Text(
    ("My ", Link("Github account", ExternalUrl("https://github.com/kssuraaj28")),
     " has a bunch of software I've written over the years. "
     "This includes ", Link("my vim configuration ",
                            ExternalUrl("https://github.com/kssuraaj28/.vim")),
     Link("and ", ExternalUrl("https://github.com/kssuraaj28/vimcoqcfg")),
     Link("many ", ExternalUrl("https://github.com/kssuraaj28/MyersColors")),
     Link("plugins. ", ExternalUrl("https://github.com/kssuraaj28/mirror.nvim")),
     "There's also some ",
     Link("software", ExternalUrl("https://kssuraaj28.github.io/swim-workout-builder/")),
     " that I use to manage my swimming. ",
     " The source for this website is ",
     Link("here. ", ExternalUrl("https://github.com/kssuraaj28/website")),
     ),)

this_section = Section("Software", (text,))
