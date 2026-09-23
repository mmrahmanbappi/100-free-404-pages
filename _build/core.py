"""Shared helpers for generating the 404 page templates."""
import html
import json

SITE = "https://mmrahmanbappi.github.io/100-free-404-pages"
REPO = "https://github.com/mmrahmanbappi/100-free-404-pages"

CATEGORIES = [
    ("minimal", "Minimal", "Clean, quiet pages built on strong typography and lots of space."),
    ("illustrated", "Illustrated", "Friendly pages with a hand-built SVG illustration at the center."),
    ("animated", "Animated", "Pages with gentle CSS animation that brings the error to life."),
    ("interactive", "Interactive", "Pages with a small game or toy, so visitors smile before they leave."),
    ("dark", "Dark and Neon", "Dark backgrounds, glowing colors and night-time moods."),
    ("retro", "Retro", "Pages inspired by old computers, arcades, print and tape."),
    ("developer", "Developer", "Terminals, code editors and error logs for tech and developer sites."),
    ("business", "Business", "Helpful, on-brand pages for companies, shops, schools and clinics."),
    ("ecommerce", "E-commerce", "Pages that turn a missing product into a way back to shopping."),
    ("seasonal", "Scenes and Seasons", "Full scenes, from rainy streets to snowy mountains."),
]

PAGES = []  # filled by the category modules


def esc(s):
    return html.escape(str(s), quote=True)


def fonts_link(families):
    if not families:
        return ""
    q = "&".join("family=" + f.replace(" ", "+") for f in families)
    return ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            f'<link href="https://fonts.googleapis.com/css2?{q}&display=swap" rel="stylesheet">\n')


BASE_CSS = """*{box-sizing:border-box}
html,body{margin:0;min-height:100%}
body{min-height:100vh;-webkit-font-smoothing:antialiased}
a{color:inherit}
img,svg{max-width:100%;display:block}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
:focus-visible{outline:3px solid currentColor;outline-offset:3px}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}}"""


def page(p, css, body, script="", fonts=(), theme="#111111"):
    """Wraps a template in a full HTML document."""
    title = f"Page not found | {p['brand']}"
    desc = "Sorry, the page you are looking for does not exist or has moved."
    fav = p.get("favicon", theme).replace("#", "%23")
    return f"""<!DOCTYPE html>
<!--
  {p['name']}: a free 404 page template
  From 100 Free 404 Pages by MM Rahman Bappi, MIT license
  {SITE}/

  How to use: replace the brand name, links and colors, then set this file
  as your site's 404 page. The guide explains how for every kind of host:
  {SITE}/guide/
-->
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<!-- A 404 page should not appear in search results, so keep noindex. -->
<meta name="robots" content="noindex, follow">
<meta name="theme-color" content="{theme}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='{fav}'/><text x='32' y='42' font-family='Arial' font-size='22' font-weight='700' text-anchor='middle' fill='white'>404</text></svg>">
{fonts_link(fonts)}<style>
{BASE_CSS}
{css.strip()}
</style>
</head>
<body>
{body.strip()}
{('<script>' + chr(10) + script.strip() + chr(10) + '</script>') if script else ''}
</body>
</html>
"""


def add(category, slug, name, brand, blurb, css, body, script="", fonts=(), theme="#111111"):
    PAGES.append(dict(category=category, slug=slug, name=name, brand=brand, blurb=blurb, css=css, body=body,
                      script=script, fonts=list(fonts), theme=theme))
