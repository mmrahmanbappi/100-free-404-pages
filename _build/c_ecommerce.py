from core import add

C = "ecommerce"

def product(name, price, color, shape="circle"):
    art = {"circle": f'<circle cx="50" cy="50" r="28" fill="{color}"/>',
           "bag": f'<path d="M25 38 h50 l-5 42 h-40 z" fill="{color}"/><path d="M38 38 v-8 a12 12 0 0 1 24 0 v8" stroke="{color}" stroke-width="5" fill="none"/>',
           "shoe": f'<path d="M15 62 q10 -22 30 -18 l20 8 q18 4 20 16 v6 h-70z" fill="{color}"/>',
           "cup": f'<path d="M30 30 h36 l-4 44 h-28z" fill="{color}"/><path d="M66 40 q14 0 10 16 q-3 8 -12 6" stroke="{color}" stroke-width="5" fill="none"/>',
           "lamp": f'<path d="M35 25 h30 l10 25 h-50z" fill="{color}"/><rect x="47" y="50" width="6" height="25" fill="#555"/><rect x="35" y="75" width="30" height="5" rx="2" fill="#555"/>',
           "shirt": f'<path d="M35 22 l15 8 l15 -8 l18 12 l-8 12 l-8 -4 v36 h-34 v-36 l-8 4 l-8 -12z" fill="{color}"/>'}[shape]
    return f'<a class="pr" href="/shop"><div class="im"><svg viewBox="0 0 100 100">{art}</svg></div><b>{name}</b><span>{price}</span></a>'

GRID = """.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(10rem,1fr));gap:1rem;margin-top:1.5rem}
.pr{text-decoration:none;color:inherit;display:block}.pr .im{aspect-ratio:1;border-radius:14px;display:grid;place-items:center;margin-bottom:.5rem}.pr svg{width:70%}.pr b{display:block;font-size:.98rem}.pr span{opacity:.7;font-size:.92rem}"""

add(C, "out-of-stock", "Out of Stock", "Northfield Goods", "A product page that says 'out of stock' and shows four similar products.",
GRID + """body{background:#fff;color:#1f2933;font-family:"DM Sans",system-ui,sans-serif}
main{max-width:62rem;margin:0 auto;padding:clamp(2rem,6vw,4rem) 1.5rem}
.tag{display:inline-block;background:#fee2e2;color:#b91c1c;font-weight:700;padding:.3rem .8rem;border-radius:6px}
h1{font-size:clamp(2rem,5vw,2.8rem);margin:.8rem 0 .6rem}p{color:#52606d;font-size:1.1rem}
.pr .im{background:#f3f4f6}a.b{display:inline-block;margin-top:1rem;background:#1f2933;color:#fff;padding:.8rem 1.3rem;border-radius:10px;text-decoration:none;font-weight:700}""",
"""<main><span class="tag">404, out of stock forever</span><h1>This product is no longer here</h1><p>It may have sold out or been removed from our shop. Here are some things you might like instead.</p><a class="b" href="/shop">Browse the shop</a><div class="pgrid">"""
+ product("Canvas Tote", "$24", "#d97706", "bag") + product("Everyday Mug", "$14", "#2563eb", "cup") + product("Desk Lamp", "$49", "#059669", "lamp") + product("Soft Tee", "$19", "#db2777", "shirt") + "</div></main>",
fonts=["DM Sans:wght@400;700"], theme="#1f2933")

add(C, "empty-cart", "Empty Cart", "Basketful", "A shopping cart icon with nothing inside and a button to keep shopping.",
"""body{display:grid;place-items:center;background:#fef9c3;color:#422006;font-family:"Rubik",system-ui,sans-serif;text-align:center;padding:2rem}
svg{width:min(60vw,220px);margin:0 auto 1.5rem}
h1{font-size:clamp(2rem,6vw,2.8rem);margin:0 0 .6rem}p{font-size:1.1rem;opacity:.8;margin:0 0 1.8rem}
a{display:inline-block;background:#ca8a04;color:#fff;padding:.9rem 1.5rem;border-radius:12px;text-decoration:none;font-weight:700}""",
"""<main><svg viewBox="0 0 200 160" aria-hidden="true"><path d="M10 20 h30 l20 90 h100 l20 -70 h-130" fill="none" stroke="#422006" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="75" cy="135" r="12" fill="#422006"/><circle cx="145" cy="135" r="12" fill="#422006"/><text x="115" y="85" font-family="Arial" font-weight="800" font-size="30" text-anchor="middle" fill="#ca8a04">404</text></svg><h1>Nothing to see in this aisle</h1><p>The page you wanted is not in our store. Your cart is safe, though.</p><a href="/shop">Keep shopping</a></main>""",
fonts=["Rubik:wght@400;700"], theme="#ca8a04")

add(C, "fashion", "Fashion Store", "Maison Vale", "An elegant fashion store page with a large serif headline and new arrivals.",
GRID + """body{background:#f7f3ee;color:#1a1a1a;font-family:"Jost",system-ui,sans-serif}
main{max-width:64rem;margin:0 auto;padding:clamp(2rem,6vw,4rem) 1.5rem}
.brand{font-family:"Cormorant Garamond",serif;font-size:1.6rem;text-align:center;margin-bottom:2.5rem}
h1{font-family:"Cormorant Garamond",serif;font-weight:500;font-size:clamp(2.6rem,7vw,4.4rem);text-align:center;margin:0}
p{text-align:center;color:#6b6259;margin:.8rem 0 1.5rem}.c{text-align:center}.c a{color:#1a1a1a;border-bottom:1px solid;text-decoration:none}
.pr .im{background:#ece5dc;border-radius:0}.pr{text-align:center}""",
"""<main><div class="brand">Maison Vale</div><h1>This piece is no longer available</h1><p>See our new arrivals for the season.</p><div class="c"><a href="/new">Shop new arrivals</a></div><div class="pgrid">"""
+ product("Linen Shirt", "$120", "#c8b6a6", "shirt") + product("Leather Tote", "$240", "#8b5e3c", "bag") + product("Suede Loafer", "$190", "#6b4f3a", "shoe") + product("Silk Scarf", "$85", "#b08968", "circle") + "</div></main>",
fonts=["Jost:wght@400;500", "Cormorant Garamond:wght@500"], theme="#8b5e3c")

add(C, "grocery", "Grocery", "Freshcart", "A grocery store page: 'this aisle is empty', with fruit and veg shortcuts.",
"""body{background:#f0fdf4;color:#14532d;font-family:"Nunito",system-ui,sans-serif}
main{max-width:56rem;margin:0 auto;padding:clamp(2rem,6vw,4rem) 1.5rem;text-align:center}
h1{font-size:clamp(2rem,6vw,3rem);margin:0 0 .5rem}p{font-size:1.1rem;color:#3f6b4f;margin:0 0 2rem}
.cats{display:flex;flex-wrap:wrap;gap:.8rem;justify-content:center}
.cats a{display:flex;align-items:center;gap:.5rem;background:#fff;border:2px solid #bbf7d0;border-radius:999px;padding:.6rem 1.1rem;text-decoration:none;font-weight:700}
.cats i{width:22px;height:22px;border-radius:50%}.search{margin:2rem auto 0;max-width:26rem;display:flex;gap:.5rem}
.search input{flex:1;padding:.8rem 1rem;border:2px solid #bbf7d0;border-radius:12px;font:inherit}.search button{background:#16a34a;color:#fff;border:0;border-radius:12px;padding:.8rem 1.1rem;font:inherit;font-weight:700}""",
"""<main><h1>Aisle 404 is empty</h1><p>We could not find that page. Try one of our fresh sections.</p><nav class="cats" aria-label="Sections"><a href="/fruit"><i style="background:#f97316"></i>Fruit</a><a href="/vegetables"><i style="background:#22c55e"></i>Vegetables</a><a href="/bakery"><i style="background:#d97706"></i>Bakery</a><a href="/dairy"><i style="background:#e5e7eb"></i>Dairy</a><a href="/offers"><i style="background:#ef4444"></i>Offers</a></nav>
<form class="search" role="search" action="/search"><label class="sr" for="q">Search products</label><input id="q" name="q" placeholder="Search products"><button>Search</button></form></main>""",
fonts=["Nunito:wght@400;800"], theme="#16a34a")

add(C, "electronics", "Electronics", "Voltmart", "A tech store page with a dark hero and a row of popular gadgets.",
GRID + """body{background:#0b0f19;color:#e5e7eb;font-family:"Manrope",system-ui,sans-serif}
main{max-width:64rem;margin:0 auto;padding:clamp(2rem,6vw,4rem) 1.5rem}
.hero{background:linear-gradient(120deg,#1e293b,#0f172a);border:1px solid #1f2a44;border-radius:20px;padding:clamp(1.5rem,5vw,3rem)}
b.n{font-size:clamp(3rem,10vw,5rem);background:linear-gradient(90deg,#22d3ee,#818cf8);-webkit-background-clip:text;background-clip:text;color:transparent}
h1{margin:.2rem 0 .6rem;font-size:clamp(1.6rem,4vw,2.2rem)}p{color:#94a3b8}
.pr .im{background:#111827;border:1px solid #1f2a44}a.b{display:inline-block;margin-top:1rem;background:#22d3ee;color:#0b0f19;padding:.8rem 1.3rem;border-radius:10px;text-decoration:none;font-weight:800}""",
"""<main><div class="hero"><b class="n" aria-hidden="true">404</b><h1>Device not found</h1><p>This product page does not exist. Check out what everyone is buying right now.</p><a class="b" href="/deals">See today's deals</a></div><div class="pgrid">"""
+ product("Wireless Buds", "$89", "#22d3ee") + product("Smart Lamp", "$59", "#818cf8", "lamp") + product("Travel Mug", "$29", "#34d399", "cup") + product("Laptop Sleeve", "$39", "#f472b6", "bag") + "</div></main>",
fonts=["Manrope:wght@400;800"], theme="#22d3ee")

add(C, "bookstore", "Bookstore", "Paper Lantern Books", "A cozy bookshop page: this chapter is missing, with a shelf of book spines.",
"""body{background:#f6efe4;color:#3e2c1c;font-family:"Lora",Georgia,serif}
main{max-width:52rem;margin:0 auto;padding:clamp(2rem,6vw,4rem) 1.5rem;text-align:center}
.shelf{display:flex;justify-content:center;align-items:flex-end;gap:6px;height:150px;border-bottom:10px solid #7a5230;margin:0 auto 2rem;max-width:26rem}
.shelf i{display:block;width:26px;border-radius:3px 3px 0 0}.shelf .gap{width:26px;height:120px;border:2px dashed #b08a5a;border-bottom:0}
h1{font-size:clamp(2rem,6vw,3rem);margin:0 0 .6rem}p{font-size:1.15rem;line-height:1.7;color:#6b5540}
a{display:inline-block;margin-top:1rem;background:#7a5230;color:#fff;padding:.85rem 1.4rem;border-radius:6px;text-decoration:none;font-family:system-ui,sans-serif;font-weight:600}""",
"""<main><div class="shelf" aria-hidden="true"><i style="height:120px;background:#9c2c2c"></i><i style="height:135px;background:#2c5f7c"></i><i style="height:110px;background:#c19a3f"></i><span class="gap"></span><i style="height:128px;background:#4d7c4a"></i><i style="height:115px;background:#6d4c7d"></i></div><h1>This chapter is missing</h1><p>Someone borrowed this page and never brought it back. Plenty of other stories are waiting on our shelves.</p><a href="/books">Browse books</a></main>""",
fonts=["Lora:wght@400;700"], theme="#7a5230"),

add(C, "furniture", "Furniture", "Oak & Linen", "A calm home store page with an empty room and a 'find it in our collections' link.",
"""body{background:#efebe4;color:#2e2a24;font-family:"Figtree",system-ui,sans-serif}
main{max-width:60rem;margin:0 auto;padding:clamp(2rem,6vw,4rem) 1.5rem;display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;align-items:center}
svg{width:100%}
h1{font-size:clamp(2rem,5vw,3rem);margin:0 0 1rem;font-weight:600}p{color:#5f574c;font-size:1.1rem;line-height:1.6}
ul{list-style:none;padding:0;margin:1.5rem 0 0;display:grid;gap:.6rem}ul a{text-decoration:none;border-bottom:1px solid #cbbfae;padding-bottom:.4rem;display:block}
@media(max-width:760px){main{grid-template-columns:1fr}}""",
"""<main><svg viewBox="0 0 300 220" aria-hidden="true"><rect x="0" y="170" width="300" height="50" fill="#d8cdbd"/><rect x="40" y="40" width="80" height="100" fill="#fff" stroke="#cbbfae" stroke-width="4"/><path d="M80 40 v100 M40 90 h80" stroke="#cbbfae" stroke-width="3"/><path d="M190 170 v-30 h70 v30" fill="none" stroke="#a58a6a" stroke-width="4" stroke-dasharray="6 6"/><text x="225" y="130" font-family="Arial" font-size="14" text-anchor="middle" fill="#a58a6a">sofa missing</text></svg>
<div><h1>This room is empty</h1><p>The item you are looking for has moved out. Our collections are full of pieces for every room.</p><ul><li><a href="/living-room">Living room</a></li><li><a href="/bedroom">Bedroom</a></li><li><a href="/lighting">Lighting</a></li><li><a href="/sale">Sale</a></li></ul></div></main>""",
fonts=["Figtree:wght@400;600"], theme="#a58a6a")

add(C, "coupon", "Coupon", "Dealday", "A tear-off coupon that gives visitors a small discount to make up for the missing page.",
"""body{display:grid;place-items:center;background:#fff1f2;color:#4c0519;font-family:"Outfit",system-ui,sans-serif;text-align:center;padding:2rem}
h1{font-size:clamp(2rem,6vw,2.8rem);margin:0 0 .6rem}p{color:#881337;margin:0 0 1.8rem}
.cp{display:flex;background:#fff;border:2px dashed #e11d48;border-radius:16px;overflow:hidden;width:min(92vw,440px);margin:0 auto 1.8rem;text-align:left}
.cp div{padding:1.2rem 1.4rem}.cp .l{flex:1}.cp .r{background:#e11d48;color:#fff;display:grid;place-items:center;font-size:1.8rem;font-weight:800}
.code{font-family:ui-monospace,monospace;font-size:1.4rem;font-weight:700;letter-spacing:.1em}
a{display:inline-block;background:#4c0519;color:#fff;padding:.85rem 1.4rem;border-radius:12px;text-decoration:none;font-weight:700}""",
"""<main><h1>Sorry, this page is missing</h1><p>To make up for it, here is a little something. Use the code at checkout.</p><div class="cp"><div class="l"><small>Your code</small><div class="code">OOPS404</div><small>10 percent off your next order</small></div><div class="r">10%</div></div><a href="/shop">Shop now</a></main>""",
fonts=["Outfit:wght@400;800"], theme="#e11d48")

add(C, "marketplace", "Marketplace", "Stallhub", "A marketplace page with a search bar and popular categories as big tiles.",
"""body{background:#f8fafc;color:#0f172a;font-family:"Inter",system-ui,sans-serif}
main{max-width:60rem;margin:0 auto;padding:clamp(2rem,6vw,4rem) 1.5rem}
h1{font-size:clamp(2rem,5vw,2.8rem);margin:0 0 .5rem}p{color:#475569;font-size:1.1rem;margin:0 0 1.5rem}
form{display:flex;background:#fff;border:2px solid #e2e8f0;border-radius:14px;overflow:hidden;margin-bottom:2rem}
input{flex:1;border:0;padding:1rem 1.1rem;font:inherit;font-size:1.05rem}button{border:0;background:#f97316;color:#fff;padding:0 1.4rem;font:inherit;font-weight:700}
.t{display:grid;grid-template-columns:repeat(auto-fit,minmax(11rem,1fr));gap:1rem}
.t a{border-radius:14px;padding:1.4rem 1.2rem;text-decoration:none;color:#fff;font-weight:800;font-size:1.15rem;min-height:110px;display:flex;align-items:flex-end}""",
"""<main><h1>We could not find that listing</h1><p>It may have sold or expired. Search for something similar, or browse a category.</p><form role="search" action="/search"><label class="sr" for="q">Search listings</label><input id="q" name="q" placeholder="What are you looking for?"><button>Search</button></form>
<nav class="t" aria-label="Categories"><a href="/c/home" style="background:#0ea5e9">Home and garden</a><a href="/c/fashion" style="background:#db2777">Fashion</a><a href="/c/electronics" style="background:#7c3aed">Electronics</a><a href="/c/vehicles" style="background:#16a34a">Vehicles</a></nav></main>""",
fonts=["Inter:wght@400;700;800"], theme="#f97316")

add(C, "gift-box", "Gift Shop", "Wrapped", "A wrapped gift box that opens to show the page is not inside, with gift ideas.",
"""body{display:grid;place-items:center;background:#ecfeff;color:#164e63;font-family:"Baloo 2",system-ui,sans-serif;text-align:center;padding:2rem}
svg{width:min(60vw,220px);margin:0 auto 1rem}
.lid{transform-origin:40px 70px;animation:open 2.5s ease-in-out infinite alternate}@keyframes open{to{transform:rotate(-18deg) translateY(-10px)}}
h1{font-size:clamp(2rem,6vw,2.8rem);margin:0 0 .5rem}p{color:#155e75;margin:0 0 1.5rem}
.ideas{display:flex;gap:.6rem;justify-content:center;flex-wrap:wrap}.ideas a{background:#fff;border:2px solid #a5f3fc;padding:.6rem 1rem;border-radius:999px;text-decoration:none;font-weight:700}""",
"""<main><svg viewBox="0 0 200 180" aria-hidden="true"><rect x="45" y="80" width="110" height="90" rx="6" fill="#06b6d4"/><rect x="92" y="80" width="16" height="90" fill="#f472b6"/><g class="lid"><rect x="38" y="60" width="124" height="26" rx="6" fill="#0891b2"/><rect x="92" y="60" width="16" height="26" fill="#f472b6"/><path d="M100 60 q-30 -30 -30 -5 q0 10 30 5 q30 5 30 -5 q0 -25 -30 5" fill="#f472b6"/></g></svg><h1>Surprise, it is empty</h1><p>The page you wanted is not in this box. Maybe one of these gift ideas will do.</p><nav class="ideas" aria-label="Gift ideas"><a href="/for-her">For her</a><a href="/for-him">For him</a><a href="/for-kids">For kids</a><a href="/under-25">Under $25</a></nav></main>""",
fonts=["Baloo 2:wght@400;800"], theme="#06b6d4")
