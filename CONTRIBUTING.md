# 收录标准

一篇论文要进列表，得同时满足三条：

1. 发表在 [config/venues.json](config/venues.json) 白名单里的刊物上。会议论文、预印本不收，Correspondence、Editorial、勘误这类也不收（抓取时按 Europe PMC 的 pubType 过滤掉了）。
2. 核心方法是大语言模型、多模态基础模型，或者建立在它们之上的智能体。传统 CNN、统计模型不算。
3. 面向临床、公共卫生或生物医学场景，不是通用 NLP。

脑机接口与脑解码是例外，走 `include_topics` 的主题级通道：主题词命中标题或摘要开头即收，不要求出现模型词。这类论文的摘要重心是病人恢复了多少功能，解码模型写在正文——Willett 那篇 Nature 语音神经假体的摘要里 `language model`、`neural network`、`transformer`、`decoder` 全都没有，卡模型词会漏掉整个领域最重要的几篇。

关键词只在标题和摘要前 700 字里匹配，长度由 `lead_chars` 控制。

数据源有两个：Europe PMC 和 Crossref。Europe PMC 对 Nature Machine Intelligence、Nature Reviews Bioengineering、NEJM AI 的收录只有 7%~13%，Crossref 按 ISSN 补齐。Crossref 没有文献类型字段，来信和社论靠 `exclude_title_prefix` 的标题前缀挡掉。

Crossref 的 `journals/{issn}` 路由只认一个 ISSN，填错不会报错，返回 0 篇。加刊物时先用 `curl 'https://api.crossref.org/journals/<issn>/works?rows=0'` 确认 total-results 不是 0。

## 新增条目的标记

每次 `fetch.py` 会给新捞到的论文写一个 `added_batch`，值是抓取当天的日期。`render.py` 读它做三件事：在 README 顶部生成「本次更新」区块、给这批条目挂一个浅粉 NEW 徽章、把这批追加进 [CHANGELOG.md](CHANGELOG.md)。

下次同步时徽章会转移到新一批身上，历史仍留在 CHANGELOG 里。

徽章用 shields.io 图片。GitHub 会剥掉 `style` 属性，`<mark>` 只有默认黄色。

## 科室图标

每条论文末尾挂的 emoji 是科室，规则在 [config/specialties.json](config/specialties.json)，`scripts/tag.py` 按标题和摘要里的关键词自动归类，一篇最多三个，按命中次数排序。

未标科室的是跨科室工作，如基础模型、智能体框架、评测基准。

改了关键词之后跑 `python3 scripts/tag.py --force` 重新全量归类。不加 `--force` 只会给没标过的补，人工改过的不动。

## 怎么补充

每周一 GitHub Action 跑 `fetch.py`，把新命中的论文以 PR 形式提出来，`status` 是 `new`。

人工那一步在 `data/papers.json` 里做：`status` 改成 `kept` 或 `rejected`，顺手补 `tags`（诊断、影像、EHR、Agent 之类），值得强调的把 `highlight` 设成 `true`。改完跑一次 `render.py`。

外部投稿直接开 Issue 贴 DOI，或者提 PR 改 `data/papers.json`。README 是生成的，别手改。

## 本地跑一遍

```bash
python3 scripts/fetch.py --dry-run   # 看这周有什么新东西
python3 scripts/fetch.py             # 写入 data/papers.json
python3 scripts/add.py <DOI>          # 按 DOI 手工加一篇（可跨白名单）
python3 scripts/tag.py               # 打科室标签
python3 scripts/triage.py            # 逐条过审
python3 scripts/render.py            # 重新生成 README 和 CHANGELOG
```
