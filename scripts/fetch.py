#!/usr/bin/env python3
"""从 Europe PMC 拉取白名单刊物上的医学大模型论文，增量并入 data/papers.json。

只用标准库，GitHub Actions 里无需装依赖。
用法：
    python3 scripts/fetch.py            # 增量抓取
    python3 scripts/fetch.py --dry-run  # 只打印新命中，不写盘
"""
import json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
UA = {"User-Agent": "awesome-medical-llm-bot/1.0 (github action)"}
GITHUB_RE = re.compile(r"https?://github\.com/[\w.\-]+/[\w.\-]+", re.I)


def load(p, default):
    f = ROOT / p
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else default


def query_journal(aliases, date_from, include, page_size=100):
    """拉取某刊在 date_from 之后、且命中任一关键词的文章（分页）。

    关键词下推到 Europe PMC 查询里，避免把 Nature Communications 这类大刊整本拉下来。
    """
    jq = " OR ".join(f'JOURNAL:"{a}"' for a in aliases)
    kq = " OR ".join(f'"{k}"' for k in include)
    q = f'({jq}) AND ({kq}) AND (FIRST_PDATE:[{date_from} TO 2100-01-01])'
    cursor, out = "*", []
    while True:
        params = urllib.parse.urlencode({
            "query": q, "format": "json", "pageSize": page_size,
            "resultType": "core", "cursorMark": cursor,
        })
        req = urllib.request.Request(f"{API}?{params}", headers=UA)
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read().decode("utf-8"))
        hits = data.get("resultList", {}).get("result", [])
        out.extend(hits)
        nxt = data.get("nextCursorMark")
        if not hits or not nxt or nxt == cursor:
            break
        cursor = nxt
        time.sleep(0.3)
    return out


def pub_types(rec):
    pt = rec.get("pubTypeList", {}).get("pubType", [])
    return [str(t).lower() for t in (pt if isinstance(pt, list) else [pt])]


def _hit(blob, terms):
    """短词（如 LLM、GPT-4、Med）按词边界匹配，长短语按子串匹配。"""
    for t in terms:
        t = t.lower()
        if len(t) <= 6 and " " not in t:
            if re.search(rf"(?<![a-z0-9]){re.escape(t)}(?![a-z0-9])", blob):
                return t
        elif t in blob:
            return t
    return None


def matches(rec, flt):
    types = pub_types(rec)
    bad = [t.lower() for t in flt.get("exclude_pub_types", [])]
    if any(any(b in t for b in bad) for t in types):
        return False
    # 只看标题 + 摘要前 lead_chars 字（论文的定位句），避免讨论段里顺带提一句就被捞进来
    lead = int(flt.get("lead_chars", 700))
    blob = f"{rec.get('title','')} {(rec.get('abstractText','') or '')[:lead]}".lower()
    full = f"{rec.get('title','')} {rec.get('abstractText','')}".lower()
    if not _hit(blob, flt["include"]):
        return False
    if _hit(full, flt["exclude"]):
        return False
    if flt.get("must_be_medical") and not _hit(blob, flt["medical_hint"]):
        return False
    return True


def to_entry(rec, group, journal_display):
    doi = (rec.get("doi") or "").lower()
    au = rec.get("authorString", "")
    first = au.split(",")[0].strip() if au else ""
    abstract = rec.get("abstractText", "") or ""
    code = GITHUB_RE.search(abstract)
    return {
        "doi": doi,
        "pmid": rec.get("pmid", ""),
        "title": (rec.get("title") or "").rstrip("."),
        "journal": journal_display,
        "group": group,
        "date": rec.get("firstPublicationDate", ""),
        "year": (rec.get("pubYear") or rec.get("firstPublicationDate", "")[:4]),
        "first_author": first,
        "url": f"https://doi.org/{doi}" if doi else
               (f"https://pubmed.ncbi.nlm.nih.gov/{rec.get('pmid')}/" if rec.get("pmid") else ""),
        "code": code.group(0).rstrip(".)") if code else "",
        "abstract": abstract[:600],
        "pub_types": pub_types(rec),
        "tags": [],          # 人工补：模型类型 / 科室 / 任务
        "highlight": False,  # 人工标：值得置顶的重磅工作
        "status": "new",     # new -> 人工审过改成 kept；不想要的改成 rejected
    }


def main():
    dry = "--dry-run" in sys.argv
    venues = load("config/venues.json", {})
    flt = load("config/filters.json", {})
    db = load("data/papers.json", {"papers": []})
    known = {p["doi"] or p["pmid"]: p for p in db["papers"]}

    added = 0
    for g in venues["groups"]:
        for j in g["journals"]:
            if not j.get("enabled", True):
                continue
            try:
                recs = query_journal(j["aliases"], flt["date_from"], flt["include"])
            except Exception as e:
                print(f"  ! {j['display']} 抓取失败: {e}", file=sys.stderr)
                continue
            hit = [r for r in recs if matches(r, flt)]
            fresh = 0
            for r in hit:
                e = to_entry(r, g["name"], j["display"])
                k = e["doi"] or e["pmid"]
                if not k or k in known:
                    continue
                known[k] = e
                db["papers"].append(e)
                fresh += 1
                added += 1
                print(f"  + [{j['display']}] {e['date']} {e['title'][:80]}")
            print(f"{j['display']}: 扫描 {len(recs)} 篇 / 命中 {len(hit)} 篇 / 新增 {fresh} 篇")

    db["papers"].sort(key=lambda p: (p.get("date") or ""), reverse=True)
    print(f"\n合计新增 {added} 篇，库内共 {len(db['papers'])} 篇")
    if not dry:
        (ROOT / "data").mkdir(exist_ok=True)
        (ROOT / "data/papers.json").write_text(
            json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
