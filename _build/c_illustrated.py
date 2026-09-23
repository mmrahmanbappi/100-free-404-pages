from core import add

C = "illustrated"

def wrap(bg, fg, accent, font, art, title, text, link="Take me home"):
    css = f"""body{{display:grid;place-items:center;background:{bg};color:{fg};font-family:"{font}",system-ui,sans-serif;padding:1.5rem;text-align:center}}
main{{max-width:34rem}}
.art{{width:min(88vw,360px);margin:0 auto 1.5rem}}
h1{{font-size:clamp(1.8rem,5vw,2.4rem);margin:0 0 .7rem}}
p{{font-size:1.1rem;line-height:1.6;opacity:.85;margin:0 0 1.8rem}}
a.b{{display:inline-block;background:{accent};color:#fff;padding:.85rem 1.5rem;border-radius:12px;font-weight:700;text-decoration:none}}"""
    body = f"""<main><div class="art" aria-hidden="true">{art}</div><h1>{title}</h1><p>{text}</p><a class="b" href="/">{link}</a></main>"""
    return css, body

css, body = wrap("#0f1b3d", "#fff", "#ff7a59", "Poppins",
"""<svg viewBox="0 0 300 240"><circle cx="150" cy="120" r="100" fill="#1b2b5a"/>
<g fill="#fff" opacity=".7"><circle cx="40" cy="30" r="2"/><circle cx="260" cy="50" r="2.5"/><circle cx="230" cy="200" r="2"/><circle cx="60" cy="190" r="1.5"/><circle cx="280" cy="140" r="1.5"/></g>
<g transform="rotate(-12 150 120)"><rect x="125" y="95" width="50" height="62" rx="18" fill="#e9edf7"/><circle cx="150" cy="85" r="28" fill="#e9edf7"/><rect x="134" y="72" width="32" height="24" rx="10" fill="#27407d"/><rect x="104" y="104" width="22" height="12" rx="6" fill="#e9edf7"/><rect x="174" y="104" width="22" height="12" rx="6" fill="#e9edf7"/><rect x="132" y="154" width="12" height="22" rx="6" fill="#e9edf7"/><rect x="156" y="154" width="12" height="22" rx="6" fill="#e9edf7"/><rect x="140" y="110" width="20" height="14" rx="3" fill="#ff7a59"/></g>
<path d="M200 60 q30 -10 50 10" stroke="#ff7a59" stroke-width="3" fill="none" stroke-dasharray="4 6"/></svg>""",
"Houston, this page is missing", "Our astronaut searched the whole galaxy and could not find it. Let us get you back to solid ground.", "Return to base")
add(C, "astronaut", "Astronaut", "Starlane", "An astronaut floating in space, drawn in SVG, on a deep blue background.", css, body, fonts=["Poppins:wght@400;700"], theme="#0f1b3d")

css, body = wrap("#fff7ed", "#43302b", "#e76f51", "Fredoka",
"""<svg viewBox="0 0 300 220"><ellipse cx="150" cy="200" rx="110" ry="10" fill="#f3dfc8"/>
<path d="M95 60 h60 v70 q0 40 -40 40 h-10 q-25 0 -25 -25 q0 -25 25 -25 h10 z" fill="#2a9d8f"/><rect x="95" y="60" width="60" height="16" fill="#e9c46a"/><rect x="95" y="84" width="60" height="6" fill="#fff" opacity=".6"/>
<text x="200" y="100" font-family="Arial" font-weight="700" font-size="48" fill="#e76f51">?</text><circle cx="215" cy="150" r="3" fill="#e76f51"/><circle cx="230" cy="135" r="2" fill="#e76f51"/></svg>""",
"We lost a sock, and this page", "Some things just disappear. This page is one of them. The rest of the site is still right where you left it.")
add(C, "lost-sock", "Lost Sock", "Snug", "A single lonely sock and a question mark, in warm cheerful colors.", css, body, fonts=["Fredoka:wght@400;600"], theme="#e76f51")

css, body = wrap("#f0f4f8", "#1f2937", "#6366f1", "Outfit",
"""<svg viewBox="0 0 300 200"><path d="M20 120 H110" stroke="#9ca3af" stroke-width="8" stroke-linecap="round"/><rect x="100" y="100" width="40" height="40" rx="6" fill="#6366f1"/><rect x="138" y="108" width="14" height="6" rx="2" fill="#4b5563"/><rect x="138" y="126" width="14" height="6" rx="2" fill="#4b5563"/>
<rect x="180" y="100" width="40" height="40" rx="6" fill="#a5b4fc"/><rect x="168" y="112" width="14" height="16" rx="3" fill="#a5b4fc"/><circle cx="192" cy="113" r="3" fill="#1f2937"/><circle cx="192" cy="127" r="3" fill="#1f2937"/><path d="M220 120 H285" stroke="#9ca3af" stroke-width="8" stroke-linecap="round"/>
<g stroke="#f59e0b" stroke-width="3" stroke-linecap="round"><path d="M158 80 l4 12"/><path d="M170 76 l-2 13"/><path d="M148 90 l8 7"/></g></svg>""",
"Looks like we got unplugged", "The page you wanted is disconnected. Plug back in from the home page and everything should work again.", "Reconnect")
add(C, "unplugged", "Unplugged", "Voltline", "A cable and plug pulled apart, with little sparks. Great for tech and service sites.", css, body, fonts=["Outfit:wght@400;700"], theme="#6366f1")

css, body = wrap("#fdf6e3", "#3d3325", "#b5651d", "Merriweather Sans",
"""<svg viewBox="0 0 300 220"><path d="M40 60 L110 40 L190 60 L260 40 V170 L190 190 L110 170 L40 190 Z" fill="#f4e4c1" stroke="#b5651d" stroke-width="3"/><path d="M110 40 V170 M190 60 V190" stroke="#b5651d" stroke-width="2" stroke-dasharray="6 5"/>
<path d="M70 150 C 100 120, 120 150, 150 110 S 200 80, 220 100" stroke="#b5651d" stroke-width="3" fill="none" stroke-dasharray="6 6"/><g stroke="#c0392b" stroke-width="5" stroke-linecap="round"><path d="M212 92 l16 16 M228 92 l-16 16"/></g></svg>""",
"X marks the wrong spot", "We followed the map, but the page is not buried here. Try the home page, where all the paths begin.", "Back to the start")
add(C, "treasure-map", "Treasure Map", "Wayfinder", "An old treasure map with a dotted path that ends at a red X.", css, body, fonts=["Merriweather Sans:wght@400;700"], theme="#b5651d")

css, body = wrap("#e0f2fe", "#0c4a6e", "#0284c7", "Baloo 2",
"""<svg viewBox="0 0 300 220"><ellipse cx="150" cy="190" rx="70" ry="10" fill="#bae6fd"/><path d="M110 150 q40 -60 80 0" fill="none"/>
<ellipse cx="150" cy="80" rx="55" ry="18" fill="#94a3b8"/><path d="M110 80 a40 30 0 0 1 80 0" fill="#bfdbfe" stroke="#64748b" stroke-width="3"/><ellipse cx="150" cy="84" rx="55" ry="10" fill="#64748b"/>
<g fill="#fde68a"><circle cx="115" cy="86" r="4"/><circle cx="135" cy="89" r="4"/><circle cx="165" cy="89" r="4"/><circle cx="185" cy="86" r="4"/></g><path d="M125 95 L105 180 H195 L175 95 Z" fill="#fef9c3" opacity=".7"/><text x="150" y="160" font-family="Arial" font-weight="700" font-size="24" text-anchor="middle" fill="#0c4a6e">404</text></svg>""",
"Abducted by aliens", "A flying saucer beamed this page up and flew away. We are negotiating its return. Meanwhile, the home page is safe.")
add(C, "ufo", "UFO", "Skyward", "A flying saucer beaming up the number 404, on a soft sky blue.", css, body, fonts=["Baloo 2:wght@400;700"], theme="#0284c7")

css, body = wrap("#1e3a2f", "#f1f5f0", "#e9b949", "Lexend",
"""<svg viewBox="0 0 300 220"><rect x="0" y="140" width="300" height="80" fill="#2f5d4b"/><path d="M0 150 q30 -8 60 0 t60 0 t60 0 t60 0 t60 0" stroke="#7fb8a4" stroke-width="3" fill="none"/>
<path d="M60 140 L60 60 Q60 40 90 30" stroke="#caa472" stroke-width="5" fill="none"/><path d="M90 30 Q200 20 210 170" stroke="#e5e7eb" stroke-width="1.5" fill="none"/><circle cx="210" cy="172" r="5" fill="#e9b949"/>
<rect x="30" y="120" width="60" height="22" rx="8" fill="#8b5e34"/><g fill="#7fb8a4"><path d="M240 190 q10 -8 20 0 q-10 8 -20 0z"/></g></svg>""",
"Nothing is biting here", "We cast our line all day, but this page never showed up. The home page usually has a better catch.")
add(C, "fishing", "Fishing", "Riverbend", "Someone fishing on a quiet lake, with no page on the hook.", css, body, fonts=["Lexend:wght@400;700"], theme="#e9b949")

css, body = wrap("#fef2f2", "#450a0a", "#dc2626", "Rubik",
"""<svg viewBox="0 0 300 230"><path d="M150 40 C 200 40, 230 80, 225 120 C 220 160, 180 170, 150 200 C 120 170, 80 160, 75 120 C 70 80, 100 40, 150 40 Z" fill="#fca5a5"/><path d="M150 200 l-4 25 M150 200 l4 25" stroke="#7f1d1d" stroke-width="2"/>
<path d="M150 70 q30 5 40 40" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round" opacity=".6"/><text x="150" y="140" font-family="Arial" font-weight="800" font-size="40" text-anchor="middle" fill="#7f1d1d">404</text></svg>""",
"This page floated away", "Someone let go of the string. The balloon, and the page inside it, are somewhere over the rooftops now.")
add(C, "balloon", "Balloon", "Joyful Events", "A red balloon with 404 written on it, drifting upward.", css, body, fonts=["Rubik:wght@400;700"], theme="#dc2626")

css, body = wrap("#faf5ff", "#3b0764", "#9333ea", "Quicksand",
"""<svg viewBox="0 0 300 220"><rect x="70" y="80" width="160" height="110" rx="6" fill="#d8b4fe"/><path d="M70 80 L110 50 H270 L230 80 Z" fill="#e9d5ff"/><path d="M230 80 L270 50 V160 L230 190 Z" fill="#c084fc"/>
<path d="M70 80 L40 110 H200 L230 80" fill="#f3e8ff" stroke="#9333ea" stroke-width="2"/><text x="150" y="150" font-family="Arial" font-weight="700" font-size="30" text-anchor="middle" fill="#3b0764" opacity=".5">empty</text></svg>""",
"The box is empty", "We opened the box where this page should be, and found nothing inside. It may have shipped to a new address.", "Browse the home page")
add(C, "empty-box", "Empty Box", "Parcelly", "An open cardboard box with nothing inside, in soft lavender.", css, body, fonts=["Quicksand:wght@400;700"], theme="#9333ea")

css, body = wrap("#0b132b", "#e0e7ff", "#5bc0be", "Nunito",
"""<svg viewBox="0 0 300 220"><g fill="#fff"><circle cx="60" cy="40" r="2"/><circle cx="250" cy="30" r="3"/><circle cx="200" cy="80" r="1.5"/><circle cx="30" cy="110" r="1.5"/><circle cx="275" cy="120" r="2"/></g><circle cx="230" cy="55" r="18" fill="#fde68a"/>
<g transform="rotate(-25 140 150)"><rect x="90" y="135" width="110" height="26" rx="8" fill="#5bc0be"/><rect x="195" y="130" width="18" height="36" rx="6" fill="#3a506b"/></g><path d="M150 165 l-25 45 M150 165 l25 45 M150 165 v45" stroke="#3a506b" stroke-width="5" stroke-linecap="round"/></svg>""",
"Not even the telescope can see it", "We pointed our telescope at every corner of the sky. No sign of this page. Maybe it was a shooting star.")
add(C, "telescope", "Telescope", "Stargazer Club", "A telescope pointed at a starry night sky and a pale yellow moon.", css, body, fonts=["Nunito:wght@400;800"], theme="#5bc0be")

css, body = wrap("#fffbeb", "#422006", "#d97706", "Chewy",
"""<svg viewBox="0 0 300 220"><ellipse cx="150" cy="195" rx="100" ry="10" fill="#fde68a"/><path d="M90 190 v-60 q0 -40 60 -40 q60 0 60 40 v60 z" fill="#92400e"/><path d="M100 190 v-55 q0 -32 50 -32 q50 0 50 32 v55" fill="#b45309"/>
<circle cx="130" cy="130" r="6" fill="#fff"/><circle cx="170" cy="130" r="6" fill="#fff"/><circle cx="131" cy="131" r="3" fill="#422006"/><circle cx="171" cy="131" r="3" fill="#422006"/><path d="M140 155 q10 -8 20 0" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M110 95 l-15 -25 l25 12 z M190 95 l15 -25 l-25 12 z" fill="#92400e"/></svg>""",
"Our cat hid this page", "We think it is under the sofa. While we look, you can find everything else from the home page.")
add(C, "hiding-cat", "Hiding Cat", "Whisker & Co.", "A sulky cartoon cat that clearly hid the page somewhere.", css, body, fonts=["Chewy"], theme="#d97706")
