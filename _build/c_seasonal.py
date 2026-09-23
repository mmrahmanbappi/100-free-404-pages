from core import add

C = "seasonal"

def scene(bg, fg, font, svg, title, text, btn_bg, btn_fg="#fff", link="Go to the home page"):
    css = f"""body{{background:{bg};color:{fg};font-family:"{font}",system-ui,sans-serif;display:flex;flex-direction:column;min-height:100vh;overflow-x:hidden}}
main{{text-align:center;padding:clamp(2rem,7vw,4rem) 1.5rem 1rem;position:relative;z-index:1}}
h1{{font-size:clamp(2rem,6vw,3rem);margin:0 0 .6rem}}p{{font-size:1.15rem;opacity:.85;margin:0 auto 1.6rem;max-width:34rem;line-height:1.6}}
a.b{{display:inline-block;background:{btn_bg};color:{btn_fg};padding:.85rem 1.5rem;border-radius:12px;text-decoration:none;font-weight:700}}
.sc{{margin-top:auto;width:100%}}.sc svg{{width:100%;height:auto;max-height:46vh}}"""
    body = f"""<main><h1>{title}</h1><p>{text}</p><a class="b" href="/">{link}</a></main><div class="sc" aria-hidden="true">{svg}</div>"""
    return css, body

css, body = scene("linear-gradient(#2c3e50,#4b6584)", "#f1f5f9", "Poppins",
"""<svg viewBox="0 0 1200 320" preserveAspectRatio="xMidYMax slice"><g fill="#1e2b38"><rect x="40" y="120" width="120" height="200"/><rect x="180" y="60" width="90" height="260"/><rect x="290" y="150" width="140" height="170"/><rect x="760" y="90" width="110" height="230"/><rect x="890" y="140" width="150" height="180"/><rect x="1060" y="70" width="100" height="250"/></g>
<g fill="#f6d365" opacity=".8"><rect x="60" y="150" width="14" height="18"/><rect x="100" y="190" width="14" height="18"/><rect x="200" y="90" width="12" height="16"/><rect x="310" y="180" width="14" height="18"/><rect x="790" y="120" width="12" height="16"/><rect x="930" y="170" width="14" height="18"/><rect x="1080" y="110" width="12" height="16"/></g>
<rect x="0" y="300" width="1200" height="20" fill="#16202a"/><rect x="560" y="140" width="10" height="160" fill="#111"/><path d="M540 140 h50 l-8 20 h-34z" fill="#ffe08a"/><path d="M548 160 L500 300 H640 L592 160Z" fill="#ffe08a" opacity=".15"/>
<g stroke="#9fb3c8" stroke-width="2" opacity=".5"><path d="M100 0 l-10 30"/><path d="M300 20 l-10 30"/><path d="M500 0 l-10 30"/><path d="M700 30 l-10 30"/><path d="M900 10 l-10 30"/><path d="M1100 0 l-10 30"/><path d="M200 60 l-10 30"/><path d="M1000 70 l-10 30"/></g></svg>""",
"Lost on a rainy night", "The streets are wet and this page is nowhere to be found. Come back inside, where it is warm.", "#f6d365", "#1e2b38", "Find shelter")
add(C, "rainy-city", "Rainy City", "Streetlight", "A city skyline at night in the rain, with one street lamp glowing.", css, body, fonts=["Poppins:wght@400;700"], theme="#f6d365")

css, body = scene("linear-gradient(#dbeafe,#f8fafc)", "#1e3a5f", "Mulish",
"""<svg viewBox="0 0 1200 340" preserveAspectRatio="xMidYMax slice"><path d="M0 340 L200 120 L320 220 L520 40 L720 240 L860 140 L1200 340Z" fill="#94a3b8"/><path d="M520 40 L470 95 L500 90 L520 110 L545 88 L575 100Z" fill="#fff"/><path d="M200 120 L170 155 L210 150 L230 140Z" fill="#fff"/><path d="M860 140 L830 175 L870 170 L890 160Z" fill="#fff"/>
<path d="M0 340 L300 230 L600 300 L900 220 L1200 300 V340Z" fill="#e2e8f0"/><g fill="#fff"><circle cx="100" cy="40" r="4"/><circle cx="300" cy="80" r="3"/><circle cx="700" cy="60" r="4"/><circle cx="950" cy="30" r="3"/><circle cx="1100" cy="100" r="4"/><circle cx="420" cy="20" r="3"/></g>
<g><rect x="1000" y="250" width="8" height="40" fill="#7c5c3c"/><path d="M1004 190 l-30 60 h60z" fill="#2f5d50"/></g></svg>""",
"Snowed under", "This page is buried somewhere under the snow. We will dig it out in spring. Until then, the home page is clear.", "#1e3a5f")
add(C, "snowy-mountains", "Snowy Mountains", "Alpine Trails", "Snow-capped mountains and snowflakes on a pale winter sky.", css, body, fonts=["Mulish:wght@400;800"], theme="#1e3a5f")

css, body = scene("linear-gradient(#ffd89b,#fcb69f)", "#5a2e0e", "Pacifico",
"""<svg viewBox="0 0 1200 300" preserveAspectRatio="xMidYMax slice"><circle cx="900" cy="140" r="90" fill="#fff3c4" opacity=".9"/><rect x="0" y="170" width="1200" height="60" fill="#4fb3bf"/><path d="M0 180 q60 -10 120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0" stroke="#fff" stroke-width="3" fill="none" opacity=".6"/>
<path d="M0 230 Q600 200 1200 230 V300 H0Z" fill="#f6d8a8"/><g><path d="M250 230 q5 -80 30 -130" stroke="#7a4a1c" stroke-width="10" fill="none"/><path d="M280 100 q-60 -10 -80 20 q40 -5 80 -20 q-20 -40 -70 -40 q40 15 70 40 q10 -45 60 -55 q-40 25 -60 55 q50 -15 80 10 q-50 -5 -80 -10" fill="#3f8f4a"/></g>
<text x="700" y="275" font-family="Arial" font-weight="700" font-size="34" fill="#c9985f" opacity=".7">404</text></svg>""",
"Gone to the beach", "This page is taking a long holiday. We wrote its number in the sand, but the waves are getting close.", "#5a2e0e", "#fff", "Back to the mainland")
add(C, "beach", "Beach", "Seashell Travel", "A sunset beach with a palm tree and '404' written in the sand.", css, body, fonts=["Pacifico"], theme="#fcb69f")
PAGES_EXTRA = True

css, body = scene("linear-gradient(#0f2027,#203a43,#2c5364)", "#e0f7fa", "Quicksand",
"""<svg viewBox="0 0 1200 320" preserveAspectRatio="xMidYMax slice"><g fill="#4dd0e1" opacity=".25"><circle cx="200" cy="80" r="6"/><circle cx="215" cy="50" r="4"/><circle cx="210" cy="25" r="3"/><circle cx="900" cy="120" r="5"/><circle cx="910" cy="90" r="3"/></g>
<path d="M0 260 q100 -40 200 0 t200 0 t200 0 t200 0 t200 0 t200 0 V320 H0Z" fill="#c2a878"/><g fill="#26a69a"><path d="M150 260 q-10 -60 10 -120 q10 60 -10 120"/><path d="M175 260 q10 -50 -5 -100 q-15 50 5 100"/><path d="M1000 260 q-15 -70 5 -140 q15 70 -5 140"/></g>
<g transform="translate(560 150)"><ellipse cx="0" cy="0" rx="60" ry="30" fill="#ffb74d"/><path d="M55 0 l35 -25 v50z" fill="#ffb74d"/><circle cx="-30" cy="-6" r="7" fill="#fff"/><circle cx="-30" cy="-6" r="3" fill="#263238"/><path d="M-10 -28 q10 -18 30 0" stroke="#f57c00" stroke-width="4" fill="none"/></g>
<text x="760" y="235" font-family="Arial" font-size="18" fill="#e0f7fa" opacity=".6">...404?</text></svg>""",
"Deep under the sea", "Our fish searched the whole ocean floor. The page you want is not down here.", "#4dd0e1", "#0f2027", "Swim back up")
add(C, "under-the-sea", "Under the Sea", "Reef Aquarium", "An underwater scene with seaweed, bubbles and a puzzled orange fish.", css, body, fonts=["Quicksand:wght@400;700"], theme="#4dd0e1")

css, body = scene("#e9f5db", "#2d3a1f", "Amatic SC",
"""<svg viewBox="0 0 1200 320" preserveAspectRatio="xMidYMax slice"><g fill="#90a955"><path d="M80 320 L150 120 L220 320Z"/><path d="M1000 320 L1070 100 L1140 320Z"/></g><g fill="#4f772d"><path d="M180 320 L260 90 L340 320Z"/><path d="M880 320 L960 130 L1040 320Z"/><path d="M340 320 L400 170 L460 320Z"/></g>
<rect x="0" y="290" width="1200" height="30" fill="#6b8e4e"/><path d="M560 320 C 590 250, 620 250, 640 200 S 700 150, 720 120" stroke="#d9c7a5" stroke-width="26" fill="none"/>
<g transform="translate(760 220)"><rect x="-4" y="0" width="8" height="70" fill="#7f5539"/><rect x="-60" y="-20" width="120" height="34" rx="4" fill="#b08968"/><text x="0" y="4" font-family="Arial" font-weight="700" font-size="18" text-anchor="middle" fill="#fff">404 this way?</text></g></svg>""",
"Lost in the woods", "The trail ends here, and the page you wanted is not at the end of it. Follow the path back to the start.", "#4f772d", "#fff", "Follow the trail home")
add(C, "forest-trail", "Forest Trail", "Pinewood Camp", "A forest with a winding path and a confused wooden signpost.", css, body, fonts=["Amatic SC:wght@700"], theme="#4f772d")

css, body = scene("linear-gradient(#fceabb,#f8b500)", "#4a2c05", "Bitter",
"""<svg viewBox="0 0 1200 300" preserveAspectRatio="xMidYMax slice"><circle cx="950" cy="80" r="60" fill="#fff5d6"/><path d="M0 230 Q300 170 600 220 T1200 210 V300 H0Z" fill="#e8a33d"/><path d="M0 260 Q400 220 800 260 T1200 250 V300 H0Z" fill="#d4892a"/>
<g transform="translate(300 150)"><rect x="-6" y="0" width="12" height="90" fill="#2e7d32"/><path d="M-6 30 q-30 -10 -40 10 q20 5 40 -10z M6 50 q30 -10 40 10 q-20 5 -40 -10z" fill="#2e7d32"/></g><g transform="translate(700 170)"><rect x="-5" y="0" width="10" height="70" fill="#2e7d32"/></g>
<g fill="#7a4d10" opacity=".4"><path d="M100 150 q20 -8 40 0"/><path d="M1080 170 q15 -6 30 0"/></g><path d="M480 250 q40 -30 90 -10" stroke="#8d6e63" stroke-width="3" fill="none" opacity=".6"/></svg>""",
"Nothing out here but sand", "We crossed the whole desert looking for this page. All we found was a cactus and a lot of sun.", "#4a2c05", "#fff", "Head back to town")
add(C, "desert", "Desert", "Dunes Expeditions", "Golden sand dunes, a big sun and a lonely cactus.", css, body, fonts=["Bitter:wght@400;700"], theme="#f8b500")

css, body = scene("#1b1433", "#f3e8ff", "Creepster",
"""<svg viewBox="0 0 1200 320" preserveAspectRatio="xMidYMax slice"><circle cx="950" cy="90" r="60" fill="#f5e6a8"/><path d="M0 320 V260 Q300 230 600 260 T1200 250 V320Z" fill="#2a1f4a"/>
<g transform="translate(540 190)"><path d="M0 0 C -45 0 -55 40 -55 60 C -55 95 -25 105 0 105 C 25 105 55 95 55 60 C 55 40 45 0 0 0Z" fill="#f97316"/><rect x="-5" y="-14" width="10" height="16" fill="#65a30d"/><path d="M-30 40 l10 -12 l10 12z M10 40 l10 -12 l10 12z" fill="#1b1433"/><path d="M-30 70 q30 20 60 0 l-8 8 l-8 -6 l-8 8 l-8 -8 l-8 6z" fill="#1b1433"/></g>
<g stroke="#3b2d63" stroke-width="6" fill="none"><path d="M150 320 V190 M150 220 l-40 -30 M150 240 l40 -35"/><path d="M1050 320 V200 M1050 230 l35 -30"/></g><g fill="#f3e8ff" opacity=".8"><path d="M300 100 q10 -10 20 0 q10 -10 20 0 q-10 -4 -20 6 q-10 -10 -20 -6z"/><path d="M800 60 q8 -8 16 0 q8 -8 16 0 q-8 -3 -16 5 q-8 -8 -16 -5z"/></g></svg>""",
"This page is a ghost", "Something spooky happened to it. We would not go looking for it after dark.", "#f97316", "#1b1433", "Run home")
add(C, "halloween", "Halloween", "Hollow Lane", "A spooky night with a grinning pumpkin, bare trees and bats. Great for October.", css, body, fonts=["Creepster"], theme="#f97316")

css, body = scene("linear-gradient(#fff1e6,#fde2e4)", "#6d2e46", "Caveat",
"""<svg viewBox="0 0 1200 300" preserveAspectRatio="xMidYMax slice"><rect x="0" y="250" width="1200" height="50" fill="#a26769"/><g transform="translate(250 130)"><rect x="-8" y="0" width="16" height="120" fill="#6d4c41"/><circle cx="0" cy="-10" r="70" fill="#e76f51"/><circle cx="-45" cy="10" r="45" fill="#f4a261"/><circle cx="45" cy="15" r="45" fill="#e9c46a"/></g>
<g transform="translate(900 150)"><rect x="-7" y="0" width="14" height="100" fill="#6d4c41"/><circle cx="0" cy="-5" r="55" fill="#f4a261"/><circle cx="35" cy="15" r="35" fill="#e76f51"/></g>
<g fill="#e76f51"><path d="M500 40 q10 -10 20 0 q-10 20 -10 30 q0 -10 -10 -30z" transform="rotate(20 510 50)"/><path d="M650 100 q10 -10 20 0 q-10 20 -10 30 q0 -10 -10 -30z" transform="rotate(-30 660 110)"/></g><g fill="#e9c46a"><path d="M580 180 q10 -10 20 0 q-10 20 -10 30 q0 -10 -10 -30z" transform="rotate(45 590 190)"/><path d="M400 220 q10 -10 20 0 q-10 20 -10 30 q0 -10 -10 -30z"/></g></svg>""",
"This page fell with the leaves", "Autumn swept it away. We are raking the whole site, but it has not turned up yet.", "#6d2e46", "#fff", "Walk back home")
add(C, "autumn-leaves", "Autumn Leaves", "Maple Row Cafe", "Warm autumn trees in orange and gold, with loose leaves in the air.", css, body, fonts=["Caveat:wght@700"], theme="#e76f51")

css, body = scene("linear-gradient(#a1c4fd,#c2e9fb)", "#123047", "Kalam",
"""<svg viewBox="0 0 1200 300" preserveAspectRatio="xMidYMax slice"><g fill="#fff"><ellipse cx="200" cy="80" rx="70" ry="25"/><ellipse cx="240" cy="65" rx="45" ry="25"/><ellipse cx="900" cy="60" rx="80" ry="26"/><ellipse cx="950" cy="45" rx="45" ry="24"/></g>
<path d="M0 240 Q300 190 600 230 T1200 220 V300 H0Z" fill="#7cc576"/><path d="M0 270 Q400 240 800 270 T1200 260 V300 H0Z" fill="#5aa65a"/>
<g transform="translate(600 120)"><path d="M0 0 L-40 -30 L-60 10 Z" fill="#ef476f"/><path d="M0 0 L40 -30 L60 10 Z" fill="#ffd166"/><path d="M0 0 L-35 30 L-10 40Z" fill="#06d6a0"/><path d="M0 0 L35 30 L10 40Z" fill="#118ab2"/><circle cx="0" cy="0" r="6" fill="#123047"/><path d="M0 6 C 20 60, -20 100, 10 150" stroke="#123047" stroke-width="2" fill="none"/></g></svg>""",
"This page flew away", "It caught the wind like a kite and is now somewhere above the clouds. Grab the string on the home page.", "#118ab2")
add(C, "kite-meadow", "Kite Meadow", "Breezy Days", "A bright spring meadow with a colorful kite flying off with the page.", css, body, fonts=["Kalam:wght@700"], theme="#118ab2")

css, body = scene("linear-gradient(#141e30,#243b55)", "#e2e8f0", "Righteous",
"""<svg viewBox="0 0 1200 320" preserveAspectRatio="xMidYMax slice"><g fill="#fff"><circle cx="100" cy="40" r="2"/><circle cx="400" cy="90" r="2"/><circle cx="600" cy="30" r="3"/><circle cx="820" cy="70" r="2"/><circle cx="1100" cy="50" r="2"/></g>
<path d="M0 320 V240 H80 V180 H140 V220 H220 V150 H300 V240 H380 V200 H460 V260 H540 V170 H620 V230 H700 V190 H780 V250 H860 V160 H940 V220 H1020 V200 H1100 V240 H1200 V320Z" fill="#0b1220"/>
<g fill="#fcd34d"><rect x="95" y="195" width="10" height="10"/><rect x="240" y="170" width="10" height="10"/><rect x="560" y="190" width="10" height="10"/><rect x="880" y="180" width="10" height="10"/><rect x="600" y="210" width="10" height="10"/></g>
<g transform="translate(700 90)"><circle r="40" fill="#fde68a"/><circle cx="14" cy="-8" r="36" fill="#1c2c45"/></g><path d="M200 60 l60 30" stroke="#fff" stroke-width="2" opacity=".6"/></svg>""",
"The city is asleep", "Everyone went home for the night, including this page. Try again from the home page.", "#fcd34d", "#0b1220", "Go home")
add(C, "city-night", "City at Night", "Nightline Transit", "A quiet city skyline at night with a crescent moon and lit windows.", css, body, fonts=["Righteous"], theme="#fcd34d")
