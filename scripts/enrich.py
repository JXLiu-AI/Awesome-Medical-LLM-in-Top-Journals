#!/usr/bin/env python3
"""给 Crossref 来源的条目补文献类型。

Crossref 没有文献类型字段，社论、新闻、通讯混在 journal-article 里。
按 DOI 批量反查 Europe PMC，把它的 pubType 补上，再交给 prune.py 过滤。
"""
import json, sys, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
UA = {"User-Agent": "awesome-medical-llm-bot/1.0"}


def main():
    db = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))
    todo = [p for p in db["papers"]
            if p.get("source") == "crossref" and p.get("pub_types") == ["journal article"]]
    print(f"待补 {len(todo)} 篇")
    by_doi = {p["doi"]: p for p in todo}
    dois = list(by_doi)
    filled = 0
    for i in range(0, len(dois), 20):
        chunk = dois[i:i + 20]
        q = " OR ".join(f'DOI:"{d}"' for d in chunk)
        url = API + "?" + urllib.parse.urlencode(
            {"query": q, "format": "json", "resultType": "core", "pageSize": 25})
        try:
            r = json.loads(urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=60).read())
        except Exception as e:
            print(f"  ! {e}", file=sys.stderr); continue
        for x in r.get("resultList", {}).get("result", []):
            p = by_doi.get((x.get("doi") or "").lower())
            if not p:
                continue
            pt = x.get("pubTypeList", {}).get("pubType", [])
            pt = [str(t).lower() for t in (pt if isinstance(pt, list) else [pt])]
            if pt:
                p["pub_types"] = pt
                p["pmid"] = x.get("pmid", "") or p.get("pmid", "")
                filled += 1
        time.sleep(0.3)
    (ROOT / "data/papers.json").write_text(
        json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"补到类型 {filled} 篇")


if __name__ == "__main__":
    main()
