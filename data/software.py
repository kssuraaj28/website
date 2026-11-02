from data_model import Link, Section, Text


text = Text(
    ("My ", Link("github", "https://github.com/kssuraaj28"),
     " has a bunch of software I've written over the years. "
     "This includes ", Link("my vim configuration ",
                            "https://github.com/kssuraaj28/.vim"),
     Link("and ", "https://github.com/kssuraaj28/vimcoqcfg"),
     Link("many ", "https://github.com/kssuraaj28/MyersColors"),
     Link("plugins. ", "https://github.com/kssuraaj28/mirror.nvim"),
     "There's also some ",
     Link("software", "https://kssuraaj28.github.io/swim-workout-builder/"),
     " that I use to manage my swimming. ",
     " The source for this website is ",
     Link("here. ", "https://github.com/kssuraaj28/website"),
     ),)

this_section = Section("Software", (text,))
