#!/usr/bin/env python3
"""
Build the data behind /feeds.

Reads _pages/feeds.opml, fetches every feed listed in it, and writes the newest
items to _data/feeds.json. Jekyll then renders /feeds at build time.

Why build-time and not client-side: Neocities sends
`Content-Security-Policy: ... connect-src 'self' ...` to free accounts, so
in-browser fetch() to any other domain is blocked. Doing the fetching here means
the page is plain HTML by the time it lands on Neocities.

    pip install feedparser
    python scripts/fetch_feeds.py
"""

import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from xml.etree import ElementTree

import feedparser

ROOT = Path(__file__).resolve().parent.parent
OPML = ROOT / "_pages" / "feeds.opml"
OUT = ROOT / "_data" / "feeds.json"

MAX_ITEMS = 100          # items rendered on /feeds
PER_FEED = 3             # newest items taken from any one feed
TIMEOUT = 20
WORKERS = 8


def read_opml(path: Path):
    """Return [(title, xml_url)] for every <outline> with an xmlUrl."""
    if not path.exists():
        sys.exit(f"no OPML at {path}")
    tree = ElementTree.parse(path)
    feeds = []
    for node in tree.iter("outline"):
        url = node.get("xmlUrl")
        if url:
            feeds.append((node.get("title") or node.get("text") or "", url))
    return feeds


def clean(html: str, limit: int = 280) -> str:
    text = re.sub(r"<[^>]+>", " ", html or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit].rstrip() + ("…" if len(text) > limit else "")


def entry_time(entry):
    for key in ("published_parsed", "updated_parsed"):
        value = entry.get(key)
        if value:
            return time.mktime(value)
    return 0.0


def pull(feed):
    title, url = feed
    try:
        parsed = feedparser.parse(url, agent="basedgirl.neocities.org/feeds")
    except Exception as exc:  # a dead blog must not fail the build
        print(f"  !! {url}: {exc}")
        return []

    site_name = title or parsed.feed.get("title") or url
    site_link = parsed.feed.get("link") or url
    items = []
    for entry in parsed.entries[:PER_FEED]:
        ts = entry_time(entry)
        if not entry.get("link"):
            continue
        items.append({
            "title": entry.get("title") or "(untitled)",
            "url": entry.get("link"),
            "site": site_name,
            "site_url": site_link,
            "date": time.strftime("%Y-%m-%d", time.localtime(ts)) if ts else "",
            "timestamp": int(ts),
            "summary": clean(entry.get("summary", "")),
        })
    print(f"  ok {len(items):>2}  {site_name}")
    return items


def main():
    feeds = read_opml(OPML)
    print(f"fetching {len(feeds)} feeds from {OPML.name}")

    socket_timeout(TIMEOUT)
    items = []
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        for result in pool.map(pull, feeds):
            items.extend(result)

    items.sort(key=lambda i: i["timestamp"], reverse=True)
    items = items[:MAX_ITEMS]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "generated": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
        "feed_count": len(feeds),
        "items": items,
    }, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {len(items)} items -> {OUT.relative_to(ROOT)}")


def socket_timeout(seconds):
    import socket
    socket.setdefaulttimeout(seconds)


if __name__ == "__main__":
    main()
