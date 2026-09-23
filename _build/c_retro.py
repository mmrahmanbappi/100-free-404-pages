from core import add

C = "retro"

add(C, "eight-bit", "8-bit", "Pixel Quest", "A pixel-art game screen: 'Game over, page not found', press start to continue.",
"""body{display:grid;place-items:center;background:#212529;color:#fff;font-family:"Press Start 2P",monospace;text-align:center;padding:1.5rem}
.s{border:6px solid #fff;padding:2rem 1.5rem;max-width:34rem;box-shadow:0 0 0 6px #212529,0 0 0 12px #fff}
h1{font-size:clamp(1.2rem,4vw,2rem);color:#e63946;margin:0 0 1.5rem;line-height:1.4}
p{font-size:.7rem;line-height:2;color:#f1faee;margin:0 0 2rem}
a{font-size:.8rem;color:#ffd166;text-decoration:none;animation:bl 1s steps(1) infinite}@keyframes bl{50%{opacity:0}}
.h{display:flex;justify-content:center;gap:6px;margin-bottom:1.5rem}.h i{width:16px;height:14px;background:#e63946;clip-path:polygon(0 30%,25% 0,50% 25%,75% 0,100% 30%,50% 100%)}.h i.e{background:#555}""",
"""<main class="s"><div class="h" aria-hidden="true"><i></i><i class="e"></i><i class="e"></i></div><h1>GAME OVER</h1><p>PAGE 404 NOT FOUND.<br>THE PRINCESS IS IN ANOTHER CASTLE.</p><a href="/">PRESS START TO GO HOME</a></main>""",
fonts=["Press Start 2P"], theme="#e63946")

add(C, "windows-dialog", "Classic Dialog", "Retrosoft", "An old desktop error window with a grey title bar and an OK button.",
"""body{display:grid;place-items:center;background:#008080;font-family:"MS Sans Serif",Tahoma,Verdana,sans-serif;padding:1.5rem}
.w{background:#c0c0c0;border:2px solid;border-color:#fff #000 #000 #fff;box-shadow:inset -1px -1px #808080,inset 1px 1px #dfdfdf;width:min(94vw,420px)}
.t{background:linear-gradient(90deg,#000080,#1084d0);color:#fff;font-weight:700;padding:3px 6px;display:flex;justify-content:space-between;align-items:center;font-size:14px}
.t span{background:#c0c0c0;color:#000;width:18px;height:16px;text-align:center;line-height:14px;border:1px solid;border-color:#fff #000 #000 #fff;font-size:12px}
.b{display:flex;gap:14px;padding:18px 16px;font-size:14px;line-height:1.5}
.i{flex:none;width:34px;height:34px;border-radius:50%;background:#d00;color:#fff;font-weight:700;display:grid;place-items:center;font-size:20px}
.f{display:flex;justify-content:center;gap:10px;padding:0 0 16px}
.f a{min-width:80px;text-align:center;background:#c0c0c0;border:2px solid;border-color:#fff #000 #000 #fff;padding:4px 10px;color:#000;text-decoration:none;font-size:14px}
.f a:first-child{outline:1px dotted #000;outline-offset:-5px}""",
"""<main class="w" role="alertdialog" aria-labelledby="t"><div class="t"><h1 id="t" style="font-size:14px;margin:0">Error 404</h1><span aria-hidden="true">x</span></div><div class="b"><div class="i" aria-hidden="true">x</div><p style="margin:0">The page you requested could not be found.<br><br>It may have been moved, renamed, or deleted.</p></div><div class="f"><a href="/">OK</a><a href="/contact">Help</a></div></main>""",
theme="#000080")

add(C, "vhs-tape", "VHS Tape", "Rewind Video", "A VHS screen with 'PLAY' in the corner, scan lines and a tracking wobble.",
"""body{display:grid;place-items:center;background:#1b1b1b;color:#e8e8e8;font-family:"VT323",monospace;text-align:center;padding:2rem;overflow:hidden}
body::after{content:"";position:fixed;inset:0;background:repeating-linear-gradient(0deg,rgba(0,0,0,.35) 0 2px,transparent 2px 4px);pointer-events:none}
.osd{position:fixed;top:24px;left:30px;font-size:2rem;color:#fff}.osd2{position:fixed;bottom:24px;right:30px;font-size:1.6rem}
b{font-size:clamp(6rem,20vw,12rem);color:#fff;text-shadow:4px 0 #ff004d,-4px 0 #00e1ff;animation:wob 3s infinite}
@keyframes wob{0%,92%,100%{transform:none}94%{transform:translateX(8px) skewX(4deg)}96%{transform:translateX(-6px)}}
p{font-size:1.6rem;margin:.5rem 0 1.5rem}a{font-size:1.6rem;color:#00e1ff}""",
"""<div class="osd" aria-hidden="true">PLAY &#9654;</div><div class="osd2" aria-hidden="true">SP 0:04:04</div><main><b aria-hidden="true">404</b><h1 class="sr">Page not found</h1><p>TRACKING ERROR. THIS TAPE IS BLANK.</p><a href="/">REWIND TO HOME</a></main>""",
fonts=["VT323"], theme="#ff004d")

add(C, "newspaper", "Newspaper", "The Daily Link", "A front page with a big headline announcing the missing page.",
"""body{background:#f4efe3;color:#1a1a1a;font-family:"Old Standard TT",Georgia,serif;padding:clamp(1rem,4vw,3rem)}
main{max-width:52rem;margin:0 auto;border-top:4px double #1a1a1a;border-bottom:4px double #1a1a1a;padding:1rem 0}
.mast{text-align:center;font-family:"UnifrakturMaguntia",serif;font-size:clamp(2.2rem,7vw,3.8rem);margin:0}
.meta{display:flex;justify-content:space-between;border-top:1px solid;border-bottom:1px solid;padding:.3rem 0;font-size:.85rem;margin:.6rem 0 1.2rem}
h1{font-size:clamp(2.2rem,7vw,4rem);line-height:1;text-align:center;margin:.5rem 0 1rem;text-transform:uppercase}
.cols{columns:2 16rem;column-gap:2rem;column-rule:1px solid #bbb;font-size:1.05rem;line-height:1.6;text-align:justify}
a{color:#1a1a1a;font-weight:700}""",
"""<main><div class="mast">The Daily Link</div><div class="meta"><span>Vol. 404</span><span>Special edition</span><span>Free</span></div><h1>Page vanishes without a trace</h1><div class="cols"><p>Visitors were left puzzled today after following a link to a page that, by every account, does not exist. Staff searched the archives and found no sign of it.</p><p>Experts believe the page was moved or retired. Readers are advised to return to the <a href="/">front page</a>, where the latest stories remain available, or to <a href="/contact">write to the editor</a>.</p></div></main>""",
fonts=["Old Standard TT:wght@400;700", "UnifrakturMaguntia"], theme="#1a1a1a")

add(C, "typewriter-paper", "Paper Note", "Letterpress", "A typed note on lined paper with a coffee ring stain.",
"""body{display:grid;place-items:center;background:#d8c9ae;font-family:"Special Elite",monospace;color:#2d2a26;padding:2rem}
.p{position:relative;background:#fffdf5;background-image:repeating-linear-gradient(#fffdf5 0 31px,#cfe0f3 31px 32px);width:min(92vw,520px);padding:3rem 2.5rem 2.5rem 4rem;box-shadow:0 10px 25px rgba(0,0,0,.25);transform:rotate(-1.5deg)}
.p::before{content:"";position:absolute;left:2.8rem;top:0;bottom:0;border-left:2px solid #f3a6a6}
.p::after{content:"";position:absolute;right:30px;top:24px;width:90px;height:90px;border-radius:50%;border:8px solid rgba(139,94,52,.18)}
h1{font-size:1.8rem;margin:0 0 1rem;line-height:32px}p{line-height:32px;margin:0 0 32px}a{color:#8b1e1e}""",
"""<main class="p"><h1>Note: page 404</h1><p>To whoever is reading this,<br>the page you wanted is not here. I looked everywhere, even under the coffee cup.</p><p>Try the <a href="/">home page</a> instead.<br>Sorry, the webmaster</p></main>""",
fonts=["Special Elite"], theme="#8b1e1e")

add(C, "arcade-cabinet", "Arcade", "Coin-Op", "An arcade screen with 'Insert coin' and a high score table where 404 is the top score.",
"""body{display:grid;place-items:center;background:#2b0f3a;color:#fff;font-family:"Press Start 2P",monospace;text-align:center;padding:1.5rem}
.cab{background:#111;border:10px solid #6a1b9a;border-radius:18px;padding:2rem 1.5rem;width:min(94vw,440px);box-shadow:0 0 40px rgba(233,30,99,.4)}
h1{font-size:clamp(1rem,4vw,1.4rem);color:#ffeb3b;margin:0 0 1.5rem;line-height:1.6}
table{margin:0 auto 1.5rem;font-size:.65rem;line-height:2.2;border-collapse:collapse}td{padding:0 .8rem}tr:first-child{color:#ff4081}
p{font-size:.6rem;line-height:1.8;color:#aaa}a{display:inline-block;margin-top:1rem;font-size:.75rem;color:#00e5ff;text-decoration:none;animation:b 1.2s steps(1) infinite}@keyframes b{50%{opacity:.2}}""",
"""<main class="cab"><h1>HIGH SCORES</h1><table aria-label="High scores"><tr><td>1ST</td><td>404</td><td>NOT FOUND</td></tr><tr><td>2ND</td><td>301</td><td>MOVED</td></tr><tr><td>3RD</td><td>200</td><td>OK</td></tr></table><p>THE PAGE YOU WANT IS NOT ON THIS MACHINE.</p><a href="/">INSERT COIN TO GO HOME</a></main>""",
fonts=["Press Start 2P"], theme="#6a1b9a")

add(C, "blueprint", "Blueprint", "Draftwork", "A technical drawing of a missing page, with measurements and notes.",
"""body{display:grid;place-items:center;background:#1c4e80;background-image:linear-gradient(rgba(255,255,255,.12) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.12) 1px,transparent 1px);background-size:24px 24px;color:#e6f0ff;font-family:"Architects Daughter",cursive;text-align:center;padding:2rem}
svg{width:min(80vw,320px);margin:0 auto 1rem}
h1{font-size:2.2rem;margin:0}p{font-size:1.2rem;margin:.6rem 0 1.4rem}a{color:#fff;font-size:1.3rem}""",
"""<main><svg viewBox="0 0 300 200" fill="none" stroke="#e6f0ff" stroke-width="2" aria-hidden="true"><rect x="80" y="30" width="140" height="140" stroke-dasharray="8 6"/><path d="M80 185 H220 M80 180 v10 M220 180 v10"/><text x="150" y="198" fill="#e6f0ff" stroke="none" font-size="12" text-anchor="middle">404 mm</text><path d="M60 30 v140 M55 30 h10 M55 170 h10"/><text x="45" y="104" fill="#e6f0ff" stroke="none" font-size="12" text-anchor="middle" transform="rotate(-90 45 104)">missing</text><path d="M100 60 L200 140 M200 60 L100 140" stroke-width="1"/><circle cx="150" cy="100" r="30"/></svg><h1>Plan 404: page not built</h1><p>This page exists only on paper.</p><a href="/">Visit the finished site</a></main>""",
fonts=["Architects Daughter"], theme="#1c4e80")

add(C, "cassette", "Cassette", "Mixtape", "A cassette tape with a hand-written label, on a warm orange background.",
"""body{display:grid;place-items:center;background:#f4a259;color:#2b2118;font-family:"Permanent Marker",cursive;text-align:center;padding:2rem}
.tape{width:min(90vw,380px);aspect-ratio:1.6;background:#2b2118;border-radius:14px;margin:0 auto 1.8rem;position:relative;padding:14px}
.lab{background:#fff8e7;border-radius:6px;height:46%;padding:.5rem;font-size:1.5rem;display:grid;place-items:center}
.win{position:absolute;left:22%;right:22%;bottom:16%;height:26%;background:#5c4b3b;border-radius:30px;display:flex;justify-content:space-around;align-items:center}
.win i{width:34px;height:34px;border-radius:50%;background:#fff8e7;border:7px dotted #2b2118;animation:r 3s linear infinite}@keyframes r{to{transform:rotate(360deg)}}
h1{font-size:2rem;margin:0}p{font-family:system-ui,sans-serif;margin:.6rem 0 1.4rem}a{color:#2b2118;font-family:system-ui,sans-serif;font-weight:800}""",
"""<main><div class="tape" aria-hidden="true"><div class="lab">Side B: 404</div><div class="win"><i></i><i></i></div></div><h1>This track is missing</h1><p>Someone recorded over this page.</p><a href="/">Play the home page</a></main>""",
fonts=["Permanent Marker"], theme="#f4a259")

add(C, "dot-matrix", "Dot Matrix", "Printworks", "A dot matrix printout with tractor feed holes and a green stripe.",
"""body{display:grid;place-items:center;background:#e9e6df;font-family:"Silkscreen",monospace;color:#333;padding:2rem}
.p{width:min(92vw,560px);background:repeating-linear-gradient(#fff 0 28px,#dff3df 28px 56px);padding:2rem 3.5rem;position:relative;box-shadow:0 4px 18px rgba(0,0,0,.15)}
.p::before,.p::after{content:"";position:absolute;top:0;bottom:0;width:22px;background:radial-gradient(circle,#e9e6df 5px,transparent 6px) 0 0/22px 28px}
.p::before{left:6px}.p::after{right:6px}
h1{font-size:1.6rem;margin:0 0 1rem;line-height:28px}p{font-size:.95rem;line-height:28px;margin:0 0 28px}a{color:#1d4ed8}""",
"""<main class="p"><h1>ERROR REPORT 404</h1><p>REQUESTED PAGE ........ NOT FOUND<br>SEARCHED .............. EVERYWHERE<br>STATUS ................ MISSING</p><p>ACTION: <a href="/">RETURN TO HOME PAGE</a></p></main>""",
fonts=["Silkscreen"], theme="#1d4ed8")

add(C, "vinyl-record", "Vinyl", "Groove Records", "A spinning vinyl record with a 404 label, like the needle skipped.",
"""body{display:grid;place-items:center;background:#f2e8cf;color:#3a2e1f;font-family:"Bebas Neue",system-ui,sans-serif;text-align:center;padding:2rem}
.v{width:min(70vw,280px);aspect-ratio:1;border-radius:50%;background:repeating-radial-gradient(circle,#111 0 2px,#1d1d1d 2px 4px);margin:0 auto 1.8rem;display:grid;place-items:center;animation:s 4s linear infinite;box-shadow:0 12px 30px rgba(0,0,0,.3)}
@keyframes s{to{transform:rotate(360deg)}}
.v span{width:36%;aspect-ratio:1;border-radius:50%;background:#bc4749;color:#f2e8cf;display:grid;place-items:center;font-size:1.8rem}
h1{font-size:clamp(2.4rem,7vw,3.6rem);margin:0;letter-spacing:.03em}p{font-family:system-ui,sans-serif;margin:.4rem 0 1.5rem}a{font-family:system-ui,sans-serif;color:#bc4749;font-weight:700}""",
"""<main><div class="v" aria-hidden="true"><span>404</span></div><h1>The needle skipped</h1><p>This page is scratched off the record.</p><a href="/">Back to the A side</a></main>""",
fonts=["Bebas Neue"], theme="#bc4749")
