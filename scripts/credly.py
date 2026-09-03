#!/usr/bin/env python3
"""Render Credly badges into README.md between CREDLY markers.

Reads the public (undocumented) endpoint
https://www.credly.com/users/<user>/badges.json — no auth needed.
Stdlib only so the workflow needs no pip install.
"""

import json
import os
import re
import sys
import urllib.request
from datetime import date

USER = os.environ.get("CREDLY_USER", "muhammad-sumon-molla-selim")
SIZE = int(os.environ.get("CREDLY_BADGE_SIZE", "110"))
README = os.environ.get("README_PATH", "README.md")
START, END = "<!-- CREDLY:START -->", "<!-- CREDLY:END -->"
PROFILE = f"https://www.credly.com/users/{USER}/badges"


def fetch():
    badges, url = [], f"https://www.credly.com/users/{USER}/badges.json"
    while url:
        req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            page = json.load(r)
        badges += page["data"]
        url = page.get("metadata", {}).get("next_page_url")
    return badges


def thumb(image_url):
    # https://images.credly.com/images/<id>/image.png -> .../size/110x110/images/<id>/image.png
    return image_url.replace("images.credly.com/images/", f"images.credly.com/size/{SIZE}x{SIZE}/images/")


def render(badges):
    badges = sorted(badges, key=lambda b: b["issued_at_date"], reverse=True)
    rows = []
    for b in badges:
        name = b["badge_template"]["name"]
        img = thumb(b["image_url"] if "image_url" in b else b["badge_template"]["image_url"])
        title = f"{name} · issued {b['issued_at_date']}"
        rows.append(
            f'<a href="https://www.credly.com/badges/{b["id"]}" title="{title}">'
            f'<img src="{img}" alt="{name}" width="{SIZE}" height="{SIZE}"></a>'
        )
    body = "\n".join(rows)
    footer = (
        f'\n\n<sub>{len(badges)} badges · synced weekly from Credly · updated {date.today()} · '
        f'<a href="{PROFILE}">verify on Credly →</a></sub>'
    )
    return f"{START}\n{body}{footer}\n{END}"


def main():
    text = open(README, encoding="utf-8").read()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        sys.exit(f"markers {START} / {END} not found in {README}")
    new = pattern.sub(lambda _: render(fetch()), text)
    if new == text:
        print("no changes")
        return
    open(README, "w", encoding="utf-8").write(new)
    print("README updated")


if __name__ == "__main__":
    main()
