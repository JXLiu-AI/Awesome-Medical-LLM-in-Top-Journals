#!/usr/bin/env python3
"""按 DOI 手工加一篇论文。

    python3 scripts/add.py 10.1038/s41467-026-75718-x

元数据从 Crossref 取。手工加的条目带 manual: true，即使所在刊物在 venues.json 里
是 enabled: false 也照常渲染，方便从走量刊里单独挑几篇进来。
"""
import json, re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    doi = sys.argv[1].lower().replace("https://doi.org/", "")
    db = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))
    if any(p["doi"] == doi for p in db["papers"]):
        print("库里已经有了"); return

    url = f"https://api.crossref.org/works/{urllib.request.quote(doi)}"
    m = json.loads(urllib.request.urlopen(url, timeout=40).read())["message"]
    parts = m.get("published", {}).get("date-parts", [[]])[0]
    date = "-".join(str(x).zfill(2) if i else str(x) for i, x in enumerate(parts))
    while len(date.split("-")) < 3:
        date += "-01"
    au = m.get("author") or []
    first = f"{au[0].get('family','')} {au[0].get('given','')[:1]}".strip() if au else ""
    ab = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.get("abstract", "") or "")).strip()
    journal = (m.get("container-title") or ["?"])[0]

    venues = json.loads((ROOT / "config/venues.json").read_text(encoding="utf-8"))
    group = next((g["name"] for g in venues["groups"]
                  for j in g["journals"] if j["display"].lower() == journal.lower()), "其他")

    db["papers"].append({
        "doi": doi, "pmid": "", "title": " ".join(m.get("title") or []).rstrip("."),
        "journal": journal, "group": group, "date": date, "year": date[:4],
        "first_author": first, "url": f"https://doi.org/{doi}", "code": "",
        "abstract": ab[:600], "pub_types": ["journal article"],
        "added_batch": "manual", "specialties": [], "tags": [],
        "highlight": False, "manual": True, "status": "kept",
    })
    db["papers"].sort(key=lambda p: p.get("date") or "", reverse=True)
    (ROOT / "data/papers.json").write_text(
        json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"已加入：[{journal}] {date} {' '.join(m.get('title') or [])[:70]}")
    print("记得跑 python3 scripts/tag.py && python3 scripts/render.py")


if __name__ == "__main__":
    main()
