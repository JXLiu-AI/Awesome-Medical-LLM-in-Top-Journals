#!/usr/bin/env python3
"""每周审校助手：把 status=new 的论文逐条过一遍。

    python3 scripts/triage.py            # 交互式过审
    python3 scripts/triage.py --list     # 只列出待审
    python3 scripts/triage.py --keep-all # 全部标 kept（赶时间时用）

交互按键：k 保留 / r 剔除 / h 保留并标为里程碑 / t 打标签 / s 跳过 / q 保存退出
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "data/papers.json"


def main():
    db = json.loads(DB.read_text(encoding="utf-8"))
    pending = [p for p in db["papers"] if p.get("status") == "new"]
    if not pending:
        print("没有待审论文。")
        return

    if "--list" in sys.argv:
        for p in pending:
            print(f"[{p['journal']}] {p['date']} {p['title']}")
        print(f"\n共 {len(pending)} 篇待审")
        return

    if "--keep-all" in sys.argv:
        for p in pending:
            p["status"] = "kept"
        DB.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"已全部标为 kept（{len(pending)} 篇）")
        return

    for i, p in enumerate(pending, 1):
        print("\n" + "=" * 78)
        print(f"[{i}/{len(pending)}] {p['journal']} · {p['date']}")
        print(p["title"])
        print(f"  {p['url']}")
        print(f"  {p['abstract'][:300]}...")
        while True:
            a = input("  k保留 / r剔除 / h里程碑 / t标签 / s跳过 / q退出 > ").strip().lower()
            if a in ("k", ""):
                p["status"] = "kept"; break
            if a == "r":
                p["status"] = "rejected"; break
            if a == "h":
                p["status"] = "kept"; p["highlight"] = True; break
            if a == "t":
                p["tags"] = [t.strip() for t in input("  标签(逗号分隔) > ").split(",") if t.strip()]
                continue
            if a == "s":
                break
            if a == "q":
                DB.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")
                print("已保存退出。")
                return
    DB.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")
    print("审校完成，记得跑 python3 scripts/render.py")


if __name__ == "__main__":
    main()
