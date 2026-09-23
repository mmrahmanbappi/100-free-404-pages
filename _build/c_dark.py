from core import add

C = "dark"

add(C, "neon-outline", "Neon Outline", "Vapor", "A glowing outlined 404 in pink and blue on a very dark purple.",
"""body{display:grid;place-items:center;background:#0d0221;color:#fff;font-family:"Orbitron",system-ui,sans-serif;text-align:center;padding:2rem}
.n{font-size:clamp(6rem,20vw,12rem);font-weight:900;color:transparent;-webkit-text-stroke:3px #ff00c8;filter:drop-shadow(0 0 12px #ff00c8) drop-shadow(0 0 30px #7a00ff);margin:0;line-height:1}
p{font-family:system-ui,sans-serif;color:#c9b8ff;margin:1.5rem 0 2rem;font-size:1.1rem}
a{font-family:system-ui,sans-serif;color:#0d0221;background:#00f0ff;box-shadow:0 0 20px #00f0ff;padding:.8rem 1.5rem;border-radius:6px;text-decoration:none;font-weight:800}""",
"""<main><h1 class="n" aria-label="Error 404">404</h1><p>This page faded into the night.</p><a href="/">Back to the lights</a></main>""",
fonts=["Orbitron:wght@900"], theme="#ff00c8")

add(C, "midnight-gradient", "Midnight Gradient", "Nocturne", "A deep blue to violet gradient with a soft glowing orb behind the text.",
"""body{display:grid;place-items:center;background:linear-gradient(160deg,#0b1026,#2b1055 60%,#4a1a6b);color:#eef;font-family:"Manrope",system-ui,sans-serif;text-align:center;padding:2rem;overflow:hidden}
main{position:relative}
main::before{content:"";position:absolute;width:420px;height:420px;left:50%;top:50%;transform:translate(-50%,-55%);background:radial-gradient(circle,rgba(167,139,250,.45),transparent 65%);z-index:-1}
b{font-size:clamp(6rem,18vw,10rem);font-weight:800;letter-spacing:-.04em}
h1{font-size:1.8rem;margin:.2rem 0 .6rem}p{color:#b8b5e8;margin:0 0 2rem}
a{color:#fff;border:1.5px solid rgba(255,255,255,.4);padding:.8rem 1.4rem;border-radius:999px;text-decoration:none;font-weight:600;backdrop-filter:blur(6px)}""",
"""<main><b aria-hidden="true">404</b><h1>It is quiet here</h1><p>No page at this address, just the night sky.</p><a href="/">Go to the home page</a></main>""",
fonts=["Manrope:wght@400;800"], theme="#4a1a6b")

add(C, "starfield", "Starfield", "Deep Field", "A field of twinkling stars made with CSS, with a clean white message.",
"""body{display:grid;place-items:center;background:#000;color:#fff;font-family:"Jost",system-ui,sans-serif;text-align:center;padding:2rem;overflow:hidden}
.st{position:fixed;inset:0;background-image:radial-gradient(1px 1px at 20% 30%,#fff,transparent),radial-gradient(1px 1px at 70% 60%,#fff,transparent),radial-gradient(2px 2px at 40% 80%,#fff,transparent),radial-gradient(1px 1px at 85% 20%,#fff,transparent),radial-gradient(1.5px 1.5px at 55% 45%,#fff,transparent),radial-gradient(1px 1px at 10% 70%,#fff,transparent),radial-gradient(2px 2px at 90% 85%,#fff,transparent);background-size:300px 300px;animation:tw 4s ease-in-out infinite alternate}
@keyframes tw{to{opacity:.4}}
main{position:relative}b{font-size:clamp(5rem,16vw,9rem);font-weight:300;letter-spacing:.1em}
h1{font-weight:400;font-size:1.6rem;margin:.5rem 0}p{color:#aaa;margin:0 0 2rem}a{color:#fff;letter-spacing:.1em}""",
"""<div class="st" aria-hidden="true"></div><main><b aria-hidden="true">404</b><h1>Lost among the stars</h1><p>The page you are looking for is light years away.</p><a href="/">Return home</a></main>""",
fonts=["Jost:wght@300;400"], theme="#000000")

add(C, "cyber-grid", "Cyber Grid", "Gridrunner", "A perspective grid floor that fades into the horizon, in eighties sci-fi style.",
"""body{display:grid;place-items:center;background:linear-gradient(#10002b 55%,#240046);color:#fff;font-family:"Audiowide",system-ui,sans-serif;text-align:center;padding:2rem;overflow:hidden}
.floor{position:fixed;left:-50%;right:-50%;bottom:0;height:45vh;background-image:linear-gradient(#f72585 2px,transparent 2px),linear-gradient(90deg,#f72585 2px,transparent 2px);background-size:60px 60px;transform:perspective(300px) rotateX(60deg);transform-origin:bottom;opacity:.6;animation:run 1.5s linear infinite}
@keyframes run{to{background-position:0 60px}}
.sun{width:180px;height:180px;border-radius:50%;background:linear-gradient(#ffd60a,#f72585);margin:0 auto 1rem}
main{position:relative;margin-bottom:20vh}h1{font-size:clamp(2rem,6vw,3.2rem);margin:0}p{font-family:system-ui,sans-serif;color:#e0aaff;margin:.8rem 0 1.6rem}
a{color:#ffd60a}""",
"""<div class="floor" aria-hidden="true"></div><main><div class="sun" aria-hidden="true"></div><h1>Error 404</h1><p>You have reached the edge of the grid.</p><a href="/">Head back to the city</a></main>""",
fonts=["Audiowide"], theme="#f72585")

add(C, "spotlight-dark", "Spotlight", "Stagehand", "A single stage spotlight lights up the 404 on an empty dark stage.",
"""body{display:grid;place-items:center;background:#0c0c0c;color:#f3efe6;font-family:"Cormorant Garamond",Georgia,serif;text-align:center;padding:2rem;overflow:hidden}
body::before{content:"";position:fixed;left:50%;top:-10%;width:520px;height:120%;transform:translateX(-50%);background:radial-gradient(ellipse at top,rgba(255,244,214,.18),transparent 60%);clip-path:polygon(40% 0,60% 0,100% 100%,0 100%)}
main{position:relative}b{font-size:clamp(6rem,18vw,10rem);font-weight:600}
h1{font-size:2rem;font-weight:500;font-style:italic;margin:0}p{font-family:system-ui,sans-serif;color:#9d978a;margin:1rem 0 2rem}
a{font-family:system-ui,sans-serif;color:#e9c46a}""",
"""<main><b aria-hidden="true">404</b><h1>The stage is empty</h1><p>The page you came to see is not performing today.</p><a href="/">See what is showing</a></main>""",
fonts=["Cormorant Garamond:ital,wght@0,600;1,500"], theme="#e9c46a")

add(C, "aurora", "Aurora", "Northern", "Soft moving northern lights in green and teal behind the message.",
"""body{display:grid;place-items:center;background:#030b16;color:#e6fff7;font-family:"Figtree",system-ui,sans-serif;text-align:center;padding:2rem;overflow:hidden}
.a{position:fixed;inset:-20%;background:radial-gradient(ellipse at 30% 40%,rgba(52,211,153,.35),transparent 50%),radial-gradient(ellipse at 70% 30%,rgba(45,212,191,.3),transparent 45%),radial-gradient(ellipse at 50% 60%,rgba(129,140,248,.25),transparent 50%);filter:blur(30px);animation:m 12s ease-in-out infinite alternate}
@keyframes m{to{transform:translate(5%,-5%) rotate(8deg)}}
main{position:relative}b{font-size:clamp(5.5rem,17vw,9rem);font-weight:800}
h1{font-size:1.8rem;margin:0 0 .6rem}p{color:#a7f3d0;margin:0 0 2rem}a{background:#34d399;color:#03201a;padding:.8rem 1.4rem;border-radius:10px;text-decoration:none;font-weight:700}""",
"""<div class="a" aria-hidden="true"></div><main><b aria-hidden="true">404</b><h1>Beautiful view, wrong page</h1><p>What you are looking for is not here.</p><a href="/">Go to the home page</a></main>""",
fonts=["Figtree:wght@400;800"], theme="#34d399")

add(C, "dark-minimal-mono", "Dark Mono", "Monolith", "A strict black and white layout with a monospaced font and a thin frame.",
"""body{background:#000;color:#fff;font-family:"JetBrains Mono",monospace;display:grid;place-items:center;padding:2rem}
main{border:1px solid #fff;padding:clamp(2rem,6vw,4rem);max-width:36rem;width:100%}
.top{display:flex;justify-content:space-between;font-size:.85rem;color:#888;margin-bottom:3rem}
h1{font-size:clamp(3rem,10vw,5rem);margin:0;font-weight:700}
p{color:#bbb;line-height:1.7;margin:1rem 0 2rem}a{color:#000;background:#fff;padding:.6rem 1rem;text-decoration:none}""",
"""<main><div class="top"><span>ERR</span><span>404</span></div><h1>Not found.</h1><p>The resource you requested does not exist on this server.</p><a href="/">&lt; home</a></main>""",
fonts=["JetBrains Mono:wght@400;700"], theme="#000000")

add(C, "lava-lamp", "Lava Lamp", "Groove", "Warm blobs slowly rise and melt together behind a dark glass panel.",
"""body{display:grid;place-items:center;background:#1a0a0a;color:#fff5eb;font-family:"Righteous",system-ui,sans-serif;text-align:center;padding:2rem;overflow:hidden}
.bl{position:fixed;inset:0;filter:blur(40px) contrast(1.2)}
.bl i{position:absolute;border-radius:50%;background:#ff6b35;animation:up 14s ease-in-out infinite}
.bl i:nth-child(1){width:260px;height:260px;left:15%;bottom:-100px}
.bl i:nth-child(2){width:200px;height:200px;right:15%;bottom:-120px;background:#f7931e;animation-delay:-5s}
.bl i:nth-child(3){width:160px;height:160px;left:45%;bottom:-80px;background:#c1121f;animation-delay:-9s}
@keyframes up{50%{transform:translateY(-70vh) scale(1.2)}}
main{position:relative;background:rgba(26,10,10,.55);backdrop-filter:blur(8px);padding:2.5rem 3rem;border-radius:24px}
b{font-size:clamp(5rem,15vw,8rem)}p{font-family:system-ui,sans-serif;color:#ffd6ba;margin:.5rem 0 1.8rem}a{color:#ffb703}""",
"""<div class="bl" aria-hidden="true"><i></i><i></i><i></i></div><main><b aria-hidden="true">404</b><h1 class="sr">Page not found</h1><p>This page melted away. Groovy, but not helpful.</p><a href="/">Go to the home page</a></main>""",
fonts=["Righteous"], theme="#ff6b35")

add(C, "matrix-rain", "Code Rain", "Rabbit Hole", "Green characters rain down the screen behind a black message box.",
"""body{background:#000;color:#00ff66;font-family:"Share Tech Mono",monospace;overflow:hidden}
canvas{position:fixed;inset:0;width:100%;height:100%}
main{position:fixed;left:50%;top:50%;transform:translate(-50%,-50%);background:rgba(0,0,0,.85);border:1px solid #00ff66;padding:2rem 2.5rem;text-align:center;box-shadow:0 0 30px rgba(0,255,102,.3)}
h1{font-size:clamp(2.5rem,8vw,4rem);margin:0}p{color:#8fffb8;margin:.8rem 0 1.5rem}a{color:#000;background:#00ff66;padding:.5rem 1rem;text-decoration:none}""",
"""<canvas id="c" aria-hidden="true"></canvas><main><h1>404</h1><p>There is no page. There is only the home page.</p><a href="/">Wake up</a></main>""",
"""const c=document.getElementById('c'),x=c.getContext('2d');let w,h,cols,y;
function size(){w=c.width=innerWidth;h=c.height=innerHeight;cols=Math.floor(w/16);y=Array(cols).fill(0)}size();addEventListener('resize',size);
const ch='404NOTFOUND01アイウエオ';
function draw(){x.fillStyle='rgba(0,0,0,.08)';x.fillRect(0,0,w,h);x.fillStyle='#00ff66';x.font='16px monospace';y.forEach((v,i)=>{x.fillText(ch[Math.floor(Math.random()*ch.length)],i*16,v*16);y[i]=v*16>h&&Math.random()>.975?0:v+1})}
if(!matchMedia('(prefers-reduced-motion: reduce)').matches)setInterval(draw,50);""",
fonts=["Share Tech Mono"], theme="#00ff66")

add(C, "eclipse", "Eclipse", "Umbra", "A solar eclipse, a black disc with a glowing golden ring, above the message.",
"""body{display:grid;place-items:center;background:#07070a;color:#f5f0e1;font-family:"Syne",system-ui,sans-serif;text-align:center;padding:2rem}
.e{width:180px;height:180px;border-radius:50%;background:#07070a;margin:0 auto 2.2rem;box-shadow:0 0 0 3px #ffd98e,0 0 40px 10px rgba(255,190,90,.6),0 0 120px 30px rgba(255,140,60,.25)}
h1{font-size:clamp(2.4rem,7vw,3.6rem);margin:0;font-weight:800}p{color:#a9a393;margin:1rem 0 2rem}
a{color:#ffd98e;border-bottom:1px solid;text-decoration:none;padding-bottom:2px}""",
"""<main><div class="e" aria-hidden="true"></div><h1>404, total darkness</h1><p>This page is hidden in the shadow. It will not come out.</p><a href="/">Step into the light</a></main>""",
fonts=["Syne:wght@400;800"], theme="#ffd98e")
