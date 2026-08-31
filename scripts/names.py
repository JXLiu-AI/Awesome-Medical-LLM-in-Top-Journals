#!/usr/bin/env python3
"""从标题和摘要里抽模型/系统名，写进 model 字段。

    python3 scripts/names.py           # 只补空的
    python3 scripts/names.py --force   # 全部重抽
    python3 scripts/names.py --list    # 只看抽出来的结果

DeepRare 这类工作标题里不带模型名（"An agentic system for rare disease diagnosis"），
不把名字提出来，读者按名字根本搜不到。
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 排除句首常见词，避免把 "We present a novel..." 里的 A/Novel 当成模型名
STOP = {"a", "an", "the", "this", "these", "two", "three", "here", "we", "our", "novel",
        "new", "large", "results", "data", "evidence", "using", "methods", "in", "to",
        "for", "and", "that", "it", "us", "ai", "llm", "gpt", "chatgpt", "medical",
        "clinical", "deep", "machine", "artificial", "general", "generative", "multimodal",
        "vision", "language", "foundation", "however", "although", "first", "second"}

TITLE_RE = re.compile(r"^([A-Z][A-Za-z0-9]*(?:[-‑][A-Za-z0-9]+)*)\s*[::]\s")
ABS_RE = re.compile(
    r"(?:here\s+we\s+(?:present|introduce|report|describe|develop(?:ed)?)|"
    r"we\s+(?:present|introduce|propose|report|develop(?:ed)?|describe|built|build)|"
    r"(?:named|called|termed|dubbed))\s+"
    r"([A-Z][A-Za-z0-9]*(?:[-‑][A-Za-z0-9]+)*)",
)


def trim(n):
    """去掉破折号后跟的冠词：DeepRare—a multi-agent 会被抽成 DeepRare-a。"""
    return re.sub(r"[-‑](?:a|an|the|is|was|which|that|[a-z])$", "", n)


def extract(title, abstract):
    m = TITLE_RE.match(title or "")
    if m and m.group(1).lower() not in STOP and len(m.group(1)) >= 3:
        return trim(m.group(1))
    ab = re.sub(r"<[^>]+>", " ", abstract or "")
    for m in ABS_RE.finditer(ab):
        n = m.group(1)
        if n.lower() in STOP or len(n) < 3:
            continue
        # 必须有大写字母或数字的混排特征，纯首字母大写的普通词不算
        if re.search(r"[A-Z]{2,}|[0-9]|[-‑]", n) or n[1:] != n[1:].lower():
            return trim(n)
    return ""


def main():
    force, only = "--force" in sys.argv, "--list" in sys.argv
    db = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))
    n = 0
    for p in db["papers"]:
        if p.get("model") and not force:
            continue
        got = extract(p.get("title", ""), p.get("abstract", ""))
        if got != p.get("model", ""):
            n += 1
        p["model"] = got
    if not only:
        (ROOT / "data/papers.json").write_text(
            json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")
    named = [p for p in db["papers"] if p.get("model")]
    print(f"抽到模型名 {len(named)} / {len(db['papers'])} 篇，变更 {n} 篇\n")
    for p in named[:40]:
        print(f"  {p['model']:<22} {p['title'][:66]}")


if __name__ == "__main__":
    main()
