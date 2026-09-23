"""Builds the gallery website: home, category pages, guide, README, sitemap."""
import json
import os
import sys
from datetime import date

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
import core  # noqa: E402
from core import CATEGORIES, REPO, SITE, esc  # noqa: E402

for m in ["c_minimal", "c_illustrated", "c_animated", "c_interactive", "c_dark", "c_retro", "c_developer",
          "c_business", "c_ecommerce", "c_seasonal"]:
    __import__(m)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().isoformat()
PAGES = core.PAGES
AUTHOR = {"@type": "Person", "@id": SITE + "/#author", "name": "MM Rahman Bappi", "url": "https://mmseo.app/",
          "sameAs": ["https://github.com/mmrahmanbappi"]}
WEBSITE = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "100 Free 404 Pages",
           "description": "Free 404 error page templates in HTML and CSS.", "inLanguage": "en",
           "publisher": {"@id": SITE + "/#author"}}

CSS = """
:root{--bg:#fbfaf8;--card:#fff;--ink:#16161d;--text:#2c2c35;--muted:#62626e;--line:#e7e5e0;--red:#d6284b;--red-soft:#fde8ec}
@media (prefers-color-scheme:dark){:root{--bg:#131318;--card:#1c1c23;--ink:#f3f3f6;--text:#dcdce2;--muted:#9d9daa;--line:#2c2c36;--red:#ff5a7a;--red-soft:#3a1a22}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:1.06rem/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Ubuntu,sans-serif}
a{color:var(--red);text-underline-offset:3px}:focus-visible{outline:3px solid var(--red);outline-offset:3px;border-radius:3px}
img{max-width:100%;height:auto;display:block}
.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;background:var(--ink);color:var(--bg);padding:.5rem 1rem;z-index:9}
.wrap{max-width:76rem;margin:0 auto;padding-left:1.25rem;padding-right:1.25rem}.narrow{max-width:46rem}
header.top{border-bottom:1px solid var(--line)}header.top .wrap{display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap;min-height:4rem}
.brand{font-weight:800;color:var(--ink);text-decoration:none;font-size:1.1rem}.brand b{color:var(--red)}
header nav{display:flex;gap:1.3rem;flex-wrap:wrap;font-size:1rem}header nav a{color:var(--text);text-decoration:none}header nav a:hover{color:var(--red)}
h1,h2,h3{color:var(--ink);line-height:1.2;letter-spacing:-.015em}
h1{font-size:clamp(2.2rem,5.5vw,3.6rem);margin:.3rem 0 1rem}h2{font-size:clamp(1.5rem,3vw,2rem);margin:0 0 1rem}h3{font-size:1.1rem;margin:0 0 .3rem}
p{margin:0 0 1.1rem}
.hero{padding:3rem 0 2rem}.lead{font-size:1.22rem;max-width:44rem}
.actions{display:flex;gap:.8rem;flex-wrap:wrap;margin:1.5rem 0 .5rem}
.btn{display:inline-block;padding:.8rem 1.3rem;border-radius:10px;font-weight:700;text-decoration:none;border:2px solid var(--ink)}
.btn.main{background:var(--ink);color:var(--bg)}.btn.alt{color:var(--ink)}.btn:hover{border-color:var(--red)}
.small{font-size:.95rem;color:var(--muted)}
.crumbs{font-size:.95rem;color:var(--muted);padding-top:1.4rem}.crumbs a{color:var(--muted)}
.chips{display:flex;flex-wrap:wrap;gap:.5rem;margin:1.5rem 0}
.chips button,.chips a{font:inherit;font-size:.95rem;padding:.45rem .9rem;border-radius:999px;border:1.5px solid var(--line);background:var(--card);color:var(--text);cursor:pointer;text-decoration:none}
.chips button[aria-pressed=true]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.grid{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(17rem,1fr));gap:1.4rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column;height:100%}
.card img{aspect-ratio:16/10;object-fit:cover;width:100%;border-bottom:1px solid var(--line)}
.card .in{padding:1rem 1.1rem 1.1rem;display:flex;flex-direction:column;gap:.35rem;flex:1}
.card .cat{font-size:.85rem;color:var(--red);font-weight:600;text-decoration:none}
.card p{font-size:.96rem;color:var(--muted);margin:0 0 .6rem;flex:1}
.card .row{display:flex;gap:.5rem}.card .row a{flex:1;text-align:center;padding:.55rem .6rem;border-radius:8px;font-weight:700;font-size:.93rem;text-decoration:none;border:1.5px solid var(--line);color:var(--ink)}
.card .row a.dl{background:var(--ink);color:var(--bg);border-color:var(--ink)}
section.band{padding:3.2rem 0;border-top:1px solid var(--line)}section.band.alt{background:var(--card)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:2.5rem}
ul.ticks{padding-left:1.2rem}ul.ticks li{margin:.35rem 0}
.cats{display:grid;grid-template-columns:repeat(auto-fill,minmax(15rem,1fr));gap:1rem;list-style:none;padding:0;margin:0}
.cats a{display:block;padding:1.1rem 1.2rem;border:1px solid var(--line);border-radius:12px;background:var(--bg);text-decoration:none;color:inherit;height:100%}
section.band:not(.alt) .cats a{background:var(--card)}.cats a:hover{border-color:var(--red)}
.cats b{color:var(--ink)}.cats span{display:block;color:var(--muted);font-size:.95rem}
details{border-bottom:1px solid var(--line);padding:1rem 0}summary{font-weight:700;color:var(--ink);cursor:pointer}details p{margin:.7rem 0 0}
pre{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:1rem 1.2rem;overflow-x:auto;font-size:.93rem;line-height:1.55}
code{font-family:ui-monospace,"Cascadia Code",Menlo,Consolas,monospace;font-size:.92em}p code,li code{background:var(--red-soft);padding:.1em .35em;border-radius:5px}
.guide h2{margin-top:2.5rem}.note{border-left:4px solid var(--red);background:var(--red-soft);padding:1rem 1.2rem;border-radius:0 10px 10px 0}
footer{border-top:1px solid var(--line);padding:2rem 0;color:var(--muted);font-size:.95rem}footer .wrap{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap}footer p{margin:0}
@media (max-width:860px){.two{grid-template-columns:1fr}}
"""


def shell(title, desc, path, og, schema, body, script=""):
    url = SITE + path
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="MM Rahman Bappi">
<meta name="theme-color" content="#d6284b">
<meta property="og:type" content="website">
<meta property="og:site_name" content="100 Free 404 Pages">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/_site/og-{og}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}/_site/og-{og}.jpg">
<link rel="icon" href="{SITE}/_site/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{SITE}/_site/site.css">
<script type="application/ld+json">
{json.dumps(schema, indent=1, ensure_ascii=False)}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap"><a class="brand" href="{SITE}/">100 Free <b>404</b> Pages</a>
<nav aria-label="Main"><a href="{SITE}/#templates">Templates</a><a href="{SITE}/guide/">How to set up</a><a href="{SITE}/#faq">FAQ</a><a href="{REPO}">GitHub</a></nav></div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap"><p>Made by <a href="https://mmseo.app/">MM Rahman Bappi</a>. Free under the MIT license.</p><p><a href="{REPO}">Source on GitHub</a></p></div></footer>
{('<script>' + script + '</script>') if script else ''}
</body>
</html>
"""


def cat_name(cid):
    return next(c[1] for c in CATEGORIES if c[0] == cid)


def card(p, show_cat=True):
    base = f"{SITE}/{p['category']}/{p['slug']}/"
    cat = f'<a class="cat" href="{SITE}/{p["category"]}/">{esc(cat_name(p["category"]))}</a>' if show_cat else ""
    return (f'<li class="card" data-cat="{p["category"]}"><a href="{base}"><img src="{base}thumb.webp" alt="{esc(p["name"])} 404 page template preview" '
            f'width="600" height="375" loading="lazy"></a><div class="in">{cat}<h3>{esc(p["name"])}</h3><p>{esc(p["blurb"])}</p>'
            f'<div class="row"><a href="{base}">Live demo</a><a class="dl" href="{base}index.html" download="404.html">Download</a></div></div></li>')


HOME_FAQ = [
    ("Are these 404 pages really free?", "Yes. All 100 templates are free for personal and commercial projects under the MIT license. You can use them on client sites too."),
    ("How do I use a template on my website?", "Download the HTML file, change the brand name, links and colors, and upload it as your 404 page. The setup guide shows the exact steps for Apache, Nginx, WordPress, Netlify, Vercel, GitHub Pages and more."),
    ("Do I need any libraries or a build tool?", "No. Each template is one HTML file with its CSS and JavaScript inside. Some use a free Google Font, which you can remove if you prefer."),
    ("Will a custom 404 page hurt my SEO?", "No, as long as your server still sends the 404 status code. A helpful 404 page keeps visitors on your site instead of leaving. Every template already includes a noindex tag."),
    ("Do the templates work on phones?", "Yes. Every template adjusts to phones, tablets and desktops, and respects the reduced motion setting."),
]


def og_image(name, title, sub, files):
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), (251, 250, 248))
    d = ImageDraw.Draw(im)
    bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
    reg = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    d.rectangle([0, 0, W, 12], fill=(214, 40, 75))
    d.text((60, 60), title, font=bold, fill=(22, 22, 29))
    d.text((62, 145), sub, font=reg, fill=(98, 98, 110))
    for i, f in enumerate(files[:6]):
        t = Image.open(f).convert("RGB").resize((340, 212), Image.LANCZOS)
        x, y = 60 + (i % 3) * 370, 215 + (i // 3) * 200
        if y + 212 > H - 10:
            t = t.crop((0, 0, 340, H - 10 - y))
        im.paste(t, (x, y))
        d.rectangle([x, y, x + 339, y + t.size[1] - 1], outline=(220, 218, 212), width=2)
    im.save(os.path.join(ROOT, "_site", f"og-{name}.jpg"), "JPEG", quality=85, optimize=True)


def build():
    os.makedirs(os.path.join(ROOT, "_site"), exist_ok=True)
    open(os.path.join(ROOT, "_site", "site.css"), "w").write(CSS.strip() + "\n")
    open(os.path.join(ROOT, "_site", "favicon.svg"), "w").write(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='#d6284b'/>"
        "<text x='32' y='41' font-family='Arial' font-size='22' font-weight='700' text-anchor='middle' fill='white'>404</text></svg>\n")
    shots = {p["slug"]: os.path.join(ROOT, p["category"], p["slug"], "screenshot.png") for p in PAGES}

    # ---------- home ----------
    og_image("home", "100 free 404 page templates", "HTML and CSS, one file each, free under the MIT license",
             [shots[s] for s in ["astronaut", "glitch", "eight-bit", "terminal", "beach", "agency"]])
    title = "100 Free 404 Page Templates (HTML and CSS)"
    desc = "Download 100 free 404 error page templates in HTML and CSS. Minimal, animated, interactive, retro and business designs. One file each, MIT license."
    schema = {"@context": "https://schema.org", "@graph": [WEBSITE, AUTHOR,
        {"@type": "CollectionPage", "@id": SITE + "/#webpage", "url": SITE + "/", "name": title, "description": desc,
         "isPartOf": {"@id": SITE + "/#website"}, "mainEntity": {"@id": SITE + "/#categories"}, "inLanguage": "en",
         "primaryImageOfPage": SITE + "/_site/og-home.jpg", "dateModified": TODAY, "author": {"@id": SITE + "/#author"}},
        {"@type": "ItemList", "@id": SITE + "/#categories", "name": "404 page template categories", "numberOfItems": len(CATEGORIES),
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/{c[0]}/", "name": f"{c[1]} 404 pages"}
                             for i, c in enumerate(CATEGORIES)]},
        {"@type": "FAQPage", "@id": SITE + "/#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in HOME_FAQ]}]}
    chips = '<button type="button" aria-pressed="true" data-f="all">All 100</button>' + "".join(
        f'<button type="button" aria-pressed="false" data-f="{c[0]}">{esc(c[1])}</button>' for c in CATEGORIES)
    body = f"""<section class="hero"><div class="wrap">
<h1>100 free 404 page templates</h1>
<p class="lead">A broken link does not have to lose you a visitor. Pick a 404 page that fits your site, change the name and links, and upload it. Every template is a single HTML file that works on phones, with no libraries to install.</p>
<div class="actions"><a class="btn main" href="#templates">Browse the templates</a><a class="btn alt" href="{SITE}/guide/">How to set up a 404 page</a></div>
<p class="small">Free for personal and commercial use under the MIT license.</p>
</div></section>
<section class="band alt" id="templates"><div class="wrap">
<h2>All templates</h2>
<p>Filter by style, open the live demo, or download the file straight away.</p>
<div class="chips" role="group" aria-label="Filter by style">{chips}</div>
<ul class="grid" id="grid">{''.join(card(p) for p in PAGES)}</ul>
</div></section>
<section class="band"><div class="wrap">
<h2>Browse by style</h2>
<ul class="cats">{''.join(f'<li><a href="{SITE}/{c[0]}/"><b>{esc(c[1])}</b><span>{esc(c[2])}</span></a></li>' for c in CATEGORIES)}</ul>
</div></section>
<section class="band alt"><div class="wrap two">
<div><h2>What makes a good 404 page</h2>
<p>People land on a 404 page because a link broke or they typed the address wrong. A good 404 page says what happened in plain words, keeps your branding so visitors know they are still on your site, and gives them a clear way forward.</p>
<p>Many of these templates add a search box, a list of popular pages, or a small game, so visitors stay instead of closing the tab.</p></div>
<div><h2>What every template includes</h2><ul class="ticks">
<li>One HTML file with the CSS and JavaScript inside</li>
<li>Works on phones, tablets and desktops</li>
<li>A clear heading and a link back to your home page</li>
<li>A noindex tag, so the error page stays out of search results</li>
<li>Support for the reduced motion setting</li>
<li>Friendly, human text you can keep or change</li>
</ul></div>
</div></section>
<section class="band" id="faq"><div class="wrap narrow"><h2>Questions</h2>
{''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in HOME_FAQ)}
</div></section>"""
    script = """const b=[...document.querySelectorAll('.chips button')],c=[...document.querySelectorAll('#grid .card')];
b.forEach(x=>x.addEventListener('click',()=>{b.forEach(y=>y.setAttribute('aria-pressed',y===x));const f=x.dataset.f;c.forEach(k=>k.hidden=f!=='all'&&k.dataset.cat!==f)}));"""
    open(os.path.join(ROOT, "index.html"), "w").write(shell(title, desc, "/", "home", schema, body, script))

    # ---------- categories ----------
    for cid, cname, cdesc in CATEGORIES:
        items = [p for p in PAGES if p["category"] == cid]
        og_image(cid, f"{cname} 404 pages", f"{len(items)} free templates in HTML and CSS", [shots[p["slug"]] for p in items])
        t = f"{cname} 404 Page Templates, Free HTML and CSS"
        if len(t) > 60:
            t = f"{cname} 404 Page Templates (Free)"
        d = f"{len(items)} free {cname.lower()} 404 error page templates. {cdesc} One HTML file each, MIT license."
        url = f"{SITE}/{cid}/"
        schema = {"@context": "https://schema.org", "@graph": [WEBSITE, AUTHOR,
            {"@type": "CollectionPage", "@id": url + "#webpage", "url": url, "name": t, "description": d,
             "isPartOf": {"@id": SITE + "/#website"}, "breadcrumb": {"@id": url + "#breadcrumb"},
             "mainEntity": {"@id": url + "#list"}, "inLanguage": "en", "dateModified": TODAY},
            {"@type": "ItemList", "@id": url + "#list", "numberOfItems": len(items), "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "item": {
                    "@type": "CreativeWork", "name": f"{p['name']} 404 page template", "description": p["blurb"],
                    "url": f"{SITE}/{cid}/{p['slug']}/", "image": f"{SITE}/{cid}/{p['slug']}/screenshot.png",
                    "encodingFormat": "text/html", "license": "https://opensource.org/licenses/MIT",
                    "isAccessibleForFree": True, "author": {"@id": SITE + "/#author"}}} for i, p in enumerate(items)]},
            {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "404 page templates", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": f"{cname} 404 pages", "item": url}]}]}
        others = "".join(f'<a href="{SITE}/{c[0]}/">{esc(c[1])}</a>' for c in CATEGORIES if c[0] != cid)
        body = f"""<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="{SITE}/">404 page templates</a> / <span aria-current="page">{esc(cname)}</span></nav></div>
<section class="hero"><div class="wrap"><h1>{esc(cname)} 404 page templates</h1><p class="lead">{esc(cdesc)} All {len(items)} are free to download and use, and each one is a single HTML file.</p></div></section>
<section class="band alt"><div class="wrap"><ul class="grid">{''.join(card(p, False) for p in items)}</ul></div></section>
<section class="band"><div class="wrap narrow"><h2>How to use one</h2>
<p>Click Download to save the template as <code>404.html</code>. Open it in any text editor, change the brand name, colors and links, then upload it to your site. The <a href="{SITE}/guide/">setup guide</a> shows how to make your server use it for every missing page.</p></div></section>
<section class="band alt"><div class="wrap"><h2>Other styles</h2><div class="chips">{others}</div></div></section>"""
        open(os.path.join(ROOT, cid, "index.html"), "w").write(shell(t, d, f"/{cid}/", cid, schema, body))

    # ---------- guide ----------
    guide()

    # ---------- site 404 ----------
    nf = open(os.path.join(ROOT, "minimal", "big-number", "index.html")).read()
    nf = nf.replace('href="/"', f'href="{SITE}/"').replace("Back to the home page", "See all 100 templates").replace("Northwind", "100 Free 404 Pages")
    open(os.path.join(ROOT, "404.html"), "w").write(nf)

    urls = [SITE + "/"] + [f"{SITE}/{c[0]}/" for c in CATEGORIES] + [SITE + "/guide/"]
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>\n" for u in urls) + "</urlset>\n")
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    readme()
    print("site built")


GUIDE_FAQ = [
    ("Should I redirect all missing pages to my home page?", "No. Redirecting every broken link to the home page confuses visitors and Google treats it as a soft 404. Show a real 404 page with the 404 status code, and only redirect pages that really moved to a new address."),
    ("How do I check that my 404 page sends the right status code?", "Open a missing address on your site, then open your browser's developer tools, go to the Network tab and reload. The first request should show the status 404. You can also run curl -I with the address in a terminal."),
    ("Where do I find broken links on my site?", "Google Search Console lists pages that return 404 in the Pages report. Fix links that point to them, or add a 301 redirect when a page moved."),
]


def guide():
    url = SITE + "/guide/"
    title = "How to Set Up a Custom 404 Page on Any Website"
    desc = "Step by step: add a custom 404 error page on Apache, Nginx, WordPress, cPanel, Netlify, Vercel, Cloudflare Pages and GitHub Pages, and keep your SEO safe."
    og_image("guide", "How to set up a 404 page", "Apache, Nginx, WordPress, Netlify, Vercel and more",
             [os.path.join(ROOT, p["category"], p["slug"], "screenshot.png") for p in PAGES[::17]])
    schema = {"@context": "https://schema.org", "@graph": [WEBSITE, AUTHOR,
        {"@type": "TechArticle", "@id": url + "#article", "headline": "How to set up a custom 404 page on any website",
         "description": desc, "url": url, "mainEntityOfPage": url, "image": SITE + "/_site/og-guide.jpg",
         "author": {"@id": SITE + "/#author"}, "publisher": {"@id": SITE + "/#author"}, "datePublished": TODAY,
         "dateModified": TODAY, "inLanguage": "en", "isPartOf": {"@id": SITE + "/#website"},
         "proficiencyLevel": "Beginner"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "404 page templates", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "How to set up a 404 page", "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in GUIDE_FAQ]}]}
    body = f"""<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="{SITE}/">404 page templates</a> / <span aria-current="page">Setup guide</span></nav></div>
<article class="wrap narrow guide">
<h1>How to set up a custom 404 page</h1>
<p class="lead">You picked a template. Now your server needs to show it whenever someone opens a page that does not exist. Find your host below and follow the steps. Each one takes a few minutes.</p>
<p>First, download a template and save it as <code>404.html</code>. Change the brand name and links, and upload it to the main folder of your website.</p>

<h2>Apache and most shared hosting</h2>
<p>If your host uses Apache or LiteSpeed (most shared hosting plans do), add this line to the <code>.htaccess</code> file in your main folder, usually <code>public_html</code>. Create the file if it does not exist.</p>
<pre><code>ErrorDocument 404 /404.html</code></pre>
<p>Use a path that starts with a slash, not a full address with https. A full address makes Apache send a redirect instead of the 404 status.</p>

<h2>cPanel</h2>
<p>In cPanel, open <b>Error Pages</b> in the Advanced section, choose your domain, click <b>404 (Not Found)</b>, paste the template code and save. cPanel writes the <code>.htaccess</code> line for you.</p>

<h2>Nginx</h2>
<p>Add this inside the <code>server</code> block of your site configuration, then reload Nginx with <code>sudo nginx -s reload</code>.</p>
<pre><code>error_page 404 /404.html;
location = /404.html {{
    internal;
}}</code></pre>

<h2>WordPress</h2>
<p>WordPress uses the <code>404.php</code> file in your theme. The safest way is a child theme: create <code>404.php</code> in the child theme folder and paste the template's HTML into it. If you want your normal header and footer, put <code>&lt;?php get_header(); ?&gt;</code> at the top and <code>&lt;?php get_footer(); ?&gt;</code> at the bottom, and keep only the main content from the template. Many themes and page builders also have a 404 page setting.</p>

<h2>Netlify, Cloudflare Pages and Vercel</h2>
<p>Put <code>404.html</code> in the folder you deploy, next to <code>index.html</code>. Netlify and Cloudflare Pages use it automatically. Vercel does the same for static sites. For Next.js, create <code>app/not-found.js</code> (or <code>pages/404.js</code>) and move the template's HTML into it.</p>

<h2>GitHub Pages</h2>
<p>Add <code>404.html</code> to the root of the branch or folder you publish. GitHub Pages shows it for every missing page and sends the correct 404 status.</p>

<h2>Keep your SEO safe</h2>
<ul class="ticks">
<li><b>Send the 404 status code.</b> The page should look friendly, but the server must still say 404. If it says 200, Google may report a soft 404.</li>
<li><b>Do not redirect everything to the home page.</b> Only redirect pages that really moved, with a 301 redirect to the new address.</li>
<li><b>Keep the noindex tag.</b> Every template includes it, so the error page itself never shows up in search results.</li>
<li><b>Use links that start with a slash</b>, like <code>/</code> and <code>/contact</code>, so they work from any address.</li>
<li><b>Check for broken links</b> in Google Search Console, in the Pages report, and fix the most visited ones first.</li>
</ul>
<p class="note">Tip: open a made-up address on your site, such as <code>/test-404</code>, to see your new page in action.</p>

<h2>Questions</h2>
{''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in GUIDE_FAQ)}
<p style="margin-top:2rem"><a class="btn main" href="{SITE}/#templates">Choose a template</a></p>
</article>"""
    os.makedirs(os.path.join(ROOT, "guide"), exist_ok=True)
    open(os.path.join(ROOT, "guide", "index.html"), "w").write(shell(title, desc, "/guide/", "guide", schema, body))


def readme():
    rows = []
    for cid, cname, cdesc in CATEGORIES:
        rows.append(f"\n### {cname}\n\n{cdesc}\n\n| Preview | Template |\n|---|---|")
        for p in [x for x in PAGES if x["category"] == cid]:
            path = f"{cid}/{p['slug']}"
            rows.append(f"| [![{p['name']}]({path}/thumb.webp)]({SITE}/{path}/) | **[{p['name']}]({path}/)**<br>{p['blurb']}<br><br>"
                        f"[Live demo]({SITE}/{path}/) / [Download]({path}/index.html) |")
    text = f"""# 100 Free 404 Page Templates

![100 free 404 page templates](_site/og-home.jpg)

100 free 404 error page templates, each in a single HTML file. Pick one that fits your site, change the name and links, and upload it. No libraries, no build step.

**[See every template with a live demo](https://mmrahmanbappi.github.io/100-free-404-pages/)** / **[How to set up a 404 page]({SITE}/guide/)**

## Why use these templates

- **One file each.** The CSS and JavaScript are inside the HTML file.
- **Works on phones.** Every template adjusts to phones, tablets and desktops.
- **Keeps visitors.** Many include a search box, popular links or a small game.
- **Safe for SEO.** Each page has a noindex tag, and the guide shows how to keep the correct 404 status.
- **Free for business use.** MIT license. Use them for your own site or for clients.

## How to use a template

1. Open the template folder and download `index.html`.
2. Rename it to `404.html`, then change the brand name, colors and links.
3. Upload it to your site and tell your server to use it. The [setup guide]({SITE}/guide/) covers Apache, Nginx, cPanel, WordPress, Netlify, Vercel, Cloudflare Pages and GitHub Pages.

## Templates
{chr(10).join(rows)}

## Contributing

New templates are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## License

[MIT](LICENSE). Free for personal and commercial use.

Made by [MM Rahman Bappi](https://mmseo.app/).
"""
    open(os.path.join(ROOT, "README.md"), "w").write(text)


if __name__ == "__main__":
    build()
