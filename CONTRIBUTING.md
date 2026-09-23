# Contributing

Thank you for helping. New 404 templates, fixes and ideas are all welcome.

## Adding a template

Templates are generated from Python files in `_build/`, one file per category (for example `_build/c_minimal.py`). Each template is one `add(...)` call with its name, a short description, CSS and HTML.

1. Add your template to the right category file.
2. Run `python3 _build/gen.py` to write the HTML files.
3. Run `python3 _build/shot.py` to take screenshots (needs Playwright with Chromium and Pillow).
4. Run `python3 _build/site.py` to rebuild the website and README.
5. Open a pull request with a screenshot.

## Rules for templates

- One HTML file, with the CSS and any JavaScript inside
- Must work on a 360 pixel wide phone
- A real `h1`, and a link back to `/`
- Keep the `noindex` robots tag
- Respect `prefers-reduced-motion`
- Plain, friendly English, no lorem ipsum
- No copyrighted images, logos or characters

## Code of conduct

Please follow the [code of conduct](CODE_OF_CONDUCT.md).
