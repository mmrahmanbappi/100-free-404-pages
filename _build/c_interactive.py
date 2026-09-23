from core import add

C = "interactive"

add(C, "flashlight", "Flashlight", "Deepcave", "The page is dark. Move your mouse or finger to shine a light and find the way home.",
"""body{background:#000;color:#f4f1e8;font-family:"Josefin Sans",system-ui,sans-serif;overflow:hidden;cursor:none}
main{position:fixed;inset:0;display:grid;place-items:center;text-align:center;padding:2rem;background:#1a1712}
main::after{content:"";position:fixed;inset:0;pointer-events:none;background:radial-gradient(circle 140px at var(--x,50%) var(--y,50%),transparent 0,rgba(0,0,0,.97) 160px)}
b{font-size:clamp(5rem,18vw,10rem)}h1{font-size:1.8rem;margin:.5rem 0}p{opacity:.8;margin:0 0 1.5rem}
a{color:#f5c542;font-weight:700;cursor:pointer}
@media(hover:none){body{cursor:auto}}""",
"""<main><div><b aria-hidden="true">404</b><h1>It is dark in here</h1><p>Move your mouse to look around. This page is not here, but the exit is.</p><a href="/">Find the exit</a></div></main>""",
"""const m=document.querySelector('main');
function mv(x,y){m.style.setProperty('--x',x+'px');m.style.setProperty('--y',y+'px')}
addEventListener('pointermove',e=>mv(e.clientX,e.clientY));
addEventListener('keydown',()=>m.style.setProperty('--x','50%'));
mv(innerWidth/2,innerHeight/2);""",
fonts=["Josefin Sans:wght@400;700"], theme="#f5c542")

add(C, "catch-the-page", "Catch the Page", "Quickstep", "A button that runs away from the cursor. Visitors try to catch the missing page.",
"""body{display:grid;place-items:center;background:#f1f5ff;color:#1e1b4b;font-family:"Nunito",system-ui,sans-serif;text-align:center;padding:2rem;overflow:hidden}
h1{font-size:clamp(2rem,6vw,3rem);margin:0 0 .6rem}p{color:#4c4a7a;margin:0 0 1rem}
#run{position:fixed;left:50%;top:65%;transform:translate(-50%,-50%);background:#4f46e5;color:#fff;border:0;padding:.9rem 1.4rem;border-radius:12px;font:inherit;font-weight:800;cursor:pointer;transition:left .2s,top .2s}
.home{color:#4f46e5;font-weight:700}#score{font-weight:800;color:#4f46e5}""",
"""<main><h1>404: the page is running away</h1><p>Try to catch it. Missed it <span id="score">0</span> times so far.</p><p><a class="home" href="/">Or just go to the home page</a></p></main>
<button id="run" type="button">Catch me</button>""",
"""const b=document.getElementById('run'),s=document.getElementById('score');let n=0;
function jump(){n++;s.textContent=n;b.style.left=(10+Math.random()*80)+'%';b.style.top=(20+Math.random()*70)+'%';if(n>=8){b.textContent='Fine, you win';b.onclick=()=>location.href='/'}}
b.addEventListener('pointerenter',()=>{if(n<8)jump()});
b.addEventListener('click',()=>{if(n<8)jump()});""",
fonts=["Nunito:wght@400;800"], theme="#4f46e5")

add(C, "memory-cards", "Memory Cards", "Mindful Play", "A tiny memory game with six cards while visitors decide where to go next.",
"""body{display:grid;place-items:center;background:#fff8f0;color:#3a2e39;font-family:"Quicksand",system-ui,sans-serif;text-align:center;padding:2rem}
h1{font-size:2rem;margin:0}p{color:#6d5c6c}
.grid{display:grid;grid-template-columns:repeat(3,72px);gap:10px;justify-content:center;margin:1.5rem 0}
.grid button{height:72px;border:0;border-radius:12px;background:#f28482;color:transparent;font-size:2rem;cursor:pointer;font-weight:700}
.grid button.up,.grid button.ok{background:#fff;color:#3a2e39;box-shadow:inset 0 0 0 2px #f28482}
a{color:#e5383b;font-weight:700}""",
"""<main><h1>404, page not found</h1><p>While you are here, can you match the pairs?</p><div class="grid" id="g"></div><p id="msg">Find all three pairs.</p><a href="/">Back to the home page</a></main>""",
"""const v=['4','0','?','4','0','?'].sort(()=>Math.random()-.5),g=document.getElementById('g'),msg=document.getElementById('msg');let open=[],done=0;
v.forEach((c,i)=>{const b=document.createElement('button');b.type='button';b.textContent=c;b.setAttribute('aria-label','Card '+(i+1));b.onclick=()=>{if(b.classList.contains('up')||b.classList.contains('ok')||open.length==2)return;b.classList.add('up');open.push(b);if(open.length==2){setTimeout(()=>{if(open[0].textContent==open[1].textContent){open.forEach(x=>{x.classList.remove('up');x.classList.add('ok')});done++;if(done==3)msg.textContent='Nice memory. Now, let us find you a real page.'}else open.forEach(x=>x.classList.remove('up'));open=[]},600)}};g.appendChild(b)});""",
fonts=["Quicksand:wght@400;700"], theme="#f28482")

add(C, "parallax-mouse", "Parallax", "Layerly", "Layers of shapes move at different speeds as you move the mouse, giving a sense of depth.",
"""body{display:grid;place-items:center;background:#0f172a;color:#e2e8f0;font-family:"Sora",system-ui,sans-serif;text-align:center;overflow:hidden;padding:2rem}
.l{position:fixed;inset:0;pointer-events:none}
.l span{position:absolute;border-radius:50%;opacity:.8}
main{position:relative}
b{font-size:clamp(6rem,20vw,11rem);font-weight:800;background:linear-gradient(90deg,#38bdf8,#a78bfa);-webkit-background-clip:text;background-clip:text;color:transparent}
p{color:#94a3b8;margin:.5rem 0 1.8rem}a{color:#38bdf8;font-weight:700}""",
"""<div class="l" data-d="20" aria-hidden="true"><span style="width:120px;height:120px;left:10%;top:15%;background:#1e3a8a"></span><span style="width:60px;height:60px;right:15%;top:25%;background:#4c1d95"></span></div>
<div class="l" data-d="50" aria-hidden="true"><span style="width:40px;height:40px;left:20%;bottom:20%;background:#0ea5e9"></span><span style="width:90px;height:90px;right:10%;bottom:15%;background:#7c3aed"></span></div>
<main><b aria-hidden="true">404</b><h1>This page is out of reach</h1><p>Move your mouse and look around. It is not here.</p><a href="/">Go to the home page</a></main>""",
"""const L=[...document.querySelectorAll('.l')];addEventListener('pointermove',e=>{const x=e.clientX/innerWidth-.5,y=e.clientY/innerHeight-.5;L.forEach(l=>{const d=+l.dataset.d;l.style.transform=`translate(${-x*d}px,${-y*d}px)`})});""",
fonts=["Sora:wght@400;800"], theme="#38bdf8")

add(C, "search-helper", "Search Helper", "Helpwise", "Suggests real pages as visitors type, using a small list you can edit in the file.",
"""body{display:grid;place-items:center;background:#f8fafc;color:#0f172a;font-family:"Inter",system-ui,sans-serif;padding:2rem}
main{width:min(92vw,520px)}
h1{font-size:2rem;margin:0 0 .4rem}p{color:#64748b;margin:0 0 1.5rem}
input{width:100%;padding:1rem 1.1rem;border:2px solid #cbd5e1;border-radius:12px;font:inherit;font-size:1.05rem}
input:focus{border-color:#0ea5e9;outline:none}
ul{list-style:none;padding:0;margin:.8rem 0 0}li a{display:block;padding:.8rem 1rem;border-radius:10px;text-decoration:none}li a:hover,li a:focus{background:#e0f2fe}
li small{color:#64748b;margin-left:.5rem}""",
"""<main><h1>We could not find that page</h1><p>Type what you were looking for and we will suggest a page.</p><label class="sr" for="q">What were you looking for?</label><input id="q" type="search" placeholder="For example: pricing, contact, blog" autocomplete="off"><ul id="r"></ul></main>""",
"""// Edit this list to match the pages on your site.
const PAGES=[['Home','/'],['Pricing','/pricing'],['Contact us','/contact'],['Blog','/blog'],['About us','/about'],['Help center','/help'],['Careers','/careers'],['Log in','/login']];
const q=document.getElementById('q'),r=document.getElementById('r');
function show(){const t=q.value.toLowerCase().trim();const list=(t?PAGES.filter(p=>p[0].toLowerCase().includes(t)||p[1].includes(t)):PAGES.slice(0,4));r.innerHTML='';list.forEach(p=>{const li=document.createElement('li'),a=document.createElement('a');a.href=p[1];a.textContent=p[0];const s=document.createElement('small');s.textContent=p[1];a.appendChild(s);li.appendChild(a);r.appendChild(li)});if(!list.length){r.innerHTML='<li>No match. Try the <a href="/">home page</a>.</li>'}}
q.addEventListener('input',show);show();""",
fonts=["Inter:wght@400;700"], theme="#0ea5e9")

add(C, "whack-a-bug", "Whack a Bug", "Squash Labs", "Little bugs pop up out of holes. Click them to fix the broken page.",
"""body{display:grid;place-items:center;background:#ecfccb;color:#1a2e05;font-family:"Lilita One",system-ui,sans-serif;text-align:center;padding:2rem}
h1{font-size:2.2rem;margin:0;font-weight:400}p{font-family:system-ui,sans-serif;color:#3f6212}
.b{display:grid;grid-template-columns:repeat(3,80px);gap:14px;justify-content:center;margin:1.5rem 0}
.h{height:80px;border-radius:50%;background:#3f6212;position:relative;overflow:hidden;border:0;cursor:pointer}
.h i{position:absolute;left:50%;bottom:-60px;width:44px;height:44px;margin-left:-22px;border-radius:50%;background:#dc2626;transition:bottom .15s}
.h.up i{bottom:18px}.h i::before,.h i::after{content:"";position:absolute;top:12px;width:8px;height:8px;border-radius:50%;background:#fff}.h i::before{left:10px}.h i::after{right:10px}
a{font-family:system-ui,sans-serif;color:#15803d;font-weight:700}""",
"""<main><h1>404: bugs broke this page</h1><p>Squash them while you are here. Fixed: <b id="s">0</b></p><div class="b" id="b"></div><a href="/">Leave the bugs and go home</a></main>""",
"""const b=document.getElementById('b'),s=document.getElementById('s');let n=0;
for(let i=0;i<6;i++){const h=document.createElement('button');h.type='button';h.className='h';h.setAttribute('aria-label','Hole '+(i+1));h.innerHTML='<i></i>';h.onclick=()=>{if(h.classList.contains('up')){h.classList.remove('up');s.textContent=++n}};b.appendChild(h)}
const H=[...b.children];setInterval(()=>{H.forEach(h=>h.classList.remove('up'));H[Math.floor(Math.random()*H.length)].classList.add('up')},900);""",
fonts=["Lilita One"], theme="#15803d")

add(C, "drag-the-zero", "Fix the Number", "Puzzlebox", "The 0 fell out of 404. Drag it back into place, or tap it, to fix the page.",
"""body{display:grid;place-items:center;background:#fdf2f8;color:#500724;font-family:"Rubik",system-ui,sans-serif;text-align:center;padding:2rem}
.n{display:flex;gap:.1em;justify-content:center;align-items:center;font-size:clamp(5rem,18vw,9rem);font-weight:800;color:#be185d}
.slot{width:.62em;height:.9em;border:4px dashed #f9a8d4;border-radius:.15em}
#z{position:relative;font-size:clamp(5rem,18vw,9rem);font-weight:800;color:#db2777;cursor:grab;touch-action:none;background:none;border:0;padding:0;font-family:inherit;margin-top:.5rem}
p{margin:1rem 0 1.5rem}a{color:#be185d;font-weight:700}""",
"""<main><h1 class="sr">Page not found</h1><div class="n" id="n" aria-hidden="true"><span>4</span><span class="slot" id="slot"></span><span>4</span></div><button id="z" type="button" aria-label="Put the zero back">0</button><p id="m">The zero fell out. Drag it back up, or tap it.</p><a href="/">Go to the home page</a></main>""",
"""const z=document.getElementById('z'),slot=document.getElementById('slot'),m=document.getElementById('m');let sx,sy,drag=false;
function fix(){slot.replaceWith(Object.assign(document.createElement('span'),{textContent:'0'}));z.remove();m.textContent='Fixed! The number is whole again. The page is still missing, though.'}
z.addEventListener('pointerdown',e=>{drag=true;sx=e.clientX;sy=e.clientY;z.setPointerCapture(e.pointerId)});
z.addEventListener('pointermove',e=>{if(drag)z.style.transform=`translate(${e.clientX-sx}px,${e.clientY-sy}px)`});
z.addEventListener('pointerup',e=>{drag=false;const a=slot.getBoundingClientRect(),b=z.getBoundingClientRect();if(Math.abs(a.x-b.x)<80&&Math.abs(a.y-b.y)<100||Math.hypot(e.clientX-sx,e.clientY-sy)<5)fix();else z.style.transform=''});""",
fonts=["Rubik:wght@400;800"], theme="#db2777")

add(C, "click-counter", "Button Masher", "Tapster", "A big button that counts clicks and says something new at each milestone.",
"""body{display:grid;place-items:center;background:#111827;color:#f9fafb;font-family:"Bungee",system-ui,sans-serif;text-align:center;padding:2rem}
h1{font-size:clamp(1.6rem,5vw,2.4rem);margin:0 0 1rem;font-weight:400}
#b{width:180px;height:180px;border-radius:50%;border:0;background:#ef4444;color:#fff;font:inherit;font-size:2.4rem;box-shadow:0 12px 0 #991b1b;cursor:pointer;transition:transform .05s,box-shadow .05s}
#b:active{transform:translateY(10px);box-shadow:0 2px 0 #991b1b}
p{font-family:system-ui,sans-serif;color:#d1d5db;min-height:3em;margin:1.8rem 0 1rem}a{font-family:system-ui,sans-serif;color:#fca5a5;font-weight:700}""",
"""<main><h1>Page 404 is not here</h1><button id="b" type="button">404</button><p id="m" aria-live="polite">Pressing the button will not bring the page back. But go on.</p><a href="/">Take me to the home page</a></main>""",
"""const b=document.getElementById('b'),m=document.getElementById('m');let n=0;const say={5:'Still missing.',15:'You are very determined.',30:'The page appreciates your effort.',50:'Fifty clicks. That is dedication.',100:'One hundred! You win nothing, but you win.'};
b.onclick=()=>{n++;b.textContent=n;if(say[n])m.textContent=say[n]};""",
fonts=["Bungee"], theme="#ef4444")

add(C, "choose-path", "Choose a Path", "Crossroads", "A signpost with three arrows pointing to real pages on the site.",
"""body{display:grid;place-items:center;background:#e7f0e1;color:#26331f;font-family:"Amatic SC",cursive;text-align:center;padding:2rem}
h1{font-size:clamp(2.6rem,8vw,4rem);margin:0}
.post{position:relative;width:260px;margin:1.5rem auto;padding-bottom:40px}
.post::before{content:"";position:absolute;left:50%;top:0;bottom:0;width:16px;margin-left:-8px;background:#7a5230;border-radius:4px}
.post a{position:relative;display:block;margin:12px 0;padding:.5rem 1rem;font-size:1.8rem;font-weight:700;text-decoration:none;color:#fff;background:#b07a45;clip-path:polygon(0 0,88% 0,100% 50%,88% 100%,0 100%);text-align:left;transition:transform .15s}
.post a.l{clip-path:polygon(12% 0,100% 0,100% 100%,12% 100%,0 50%);text-align:right}
.post a:hover,.post a:focus{transform:scale(1.05)}
p{font-family:system-ui,sans-serif;font-size:1.05rem;color:#4a5d40}""",
"""<main><h1>404: you took a wrong turn</h1><p>This page does not exist. Pick a direction.</p><nav class="post" aria-label="Where to next"><a href="/">Home</a><a class="l" href="/blog">Blog</a><a href="/contact">Contact</a></nav></main>""",
fonts=["Amatic SC:wght@700"], theme="#b07a45")

add(C, "tiny-snake", "Snake", "Pixel Garden", "A playable mini snake game. Use arrow keys or swipe to play.",
"""body{display:grid;place-items:center;background:#1b2d1f;color:#d8f3dc;font-family:"Press Start 2P",monospace;text-align:center;padding:1.5rem}
h1{font-size:clamp(.9rem,3vw,1.3rem);line-height:1.6;margin:0 0 1rem}
canvas{background:#2d4a31;border:4px solid #95d5b2;image-rendering:pixelated;width:min(80vw,320px);height:auto;touch-action:none}
p{font-size:.6rem;line-height:1.8;margin:1rem 0}a{color:#95d5b2}""",
"""<main><h1>404 page not found</h1><canvas id="c" width="160" height="160" aria-label="Snake game"></canvas><p>Arrow keys or swipe to play. Score: <span id="s">0</span></p><a href="/">Exit to home page</a></main>""",
"""const c=document.getElementById('c'),x=c.getContext('2d'),S=document.getElementById('s'),N=16,G=10;let sn=[[8,8]],d=[1,0],f=[3,3],sc=0;
function place(){f=[Math.floor(Math.random()*N),Math.floor(Math.random()*N)]}
function step(){const h=[(sn[0][0]+d[0]+N)%N,(sn[0][1]+d[1]+N)%N];if(sn.some(p=>p[0]==h[0]&&p[1]==h[1])){sn=[[8,8]];d=[1,0];sc=0}sn.unshift(h);if(h[0]==f[0]&&h[1]==f[1]){sc++;place()}else sn.pop();S.textContent=sc;
x.fillStyle='#2d4a31';x.fillRect(0,0,160,160);x.fillStyle='#ffd166';x.fillRect(f[0]*G,f[1]*G,G,G);x.fillStyle='#95d5b2';sn.forEach(p=>x.fillRect(p[0]*G,p[1]*G,G-1,G-1))}
const K={ArrowUp:[0,-1],ArrowDown:[0,1],ArrowLeft:[-1,0],ArrowRight:[1,0]};addEventListener('keydown',e=>{const k=K[e.key];if(k&&!(k[0]==-d[0]&&k[1]==-d[1])){d=k;e.preventDefault()}});
let t0;c.addEventListener('pointerdown',e=>t0=[e.clientX,e.clientY]);c.addEventListener('pointerup',e=>{if(!t0)return;const dx=e.clientX-t0[0],dy=e.clientY-t0[1];const k=Math.abs(dx)>Math.abs(dy)?[Math.sign(dx),0]:[0,Math.sign(dy)];if(!(k[0]==-d[0]&&k[1]==-d[1]))d=k});
setInterval(step,140);""",
fonts=["Press Start 2P"], theme="#95d5b2")
