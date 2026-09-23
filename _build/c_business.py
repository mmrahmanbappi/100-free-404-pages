from core import add

C = "business"

def site_header(brand, color):
    return f"""<header class="hd"><a class="logo" href="/"><span class="dot" style="background:{color}"></span>{brand}</a><nav><a href="/">Home</a><a href="/services">Services</a><a href="/about">About</a><a href="/contact">Contact</a></nav></header>"""

HD = """.hd{display:flex;justify-content:space-between;align-items:center;padding:1.2rem clamp(1.2rem,5vw,4rem);flex-wrap:wrap;gap:1rem}
.logo{display:flex;align-items:center;gap:.5rem;font-weight:800;text-decoration:none;font-size:1.15rem}.dot{width:14px;height:14px;border-radius:4px}
.hd nav{display:flex;gap:1.3rem;flex-wrap:wrap}.hd nav a{text-decoration:none;opacity:.8}"""

add(C, "corporate", "Corporate", "Meridian Group", "A calm corporate page with the site header, a clear message and four useful links.",
HD + """body{background:#fff;color:#14213d;font-family:"Inter",system-ui,sans-serif}
main{max-width:64rem;margin:0 auto;padding:clamp(2rem,8vw,6rem) clamp(1.2rem,5vw,4rem)}
small{color:#1d4ed8;font-weight:700}h1{font-size:clamp(2.2rem,5vw,3.4rem);margin:.5rem 0 1rem;letter-spacing:-.02em}
p{font-size:1.15rem;color:#4b5563;max-width:38rem;line-height:1.6}
.links{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:1rem;margin-top:2.5rem}
.links a{border:1px solid #e5e7eb;border-radius:12px;padding:1.2rem;text-decoration:none}.links a:hover{border-color:#1d4ed8}
.links b{display:block;margin-bottom:.3rem}.links span{color:#6b7280;font-size:.95rem}""",
site_header("Meridian Group", "#1d4ed8") + """<main><small>Error 404</small><h1>We cannot find that page</h1><p>The page may have moved when we updated our website. These sections should help you find what you need.</p>
<div class="links"><a href="/services"><b>Our services</b><span>What we do for clients</span></a><a href="/about"><b>About us</b><span>Our history and team</span></a><a href="/news"><b>News</b><span>Latest announcements</span></a><a href="/contact"><b>Contact</b><span>Talk to a real person</span></a></div></main>""",
fonts=["Inter:wght@400;700;800"], theme="#1d4ed8")

add(C, "saas", "SaaS", "Relay", "A product page style with a gradient badge, a button to the dashboard and help links.",
HD + """body{background:linear-gradient(180deg,#f5f3ff,#fff 60%);color:#1e1b4b;font-family:"Plus Jakarta Sans",system-ui,sans-serif}
main{text-align:center;padding:clamp(3rem,10vw,7rem) 1.5rem;max-width:40rem;margin:0 auto}
.badge{display:inline-block;padding:.35rem .9rem;border-radius:999px;background:linear-gradient(90deg,#8b5cf6,#ec4899);color:#fff;font-weight:700;font-size:.9rem}
h1{font-size:clamp(2.2rem,6vw,3.4rem);margin:1rem 0;letter-spacing:-.02em}p{color:#5b5780;font-size:1.15rem;line-height:1.6}
.row{display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap;margin:2rem 0 1.4rem}.row a{padding:.85rem 1.4rem;border-radius:12px;text-decoration:none;font-weight:700}
.p{background:#1e1b4b;color:#fff}.s{background:#fff;border:1.5px solid #ddd6fe}
.help{font-size:.95rem;color:#5b5780}.help a{color:#7c3aed}""",
site_header("Relay", "#8b5cf6") + """<main><span class="badge">404</span><h1>This page is not available</h1><p>The link may be old, or the feature may have moved to a new place in the app.</p><div class="row"><a class="p" href="/app">Open your dashboard</a><a class="s" href="/">Go to the homepage</a></div><p class="help">Need help? Visit the <a href="/docs">docs</a> or <a href="/contact">contact support</a>.</p></main>""",
fonts=["Plus Jakarta Sans:wght@400;700;800"], theme="#8b5cf6")

add(C, "law-firm", "Law Firm", "Hartley & Webb", "A formal, trustworthy page for a law or accounting firm, with a phone number.",
HD + """body{background:#faf8f4;color:#1f2a37;font-family:"Libre Baskerville",Georgia,serif}
.hd{border-bottom:1px solid #e3ddd0;font-family:system-ui,sans-serif}
main{max-width:46rem;margin:0 auto;padding:clamp(3rem,10vw,6rem) 1.5rem;text-align:center}
.seal{width:70px;height:70px;border-radius:50%;border:2px solid #7c5c2b;color:#7c5c2b;display:grid;place-items:center;margin:0 auto 1.5rem;font-size:1.1rem}
h1{font-size:clamp(2rem,5vw,2.8rem);font-weight:400;margin:0 0 1rem}p{font-size:1.1rem;line-height:1.8;color:#4b5563}
.tel{display:inline-block;margin-top:1.5rem;font-family:system-ui,sans-serif;background:#1f2a37;color:#fff;padding:.9rem 1.5rem;text-decoration:none}""",
site_header("Hartley &amp; Webb", "#7c5c2b") + """<main><div class="seal" aria-hidden="true">404</div><h1>This page could not be found</h1><p>We may have moved or retired the page you are looking for. If you need advice today, our team is available by phone during office hours, or you can return to our <a href="/">home page</a>.</p><a class="tel" href="tel:+15550100">Call +1 555 0100</a></main>""",
fonts=["Libre Baskerville"], theme="#7c5c2b")

add(C, "clinic", "Clinic", "Greenfield Clinic", "A clear, reassuring page for a clinic or health service, with booking and urgent care notes.",
HD + """body{background:#f0faf7;color:#123b33;font-family:"Nunito Sans",system-ui,sans-serif}
main{max-width:56rem;margin:0 auto;padding:clamp(2rem,8vw,5rem) 1.5rem;display:grid;grid-template-columns:1.3fr 1fr;gap:2rem;align-items:start}
h1{font-size:clamp(2rem,5vw,3rem);margin:0 0 1rem}p{font-size:1.1rem;line-height:1.7;color:#3d6158}
.b{display:inline-block;background:#0f766e;color:#fff;padding:.85rem 1.4rem;border-radius:10px;text-decoration:none;font-weight:700;margin-top:1rem}
aside{background:#fff;border-radius:16px;padding:1.5rem;border:1px solid #cdeee5}aside h2{font-size:1.1rem;margin:0 0 .6rem}aside p{font-size:1rem;margin:0 0 1rem}
.urgent{border-left:4px solid #dc2626;padding-left:.8rem}
@media(max-width:760px){main{grid-template-columns:1fr}}""",
site_header("Greenfield Clinic", "#0f766e") + """<main><div><h1>Sorry, we cannot find that page</h1><p>The page may have moved. You can still book an appointment online or find our opening hours from the home page.</p><a class="b" href="/book">Book an appointment</a></div>
<aside><h2>Quick links</h2><p><a href="/">Home</a><br><a href="/services">Our services</a><br><a href="/hours">Opening hours</a></p><p class="urgent"><b>In an emergency</b>, call your local emergency number straight away.</p></aside></main>""",
fonts=["Nunito Sans:wght@400;700;800"], theme="#0f766e")

add(C, "school", "School", "Brookfield School", "A bright page for a school or college with links for parents, students and staff.",
HD + """body{background:#fffdf5;color:#1c2c4c;font-family:"Lexend",system-ui,sans-serif}
main{max-width:60rem;margin:0 auto;padding:clamp(2rem,8vw,5rem) 1.5rem;text-align:center}
.n{font-size:clamp(4rem,14vw,7rem);font-weight:800;color:#f59e0b;margin:0;line-height:1}
h1{font-size:clamp(1.8rem,4vw,2.4rem);margin:.5rem 0 1rem}p{color:#4a5a78;font-size:1.1rem}
.g{display:grid;grid-template-columns:repeat(auto-fit,minmax(14rem,1fr));gap:1rem;margin-top:2rem;text-align:left}
.g a{background:#fff;border-radius:14px;padding:1.3rem;text-decoration:none;box-shadow:0 8px 24px -16px rgba(28,44,76,.4);border-top:5px solid var(--c)}
.g b{display:block;font-size:1.1rem}.g span{color:#6a7896;font-size:.95rem}""",
site_header("Brookfield School", "#f59e0b") + """<main><div class="n" aria-hidden="true">404</div><h1>This page has gone missing</h1><p>It may have been an old notice or a page from last term. Choose where you want to go.</p>
<div class="g"><a href="/parents" style="--c:#f59e0b"><b>Parents</b><span>Term dates, letters and payments</span></a><a href="/students" style="--c:#3b82f6"><b>Students</b><span>Timetables and homework</span></a><a href="/admissions" style="--c:#10b981"><b>Admissions</b><span>How to apply</span></a></div></main>""",
fonts=["Lexend:wght@400;800"], theme="#f59e0b")

add(C, "restaurant", "Restaurant", "Olive & Ember", "A warm restaurant page: the dish is off the menu, with links to the menu and bookings.",
HD + """body{background:#1f1a17;color:#f5ece1;font-family:"Cormorant",Georgia,serif}
.hd a{color:#f5ece1}
main{max-width:44rem;margin:0 auto;padding:clamp(3rem,10vw,6rem) 1.5rem;text-align:center}
.k{font-family:system-ui,sans-serif;font-size:.9rem;color:#d4a373;letter-spacing:.08em}
h1{font-size:clamp(2.4rem,7vw,4rem);font-weight:600;margin:.6rem 0;line-height:1.1}
p{font-size:1.3rem;color:#cbbfb1;line-height:1.6;font-style:italic}
.row{display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap;margin-top:2rem;font-family:system-ui,sans-serif}
.row a{padding:.85rem 1.4rem;text-decoration:none;font-weight:600;border:1px solid #d4a373;color:#d4a373}.row a.p{background:#d4a373;color:#1f1a17}""",
site_header("Olive &amp; Ember", "#d4a373") + """<main><div class="k">Error 404</div><h1>This dish is off the menu</h1><p>The page you ordered is not available tonight. Our chefs recommend the full menu instead.</p><div class="row"><a class="p" href="/menu">See the menu</a><a href="/book">Book a table</a></div></main>""",
fonts=["Cormorant:ital,wght@0,600;1,500"], theme="#d4a373")

add(C, "hotel", "Hotel", "Harbor House Hotel", "A hotel page with a check-in style card and links to rooms and bookings.",
HD + """body{background:#eef3f7;color:#0f2537;font-family:"Mulish",system-ui,sans-serif}
main{display:grid;place-items:center;padding:clamp(2rem,8vw,5rem) 1.5rem}
.card{background:#fff;border-radius:20px;overflow:hidden;width:min(94vw,520px);box-shadow:0 30px 60px -35px rgba(15,37,55,.5)}
.top{background:#0f2537;color:#fff;padding:1.4rem 1.6rem;display:flex;justify-content:space-between;align-items:center}
.top b{font-size:2.4rem}.top span{opacity:.75}
.body{padding:1.6rem}h1{font-size:1.6rem;margin:0 0 .6rem}p{color:#4c6275;line-height:1.6}
.row{display:flex;gap:.7rem;flex-wrap:wrap;margin-top:1.2rem}.row a{padding:.75rem 1.2rem;border-radius:10px;text-decoration:none;font-weight:700}.p{background:#c29b57;color:#fff}.s{background:#eef3f7}""",
site_header("Harbor House", "#c29b57") + """<main><div class="card"><div class="top"><div><span>Room</span><br><b>404</b></div><span>Not available</span></div><div class="body"><h1>This room does not exist</h1><p>The page you tried to open is not part of our hotel. You can still see our rooms, or book your stay directly.</p><div class="row"><a class="p" href="/book">Check availability</a><a class="s" href="/rooms">View rooms</a></div></div></div></main>""",
fonts=["Mulish:wght@400;700;800"], theme="#c29b57")

add(C, "real-estate", "Real Estate", "Keystone Homes", "A property listing card showing the page as 'sold', with a link to current listings.",
HD + """body{background:#f7f7f7;color:#1f2937;font-family:"Outfit",system-ui,sans-serif}
main{max-width:58rem;margin:0 auto;padding:clamp(2rem,8vw,5rem) 1.5rem;display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;align-items:center}
.l{position:relative;background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 20px 40px -25px rgba(0,0,0,.3)}
.img{height:190px;background:linear-gradient(135deg,#a7c4a0,#dce8d9);display:grid;place-items:end center}
.img svg{width:60%}
.sold{position:absolute;top:18px;left:-40px;transform:rotate(-35deg);background:#dc2626;color:#fff;padding:.3rem 3rem;font-weight:800}
.info{padding:1rem 1.2rem}.info b{font-size:1.3rem}.info span{color:#6b7280}
h1{font-size:clamp(2rem,5vw,2.8rem);margin:0 0 1rem}p{color:#4b5563;line-height:1.6;font-size:1.1rem}
a.b{display:inline-block;margin-top:1rem;background:#166534;color:#fff;padding:.85rem 1.4rem;border-radius:10px;text-decoration:none;font-weight:700}
@media(max-width:760px){main{grid-template-columns:1fr}}""",
site_header("Keystone Homes", "#166534") + """<main><div class="l" aria-hidden="true"><div class="sold">SOLD</div><div class="img"><svg viewBox="0 0 200 110"><path d="M20 110 V50 L100 5 L180 50 V110 Z" fill="#fff"/><rect x="85" y="65" width="30" height="45" fill="#166534"/><rect x="40" y="60" width="28" height="22" fill="#cfe3f5"/><rect x="132" y="60" width="28" height="22" fill="#cfe3f5"/></svg></div><div class="info"><b>404 Missing Lane</b><br><span>No longer listed</span></div></div>
<div><h1>This listing is gone</h1><p>The property may have sold, or the page moved. There are plenty of homes still available.</p><a class="b" href="/listings">See current listings</a></div></main>""",
fonts=["Outfit:wght@400;700;800"], theme="#166534")

add(C, "nonprofit", "Nonprofit", "Open Hands", "A friendly nonprofit page with a donate button and ways to get involved.",
HD + """body{background:#fff7f2;color:#3d1f12;font-family:"Karla",system-ui,sans-serif}
main{max-width:46rem;margin:0 auto;padding:clamp(3rem,10vw,6rem) 1.5rem;text-align:center}
.heart{width:70px;margin:0 auto 1.2rem}
h1{font-size:clamp(2rem,5vw,3rem);margin:0 0 1rem}p{font-size:1.15rem;color:#6d4636;line-height:1.7}
.row{display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap;margin-top:2rem}.row a{padding:.9rem 1.5rem;border-radius:999px;text-decoration:none;font-weight:800}.p{background:#e85d04;color:#fff}.s{border:2px solid #e85d04;color:#e85d04}""",
site_header("Open Hands", "#e85d04") + """<main><svg class="heart" viewBox="0 0 64 58" aria-hidden="true"><path d="M32 56 C 10 40, 0 28, 0 16 A 16 16 0 0 1 32 10 A 16 16 0 0 1 64 16 C 64 28, 54 40, 32 56Z" fill="#e85d04"/></svg><h1>We could not find this page</h1><p>But you can still make a difference today. Every gift helps families in our community.</p><div class="row"><a class="p" href="/donate">Donate now</a><a class="s" href="/volunteer">Volunteer with us</a></div></main>""",
fonts=["Karla:wght@400;800"], theme="#e85d04")

add(C, "agency", "Creative Agency", "Studio Kiln", "A bold agency page with giant type, a marquee of services and a project link.",
HD + """body{background:#f2f0e9;color:#111;font-family:"Syne",system-ui,sans-serif;overflow-x:hidden}
main{padding:clamp(2rem,6vw,4rem) clamp(1.2rem,5vw,4rem)}
h1{font-size:clamp(3.5rem,13vw,10rem);line-height:.9;margin:0;font-weight:800;letter-spacing:-.04em}
h1 em{font-style:normal;color:#ff4d00}
.mq{border-top:2px solid #111;border-bottom:2px solid #111;margin:2.5rem -4rem;padding:.8rem 0;white-space:nowrap;overflow:hidden;font-size:1.4rem;font-weight:700}
.mq span{display:inline-block;animation:m 18s linear infinite}@keyframes m{to{transform:translateX(-50%)}}
p{font-family:system-ui,sans-serif;font-size:1.15rem;max-width:30rem}a.b{display:inline-block;background:#111;color:#f2f0e9;padding:1rem 1.6rem;text-decoration:none;font-weight:700;margin-top:1rem}""",
site_header("Studio Kiln", "#ff4d00") + """<main><h1>Page<br><em>not found.</em></h1><div class="mq" aria-hidden="true"><span>Branding / Web design / Motion / Strategy / Branding / Web design / Motion / Strategy / Branding / Web design / Motion / Strategy / Branding / Web design / Motion / Strategy /&nbsp;</span></div><p>This project is not in our portfolio anymore. Take a look at what we are working on now.</p><a class="b" href="/work">See our work</a></main>""",
fonts=["Syne:wght@400;800"], theme="#ff4d00")
