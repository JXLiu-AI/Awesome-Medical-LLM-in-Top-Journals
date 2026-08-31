#!/usr/bin/env python3
"""用当前 filters.json 重新审视已入库的论文，剔除不再命中的。

    python3 scripts/prune.py --dry-run   # 只看会剔除哪些
    python3 scripts/prune.py             # 真的剔除

改了关键词表之后用它清理历史数据。manual 条目和人工标了 kept 的不动。
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from fetch import _pat, bad_title  # noqa: E402


def main():
    dry = "--dry-run" in sys.argv
    flt = json.loads((ROOT / "config/filters.json").read_text(encoding="utf-8"))
    db = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))
    keep, drop = [], []
    for p in db["papers"]:
        if p.get("manual") or p.get("status") == "kept":
            keep.append(p); continue
        lead = f"{p.get('title','')} {p.get('abstract','')}".lower()
        bad = [t.lower() for t in flt.get("exclude_pub_types", [])]
        ok = (not bad_title(p.get("title", ""), flt)
              and not any(p["doi"].startswith(x) for x in flt.get("exclude_doi_prefix", []))
              and not any(any(b in t for b in bad) for t in p.get("pub_types", []))
              and (any(re.search(_pat(k), lead) for k in flt["include"])
                   or any(re.search(_pat(k), lead)
                          for k in flt.get("include_topics", {}).get("terms", [])))
              and not any(re.search(_pat(k), lead) for k in flt["exclude"])
              and any(re.search(_pat(k), lead) for k in flt["medical_hint"]))
        (keep if ok else drop).append(p)
    for p in drop:
        print(f"  - [{p['journal']}] {p['date']} {p['title'][:70]}")
    print(f"\n剔除 {len(drop)} 篇，剩 {len(keep)} 篇")
    if not dry:
        db["papers"] = keep
        (ROOT / "data/papers.json").write_text(
            json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
