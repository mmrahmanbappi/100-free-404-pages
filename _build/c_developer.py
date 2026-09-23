from core import add

C = "developer"
MONO = ["JetBrains Mono:wght@400;700"]

add(C, "terminal", "Terminal", "Shellbox", "A terminal window that runs a command, prints 'not found' and suggests going home.",
"""body{display:grid;place-items:center;background:#1e1e2e;font-family:"JetBrains Mono",monospace;color:#cdd6f4;padding:1.5rem}
.w{width:min(96vw,680px);background:#11111b;border-radius:12px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.4)}
.bar{background:#313244;padding:.7rem 1rem;display:flex;gap:.5rem}.bar i{width:12px;height:12px;border-radius:50%}
.c{padding:1.5rem;font-size:.95rem;line-height:1.8}.g{color:#a6e3a1}.r{color:#f38ba8}.y{color:#f9e2af}.m{color:#6c7086}
.cur{display:inline-block;width:9px;height:1.1em;background:#cdd6f4;vertical-align:text-bottom;animation:b 1s steps(1) infinite}@keyframes b{50%{opacity:0}}
a{color:#89b4fa}h1{font-size:inherit;margin:0;font-weight:400;display:inline}""",
"""<main class="w"><div class="bar" aria-hidden="true"><i style="background:#f38ba8"></i><i style="background:#f9e2af"></i><i style="background:#a6e3a1"></i></div><div class="c">
<div><span class="g">visitor@site</span>:<span class="y">~</span>$ cd /this-page</div>
<div><span class="r">bash: cd: /this-page: <h1>404 page not found</h1></span></div>
<div><span class="g">visitor@site</span>:<span class="y">~</span>$ ls</div>
<div><a href="/">home/</a>&nbsp;&nbsp;<a href="/blog">blog/</a>&nbsp;&nbsp;<a href="/docs">docs/</a>&nbsp;&nbsp;<a href="/contact">contact/</a></div>
<div class="m"># tip: click a folder to go there</div>
<div><span class="g">visitor@site</span>:<span class="y">~</span>$ <span class="cur"></span></div></div></main>""",
fonts=MONO, theme="#89b4fa")

add(C, "code-editor", "Code Editor", "Devnote", "A code editor with line numbers, where the page file is highlighted as missing.",
"""body{display:grid;place-items:center;background:#0d1117;color:#c9d1d9;font-family:"Fira Code",monospace;padding:1.5rem}
.ed{width:min(96vw,720px);background:#161b22;border:1px solid #30363d;border-radius:10px;overflow:hidden}
.tabs{display:flex;background:#010409;font-size:.85rem}.tabs span{padding:.6rem 1rem;border-right:1px solid #30363d;color:#8b949e}.tabs .on{background:#161b22;color:#f0f6fc;border-top:2px solid #f78166}
pre{margin:0;padding:1.2rem 0;font:inherit;font-size:.92rem;line-height:1.75;overflow-x:auto}
.l{display:block;padding:0 1.2rem}.l::before{content:attr(data-n);display:inline-block;width:2.2rem;color:#484f58}
.k{color:#ff7b72}.s{color:#a5d6ff}.f{color:#d2a8ff}.c{color:#8b949e}.err{background:rgba(248,81,73,.15);border-left:3px solid #f85149}
a{color:#58a6ff}""",
"""<main class="ed"><div class="tabs"><span class="on">page.html</span><span>index.html</span></div><pre>
<span class="l" data-n="1"><span class="k">const</span> page = <span class="f">find</span>(<span class="s">"this-page"</span>);</span>
<span class="l err" data-n="2"><span class="c">// Error 404: page is undefined</span></span>
<span class="l" data-n="3"><span class="k">if</span> (!page) {</span>
<span class="l" data-n="4">  <span class="f">goHome</span>(); <span class="c">// <a href="/">click here to go home</a></span></span>
<span class="l" data-n="5">}</span>
</pre></main><h1 class="sr">Page not found</h1>""",
fonts=["Fira Code:wght@400;600"], theme="#f78166")

add(C, "http-response", "HTTP Response", "Headerline", "The raw HTTP response for a 404, with headers and a short JSON body.",
"""body{display:grid;place-items:center;background:#fafafa;color:#1f2937;font-family:"IBM Plex Mono",monospace;padding:1.5rem}
main{width:min(94vw,600px)}
h1{font-family:"IBM Plex Sans",system-ui,sans-serif;font-size:2rem;margin:0 0 1rem}
pre{background:#fff;border:1px solid #e5e7eb;border-radius:10px;padding:1.3rem;font:inherit;font-size:.92rem;line-height:1.7;overflow-x:auto;margin:0 0 1.5rem}
.s{color:#dc2626;font-weight:700}.h{color:#6b7280}.v{color:#059669}
a{font-family:"IBM Plex Sans",system-ui,sans-serif;background:#111827;color:#fff;padding:.7rem 1.2rem;border-radius:8px;text-decoration:none}""",
"""<main><h1>Page not found</h1><pre><span class="s">HTTP/1.1 404 Not Found</span>
<span class="h">Content-Type:</span> application/json
<span class="h">Cache-Control:</span> no-store

{
  <span class="v">"error"</span>: "not_found",
  <span class="v">"message"</span>: "This page does not exist.",
  <span class="v">"try"</span>: ["/", "/docs", "/contact"]
}</pre><a href="/">GET /</a></main>""",
fonts=["IBM Plex Mono", "IBM Plex Sans:wght@600"], theme="#111827")

add(C, "json-viewer", "JSON Viewer", "Objectify", "A friendly JSON tree view of the error, in soft pastel colors.",
"""body{display:grid;place-items:center;background:#fdf6f0;color:#3b3355;font-family:"Victor Mono",monospace;padding:1.5rem}
main{width:min(94vw,520px);background:#fff;border-radius:16px;padding:1.8rem;box-shadow:0 20px 40px -25px rgba(59,51,85,.35)}
h1{font-family:system-ui,sans-serif;font-size:1.4rem;margin:0 0 1rem}
ul{list-style:none;margin:0;padding-left:1.2rem;border-left:2px dotted #e4dcf5;line-height:1.9}
.k{color:#b5179e}.n{color:#f77f00}.s{color:#2a9d8f}.b{color:#4361ee}
a{color:#4361ee}""",
"""<main><h1>Error 404</h1><ul><li><span class="k">"status"</span>: <span class="n">404</span>,</li><li><span class="k">"found"</span>: <span class="b">false</span>,</li><li><span class="k">"page"</span>: <span class="b">null</span>,</li><li><span class="k">"suggestion"</span>: {<ul><li><span class="k">"home"</span>: <a class="s" href="/">"/"</a>,</li><li><span class="k">"help"</span>: <a class="s" href="/help">"/help"</a></li></ul>}</li></ul></main>""",
fonts=["Victor Mono:wght@400;600"], theme="#b5179e")

add(C, "stack-trace", "Stack Trace", "Tracewell", "A funny stack trace that explains exactly how the visitor got lost.",
"""body{background:#fff5f5;color:#3f1d1d;font-family:"Roboto Mono",monospace;padding:clamp(1.5rem,5vw,4rem)}
main{max-width:52rem;margin:0 auto}
h1{font-family:"Roboto",system-ui,sans-serif;color:#c53030;font-size:clamp(1.8rem,5vw,2.6rem);margin:0 0 .4rem}
.sub{font-family:"Roboto",system-ui,sans-serif;color:#7b3a3a;margin:0 0 1.5rem}
pre{background:#fff;border-left:4px solid #c53030;padding:1.2rem 1.4rem;font:inherit;font-size:.9rem;line-height:1.8;overflow-x:auto}
.at{color:#9b4d4d}.hi{background:#fed7d7}
a{font-family:"Roboto",system-ui,sans-serif;display:inline-block;margin-top:1.4rem;background:#c53030;color:#fff;padding:.7rem 1.2rem;border-radius:6px;text-decoration:none}""",
"""<main><h1>PageNotFoundError: 404</h1><p class="sub">Unhandled exception while looking for this page.</p><pre>Traceback (most recent call last):
  <span class="at">at</span> visitor.clickLink(old-bookmark)
  <span class="at">at</span> browser.follow(url)
  <span class="at">at</span> server.lookup(path)
<span class="hi">  <span class="at">at</span> server.lookup: page does not exist</span>
PageNotFoundError: the page was moved or deleted</pre><a href="/">Recover: go to home</a></main>""",
fonts=["Roboto Mono", "Roboto:wght@400;700"], theme="#c53030")

add(C, "git-log", "Git Log", "Commitly", "A git log that shows the commit where the page was deleted.",
"""body{display:grid;place-items:center;background:#24292f;color:#e6edf3;font-family:"Source Code Pro",monospace;padding:1.5rem}
main{width:min(96vw,680px)}
h1{font-size:1rem;color:#8b949e;font-weight:400;margin:0 0 1rem}
.c{border-left:2px solid #3fb950;padding:0 0 1.2rem 1.2rem;position:relative;line-height:1.6}
.c::before{content:"";position:absolute;left:-7px;top:4px;width:12px;height:12px;border-radius:50%;background:#3fb950}
.c.del{border-color:#f85149}.c.del::before{background:#f85149}
.h{color:#d29922}.m{color:#f0f6fc;font-weight:600}.a{color:#8b949e;font-size:.85rem}
a{color:#58a6ff}""",
"""<main><h1>$ git log --oneline this-page.html</h1>
<div class="c del"><span class="h">4f04e04</span> <span class="m">Remove old page (404 page not found)</span><br><span class="a">Webmaster, just now</span></div>
<div class="c"><span class="h">a1b2c3d</span> <span class="m">Move content to the home page</span><br><span class="a">Webmaster, last week</span></div>
<div class="c"><span class="h">9e8d7c6</span> <span class="m">First version of this page</span><br><span class="a">Webmaster, long ago</span></div>
<p>$ git checkout <a href="/">home</a></p></main>""",
fonts=["Source Code Pro:wght@400;600"], theme="#3fb950")

add(C, "browser-console", "Console", "Devtools Diner", "A browser console panel with a red error line and a helpful log message.",
"""body{display:grid;place-items:center;background:#e8eaed;font-family:system-ui,sans-serif;padding:1.5rem}
.p{width:min(96vw,720px);background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,.12);font-family:Menlo,Consolas,monospace;font-size:.85rem}
.tb{display:flex;gap:1.2rem;padding:.55rem 1rem;border-bottom:1px solid #dadce0;color:#5f6368;font-family:system-ui,sans-serif}.tb .on{color:#1a73e8;border-bottom:2px solid #1a73e8}
.row{padding:.55rem 1rem;border-bottom:1px solid #f1f3f4;display:flex;gap:.6rem}
.e{background:#fce8e6;color:#c5221f}.w{background:#fef7e0;color:#7a5b00}.i{color:#202124}
.i::before{content:">";color:#1a73e8}
a{color:#1a73e8}""",
"""<main class="p"><div class="tb"><span>Elements</span><span class="on">Console</span><span>Network</span></div>
<div class="row e">GET /this-page 404 (Not Found)</div>
<div class="row w">Warning: the link you followed may be old or mistyped.</div>
<div class="row i">&nbsp;<h1 style="font:inherit;margin:0">console.log("Page not found. Try the home page.")</h1></div>
<div class="row i">&nbsp;location.href = "<a href="/">/</a>"</div></main>""",
theme="#1a73e8")

add(C, "man-page", "Man Page", "Manual", "A Unix manual page for the missing page, with name, synopsis and 'see also'.",
"""body{background:#fdfdfb;color:#222;font-family:"Courier Prime",monospace;padding:clamp(1.5rem,5vw,4rem)}
main{max-width:46rem;margin:0 auto;line-height:1.7}
.hd{display:flex;justify-content:space-between;font-weight:700}
h2{font-size:1rem;margin:1.6rem 0 .3rem}h2+p,h2+div{margin:0 0 0 3rem}
h1{font-size:1rem;display:inline;font-weight:400}a{color:#1848a0}""",
"""<main><div class="hd"><span>PAGE(404)</span><span>Site Manual</span><span>PAGE(404)</span></div>
<h2>NAME</h2><p><h1>page, the page you wanted: not found</h1></p>
<h2>SYNOPSIS</h2><p>page [--moved] [--deleted] [--typo]</p>
<h2>DESCRIPTION</h2><p>The requested page does not exist on this server. It may have been moved or deleted, or the address may contain a typo.</p>
<h2>SEE ALSO</h2><p><a href="/">home(1)</a>, <a href="/search">search(1)</a>, <a href="/contact">contact(7)</a></p></main>""",
fonts=["Courier Prime:wght@400;700"], theme="#1848a0")

add(C, "compiler-error", "Compiler Error", "Buildbot", "A build that failed with a friendly compiler message pointing to the typo.",
"""body{display:grid;place-items:center;background:#282c34;color:#abb2bf;font-family:"Ubuntu Mono",monospace;padding:1.5rem;font-size:1.05rem}
main{width:min(96vw,640px)}
.l{line-height:1.7}.r{color:#e06c75;font-weight:700}.b{color:#61afef}.g{color:#98c379}.y{color:#e5c07b}
.src{margin:.3rem 0;padding-left:1rem;border-left:2px solid #3e4451}
h1{font-size:inherit;display:inline;margin:0}a{color:#98c379}""",
"""<main><div class="l"><span class="r">error[E404]</span>: <h1>page not found</h1></div>
<div class="l"> <span class="b">--&gt;</span> your-browser:1:9</div>
<div class="src">GET /the-page-you-wanted<br><span class="r">&nbsp;&nbsp;&nbsp;&nbsp;^^^^^^^^^^^^^^^^^^^^^ no page with this name</span></div>
<div class="l"><span class="g">help</span>: did you mean <a href="/">/</a> (the home page)?</div>
<div class="l"><span class="y">note</span>: the page may have been moved or deleted</div></main>""",
fonts=["Ubuntu Mono:wght@400;700"], theme="#e06c75")

add(C, "regex-test", "Regex Tester", "Patternly", "A regex tester where the pattern for the page matches nothing at all.",
"""body{display:grid;place-items:center;background:#f5f7fb;color:#1c2333;font-family:"Inter",system-ui,sans-serif;padding:1.5rem}
main{width:min(94vw,560px)}
h1{font-size:1.8rem;margin:0 0 1.2rem}
label{display:block;font-size:.85rem;color:#5b6475;margin:1rem 0 .3rem}
.box{background:#fff;border:1.5px solid #d7dce6;border-radius:10px;padding:.8rem 1rem;font-family:"JetBrains Mono",monospace}
.re{color:#7c3aed}.res{color:#dc2626;font-weight:600}
a{display:inline-block;margin-top:1.4rem;color:#7c3aed;font-weight:700}""",
"""<main><h1>No match found (404)</h1><label>Pattern</label><div class="box re">/^the-page-you-want$/</div><label>Tested against this site</label><div class="box">home, blog, docs, contact, about</div><label>Result</label><div class="box res">0 matches</div><a href="/">Try the home page instead</a></main>""",
fonts=["Inter:wght@400;700", "JetBrains Mono"], theme="#7c3aed")
