from core import add

C = "minimal"

add(C, "big-number", "Big Number", "Northwind", "A huge 404 in a light weight, with one line of text and one button.",
"""body{display:grid;place-items:center;background:#f7f7f5;color:#161616;font-family:Inter,system-ui,sans-serif;padding:2rem}
main{text-align:center;max-width:36rem}
.n{font-size:clamp(7rem,28vw,18rem);font-weight:200;line-height:.9;letter-spacing:-.06em;margin:0}
p{font-size:1.2rem;color:#555;margin:1.5rem 0 2rem}
a.b{display:inline-block;background:#161616;color:#fff;padding:.9rem 1.6rem;border-radius:999px;text-decoration:none;font-weight:600}""",
"""<main><h1 class="n" aria-label="Error 404">404</h1><p>This page is not here. It may have moved, or the link may be wrong.</p><a class="b" href="/">Back to the home page</a></main>""",
fonts=["Inter:wght@200;400;600"], theme="#161616")

add(C, "split-screen", "Split Screen", "Halden", "A two-column layout: the error code on one side, helpful links on the other.",
"""body{display:grid;grid-template-columns:1fr 1fr;background:#fff;color:#1b1f24;font-family:"DM Sans",system-ui,sans-serif}
.l{background:#1b1f24;color:#fff;display:grid;place-items:center;padding:3rem}
.l span{font-size:clamp(5rem,14vw,11rem);font-weight:700;letter-spacing:-.04em}
.r{display:flex;flex-direction:column;justify-content:center;padding:3rem clamp(2rem,6vw,6rem)}
h1{font-size:2.2rem;margin:0 0 1rem}
p{color:#5a6069;font-size:1.1rem;line-height:1.6;margin:0 0 2rem}
ul{list-style:none;padding:0;margin:0;border-top:1px solid #e5e7ea}
li a{display:flex;justify-content:space-between;padding:1rem 0;border-bottom:1px solid #e5e7ea;text-decoration:none;font-weight:500}
li a:hover{color:#2458d6}
@media(max-width:760px){body{grid-template-columns:1fr}.l{padding:2rem}}""",
"""<div class="l" aria-hidden="true"><span>404</span></div>
<main class="r"><h1>We could not find that page</h1><p>Try one of these instead. They are the pages people visit most.</p>
<ul><li><a href="/">Home <span aria-hidden="true">&rsaquo;</span></a></li><li><a href="/about">About us <span aria-hidden="true">&rsaquo;</span></a></li><li><a href="/blog">Blog <span aria-hidden="true">&rsaquo;</span></a></li><li><a href="/contact">Contact <span aria-hidden="true">&rsaquo;</span></a></li></ul></main>""",
fonts=["DM Sans:wght@400;500;700"], theme="#1b1f24")

add(C, "outline", "Outline", "Kestrel", "An outlined 404 with a thin stroke and a calm off-white background.",
"""body{display:grid;place-items:center;background:#f3f1ec;color:#23211d;font-family:"Space Grotesk",system-ui,sans-serif;padding:2rem}
main{text-align:center}
.n{font-size:clamp(7rem,26vw,16rem);font-weight:700;color:transparent;-webkit-text-stroke:2px #23211d;line-height:1;margin:0}
h1{font-size:1.6rem;margin:1rem 0 .5rem}
p{color:#6b665c;margin:0 0 2rem}
a{font-weight:700;text-decoration:none;border-bottom:2px solid #23211d;padding-bottom:2px}""",
"""<main><div class="n" aria-hidden="true">404</div><h1>Page not found</h1><p>Nothing lives at this address.</p><a href="/">Go home</a></main>""",
fonts=["Space Grotesk:wght@400;700"], theme="#23211d")

add(C, "left-aligned", "Left Aligned", "Pinecrest", "A left-aligned layout that reads like a short letter, with a search box.",
"""body{background:#fff;color:#1d2a24;font-family:"Source Serif 4",Georgia,serif;display:flex;align-items:center;min-height:100vh;padding:2rem}
main{max-width:40rem;margin-left:clamp(0rem,10vw,10rem)}
small{font-family:system-ui,sans-serif;color:#2f7a55;font-weight:600;letter-spacing:.02em}
h1{font-size:clamp(2.4rem,6vw,3.8rem);line-height:1.1;margin:.6rem 0 1.2rem;font-weight:600}
p{font-size:1.25rem;line-height:1.6;color:#4b5a53}
form{display:flex;gap:.5rem;margin:2rem 0;font-family:system-ui,sans-serif}
input{flex:1;padding:.85rem 1rem;border:1.5px solid #cfd8d3;border-radius:8px;font:inherit}
button{padding:.85rem 1.2rem;border:0;border-radius:8px;background:#2f7a55;color:#fff;font:inherit;font-weight:600;cursor:pointer}
nav a{font-family:system-ui,sans-serif;margin-right:1.5rem;color:#2f7a55}""",
"""<main><small>Error 404</small><h1>Sorry, we could not find that page.</h1><p>The page may have been moved or deleted. You can search the site, or start again from one of the links below.</p>
<form role="search" action="/search"><label class="sr" for="q">Search this site</label><input id="q" name="q" type="search" placeholder="Search this site"><button>Search</button></form>
<nav><a href="/">Home</a><a href="/help">Help center</a><a href="/contact">Contact us</a></nav></main>""",
fonts=["Source Serif 4:wght@400;600"], theme="#2f7a55")

add(C, "circle", "Circle", "Orbit Studio", "A single large circle frames the message. Simple and memorable.",
"""body{display:grid;place-items:center;background:#eef1f6;font-family:Manrope,system-ui,sans-serif;color:#18223a;padding:1.5rem}
.c{width:min(80vw,460px);aspect-ratio:1;border-radius:50%;background:#fff;box-shadow:0 30px 60px -30px rgba(24,34,58,.35);display:grid;place-items:center;text-align:center;padding:2rem}
b{display:block;font-size:clamp(3.5rem,14vw,6rem);color:#3b5bdb;line-height:1}
h1{font-size:1.4rem;margin:.6rem 0}
p{color:#5c6782;margin:0 0 1.2rem}
a{color:#3b5bdb;font-weight:700}""",
"""<main class="c"><div><b aria-hidden="true">404</b><h1>Lost in space</h1><p>This page does not exist.</p><a href="/">Take me home</a></div></main>""",
fonts=["Manrope:wght@400;700;800"], theme="#3b5bdb")

add(C, "serif-editorial", "Serif Editorial", "The Ledger", "A magazine-style page with a large serif headline and a thin rule.",
"""body{background:#fbfaf7;color:#1a1a1a;font-family:"Playfair Display",Georgia,serif;display:grid;place-items:center;padding:2rem}
main{max-width:44rem;text-align:center}
.k{font-family:system-ui,sans-serif;font-size:.9rem;color:#8a1c1c;letter-spacing:.05em}
h1{font-size:clamp(2.6rem,7vw,4.6rem);font-weight:700;line-height:1.05;margin:1rem 0}
hr{width:5rem;border:0;border-top:2px solid #1a1a1a;margin:1.8rem auto}
p{font-family:Georgia,serif;font-size:1.2rem;line-height:1.7;color:#444;font-style:italic}
a{display:inline-block;margin-top:1.5rem;font-family:system-ui,sans-serif;font-weight:600;color:#8a1c1c}""",
"""<main><div class="k">Error 404, page missing</div><h1>This story could not be found</h1><hr><p>The article you are looking for may have been moved, renamed or taken down. Our front page has everything that is new today.</p><a href="/">Read today's front page</a></main>""",
fonts=["Playfair Display:wght@700"], theme="#8a1c1c")

add(C, "stacked-lines", "Stacked Lines", "Linea", "The numbers 4, 0 and 4 stacked in three bold rows, with a short note.",
"""body{display:grid;grid-template-columns:auto 1fr;align-items:center;gap:clamp(2rem,6vw,6rem);background:#101010;color:#f2f2f2;font-family:"Archivo",system-ui,sans-serif;padding:clamp(2rem,6vw,6rem)}
.s span{display:block;font-size:clamp(4rem,12vw,9rem);font-weight:900;line-height:.85}
.s span:nth-child(2){color:#ffd23f}
h1{font-size:2rem;margin:0 0 1rem}
p{color:#b3b3b3;font-size:1.15rem;line-height:1.6;max-width:28rem}
a{display:inline-block;margin-top:1.5rem;background:#ffd23f;color:#101010;padding:.8rem 1.4rem;font-weight:800;text-decoration:none}
@media(max-width:640px){body{grid-template-columns:1fr}}""",
"""<div class="s" aria-hidden="true"><span>4</span><span>0</span><span>4</span></div>
<main><h1>Wrong turn</h1><p>The page you asked for is not on this site. Check the address for typos, or head back to the start.</p><a href="/">Home page</a></main>""",
fonts=["Archivo:wght@400;900"], theme="#ffd23f")

add(C, "card-center", "Card", "Meadow", "A soft card in the middle of a pale green page, with two buttons.",
"""body{display:grid;place-items:center;background:#e8f3ec;font-family:Nunito,system-ui,sans-serif;color:#1f3a2c;padding:1.5rem}
.card{background:#fff;border-radius:20px;padding:clamp(2rem,5vw,3.5rem);max-width:30rem;text-align:center;box-shadow:0 20px 40px -24px rgba(31,58,44,.35)}
.code{display:inline-block;background:#e8f3ec;color:#2d7a4f;font-weight:800;padding:.3rem .8rem;border-radius:999px}
h1{font-size:1.9rem;margin:1rem 0 .6rem}
p{color:#557262;line-height:1.6}
.row{display:flex;gap:.7rem;justify-content:center;flex-wrap:wrap;margin-top:1.6rem}
.row a{padding:.8rem 1.3rem;border-radius:12px;text-decoration:none;font-weight:700}
.p{background:#2d7a4f;color:#fff}.s{background:#e8f3ec;color:#2d7a4f}""",
"""<main class="card"><span class="code">404</span><h1>We cannot find that page</h1><p>It might be an old link, or the page may have moved. Here are two good places to go next.</p><div class="row"><a class="p" href="/">Go to home</a><a class="s" href="/contact">Tell us what broke</a></div></main>""",
fonts=["Nunito:wght@400;700;800"], theme="#2d7a4f")

add(C, "half-cut", "Half Cut", "Fold", "A 404 sliced in half horizontally, as if the page was torn.",
"""body{display:grid;place-items:center;background:#fff;color:#0f172a;font-family:"Sora",system-ui,sans-serif;padding:2rem;text-align:center}
.n{position:relative;font-size:clamp(7rem,24vw,15rem);font-weight:800;line-height:1;letter-spacing:-.04em;height:1em}
.n span{position:absolute;inset:0}
.n .t{clip-path:inset(0 0 52% 0);transform:translateX(-10px)}
.n .b{clip-path:inset(48% 0 0 0);transform:translateX(10px);color:#e11d48}
h1{font-size:1.6rem;margin:1.8rem 0 .5rem}
p{color:#64748b;margin:0 0 1.8rem}
a{color:#e11d48;font-weight:700}""",
"""<main><div class="n" aria-hidden="true"><span class="t">404</span><span class="b">404</span></div><h1>Something broke along the way</h1><p>The page you are looking for is not here.</p><a href="/">Start over</a></main>""",
fonts=["Sora:wght@400;800"], theme="#e11d48")

add(C, "grid-lines", "Grid Lines", "Blueprint Co.", "A fine grid background with the message placed like a note on graph paper.",
"""body{display:grid;place-items:center;background:#fff;background-image:linear-gradient(#eef0f4 1px,transparent 1px),linear-gradient(90deg,#eef0f4 1px,transparent 1px);background-size:32px 32px;color:#1e293b;font-family:"IBM Plex Sans",system-ui,sans-serif;padding:2rem}
main{background:#fff;border:1.5px solid #1e293b;padding:2.5rem;max-width:32rem;box-shadow:8px 8px 0 #1e293b}
.t{font-family:"IBM Plex Mono",monospace;font-size:.95rem;color:#2563eb}
h1{font-size:2rem;margin:.6rem 0 1rem}
p{line-height:1.6;color:#475569}
a{display:inline-block;margin-top:1rem;background:#2563eb;color:#fff;padding:.75rem 1.2rem;text-decoration:none;font-weight:600}""",
"""<main><div class="t">status: 404 not found</div><h1>This page is off the plan</h1><p>We checked every line and could not find it. The page may have moved during a redesign.</p><a href="/">Back to the main page</a></main>""",
fonts=["IBM Plex Sans:wght@400;600", "IBM Plex Mono"], theme="#2563eb")
