#!/usr/bin/env python3
"""由 data/papers.json 重新生成 README.md 的论文区（模板：README.template.md）。"""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARK_A, MARK_B = "<!-- PAPERS:BEGIN -->", "<!-- PAPERS:END -->"
STAT_A, STAT_B = "<!-- STATS:BEGIN -->", "<!-- STATS:END -->"


def row(p):
    star = "⭐ " if p.get("highlight") else ""
    title = f"[{p['title']}]({p['url']})" if p["url"] else p["title"]
    code = f" [[code]]({p['code']})" if p.get("code") else ""
    tags = " ".join(f"`{t}`" for t in p.get("tags", []))
    au = f"{p['first_author']} et al." if p.get("first_author") else ""
    return f"- {star}**{title}**{code}<br/>{au} · *{p['journal']}* · {p['date']} {tags}".rstrip()


def main():
    db = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))
    venues = json.loads((ROOT / "config/venues.json").read_text(encoding="utf-8"))
    papers = [p for p in db["papers"] if p.get("status") != "rejected"]

    order = [(g["name"], g.get("emoji", ""),
              [(j["display"], j.get("tier", 2)) for j in g["journals"] if j.get("enabled", True)])
             for g in venues["groups"]]
    by_gj = defaultdict(lambda: defaultdict(list))
    for p in papers:
        by_gj[p["group"]][p["journal"]].append(p)

    out = []
    for gname, emoji, journals in order:
        if not by_gj.get(gname):
            continue
        out.append(f"### {emoji} {gname}\n")
        for jd, tier in journals:
            items = by_gj[gname].get(jd)
            if not items:
                continue
            items.sort(key=lambda p: p.get("date", ""), reverse=True)
            openness = " open" if tier == 1 else ""
            badge = "" if tier == 1 else " · <sub>Tier 2</sub>"
            out.append(f"<details{openness}>\n<summary><b>{jd}</b>（{len(items)}）{badge}</summary>\n")
            out.extend(row(p) for p in items)
            out.append("\n</details>\n")
    papers_md = "\n".join(out)

    hi = sorted([p for p in papers if p.get("highlight")],
                key=lambda p: p.get("date", ""), reverse=True)
    recent = sorted(papers, key=lambda p: p.get("date", ""), reverse=True)[:15]
    top_md = ""
    if hi:
        top_md += "#### 🏆 里程碑\n\n" + "\n".join(row(p) for p in hi) + "\n\n"
    top_md += "#### 🆕 最近收录\n\n" + "\n".join(row(p) for p in recent)
    papers_md = top_md + "\n\n---\n\n" + papers_md

    # 统计表
    counts = defaultdict(int)
    for p in papers:
        counts[p["journal"]] += 1
    stats = ["| 刊物 | 收录数 |", "| --- | ---: |"]
    stats += [f"| {j} | {c} |" for j, c in sorted(counts.items(), key=lambda x: -x[1])]
    stats.append(f"| **合计** | **{len(papers)}** |")
    stats_md = "\n".join(stats)

    tpl = (ROOT / "README.template.md").read_text(encoding="utf-8")
    def splice(text, a, b, body):
        head, rest = text.split(a, 1)
        _, tail = rest.split(b, 1)
        return f"{head}{a}\n{body}\n{b}{tail}"
    tpl = splice(tpl, MARK_A, MARK_B, papers_md)
    tpl = splice(tpl, STAT_A, STAT_B, stats_md)
    (ROOT / "README.md").write_text(tpl, encoding="utf-8")
    print(f"README.md 已生成：{len(papers)} 篇")


if __name__ == "__main__":
    main()
