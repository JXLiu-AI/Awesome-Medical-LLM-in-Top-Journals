#!/usr/bin/env python3
"""按 config/specialties.json 给论文打科室标签，写进 data/papers.json 的 specialties 字段。

    python3 scripts/tag.py           # 只给没标过的打（人工改过的不动）
    python3 scripts/tag.py --force   # 全部重打，覆盖人工结果
    python3 scripts/tag.py --stats   # 只看各科室命中分布
"""
import json, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _pat(term):
    """前边界一律要求，后边界只对缩写类短词要求。

    前边界挡住 behavioral health 命中 oral health；
    后边界只给 PET、ECG、EHR 这类短词，好让 radiolog、patholog 这些词干仍能匹配 radiology、pathology。
    """
    t = term.lower()
    tail = "(?![a-z0-9])" if (len(t) <= 6 and " " not in t) else ""
    return rf"(?<![a-z0-9]){re.escape(t)}{tail}"


def hits(blob, kws):
    return sum(len(re.findall(_pat(k), blob)) for k in kws)


def main():
    force = "--force" in sys.argv
    cfg = json.loads((ROOT / "config/specialties.json").read_text(encoding="utf-8"))
    db = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))
    cap = cfg.get("max_per_paper", 3)

    changed = 0
    for p in db["papers"]:
        if p.get("specialties") and not force:
            continue
        blob = f"{p.get('title','')} {p.get('abstract','')}".lower()
        scored = [(hits(blob, s["kw"]), s["key"]) for s in cfg["specialties"]]
        picked = [k for n, k in sorted(scored, key=lambda x: -x[0]) if n > 0][:cap]
        if picked != p.get("specialties"):
            changed += 1
        p["specialties"] = picked

    if "--stats" not in sys.argv:
        (ROOT / "data/papers.json").write_text(
            json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")

    c = Counter(k for p in db["papers"] for k in p.get("specialties", []))
    name = {s["key"]: f"{s['icon']} {s['name']}" for s in cfg["specialties"]}
    for k, n in c.most_common():
        print(f"{n:4d}  {name.get(k, k)}")
    untagged = sum(1 for p in db["papers"] if not p.get("specialties"))
    print(f"\n变更 {changed} 篇；未归类 {untagged} 篇（共 {len(db['papers'])} 篇）")


if __name__ == "__main__":
    main()
