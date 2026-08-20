# Awesome Medical LLMs in Top Journals

> 只收 **Nature / Science / Cell / Lancet / NEJM / JAMA 正刊与旗舰子刊**（近三年）上的医学大模型与医学基础模型工作。
> 每周自动抓取 + 人工审校，不做综述附属品，只做长期维护的追踪表。

[![weekly update](https://github.com/JXLiu-AI/Awesome-Medical-LLM-in-Top-Journals/actions/workflows/update.yml/badge.svg)](https://github.com/JXLiu-AI/Awesome-Medical-LLM-in-Top-Journals/actions/workflows/update.yml)
![papers](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/JXLiu-AI/Awesome-Medical-LLM-in-Top-Journals/main/data/papers.json&query=$.papers.length&label=papers)

## 为什么再做一个

现有的医学大模型清单大多是某篇综述的附属仓库，论文见刊之后就停止更新；而按刊物族组织的 AI4X 清单又不聚焦医学大模型。
本仓库的取舍是：**范围窄（只收顶刊）、更新勤（每周自动化）、可复核（每条都有 DOI 与抓取来源）**。

范围刻意收紧到"一个人读得完"的量级：npj Digital Medicine、JAMIA、Nature Communications、JAMA Network Open
这类走量的数字健康刊已在 [config/venues.json](config/venues.json) 里标为 `enabled: false`——
它们一年产出几百篇 LLM 论文，收进来会把正刊工作淹掉。需要的话把对应刊物的 `enabled` 改成 `true`，重跑一次即可。

- 收录标准见 [CONTRIBUTING.md](CONTRIBUTING.md)
- 刊物白名单：[config/venues.json](config/venues.json)（想加刊改这个文件）
- 命中关键词：[config/filters.json](config/filters.json)
- 结构化数据：[data/papers.json](data/papers.json)（可直接被别的项目引用）
- 历次更新流水：[CHANGELOG.md](CHANGELOG.md)

## 收录概览

<!-- STATS:BEGIN -->
<!-- STATS:END -->

## 论文列表

<img src="https://img.shields.io/badge/NEW-FFD1DC?style=flat-square&logoColor=333" alt="new" align="top"> = 本次同步新增 ｜ ⭐ = 里程碑工作（人工标注）

历次新增的完整流水见 [CHANGELOG.md](CHANGELOG.md)。

<!-- PAPERS:BEGIN -->
<!-- PAPERS:END -->

## 引用

如果这个列表对你的工作有帮助，欢迎 star 或在综述中引用本仓库。

## License

CC0-1.0（论文元数据来自 Europe PMC，遵循其开放许可）。
