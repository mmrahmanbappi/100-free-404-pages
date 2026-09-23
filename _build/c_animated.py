from core import add

C = "animated"

add(C, "glitch", "Glitch", "Static", "A glitching 404 with red and cyan color shifts on a black screen.",
"""body{display:grid;place-items:center;background:#0a0a0a;color:#fff;font-family:"Space Mono",monospace;text-align:center;padding:2rem}
.g{position:relative;font-size:clamp(6rem,22vw,13rem);font-weight:700;line-height:1}
.g::before,.g::after{content:"404";position:absolute;inset:0}
.g::before{color:#ff2a6d;animation:g1 2.4s infinite steps(1)}
.g::after{color:#05d9e8;animation:g2 2.4s infinite steps(1)}
@keyframes g1{0%,100%{clip-path:inset(0 0 80% 0);transform:translate(-4px,0)}20%{clip-path:inset(40% 0 30% 0);transform:translate(4px,0)}40%{clip-path:inset(70% 0 5% 0);transform:translate(-2px,0)}60%{clip-path:inset(10% 0 60% 0);transform:translate(3px,0)}80%{clip-path:inset(0 0 0 0);transform:none;opacity:0}}
@keyframes g2{0%,100%{clip-path:inset(60% 0 10% 0);transform:translate(4px,0)}25%{clip-path:inset(20% 0 55% 0);transform:translate(-4px,0)}50%{clip-path:inset(80% 0 0 0);transform:translate(2px,0)}75%{clip-path:inset(0 0 0 0);opacity:0}}
p{color:#9a9a9a;margin:1.5rem 0 2rem}
a{color:#05d9e8}""",
"""<main><h1 class="g" aria-label="Error 404">404</h1><p>Signal lost. The page you requested could not be found.</p><a href="/">Restore signal</a></main>""",
fonts=["Space Mono:wght@400;700"], theme="#ff2a6d")

add(C, "floating-numbers", "Floating Numbers", "Drift", "Each digit of 404 floats up and down on its own, like it is underwater.",
"""body{display:grid;place-items:center;background:linear-gradient(180deg,#a1c4fd,#c2e9fb);color:#123;font-family:Fredoka,system-ui,sans-serif;text-align:center;padding:2rem}
.d{display:flex;gap:.2em;justify-content:center;font-size:clamp(6rem,20vw,12rem);font-weight:700;color:#fff;text-shadow:0 12px 30px rgba(18,51,85,.25)}
.d span{animation:f 3s ease-in-out infinite}
.d span:nth-child(2){animation-delay:.4s}.d span:nth-child(3){animation-delay:.8s}
@keyframes f{0%,100%{transform:translateY(0)}50%{transform:translateY(-22px)}}
h1{font-size:1.8rem;margin:1rem 0 .5rem}p{margin:0 0 1.8rem;opacity:.8}
a{background:#123;color:#fff;padding:.8rem 1.4rem;border-radius:999px;text-decoration:none;font-weight:600}""",
"""<main><div class="d" aria-hidden="true"><span>4</span><span>0</span><span>4</span></div><h1>This page drifted away</h1><p>We cannot find what you are looking for.</p><a href="/">Swim back home</a></main>""",
fonts=["Fredoka:wght@400;700"], theme="#123355")

add(C, "typewriter", "Typewriter", "Inkwell", "The message types itself out letter by letter, with a blinking cursor.",
"""body{display:grid;place-items:center;background:#f5f0e6;color:#2b2622;font-family:"Courier Prime",monospace;padding:2rem}
main{max-width:40rem}
.t{font-size:clamp(1.4rem,4vw,2.2rem);overflow:hidden;white-space:nowrap;border-right:3px solid #2b2622;width:0;animation:type 3s steps(30) .5s forwards,blink .8s step-end infinite}
@keyframes type{to{width:30ch}}@keyframes blink{50%{border-color:transparent}}
h1{font-size:1rem;letter-spacing:.2em;color:#8c7b6b;margin:0 0 1rem}
p{margin:2rem 0;line-height:1.6;opacity:0;animation:show .6s 3.6s forwards}@keyframes show{to{opacity:1}}
a{color:#b23a3a;font-weight:700}""",
"""<main><h1>ERROR 404</h1><div class="t">Dear reader, this page is gone.</div><p>We looked in every drawer and every folder. It is not here. Perhaps the home page has what you need.<br><br><a href="/">Return to the home page</a></p></main>""",
fonts=["Courier Prime:wght@400;700"], theme="#b23a3a")

add(C, "pulse-radar", "Radar", "Scout", "A radar sweeps the screen looking for the page, and finds nothing.",
"""body{display:grid;place-items:center;background:#06140f;color:#b7f7d2;font-family:"Chakra Petch",system-ui,sans-serif;text-align:center;padding:2rem}
.r{position:relative;width:min(70vw,280px);aspect-ratio:1;border-radius:50%;border:2px solid #1f6b4a;margin:0 auto 2rem;background:radial-gradient(circle,transparent 30%,rgba(31,107,74,.25) 31%,transparent 32%,transparent 60%,rgba(31,107,74,.25) 61%,transparent 62%)}
.r::before{content:"";position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 0deg,rgba(52,211,153,.55),transparent 25%);animation:spin 3s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.r::after{content:"";position:absolute;left:50%;top:50%;width:10px;height:10px;margin:-5px;border-radius:50%;background:#34d399}
h1{font-size:2rem;margin:0 0 .6rem}p{opacity:.75;margin:0 0 1.6rem}a{color:#34d399;font-weight:600}""",
"""<main><div class="r" aria-hidden="true"></div><h1>404: no signal found</h1><p>We scanned the whole area. This page is not in range.</p><a href="/">Return to home base</a></main>""",
fonts=["Chakra Petch:wght@400;600"], theme="#34d399")

add(C, "bouncing-ball", "Bouncing Ball", "Hopscotch", "The zero in 404 is a ball that keeps bouncing between the fours.",
"""body{display:grid;place-items:center;background:#fff4e6;color:#3d2c1e;font-family:"Baloo 2",system-ui,sans-serif;text-align:center;padding:2rem}
.n{display:flex;align-items:flex-end;justify-content:center;gap:1rem;font-size:clamp(6rem,20vw,11rem);font-weight:800;color:#ff6b35;height:1.2em}
.ball{width:.7em;height:.7em;border-radius:50%;background:#ffb627;animation:bounce 1s cubic-bezier(.3,0,.6,1) infinite alternate;margin-bottom:.12em}
@keyframes bounce{from{transform:translateY(-.6em)}to{transform:translateY(0) scaleY(.88)}}
h1{font-size:1.8rem;margin:1.2rem 0 .5rem}p{margin:0 0 1.8rem;opacity:.8}
a{background:#ff6b35;color:#fff;padding:.8rem 1.5rem;border-radius:14px;text-decoration:none;font-weight:700}""",
"""<main><div class="n" aria-hidden="true"><span>4</span><span class="ball"></span><span>4</span></div><h1>This page bounced</h1><p>It jumped off the site and did not come back.</p><a href="/">Go to the home page</a></main>""",
fonts=["Baloo 2:wght@400;800"], theme="#ff6b35")

add(C, "waves", "Waves", "Tidewater", "Animated ocean waves roll along the bottom of the page.",
"""body{display:grid;place-items:center;background:#e6f4f1;color:#0b3c49;font-family:Lexend,system-ui,sans-serif;text-align:center;padding:2rem 2rem 10rem;overflow-x:hidden}
.w{position:fixed;left:0;right:0;bottom:0;height:160px}
.w svg{position:absolute;bottom:0;width:200%;height:100%;animation:wave 8s linear infinite}
.w svg:nth-child(2){animation-duration:13s;opacity:.6}
@keyframes wave{to{transform:translateX(-50%)}}
b{font-size:clamp(5rem,16vw,9rem);color:#0b7a75;line-height:1}
h1{font-size:1.8rem;margin:1rem 0 .5rem}p{margin:0 0 1.8rem}
a{background:#0b3c49;color:#fff;padding:.8rem 1.4rem;border-radius:10px;text-decoration:none;font-weight:600}""",
"""<main><b aria-hidden="true">404</b><h1>Lost at sea</h1><p>The tide carried this page away. Let us get you back to shore.</p><a href="/">Head back to shore</a></main>
<div class="w" aria-hidden="true"><svg viewBox="0 0 1200 160" preserveAspectRatio="none"><path d="M0 80 Q150 30 300 80 T600 80 T900 80 T1200 80 V160 H0Z" fill="#0b7a75"/></svg><svg viewBox="0 0 1200 160" preserveAspectRatio="none"><path d="M0 100 Q150 60 300 100 T600 100 T900 100 T1200 100 V160 H0Z" fill="#14a7a0"/></svg></div>""",
fonts=["Lexend:wght@400;700"], theme="#0b7a75")

add(C, "flicker-sign", "Flicker Sign", "Nightowl Diner", "A neon sign that flickers on and off, like a diner at midnight.",
"""body{display:grid;place-items:center;background:#120b1e;color:#fff;font-family:Monoton,cursive;text-align:center;padding:2rem}
.s{font-size:clamp(4rem,16vw,9rem);color:#ff4fd8;text-shadow:0 0 8px #ff4fd8,0 0 24px #ff4fd8,0 0 60px #b3009b;animation:fl 4s infinite}
@keyframes fl{0%,18%,22%,25%,53%,57%,100%{opacity:1}20%,24%,55%{opacity:.25}}
p{font-family:system-ui,sans-serif;color:#cdbfe0;margin:1.5rem 0 2rem;font-size:1.1rem}
a{font-family:system-ui,sans-serif;color:#62f3ff;text-shadow:0 0 10px #62f3ff;font-weight:700}""",
"""<main><h1 class="s" aria-label="Error 404">404</h1><p>We are closed at this address. The kitchen is open on the home page.</p><a href="/">Go to the home page</a></main>""",
fonts=["Monoton"], theme="#ff4fd8")

add(C, "rotating-planet", "Planet", "Orbital", "A ringed planet slowly turns while a small moon circles around it.",
"""body{display:grid;place-items:center;background:radial-gradient(circle at 30% 20%,#2a1b5e,#0b0820 70%);color:#ecebff;font-family:"Exo 2",system-ui,sans-serif;text-align:center;padding:2rem}
.sys{position:relative;width:220px;height:220px;margin:0 auto 1.5rem}
.planet{position:absolute;inset:50px;border-radius:50%;background:linear-gradient(135deg,#ffb86b,#ff5e7e)}
.ring{position:absolute;left:0;right:0;top:95px;height:30px;border:6px solid rgba(255,214,165,.8);border-radius:50%;transform:rotate(-15deg)}
.orbit{position:absolute;inset:0;animation:o 6s linear infinite}
.orbit::after{content:"";position:absolute;top:0;left:50%;width:18px;height:18px;margin-left:-9px;border-radius:50%;background:#c7d2fe}
@keyframes o{to{transform:rotate(360deg)}}
h1{font-size:2rem;margin:0 0 .5rem}p{opacity:.8;margin:0 0 1.8rem}
a{border:2px solid #ffb86b;color:#ffb86b;padding:.75rem 1.3rem;border-radius:999px;text-decoration:none;font-weight:700}""",
"""<main><div class="sys" aria-hidden="true"><div class="planet"></div><div class="ring"></div><div class="orbit"></div></div><h1>404: planet not found</h1><p>This page is outside our solar system.</p><a href="/">Fly home</a></main>""",
fonts=["Exo 2:wght@400;700"], theme="#ff5e7e")

add(C, "loading-bar", "Endless Loading", "Loopline", "A loading bar that fills up and then gives up, over and over.",
"""body{display:grid;place-items:center;background:#fafafa;color:#1c1c1c;font-family:"Plus Jakarta Sans",system-ui,sans-serif;text-align:center;padding:2rem}
main{width:min(90vw,440px)}
.bar{height:14px;background:#e6e6e6;border-radius:99px;overflow:hidden;margin:2rem 0 .6rem}
.bar i{display:block;height:100%;background:#7c3aed;border-radius:99px;animation:load 3.5s ease-in-out infinite}
@keyframes load{0%{width:0}70%{width:99%}80%{width:99%}100%{width:0}}
small{color:#888}
h1{font-size:2rem;margin:0}p{color:#555;margin:1.5rem 0}
a{color:#7c3aed;font-weight:700}""",
"""<main><h1>Loading page 404...</h1><div class="bar" aria-hidden="true"><i></i></div><small>99 percent, then nothing. It is not coming.</small><p>This page does not exist, so it will never finish loading.</p><a href="/">Go somewhere that loads</a></main>""",
fonts=["Plus Jakarta Sans:wght@400;700"], theme="#7c3aed")

add(C, "falling-letters", "Falling Letters", "Tumble", "The words 'page not found' fall down one letter at a time and land in a pile.",
"""body{display:grid;place-items:center;background:#1d3557;color:#f1faee;font-family:"Rubik",system-ui,sans-serif;text-align:center;padding:2rem}
.f{font-size:clamp(2rem,7vw,4rem);font-weight:800}
.f span{display:inline-block;animation:fall 1s cubic-bezier(.5,0,.7,1.4) both}
@keyframes fall{from{transform:translateY(-80vh) rotate(-30deg);opacity:0}to{transform:none;opacity:1}}
b{display:block;font-size:1rem;color:#a8dadc;letter-spacing:.2em;margin-bottom:1rem}
p{color:#a8dadc;margin:2rem 0}a{background:#e63946;color:#fff;padding:.8rem 1.4rem;border-radius:8px;text-decoration:none;font-weight:700}""",
"""<main><b>404</b><h1 class="f" aria-label="Page not found"><span style="animation-delay:.05s">P</span><span style="animation-delay:.1s">a</span><span style="animation-delay:.15s">g</span><span style="animation-delay:.2s">e</span> <span style="animation-delay:.3s">n</span><span style="animation-delay:.35s">o</span><span style="animation-delay:.4s">t</span> <span style="animation-delay:.5s">f</span><span style="animation-delay:.55s">o</span><span style="animation-delay:.6s">u</span><span style="animation-delay:.65s">n</span><span style="animation-delay:.7s">d</span></h1><p>It all came crashing down. Let us build it back up from the start.</p><a href="/">Start again</a></main>""",
fonts=["Rubik:wght@400;800"], theme="#e63946")
