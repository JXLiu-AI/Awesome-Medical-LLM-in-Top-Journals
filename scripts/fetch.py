#!/usr/bin/env python3
"""从 Europe PMC 拉取白名单刊物上的医学大模型论文，增量并入 data/papers.json。

只用标准库，GitHub Actions 里无需装依赖。
用法：
    python3 scripts/fetch.py            # 增量抓取
    python3 scripts/fetch.py --dry-run  # 只打印新命中，不写盘
"""
import datetime, fcntl, json, re, sys, time, urllib.parse, urllib.request
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


def _pat(term):
    """前边界一律要求；后边界只给缩写和带数字的词，不给词干。

    按长度判断会两头出错：ambient AI 有 10 个字符不加边界就命中 ambient air；
    clinic、biomed 只有 6 个字符，加了边界反而匹配不上 clinical、biomedical。
    缩写全大写（PET、LLM、EHR）或带数字（GPT-4），词干是小写，据此区分。
    边界前允许一个复数 s，否则 large language model 匹配不上 Large Language Models。
    """
    last = term.split()[-1] if " " in term else term
    tail = "s?(?![a-z0-9])" if (last.isupper() or any(c.isdigit() for c in last)) else ""
    return rf"(?<![a-z0-9]){re.escape(term.lower())}{tail}"


def _hit(blob, terms):
    for t in terms:
        if re.search(_pat(t), blob):
            return t
    return None


CROSSREF = "https://api.crossref.org/journals/{issn}/works"


def query_crossref(issn, date_from):
    """Crossref 按 ISSN 拉全刊。Europe PMC 对 Nature Machine Intelligence、
    Nature Reviews Bioengineering、NEJM AI 这几本的收录只有 7%~13%，靠它补齐。"""
    cur, out = "*", []
    while True:
        params = urllib.parse.urlencode({
            "filter": f"from-pub-date:{date_from},type:journal-article",
            "rows": 1000, "cursor": cur,
            "select": "DOI,title,abstract,container-title,published,author,type",
            "mailto": "noreply@example.com",
        })
        req = urllib.request.Request(CROSSREF.format(issn=issn) + "?" + params, headers=UA)
        with urllib.request.urlopen(req, timeout=90) as r:
            d = json.loads(r.read().decode("utf-8"))
        items = d["message"].get("items", [])
        out.extend(items)
        nxt = d["message"].get("next-cursor")
        if not items or not nxt or nxt == cur:
            break
        cur = nxt
        time.sleep(0.2)
    return out


def cr_to_epmc(it):
    """把 Crossref 记录整形成 Europe PMC 的字段名，好走同一套 matches()。"""
    title = " ".join(it.get("title") or []).strip()
    ab = re.sub(r"<[^>]+>", " ", it.get("abstract", "") or "")
    ab = re.sub(r"\s+", " ", ab).strip()
    parts = (it.get("published", {}) or {}).get("date-parts", [[]])[0]
    date = "-".join(f"{p:02d}" if i else str(p) for i, p in enumerate(parts)) if parts else ""
    while len(date.split("-")) < 3:
        date += "-01"
    au = it.get("author") or []
    astr = ", ".join(f"{a.get('family','')} {a.get('given','')[:1]}".strip() for a in au[:3])
    sub = (it.get("subtype") or "").lower()
    pt = ["journal article"] if sub in ("", "article") else [sub]
    if re.match(r"^(author )?correction|^erratum|^retraction", title, re.I):
        pt = ["correction"]
    return {"title": title, "abstractText": ab, "doi": it.get("DOI", "").lower(),
            "pmid": "", "firstPublicationDate": date, "pubYear": date[:4],
            "authorString": astr, "pubTypeList": {"pubType": pt}}


def bad_title(title, flt):
    """Crossref 记录没有 pubType，只能从标题识别来信、社论、勘误。"""
    t = re.sub(r"^[\s\"'\u201c\u2018]+", "", (title or "").lower())
    return any(re.match(rf"{re.escape(x)}\b", t) for x in flt.get("exclude_title_prefix", []))


def matches(rec, flt):
    if bad_title(rec.get("title", ""), flt):
        return False
    doi = (rec.get("doi") or "").lower()
    if any(doi.startswith(x) for x in flt.get("exclude_doi_prefix", [])):
        return False   # Nature 新闻走 10.1038/d41586 前缀
    types = pub_types(rec)
    bad = [t.lower() for t in flt.get("exclude_pub_types", [])]
    if any(any(b in t for b in bad) for t in types):
        return False
    # 只看标题 + 摘要前 lead_chars 字（论文的定位句），避免讨论段里顺带提一句就被捞进来
    lead = int(flt.get("lead_chars", 700))
    blob = f"{rec.get('title','')} {(rec.get('abstractText','') or '')[:lead]}".lower()
    full = f"{rec.get('title','')} {rec.get('abstractText','')}".lower()
    topic = _hit(blob, flt.get("include_topics", {}).get("terms", []))
    if not _hit(blob, flt["include"]) and not topic:
        return False
    if _hit(full, flt["exclude"]):
        return False
    if flt.get("must_be_medical") and not _hit(blob, flt["medical_hint"]):
        return False
    return True


BATCH = datetime.date.today().isoformat()


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
        "source": "epmc" if rec.get("pmid") else "crossref",
        "added_batch": BATCH,   # 本条是哪一次同步捞进来的，render 据此标"本次新增"
        "tags": [],          # 人工补：模型类型 / 科室 / 任务
        "highlight": False,  # 人工标：值得置顶的重磅工作
        "status": "new",     # new -> 人工审过改成 kept；不想要的改成 rejected
    }


def main():
    # 抓取要跑十几分钟，期间若有别的脚本（add.py 等）写库，结果会被互相覆盖。
    lock = open(ROOT / "data/.lock", "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        sys.exit("data/papers.json 正被另一个进程写入，稍后再试")

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
            if j.get("issn"):
                try:
                    recs += [cr_to_epmc(x) for x in query_crossref(j["issn"], flt["date_from"])]
                except Exception as e:
                    print(f"  ! {j['display']} Crossref 失败: {e}", file=sys.stderr)
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

    db.setdefault("batches", [])
    if added:
        db["batches"] = [b for b in db["batches"] if b["batch"] != BATCH]
        db["batches"].append({"batch": BATCH, "added": added})
        db["batches"].sort(key=lambda b: b["batch"])
    db["latest_batch"] = BATCH if added else db.get("latest_batch", "")
    db["papers"].sort(key=lambda p: (p.get("date") or ""), reverse=True)
    print(f"\n合计新增 {added} 篇，库内共 {len(db['papers'])} 篇")
    if not dry:
        (ROOT / "data").mkdir(exist_ok=True)
        (ROOT / "data/papers.json").write_text(
            json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
