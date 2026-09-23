"""Takes a screenshot of every template (needs Playwright with Chromium)."""
import glob
import os

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLOW = {"typewriter": 4300, "falling-letters": 1800, "loading-bar": 2400}

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 750})
    for f in sorted(glob.glob(os.path.join(ROOT, "*", "*", "index.html"))):
        d = os.path.dirname(f)
        slug = os.path.basename(d)
        pg.goto("file://" + f, wait_until="networkidle")
        pg.wait_for_timeout(SLOW.get(slug, 1300))
        png = os.path.join(d, "screenshot.png")
        pg.screenshot(path=png)
        im = Image.open(png).convert("RGB")
        im.save(png, optimize=True)
        im.resize((600, 375), Image.LANCZOS).save(os.path.join(d, "thumb.webp"), "WEBP", quality=80, method=6)
    b.close()
print("screenshots done")
