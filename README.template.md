# Awesome Medical LLMs in Top Journals

医学大模型、医学基础模型的论文清单。收录范围限于 Nature、Science、Cell、Lancet、NEJM、JAMA 的正刊及其旗舰子刊，时间自 2023 年 8 月起。每周从 Europe PMC 自动抓一次，人工过一遍再合并。

[![weekly update](https://github.com/JXLiu-AI/Awesome-Medical-LLM-in-Top-Journals/actions/workflows/update.yml/badge.svg)](https://github.com/JXLiu-AI/Awesome-Medical-LLM-in-Top-Journals/actions/workflows/update.yml)
![papers](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/JXLiu-AI/Awesome-Medical-LLM-in-Top-Journals/main/data/papers.json&query=$.papers.length&label=papers)

## 范围

刊物白名单在 [config/venues.json](config/venues.json)。npj Digital Medicine、JAMIA、Nature Communications、JAMA Network Open 这几本目前是关着的（`enabled: false`），它们一年有几百篇相关论文，一并收进来会把正刊的工作淹掉。想要的话把对应刊物的 `enabled` 改成 `true`，重跑一次就有了。

命中关键词在 [config/filters.json](config/filters.json)，只匹配标题和摘要开头，避免讨论段里顺带提一句就被收进来。详细的收录标准见 [CONTRIBUTING.md](CONTRIBUTING.md)。

结构化数据在 [data/papers.json](data/papers.json)，每条都带 DOI，可以直接拿去用。历次新增记录在 [CHANGELOG.md](CHANGELOG.md)。

## 收录概览

<!-- STATS:BEGIN -->
<!-- STATS:END -->

## 论文列表

每条末尾的图标是科室，一篇最多挂三个，按关键词自动归类（规则在 [config/specialties.json](config/specialties.json)）：

<!-- LEGEND:BEGIN -->
<!-- LEGEND:END -->

<img src="https://img.shields.io/badge/NEW-FFD1DC?style=flat-square&logoColor=333" alt="new" align="top"> 是本次同步新增，⭐ 是人工标的重点工作。

<!-- PAPERS:BEGIN -->
<!-- PAPERS:END -->

## 补充与勘误

漏收、误收、链接失效，欢迎开 Issue 或提 PR。注意 README 是脚本生成的，改动请落在 [data/papers.json](data/papers.json)。

## License

CC0-1.0。论文元数据来自 Europe PMC。
