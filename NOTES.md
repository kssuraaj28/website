# How hosting works

- When you put a url (www.example.com/something) on a browser, the browser
sends a request to www.example.com. The request is a HTTP GET request for /something.
- Web servers can interpret this request to give back whatever they want.
- When you host a 'static website' using some directory `dist` , there seems to be an informal spec that web servers use to  translate GET requests as follows:
  + / --  dist/index.html
  + /about --  dist/about/index.html or dist/about.html
  + /about.html --  dist/about.html
  + /about/ --  dist/about/index.html
Moreover, relative links on these resolve differently (by browsers)
If you were on /about/ then it would be /about/link. 
If you were on /about, it would be /link. 

# Website discipline
- For my website, I'm going to maintain very strict link discipline.
- To start, I will only have one html page. No blog / fun to start.
- Hrefs links will always be fully qualified (no `about`, `about/`, `/about/`, etc.). 
  + Change this when you add images.
  + And when you add a blog, etc.
- However, the one exception to this is local section ids. Here, relative is okay. TODO: Not a great idea to have exception.

## Eventually
  + Every link on my website is going to be /<base>/....
    If you allowed relative paths, then about and about/ will have different behavior
    I don't want to rely on webservers to redirect about to about/
  + Web pages always end with /. So no /about/index.html
  + Other resources (files, js, etc.) will look like /<base>/<name>.<ext>
  + I could have a set of approved resources types (pdf's, etc.)??

# htpy
- When you do  `a[1,2]`, `__getitem__` is called with with tuple `(1,2)`.
- `p['x', 'y']` and `p['xy']` both generate the same html 

# Disjoint unions in python
There seem to be (at least) three ways to do disjoint unions in python.
Suppose type(A) = type, type(B) = type

- Union = Bold | Link
  + type(Union) --> typing.Union
  + isinstance(x, Bold) -> isinstance(x, Union)
  + If you did Bold | 5, there would be a runtime error.
- type Union = Bold | Link
  + type(Union) --> typing.TypeAliasType
  + isinstance(x, Bold) --> False
  + However there is some evaluate_value thing that is possible too
  + If you did Bold | 5, there would not be a runtime error.
  + Looks like this type thing exists for laziness TODO
- class Union: pass. class Bold(Union): .. . class Link(Union)
  + type(Union) --> type

All of them are slightly different. See also the expression problem.


# About dataclasses
- A dataclass decorator implements a bunch of standard methods like init, etc. for us.
- It's easy to do construction, pattern matching, etc.
- When you make it frozen, the __setattr__ and __delattr__  methods error. However, you can still use 
- object.__setattr__(self, key, val)

# The expression problem
- Functional programming or OOP..
- I think that both might work. FP is 'easier' to add methods, 
and OOP makes it easier to add types.
- I'm just choosing FP. Just seems simpler.

# Typechecking using pyright
- Run `uvx pyright` in the project root.  (Same as `uv tool run pyright` I think)
- Or `uv add --dev pyright` and `uv run pyright`.
-  When you do `uv add --dev pyright`, you don't need internet to use it..
- Also, `uv add --dev` is short for `uv add --group dev`
- When you do `uv sync`, default-groups get installed. `dev` is a default-group by default.
- So, if you do `uv add --group xxx yyy; uv sync`, `yyy` will go away, because `sync` only puts the default groups. Use `uv sync --group yyy` to reinstall.

# Margin, border, padding, content
Every visible element laid our like this.

            margin (transparent, outside)
     ┌────────────── border (a visible line) ─────┐
     │   padding (inside, shows the background)   │
     │            content                         │
     └────────────────────────────────────────────┘

# Basic CSS coloring
```
        "background-color" : "lightblue",
        "color" : "blue", # Color of text, inherited
        "border" : "10px solid",
        "border-color" : "green",
```

"background-color" : "transparent" is the default

# grid-template-columns
- grid-template-columns only makes sense when display is "grid"
- It is a space separated list of column widths,
- Lots of different 'widths'
  + fixed (px, em (font size), rem (root font size), %), 
  + fr (fraction of remaining space), 
  + auto
  + minmax

# CSS heights
- You use the height property.
- Possible values: 
  + '100%' (of parents height)
  + '100vh' (100% of viewport height)
  + 'auto' space based on children height

If a child is higher than a parent,
what happens is determined by the parent's overflow property..
  - visible
  - hidden / clip
  - auto


------------------------------------------------


## file:// nonsense
There isn't one. With file://, the browser reads the file from disk itself, through the operating system, the same way a text editor opens a file. No HTTP is involved, so there's no request or response, no status codes and no headers.

The browser fills in what a server would normally provide:
- File type: guessed from the extension (.html, .css), whereas a server sends a Content-Type header.
- Missing files: an error page from the browser itself, not a 404 from a server.
- Folders: the browser shows its own directory listing.

DevTools still lists file:// loads in the Network tab, but there's no real traffic behind them. Some browsers show a made-up status like 200 or "Finished."

# TODO
assets
Mobile layout. Media queries.
Add a readme
Favicon
