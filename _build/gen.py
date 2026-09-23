"""Writes all 100 templates to <category>/<slug>/index.html."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import core  # noqa: E402

for m in ["c_minimal", "c_illustrated", "c_animated", "c_interactive", "c_dark", "c_retro", "c_developer",
          "c_business", "c_ecommerce", "c_seasonal"]:
    __import__(m)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    for p in core.PAGES:
        d = os.path.join(ROOT, p["category"], p["slug"])
        os.makedirs(d, exist_ok=True)
        html = core.page(p, p["css"], p["body"], p["script"], p["fonts"], p["theme"])
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
    print("wrote", len(core.PAGES), "templates")


if __name__ == "__main__":
    main()
