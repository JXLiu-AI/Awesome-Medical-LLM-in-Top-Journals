# 收录标准

一篇论文进入本列表，需同时满足：

1. **刊物**：发表在 [config/venues.json](config/venues.json) 白名单内的正刊或子刊。会议论文、预印本、Correspondence/News 类短文不收（Comment/Editorial 如果有独立观点可标 `type: comment` 保留）。
2. **主题**：核心方法是大语言模型、多模态基础模型或其智能体形态；纯粹的传统 CNN/统计模型不收。
3. **医学相关**：面向临床、公共卫生、生物医学场景，而非通用 NLP。

## 怎么补充

- **自动**：每周一 GitHub Action 会跑 `scripts/fetch.py`，把新命中的论文以 PR 形式提出来，`status` 标为 `new`。
- **人工**：在 `data/papers.json` 里把 `status` 改成 `kept` 或 `rejected`，补 `tags`（如 `诊断` `影像` `EHR` `Agent`），把里程碑工作的 `highlight` 设为 `true`，然后跑 `python3 scripts/render.py` 重新生成 README。
- **外部投稿**：直接开 Issue 贴 DOI，或提 PR 改 `data/papers.json`（不要手改 README，它是生成的）。

## 新增条目怎么标出来

每次 `fetch.py` 会给新捞到的论文打上 `added_batch`（当天日期），`render.py` 据此：

- 在 README 顶部生成「本次更新 · YYYY-MM-DD」区块，只列这一批；
- 给这批条目挂一个浅粉 `NEW` 徽章，正文列表里一眼能扫到；
- 把这一批追加进 [CHANGELOG.md](CHANGELOG.md)，永久留痕。

徽章用的是 shields.io 图片而不是 `<mark>`：GitHub 的 sanitizer 会剥掉 `style` 属性，`<mark>` 只能是默认黄色，指定不了浅粉。

下一次同步时，上一批的徽章会自动消失（只有 `latest_batch` 那一批带徽章），历史仍留在 CHANGELOG 里。

## 本地跑一遍

```bash
python3 scripts/fetch.py --dry-run   # 看看这周有什么新东西
python3 scripts/fetch.py             # 写入 data/papers.json
python3 scripts/render.py            # 重新生成 README.md
```
