#!/usr/bin/env python3
"""Catch the things that break when you move a Jekyll site around."""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors, warnings = [], []

TEXT = {".html", ".md", ".xml", ".json", ".yml", ".rss", ".opml", ".txt", ".css"}
files = [p for p in ROOT.rglob("*") if p.is_file() and p.suffix.lower() in TEXT]

def read(p):
    try: return p.read_text(encoding="utf-8")
    except UnicodeDecodeError: return ""

# 1. every {% include x %} resolves
includes = {p.name for p in (ROOT / "_includes").glob("*")}
for p in files:
    for m in re.finditer(r"\{%\s*include\s+([\w.\-/]+)", read(p)):
        if m.group(1) not in includes:
            errors.append(f"missing include '{m.group(1)}' referenced by {p.relative_to(ROOT)}")

# 2. every layout: x resolves
layouts = {p.stem for p in (ROOT / "_layouts").glob("*.html")}
for p in files:
    t = read(p)
    if not t.startswith("---"): continue
    try: fm = t[3:t.index("---", 3)]
    except ValueError: continue
    m = re.search(r"^layout:\s*[\"']?([\w\-]+)", fm, re.M)
    if m and m.group(1) not in layouts:
        errors.append(f"missing layout '{m.group(1)}' used by {p.relative_to(ROOT)}")

# layouts declared in _config defaults
cfg = read(ROOT / "_config.yml")
for m in re.finditer(r'layout:\s*"([\w\-]+)"', cfg):
    if m.group(1) not in layouts:
        errors.append(f"_config.yml default layout '{m.group(1)}' does not exist")
# the gallery plugin hardcodes one
if "gallery" not in layouts:
    errors.append("_plugins/graphics_gallery.rb needs _layouts/gallery.html")

# 3. every file in _pages declares a permalink (else it serves from /_pages/...)
for p in (ROOT / "_pages").rglob("*"):
    if not p.is_file(): continue
    t = read(p)
    if not t.startswith("---"):
        errors.append(f"{p.relative_to(ROOT)} has no front matter -> would render at /_pages/...")
        continue
    fm = t[3:t.index("---", 3)] if "---" in t[3:] else ""
    if "permalink:" not in fm:
        errors.append(f"{p.relative_to(ROOT)} has no permalink -> would render at /_pages/...")

# 4. local asset references exist on disk
ref = re.compile(r'(?:src|href)="(/(?:assets|graphics)/[^"]+)"')
for p in files:
    for m in ref.finditer(read(p)):
        target = ROOT / m.group(1).lstrip("/").split("?")[0]
        if not target.exists():
            errors.append(f"broken asset {m.group(1)} in {p.relative_to(ROOT)}")

# 5. leftovers from the original site
for p in files:
    if p.parts[-2:][0] in ("_posts", "_library", "_wiki"): continue
    t = read(p)
    for needle in ("tomcritchlow.com", "tjcritchlow", "buttondown.email"):
        if needle in t and p.name not in ("README.md", "_config.yml", "about.md"):
            warnings.append(f"'{needle}' still in {p.relative_to(ROOT)}")

# 6. the invalid `| limit:` filter inside for tags
for p in files:
    if re.search(r"\{%\s*for\s+\w+\s+in\s+[\w.]+\s*\|\s*limit", read(p)):
        errors.append(f"invalid `| limit:` inside for tag in {p.relative_to(ROOT)}")

# 7. nothing Neocities free will reject
ALLOWED = set("apng asc atom avif bin cjs css csv dae eot epub geojson gif glb glsl gltf gpg htm "
              "html ico jpeg jpg js json jxl key kml knowl less manifest map markdown md mf mid "
              "midi mjs mtl obj opml osdx otf pdf pgp pls png py rdf resolveHandle rss sass scss "
              "sf2 svg text toml ts tsv ttf txt webapp webmanifest webp woff woff2 xcf xml yaml yml".split())
for p in ROOT.rglob("*"):
    if not p.is_file(): continue
    rel = p.relative_to(ROOT)
    if rel.parts[0] in (".github", "_plugins", "scripts", "_data", "_layouts", "_includes"): continue
    if rel.name in ("Gemfile", "README.md", ".gitignore", "_config.yml", ".gitkeep"): continue
    ext = p.suffix.lstrip(".").lower()
    if ext and ext not in ALLOWED:
        warnings.append(f"Neocities free would reject .{ext}: {rel}")

# 8. nav targets resolve to a real permalink somewhere
perms = set()
for p in files:
    t = read(p)
    if t.startswith("---"):
        fm = t[3:t.index("---", 3)] if "---" in t[3:] else ""
        m = re.search(r"^permalink:\s*(\S+)", fm, re.M)
        if m: perms.add(m.group(1))
perms |= {"/wiki/", "/library/", "/graphics/"}  # collections + generated
nav = read(ROOT / "_data/nav.yml")
for m in re.finditer(r'url:\s*"(/[^"]*)"', nav):
    u = m.group(1)
    if u == "/": continue
    if u not in perms:
        errors.append(f"nav points at {u} but no page declares that permalink")

print("=" * 62)
for e in errors:   print("ERROR   ", e)
for w in warnings: print("warning ", w)
print("=" * 62)
print(f"{len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
