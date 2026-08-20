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
| 刊物 | 收录数 |
| --- | ---: |
| Nature Medicine | 70 |
| The Lancet Digital Health | 25 |
| Nature Biomedical Engineering | 23 |
| Nature | 18 |
| Radiology: Artificial Intelligence | 16 |
| NEJM AI | 10 |
| BMJ | 7 |
| JAMA | 6 |
| Nature Methods | 5 |
| The Lancet | 4 |
| Nature Machine Intelligence | 4 |
| Science | 3 |
| Nature Biotechnology | 3 |
| Cell | 3 |
| Science Translational Medicine | 1 |
| Nature Reviews Bioengineering | 1 |
| **合计** | **199** |
<!-- STATS:END -->

## 论文列表

每条末尾的图标是科室，一篇最多挂三个，按关键词自动归类（规则在 [config/specialties.json](config/specialties.json)）：

<!-- LEGEND:BEGIN -->
🩻 放射影像（33） ｜ 🔬 病理（26） ｜ 🎗️ 肿瘤（21） ｜ 📋 病历文书（14） ｜ 🧬 基因组（10） ｜ 💊 药学（9） ｜ 🧩 精神心理（8） ｜ 👁️ 眼科（8） ｜ 🌍 公共卫生（8） ｜ 🩺 全科基层（6） ｜ 🧠 神经（6） ｜ 🚑 急诊重症（5） ｜ 🫀 心血管（5） ｜ 🎓 医学教育（5） ｜ 🦷 口腔（2） ｜ 🔎 消化内镜（2） ｜ 🩹 皮肤（2） ｜ 🌊 超声（2） ｜ ✂️ 外科手术（2） ｜ 🦴 骨科（1） ｜ 🫁 呼吸（1）

未标科室的 73 篇多为跨科室的通用工作（基础模型、智能体、评测基准）。
<!-- LEGEND:END -->

<img src="https://img.shields.io/badge/NEW-FFD1DC?style=flat-square&logoColor=333" alt="new" align="top"> 是本次同步新增，⭐ 是人工标的重点工作。

<!-- PAPERS:BEGIN -->
#### 最近收录

- **[A clinically validated framework for auditing AI chatbot behavior in mental health interactions](https://doi.org/10.1038/s41591-026-04577-2)**<br/>Weilnhammer V et al. · *Nature Medicine* · 2026-08-07 🧩
- **[End-to-end multimodal pathology foundation model with clinical dialogue](https://doi.org/10.1038/s41591-026-04521-4)**<br/>Vorontsov E et al. · *Nature Medicine* · 2026-07-31 🔬
- **[Towards a unified foundation model for medical imaging](https://doi.org/10.1016/j.landig.2026.101013)**<br/>Jin K et al. · *The Lancet Digital Health* · 2026-07-27
- **[MerMED-FM: Multimodal, Multi-Disease Medical Imaging Foundation Model](https://doi.org/10.1016/j.landig.2026.101007)**<br/>Zhou Y et al. · *The Lancet Digital Health* · 2026-07-27
- **[Pathology-CoT: learning visual chain-of-thought agents from expert whole-slide image diagnosis behaviour](https://doi.org/10.1038/s41551-026-01739-y)**<br/>Wang S et al. · *Nature Biomedical Engineering* · 2026-07-24 🔬
- **[CLEAR: an auditable foundation model for radiology grounded in clinical concepts](https://doi.org/10.1038/s41551-026-01741-4)**<br/>Han T et al. · *Nature Biomedical Engineering* · 2026-07-22 🩻
- **[Large-scale multi-sequence pretraining for generalizable MRI analysis in versatile clinical applications](https://doi.org/10.1038/s41551-026-01740-5)**<br/>Qiu Z et al. · *Nature Biomedical Engineering* · 2026-07-13 🩻
- **[Autonomous biomedical research with an artificial intelligence agent](https://doi.org/10.1126/science.adz4351)**<br/>Huang K et al. · *Science* · 2026-07-09
- **[Generalizable AI predicts immunotherapy outcomes across cancers and treatments](https://doi.org/10.1038/s41591-026-04502-7)**<br/>Shen W et al. · *Nature Medicine* · 2026-07-03 🎗️
- **[BoneCoT: multicentre validation of a whole-body skeleton foundation model for bone metastases guided by clinician-derived chain of thought](https://doi.org/10.1038/s41551-026-01736-1)**<br/>Zhao H et al. · *Nature Biomedical Engineering* · 2026-07-02 🎗️🦴🩻
- **[When Patients Share Everything With an AI Chatbot: Risks and Opportunities of Large Language Models](https://doi.org/10.1001/jama.2026.9507)**<br/>Ajunwa I et al. · *JAMA* · 2026-07-01
- **[ReclAIm: A Multiagent Framework for Monitoring and Correcting Performance Decline in Medical Imaging AI](https://doi.org/10.1148/ryai.250923)**<br/>Tzanis E et al. · *Radiology: Artificial Intelligence* · 2026-07-01
- **[Alignment of Policy, Practice, and Patient Safety for Trustworthy AI in Radiology](https://doi.org/10.1148/ryai.250982)**<br/>Doo FX et al. · *Radiology: Artificial Intelligence* · 2026-07-01 🩻
- **[Clinical decision support in hematological malignancies using a case-grounded AI agent](https://doi.org/10.1038/s41591-026-04494-4)**<br/>Zoller J et al. · *Nature Medicine* · 2026-06-30 🎗️
- **[Generative AI-enabled clinical decision support system in primary care: a pragmatic, cluster-randomized trial](https://doi.org/10.1038/s41591-026-04503-6)**<br/>Agweyu A et al. · *Nature Medicine* · 2026-06-26 🩺📋

---

### Nature 正刊与子刊

<details open>
<summary><b>Nature</b>（18）</summary>

- **[Towards conversational artificial intelligence for disease management](https://doi.org/10.1038/s41586-026-10764-5)**<br/>Liévin V et al. · *Nature* · 2026-06-17 💊
- **[Towards autonomous medical artificial intelligence agents](https://doi.org/10.1038/s41586-026-10675-5)**<br/>Ferber D et al. · *Nature* · 2026-06-17 📋
- **[Merlin: a computed tomography vision-language foundation model and dataset](https://doi.org/10.1038/s41586-026-10181-8)**<br/>Blankemeier L et al. · *Nature* · 2026-03-04 🩻
- **[An agentic system for rare disease diagnosis with traceable reasoning](https://doi.org/10.1038/s41586-025-10097-9)**<br/>Zhao W et al. · *Nature* · 2026-02-18 🧬🩺
- **[A foundation model to predict and capture human cognition](https://doi.org/10.1038/s41586-025-09215-4)**<br/>Binz M et al. · *Nature* · 2025-07-02
- **[A fully open AI foundation model applied to chest radiography](https://doi.org/10.1038/s41586-025-09079-8)**<br/>Ma D et al. · *Nature* · 2025-06-11 🩻
- **[Towards accurate differential diagnosis with large language models](https://doi.org/10.1038/s41586-025-08869-4)**<br/>McDuff D et al. · *Nature* · 2025-04-09
- **[Towards conversational diagnostic artificial intelligence](https://doi.org/10.1038/s41586-025-08866-7)**<br/>Tu T et al. · *Nature* · 2025-04-09
- **[Multimodal generative AI for medical image interpretation](https://doi.org/10.1038/s41586-025-08675-y)**<br/>Rao VM et al. · *Nature* · 2025-03-26 🩻
- **[A vision-language foundation model for precision oncology](https://doi.org/10.1038/s41586-024-08378-w)**<br/>Xiang J et al. · *Nature* · 2025-01-08 🔬🎗️📋
- **[Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6)**<br/>Hollmann N et al. · *Nature* · 2025-01-08 💊
- **[A cell atlas foundation model for scalable search of similar human cells](https://doi.org/10.1038/s41586-024-08411-y)**<br/>Heimberg G et al. · *Nature* · 2024-11-20 🧬
- **[Foundation models for fast, label-free detection of glioma infiltration](https://doi.org/10.1038/s41586-024-08169-3)**<br/>Kondepudi A et al. · *Nature* · 2024-11-13 🧠✂️🎗️
- **[A pathology foundation model for cancer diagnosis and prognosis prediction](https://doi.org/10.1038/s41586-024-07894-z)**<br/>Wang X et al. · *Nature* · 2024-09-04 🔬🎗️
- **[Detecting hallucinations in large language models using semantic entropy](https://doi.org/10.1038/s41586-024-07421-0)**<br/>Farquhar S et al. · *Nature* · 2024-06-19 🩻
- **[A multimodal generative AI copilot for human pathology](https://doi.org/10.1038/s41586-024-07618-3)**<br/>Lu MY et al. · *Nature* · 2024-06-12 🔬
- **[A whole-slide foundation model for digital pathology from real-world data](https://doi.org/10.1038/s41586-024-07441-w)**<br/>Xu H et al. · *Nature* · 2024-05-22 🔬🎗️
- **[A foundation model for generalizable disease detection from retinal images](https://doi.org/10.1038/s41586-023-06555-x)**<br/>Zhou Y et al. · *Nature* · 2023-09-13 👁️

</details>

<details open>
<summary><b>Nature Medicine</b>（70）</summary>

- **[A clinically validated framework for auditing AI chatbot behavior in mental health interactions](https://doi.org/10.1038/s41591-026-04577-2)**<br/>Weilnhammer V et al. · *Nature Medicine* · 2026-08-07 🧩
- **[End-to-end multimodal pathology foundation model with clinical dialogue](https://doi.org/10.1038/s41591-026-04521-4)**<br/>Vorontsov E et al. · *Nature Medicine* · 2026-07-31 🔬
- **[Generalizable AI predicts immunotherapy outcomes across cancers and treatments](https://doi.org/10.1038/s41591-026-04502-7)**<br/>Shen W et al. · *Nature Medicine* · 2026-07-03 🎗️
- **[Clinical decision support in hematological malignancies using a case-grounded AI agent](https://doi.org/10.1038/s41591-026-04494-4)**<br/>Zoller J et al. · *Nature Medicine* · 2026-06-30 🎗️
- **[Generative AI-enabled clinical decision support system in primary care: a pragmatic, cluster-randomized trial](https://doi.org/10.1038/s41591-026-04503-6)**<br/>Agweyu A et al. · *Nature Medicine* · 2026-06-26 🩺📋
- **[Evaluating the robustness and readiness of large frontier models in health AI applications](https://doi.org/10.1038/s41591-026-04501-8)**<br/>Gu Y et al. · *Nature Medicine* · 2026-06-26
- **[General-purpose large language models outperform specialized clinical AI tools on medical benchmarks](https://doi.org/10.1038/s41591-026-04431-5)**<br/>Vishwanath K et al. · *Nature Medicine* · 2026-06-12
- **[Autonomous pathology research using agentic AI shows potential in oncology](https://doi.org/10.1038/s41591-026-04403-9)**<br/> · *Nature Medicine* · 2026-06-01 🔬🎗️
- **[Advancing conversational diagnostic AI with multimodal reasoning](https://doi.org/10.1038/s41591-026-04371-0)**<br/>Saab K et al. · *Nature Medicine* · 2026-05-14
- **[ChatGPT Health triage advice falls short in key cases](https://doi.org/10.1038/s41591-026-04427-1)**<br/> · *Nature Medicine* · 2026-05-01 🚑
- **[An agentic framework for autonomous scientific discovery in cancer pathology](https://doi.org/10.1038/s41591-026-04357-y)**<br/>Trost F et al. · *Nature Medicine* · 2026-04-29 🔬🎗️
- **[A cognitive layer architecture to support large-language model performance in psychotherapy interactions](https://doi.org/10.1038/s41591-026-04278-w)**<br/>Rollwage M et al. · *Nature Medicine* · 2026-03-12 🧩
- **[A clinical environment simulator for dynamic AI evaluation](https://doi.org/10.1038/s41591-026-04252-6)**<br/>Luo L et al. · *Nature Medicine* · 2026-03-12
- **[LLM-assisted systematic review of large language models in clinical medicine](https://doi.org/10.1038/s41591-026-04229-5)**<br/>Chen SF et al. · *Nature Medicine* · 2026-03-03
- **[ChatGPT Health performance in a structured test of triage recommendations](https://doi.org/10.1038/s41591-026-04297-7)**<br/>Ramaswamy A et al. · *Nature Medicine* · 2026-02-23 🚑
- **[Reliability of LLMs as medical assistants for the general public: a randomized preregistered study](https://doi.org/10.1038/s41591-025-04074-y)**<br/>Bean AM et al. · *Nature Medicine* · 2026-02-09 🌍
- **[A large language model for complex cardiology care](https://doi.org/10.1038/s41591-025-04190-9)**<br/>O'Sullivan JW et al. · *Nature Medicine* · 2026-02-06 🫀
- **[Scaling medical AI across clinical contexts](https://doi.org/10.1038/s41591-025-04184-7)**<br/>Li MM et al. · *Nature Medicine* · 2026-02-03 📋
- **[Holistic evaluation of large language models for medical tasks with MedHELM](https://doi.org/10.1038/s41591-025-04151-2)**<br/>Bedi S et al. · *Nature Medicine* · 2026-01-20 📋
- **[An LLM chatbot to facilitate primary-to-specialist care transitions: a randomized controlled trial](https://doi.org/10.1038/s41591-025-04176-7)**<br/>Tao X et al. · *Nature Medicine* · 2026-01-19 🩺
- **[A multimodal sleep foundation model for disease prediction](https://doi.org/10.1038/s41591-025-04133-4)**<br/>Thapa R et al. · *Nature Medicine* · 2026-01-06 🧩
- **[Generative AI-based low-dose digital subtraction angiography for intra-operative radiation dose reduction: a randomized controlled trial](https://doi.org/10.1038/s41591-025-04042-6)**<br/>Zhao H et al. · *Nature Medicine* · 2026-01-02 🩻
- **[A multimodal whole-slide foundation model for pathology](https://doi.org/10.1038/s41591-025-03982-3)**<br/>Ding T et al. · *Nature Medicine* · 2025-11-05 🔬
- **[A full life cycle biological clock based on routine clinical data and its impact in health and diseases](https://doi.org/10.1038/s41591-025-04006-w)**<br/>Wang K et al. · *Nature Medicine* · 2025-10-27 📋
- **[Generative artificial intelligence in medicine](https://doi.org/10.1038/s41591-025-03983-2)**<br/>Teo ZL et al. · *Nature Medicine* · 2025-10-06
- **[Rapid deployment of large language model DeepSeek in Chinese hospitals demands a regulatory response](https://doi.org/10.1038/s41591-025-03836-y)**<br/>Shen T et al. · *Nature Medicine* · 2025-10-01
- **[An eyecare foundation model for clinical assistance: a randomized controlled trial](https://doi.org/10.1038/s41591-025-03900-7)**<br/>Wu Y et al. · *Nature Medicine* · 2025-08-28 👁️
- **[Global distribution of research efforts, disease burden, and impact of US public funding withdrawal](https://doi.org/10.1038/s41591-025-03923-0)**<br/>Schmallenbach L et al. · *Nature Medicine* · 2025-08-27
- **[A personal health large language model for sleep and fitness coaching](https://doi.org/10.1038/s41591-025-03888-0)**<br/>Khasentino J et al. · *Nature Medicine* · 2025-08-14
- **[Large language model-based biological age prediction in large-scale populations](https://doi.org/10.1038/s41591-025-03856-8)**<br/>Li Y et al. · *Nature Medicine* · 2025-07-23
- **[Real-world deployment of a fine-tuned pathology foundation model for lung cancer biomarker detection](https://doi.org/10.1038/s41591-025-03780-x)**<br/>Campanella G et al. · *Nature Medicine* · 2025-07-09 🔬🎗️🧬
- **[A multimodal vision foundation model for clinical dermatology](https://doi.org/10.1038/s41591-025-03747-y)**<br/>Yan S et al. · *Nature Medicine* · 2025-06-06 🩹🎗️
- **[A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial](https://doi.org/10.1038/s41591-025-03743-2)**<br/>Xu Z et al. · *Nature Medicine* · 2025-06-03 🫁
- **[The MI-CLAIM-GEN checklist for generative artificial intelligence in health](https://doi.org/10.1038/s41591-024-03470-0)**<br/>Miao BY et al. · *Nature Medicine* · 2025-05-01
- **[Comparative benchmarking of the DeepSeek large language model on medical tasks and clinical reasoning](https://doi.org/10.1038/s41591-025-03726-3)**<br/>Tordjman M et al. · *Nature Medicine* · 2025-04-23 🎓🎗️
- **[Benchmark evaluation of DeepSeek large language models in clinical decision-making](https://doi.org/10.1038/s41591-025-03727-2)**<br/>Sandmann S et al. · *Nature Medicine* · 2025-04-23
- **[A vaccine chatbot intervention for parents to improve HPV vaccination uptake among middle school girls: a cluster randomized trial](https://doi.org/10.1038/s41591-025-03618-6)**<br/>Hou Z et al. · *Nature Medicine* · 2025-04-07
- **[Sociodemographic biases in medical decision making by large language models](https://doi.org/10.1038/s41591-025-03626-6)**<br/>Omar M et al. · *Nature Medicine* · 2025-04-07 🚑
- **[Medical large language model for diagnostic reasoning across specialties](https://doi.org/10.1038/s41591-025-03520-1)**<br/> · *Nature Medicine* · 2025-03-01
- **[GPT-4 assistance for improvement of physician performance on patient care tasks: a randomized controlled trial](https://doi.org/10.1038/s41591-024-03456-y)**<br/>Goh E et al. · *Nature Medicine* · 2025-02-05
- **[Artificial intelligence in drug development](https://doi.org/10.1038/s41591-024-03434-4)**<br/>Zhang K et al. · *Nature Medicine* · 2025-01-20
- **[The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5)**<br/>Gallifant J et al. · *Nature Medicine* · 2025-01-08
- **[Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7)**<br/>Singhal K et al. · *Nature Medicine* · 2025-01-08 🎓
- **[Medical large language models are vulnerable to data-poisoning attacks](https://doi.org/10.1038/s41591-024-03445-1)**<br/>Alber DA et al. · *Nature Medicine* · 2025-01-08
- **[A generalist medical language model for disease diagnosis assistance](https://doi.org/10.1038/s41591-024-03416-6)**<br/>Liu X et al. · *Nature Medicine* · 2025-01-08
- **[An evaluation framework for clinical use of large language models in patient interaction tasks](https://doi.org/10.1038/s41591-024-03328-5)**<br/>Johri S et al. · *Nature Medicine* · 2025-01-02
- **[Self-improving generative foundation model for synthetic medical image generation and clinical applications](https://doi.org/10.1038/s41591-024-03359-y)**<br/>Wang J et al. · *Nature Medicine* · 2024-12-11
- **[Safety principles for medical summarization using generative AI](https://doi.org/10.1038/s41591-024-03313-y)**<br/>Obika D et al. · *Nature Medicine* · 2024-12-01
- **[An explainable foundation model for drug repurposing](https://doi.org/10.1038/s41591-024-03333-8)**<br/>Bessadok A et al. · *Nature Medicine* · 2024-12-01
- **[Collaboration between clinicians and vision-language models in radiology report generation](https://doi.org/10.1038/s41591-024-03302-1)**<br/>Tanno R et al. · *Nature Medicine* · 2024-11-07 🩻
- **[A foundation model for clinician-centered drug repurposing](https://doi.org/10.1038/s41591-024-03233-x)**<br/>Huang K et al. · *Nature Medicine* · 2024-09-25
- **[A toolbox for surfacing health equity harms and biases in large language models](https://doi.org/10.1038/s41591-024-03258-2)**<br/>Pfohl SR et al. · *Nature Medicine* · 2024-09-23 🌍
- **[A generalist vision-language foundation model for diverse biomedical tasks](https://doi.org/10.1038/s41591-024-03185-2)**<br/>Zhang K et al. · *Nature Medicine* · 2024-08-07
- **[Influence of believed AI involvement on the perception of digital medical advice](https://doi.org/10.1038/s41591-024-03180-7)**<br/>Reis M et al. · *Nature Medicine* · 2024-07-25
- **[A foundation model for clinical-grade computational pathology and rare cancers detection](https://doi.org/10.1038/s41591-024-03141-0)**<br/>Vorontsov E et al. · *Nature Medicine* · 2024-07-22 🔬🎗️
- **[Integrated image-based deep learning and language models for primary diabetes care](https://doi.org/10.1038/s41591-024-03139-8)**<br/>Li J et al. · *Nature Medicine* · 2024-07-19 👁️🌍🩺
- **[Outpatient reception via collaboration between nurses and a large language model: a randomized controlled trial](https://doi.org/10.1038/s41591-024-03148-7)**<br/>Wan P et al. · *Nature Medicine* · 2024-07-15 🩺
- **[Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1)**<br/>Hager P et al. · *Nature Medicine* · 2024-07-04
- **[Artificial intelligence in surgery](https://doi.org/10.1038/s41591-024-02970-3)**<br/>Varghese C et al. · *Nature Medicine* · 2024-05-13 ✂️
- **[Vision-language foundation model for echocardiogram interpretation](https://doi.org/10.1038/s41591-024-02959-y)**<br/>Christensen M et al. · *Nature Medicine* · 2024-04-30 🫀🌊
- **[The health risks of generative AI-based wellness apps](https://doi.org/10.1038/s41591-024-02943-6)**<br/>De Freitas J et al. · *Nature Medicine* · 2024-04-29 🧩
- **[Large language models for preventing medication direction errors in online pharmacies](https://doi.org/10.1038/s41591-024-02933-8)**<br/>Pais C et al. · *Nature Medicine* · 2024-04-25 💊
- **[Transparent medical image AI via an image-text foundation model grounded in medical literature](https://doi.org/10.1038/s41591-024-02887-x)**<br/>Kim C et al. · *Nature Medicine* · 2024-04-16
- **[Generative models improve fairness of medical classifiers under distribution shifts](https://doi.org/10.1038/s41591-024-02838-6)**<br/>Ktena I et al. · *Nature Medicine* · 2024-04-10
- **[A visual-language foundation model for computational pathology](https://doi.org/10.1038/s41591-024-02856-4)**<br/>Lu MY et al. · *Nature Medicine* · 2024-03-19 🔬
- **[Towards a general-purpose foundation model for computational pathology](https://doi.org/10.1038/s41591-024-02857-3)**<br/>Chen RJ et al. · *Nature Medicine* · 2024-03-19 🔬
- **[Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5)**<br/>Van Veen D et al. · *Nature Medicine* · 2024-02-27 📋🩻
- **[Closing the accessibility gap to mental health treatment with a personalized self-referral chatbot](https://doi.org/10.1038/s41591-023-02766-x)**<br/>Habicht J et al. · *Nature Medicine* · 2024-02-05 🩺🧩
- **[Large language model AI chatbots require approval as medical devices](https://doi.org/10.1038/s41591-023-02412-6)**<br/>Gilbert S et al. · *Nature Medicine* · 2023-10-01
- **[A visual-language foundation model for pathology image analysis using medical Twitter](https://doi.org/10.1038/s41591-023-02504-3)**<br/>Huang Z et al. · *Nature Medicine* · 2023-08-17 🔬

</details>

<details open>
<summary><b>Nature Biomedical Engineering</b>（23）</summary>

- **[Pathology-CoT: learning visual chain-of-thought agents from expert whole-slide image diagnosis behaviour](https://doi.org/10.1038/s41551-026-01739-y)**<br/>Wang S et al. · *Nature Biomedical Engineering* · 2026-07-24 🔬
- **[CLEAR: an auditable foundation model for radiology grounded in clinical concepts](https://doi.org/10.1038/s41551-026-01741-4)**<br/>Han T et al. · *Nature Biomedical Engineering* · 2026-07-22 🩻
- **[Large-scale multi-sequence pretraining for generalizable MRI analysis in versatile clinical applications](https://doi.org/10.1038/s41551-026-01740-5)**<br/>Qiu Z et al. · *Nature Biomedical Engineering* · 2026-07-13 🩻
- **[BoneCoT: multicentre validation of a whole-body skeleton foundation model for bone metastases guided by clinician-derived chain of thought](https://doi.org/10.1038/s41551-026-01736-1)**<br/>Zhao H et al. · *Nature Biomedical Engineering* · 2026-07-02 🎗️🦴🩻
- **[Towards clinical-level interpretation of dental panoramic radiography using an instance-guided vision-language model](https://doi.org/10.1038/s41551-026-01713-8)**<br/>Zhu Q et al. · *Nature Biomedical Engineering* · 2026-06-25 🩻🦷
- **[A three-dimensional multi-modal foundation model for optical coherence tomography](https://doi.org/10.1038/s41551-026-01662-2)**<br/>Liu Z et al. · *Nature Biomedical Engineering* · 2026-04-24 👁️
- **[Towards a general-purpose foundation model for functional MRI analysis](https://doi.org/10.1038/s41551-026-01666-y)**<br/>Wang C et al. · *Nature Biomedical Engineering* · 2026-04-23 🩻🧠
- **[3D foundation model for generalizable disease detection in head computed tomography](https://doi.org/10.1038/s41551-026-01668-w)**<br/>Zhu W et al. · *Nature Biomedical Engineering* · 2026-04-22 🩻🔬🧠
- **[Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses](https://doi.org/10.1038/s41551-026-01634-6)**<br/>Bu D et al. · *Nature Biomedical Engineering* · 2026-03-30
- **[Generalist foundation models from a multimodal dataset for 3D computed tomography](https://doi.org/10.1038/s41551-025-01599-y)**<br/>Hamamci IE et al. · *Nature Biomedical Engineering* · 2026-02-12 🩻
- **[Learning neuroimaging models from health system-scale data](https://doi.org/10.1038/s41551-025-01608-0)**<br/>Lyu Y et al. · *Nature Biomedical Engineering* · 2026-02-06 🩻🧠
- **[Making large language models reliable data science programming copilots for biomedical research](https://doi.org/10.1038/s41551-025-01587-2)**<br/>Wang Z et al. · *Nature Biomedical Engineering* · 2026-01-22 🎗️🧬
- **[A multimodal vision-language model for generalizable annotation-free pathology localization](https://doi.org/10.1038/s41551-025-01574-7)**<br/>Yang H et al. · *Nature Biomedical Engineering* · 2026-01-06 🔬
- **[Benchmarking foundation models as feature extractors for weakly supervised computational pathology](https://doi.org/10.1038/s41551-025-01516-3)**<br/>Neidlinger P et al. · *Nature Biomedical Engineering* · 2025-10-01 🔬🔎
- **[A collaborative large language model for drug analysis](https://doi.org/10.1038/s41551-025-01471-z)**<br/>Zhou H et al. · *Nature Biomedical Engineering* · 2025-09-23
- **[A generalist foundation model and database for open-world medical image segmentation](https://doi.org/10.1038/s41551-025-01497-3)**<br/>Zhang S et al. · *Nature Biomedical Engineering* · 2025-09-05
- **[A generalizable pathology foundation model using a unified knowledge distillation pretraining framework](https://doi.org/10.1038/s41551-025-01488-4)**<br/>Ma J et al. · *Nature Biomedical Engineering* · 2025-09-02 🔬
- **[Unconditional latent diffusion models memorize patient imaging data](https://doi.org/10.1038/s41551-025-01468-8)**<br/>Dar SUH et al. · *Nature Biomedical Engineering* · 2025-08-11
- **[A data-efficient strategy for building high-performing medical foundation models](https://doi.org/10.1038/s41551-025-01365-0)**<br/>Sun Y et al. · *Nature Biomedical Engineering* · 2025-03-05 👁️
- **[A foundation model for enhancing magnetic resonance images and downstream segmentation, registration and diagnostic tasks](https://doi.org/10.1038/s41551-024-01283-7)**<br/>Sun Y et al. · *Nature Biomedical Engineering* · 2024-12-05
- **[A multimodal machine learning model for the stratification of breast cancer risk](https://doi.org/10.1038/s41551-024-01302-7)**<br/>Qian X et al. · *Nature Biomedical Engineering* · 2024-12-04 🎗️🩻🌊
- **[A vision-language foundation model for the generation of realistic chest X-ray images](https://doi.org/10.1038/s41551-024-01246-y)**<br/>Bluethgen C et al. · *Nature Biomedical Engineering* · 2024-08-26 🩻🔬
- **[Auditing the inference processes of medical-image classifiers by leveraging generative AI and the expertise of physicians](https://doi.org/10.1038/s41551-023-01160-9)**<br/>DeGrave AJ et al. · *Nature Biomedical Engineering* · 2023-12-28 🩹

</details>

<details open>
<summary><b>Nature Machine Intelligence</b>（4）</summary>

- **[Cardiac health assessment across scenarios and devices using a multimodal foundation model pretrained on data from 1.7 million individuals](https://doi.org/10.1038/s42256-026-01180-5)**<br/>Gu X et al. · *Nature Machine Intelligence* · 2026-02-24 🫀
- **[Generating 3D Binding Molecules Using Shape-Conditioned Diffusion Models with Guidance](https://doi.org/10.1038/s42256-025-01030-w)**<br/>Chen Z et al. · *Nature Machine Intelligence* · 2025-05-12
- **[Accelerating histopathology workflows with generative AI-based virtually multiplexed tumour profiling](https://doi.org/10.1038/s42256-024-00889-5)**<br/>Pati P et al. · *Nature Machine Intelligence* · 2024-09-09 🔬🎗️
- **[Augmenting large language models with chemistry tools](https://doi.org/10.1038/s42256-024-00832-8)**<br/>M Bran A et al. · *Nature Machine Intelligence* · 2024-05-08 💊

</details>

<details open>
<summary><b>Nature Biotechnology</b>（3）</summary>

- **[Agentic AI and the rise of in silico team science in biomedical research](https://doi.org/10.1038/s41587-026-03035-1)**<br/>Li B et al. · *Nature Biotechnology* · 2026-02-24 💊
- **[Intestinal mucosal barrier repair and immune regulation with an AI-developed gut-restricted PHD inhibitor](https://doi.org/10.1038/s41587-024-02503-w)**<br/>Fu Y et al. · *Nature Biotechnology* · 2024-12-11 🔎💊
- **[ChatGPT and medicine: how AI language models are shaping the future and health related careers](https://doi.org/10.1038/s41587-023-02011-3)**<br/>Yan M et al. · *Nature Biotechnology* · 2023-11-01

</details>

<details open>
<summary><b>Nature Methods</b>（5）</summary>

- **[Novae: a graph-based foundation model for spatial transcriptomics data](https://doi.org/10.1038/s41592-025-02899-6)** [[code]](https://github.com/MICS-Lab/novae)<br/>Blampey Q et al. · *Nature Methods* · 2025-12-10
- **[A visual-omics foundation model to bridge histopathology with spatial transcriptomics](https://doi.org/10.1038/s41592-025-02707-1)**<br/>Chen W et al. · *Nature Methods* · 2025-05-29 🔬🧬
- **[A foundation model unlocks unified biomedical image analysis](https://doi.org/10.1038/s41592-024-02519-9)**<br/>Huang Y et al. · *Nature Methods* · 2025-01-01
- **[A foundation model for joint segmentation, detection and recognition of biomedical objects across nine modalities](https://doi.org/10.1038/s41592-024-02499-w)**<br/>Zhao T et al. · *Nature Methods* · 2024-11-18
- **[Large-scale foundation model on single-cell transcriptomics](https://doi.org/10.1038/s41592-024-02305-7)**<br/>Hao M et al. · *Nature Methods* · 2024-06-06

</details>

<details open>
<summary><b>Nature Reviews Bioengineering</b>（1）</summary>

- **[Diffusion models in bioinformatics and computational biology](https://doi.org/10.1038/s44222-023-00114-9)**<br/>Guo Z et al. · *Nature Reviews Bioengineering* · 2023-10-27 💊

</details>

### Science 正刊与子刊

<details open>
<summary><b>Science</b>（3）</summary>

- **[Autonomous biomedical research with an artificial intelligence agent](https://doi.org/10.1126/science.adz4351)**<br/>Huang K et al. · *Science* · 2026-07-09
- **[Performance of a large language model on the reasoning tasks of a physician](https://doi.org/10.1126/science.adz4433)**<br/>Brodeur PG et al. · *Science* · 2026-04-30
- **[Hallucinating hallucinogens](https://doi.org/10.1126/science.adk8626)**<br/>Skinnider MA. et al. · *Science* · 2023-11-09

</details>

<details open>
<summary><b>Science Translational Medicine</b>（1）</summary>

- **[AI-CURA, an automated LLM workflow for high-accuracy genetic variant classification](https://doi.org/10.1126/scitranslmed.adz4172)**<br/>Ma W et al. · *Science Translational Medicine* · 2026-06-24 🧬🔬

</details>

### Cell 正刊与子刊

<details open>
<summary><b>Cell</b>（3）</summary>

- **[The generative era of medical AI](https://doi.org/10.1016/j.cell.2025.05.018)**<br/>Fahrner LJ et al. · *Cell* · 2025-07-01 🔬
- **[Large language models deconstruct the clinical intuition behind diagnosing autism](https://doi.org/10.1016/j.cell.2025.02.025)**<br/>Stanley J et al. · *Cell* · 2025-03-26 🧬
- **[Empowering biomedical discovery with AI agents](https://doi.org/10.1016/j.cell.2024.09.022)**<br/>Gao S et al. · *Cell* · 2024-10-01

</details>

### 顶级医学期刊

<details open>
<summary><b>NEJM AI</b>（10）</summary>

- **[LLM-Assisted Reanalysis of Unsolved Rare Disease Genomes Increases Diagnostic Yield](https://doi.org/10.1056/aics2501343)**<br/>Jaech A et al. · *NEJM AI* · 2026-06-25 🧬
- **[Assessing Generative AI Chatbots for Alcohol Misuse Support: A Longitudinal Simulation Study](https://doi.org/10.1056/aics2500676)**<br/>Uscher-Pines L et al. · *NEJM AI* · 2026-01-22 🦷
- **[A foundation transformer model with self-supervised learning for ECG-based assessment of cardiac and coronary function](https://doi.org/10.1056/aioa2500164)**<br/>Moody JB et al. · *NEJM AI* · 2025-11-26 🫀
- **[An Electrocardiogram Foundation Model Built on over 10 Million Recordings](https://doi.org/10.1056/aioa2401033)**<br/>Li J et al. · *NEJM AI* · 2025-06-26 🫀
- **[The use of artificial intelligence for cancer therapeutic decision-making](https://doi.org/10.1056/aira2401164)**<br/>Elemento O et al. · *NEJM AI* · 2025-04-17 🎗️🩻🔬
- **[Large Language Models for More Efficient Reporting of Hospital Quality Measures](https://doi.org/10.1056/aics2400420)**<br/>Boussina A et al. · *NEJM AI* · 2024-10-21 🚑
- **[FHIR-GPT Enhances Health Interoperability with Large Language Models](https://doi.org/10.1056/aics2300301)**<br/>Li Y et al. · *NEJM AI* · 2024-07-19 🌍📋
- **[Comparative Evaluation of LLMs in Clinical Oncology](https://doi.org/10.1056/aioa2300151)**<br/>Rydzewski NR et al. · *NEJM AI* · 2024-04-16 🎗️
- **[CORAL: Expert-Curated Oncology Reports to Advance Language Model Inference](https://doi.org/10.1056/aidbp2300110)**<br/>Sushil M et al. · *NEJM AI* · 2024-03-13 🎗️📋
- **[Almanac - Retrieval-Augmented Language Models for Clinical Medicine](https://doi.org/10.1056/aioa2300068)**<br/>Zakka C et al. · *NEJM AI* · 2024-01-25

</details>

<details open>
<summary><b>The Lancet</b>（4）</summary>

- **[Targeted advertising in generative artificial intelligence chatbots: a new public health risk](https://doi.org/10.1016/s0140-6736(26)00464-2)**<br/>Backholer K et al. · *The Lancet* · 2026-04-02 🌍
- **[Assessing generative artificial intelligence for mental health](https://doi.org/10.1016/s0140-6736(25)01237-1)**<br/>Torous J et al. · *The Lancet* · 2025-06-11 🧩
- **[A clinical certification pathway for generalist medical AI systems](https://doi.org/10.1016/s0140-6736(24)02797-1)**<br/>Rajpurkar P et al. · *The Lancet* · 2025-01-01
- **[Explaining differential socioeconomic effects in population health interventions: development and application of a new tool to classify intervention agentic demand](https://doi.org/10.1016/s0140-6736(23)02056-1)**<br/>Garrott K et al. · *The Lancet* · 2023-11-01 🌍

</details>

<details open>
<summary><b>The Lancet Digital Health</b>（25）</summary>

- **[Towards a unified foundation model for medical imaging](https://doi.org/10.1016/j.landig.2026.101013)**<br/>Jin K et al. · *The Lancet Digital Health* · 2026-07-27
- **[MerMED-FM: Multimodal, Multi-Disease Medical Imaging Foundation Model](https://doi.org/10.1016/j.landig.2026.101007)**<br/>Zhou Y et al. · *The Lancet Digital Health* · 2026-07-27
- **[Beyond language: generative artificial intelligence as a general computing model for medicine](https://doi.org/10.1016/j.landig.2026.101011)**<br/>Sitek A et al. · *The Lancet Digital Health* · 2026-06-08 💊
- **[Effects of large language model-generated, patient-oriented discharge summaries on patient activation: a single-centre, single-blind, randomised controlled trial in Germany](https://doi.org/10.1016/j.landig.2026.100991)**<br/>Rust P et al. · *The Lancet Digital Health* · 2026-05-18 📋
- **[ChatGPT for obesity management: a review of evidence, potential challenges, and clinical implications](https://doi.org/10.1016/j.landig.2026.100980)**<br/>Motevalli M et al. · *The Lancet Digital Health* · 2026-04-10 👁️
- **[Molecular alterations prediction in gliomas via an interpretable deep learning model: a multicentre and retrospective study](https://doi.org/10.1016/j.landig.2025.100977)**<br/>Han C et al. · *The Lancet Digital Health* · 2026-04-01 🔬🧠🧬
- **[Agentic artificial intelligence in eye care: is clinical autonomy finally within reach?](https://doi.org/10.1016/j.landig.2025.100967)**<br/>Zou K et al. · *The Lancet Digital Health* · 2026-02-19 👁️
- **[Large language models for simplifying radiology reports: a systematic review and meta-analysis of patient, public, and clinician evaluations](https://doi.org/10.1016/j.landig.2025.100960)**<br/>Alabed S et al. · *The Lancet Digital Health* · 2026-02-16 🩻
- **[CARDBiomedBench: a benchmark for evaluating the performance of large language models in biomedical research](https://doi.org/10.1016/j.landig.2025.100943)**<br/>Bianchi O et al. · *The Lancet Digital Health* · 2026-01-31 🧠🧬💊
- **[Development and validation of a pre-trained language model for neonatal morbidities: a retrospective, multicentre, prognostic study](https://doi.org/10.1016/j.landig.2025.100926)**<br/>Xie F et al. · *The Lancet Digital Health* · 2025-12-18 📋
- **[Physician input improves generative artificial intelligence models' diagnostic performance in solving complex clinical cases](https://doi.org/10.1016/j.landig.2025.100922)**<br/>Lam K et al. · *The Lancet Digital Health* · 2025-11-22
- **[How can artificial intelligence transform the training of medical students and physicians?](https://doi.org/10.1016/j.landig.2025.100900)**<br/>Ning Y et al. · *The Lancet Digital Health* · 2025-10-04 🎓🌍
- **[Exploring the potential of generative artificial intelligence in medical image synthesis: opportunities, challenges, and future directions](https://doi.org/10.1016/j.landig.2025.100890)**<br/>Khosravi B et al. · *The Lancet Digital Health* · 2025-08-14
- **[Value of artificial intelligence in neuro-oncology](https://doi.org/10.1016/j.landig.2025.100876)**<br/>Voigtlaender S et al. · *The Lancet Digital Health* · 2025-08-08 🎗️
- **[Large language models for the mental health community: framework for translating code to care](https://doi.org/10.1016/s2589-7500(24)00255-3)**<br/>Malgaroli M et al. · *The Lancet Digital Health* · 2025-01-07 🧩📋
- **[The potential of Generative Pre-trained Transformer 4 (GPT-4) to analyse medical notes in three different languages: a retrospective model-evaluation study](https://doi.org/10.1016/s2589-7500(24)00246-2)**<br/>Menezes MCS et al. · *The Lancet Digital Health* · 2025-01-01
- **[Attitudes and perceptions of medical researchers towards the use of artificial intelligence chatbots in the scientific process: an international cross-sectional survey](https://doi.org/10.1016/s2589-7500(24)00202-4)**<br/>Ng JY et al. · *The Lancet Digital Health* · 2024-11-15
- **[Generative artificial intelligence and ethical considerations in health care: a scoping review and ethics checklist](https://doi.org/10.1016/s2589-7500(24)00143-2)**<br/>Ning Y et al. · *The Lancet Digital Health* · 2024-09-17
- **[A future role for health applications of large language models depends on regulators enforcing safety standards](https://doi.org/10.1016/s2589-7500(24)00124-9)**<br/>Freyer O et al. · *The Lancet Digital Health* · 2024-09-01
- **[ChatGPT for digital pathology research](https://doi.org/10.1016/s2589-7500(24)00114-6)**<br/>Omar M et al. · *The Lancet Digital Health* · 2024-07-09 🔬
- **[The effect of using a large language model to respond to patient messages](https://doi.org/10.1016/s2589-7500(24)00060-8)**<br/>Chen S et al. · *The Lancet Digital Health* · 2024-04-24
- **[Ethical and regulatory challenges of large language models in medicine](https://doi.org/10.1016/s2589-7500(24)00061-x)**<br/>Ong JCL et al. · *The Lancet Digital Health* · 2024-04-23
- **[Assessing the potential of GPT-4 to perpetuate racial and gender biases in health care: a model evaluation study](https://doi.org/10.1016/s2589-7500(23)00225-x)**<br/>Zack T et al. · *The Lancet Digital Health* · 2024-01-01
- **[Large language models and their impact in ophthalmology](https://doi.org/10.1016/s2589-7500(23)00201-7)**<br/>Betzler BK et al. · *The Lancet Digital Health* · 2023-12-01 👁️
- **[Predicting seizure recurrence after an initial seizure-like episode from routine clinical notes using large language models: a retrospective cohort study](https://doi.org/10.1016/s2589-7500(23)00179-6)**<br/>Beaulieu-Jones BK et al. · *The Lancet Digital Health* · 2023-12-01 📋

</details>

<details open>
<summary><b>JAMA</b>（6）</summary>

- **[When Patients Share Everything With an AI Chatbot: Risks and Opportunities of Large Language Models](https://doi.org/10.1001/jama.2026.9507)**<br/>Ajunwa I et al. · *JAMA* · 2026-07-01
- **[Can Open-Source AI Models Diagnose Complex Cases as Well as GPT-4?](https://doi.org/10.1001/jama.2025.2806)**<br/>Perlis R et al. · *JAMA* · 2025-05-01
- **[Manual vs AI-Assisted Prescreening for Trial Eligibility Using Large Language Models-A Randomized Clinical Trial](https://doi.org/10.1001/jama.2024.28047)**<br/>Unlu O et al. · *JAMA* · 2025-03-01
- **[Testing and Evaluation of Health Care Applications of Large Language Models: A Systematic Review](https://doi.org/10.1001/jama.2024.21700)**<br/>Bedi S et al. · *JAMA* · 2025-01-01
- **[An AI Chatbot Outperformed Physicians and Physicians Plus AI in a Trial-What Does That Mean?](https://doi.org/10.1001/jama.2024.23860)**<br/>Hswen Y et al. · *JAMA* · 2025-01-01
- **[Will Generative Artificial Intelligence Deliver on Its Promise in Health Care?](https://doi.org/10.1001/jama.2023.25054)**<br/>Wachter RM et al. · *JAMA* · 2024-01-01 📋

</details>

<details open>
<summary><b>BMJ</b>（7）</summary>

- **[Clinical competencies for using generative AI in patient care](https://doi.org/10.1136/bmj-2025-085324)**<br/>Lewis M et al. · *BMJ* · 2025-12-02
- **[How generative AI affects patient agency](https://doi.org/10.1136/bmj-2025-085323)**<br/>Blease C et al. · *BMJ* · 2025-11-25
- **[ChatGPT: More than a million users show signs of mental health distress and mania each week, internal data suggest](https://doi.org/10.1136/bmj.r2290)**<br/>O'Dowd A. et al. · *BMJ* · 2025-10-30 🧩
- **[Reporting guidelines for chatbot health advice studies: explanation and elaboration for the Chatbot Assessment Reporting Tool (CHART)](https://doi.org/10.1136/bmj-2024-083305)**<br/>CHART Collaborative. et al. · *BMJ* · 2025-08-01
- **[Should medical students be encouraged to use generative artificial intelligence to study?](https://doi.org/10.1136/bmj.r1418)**<br/>Sibal R et al. · *BMJ* · 2025-07-23 🎓
- **[Current safeguards, risk mitigation, and transparency measures of large language models against the generation of health disinformation: repeated cross sectional analysis](https://doi.org/10.1136/bmj-2023-078538)**<br/>Menz BD et al. · *BMJ* · 2024-03-20
- **[Sixty seconds on . . . ChatGPT and medical exams](https://doi.org/10.1136/bmj.q675)**<br/>Wise J. et al. · *BMJ* · 2024-03-18

</details>

### 影像与医学信息学旗舰刊

<details open>
<summary><b>Radiology: Artificial Intelligence</b>（16）</summary>

- **[ReclAIm: A Multiagent Framework for Monitoring and Correcting Performance Decline in Medical Imaging AI](https://doi.org/10.1148/ryai.250923)**<br/>Tzanis E et al. · *Radiology: Artificial Intelligence* · 2026-07-01
- **[Alignment of Policy, Practice, and Patient Safety for Trustworthy AI in Radiology](https://doi.org/10.1148/ryai.250982)**<br/>Doo FX et al. · *Radiology: Artificial Intelligence* · 2026-07-01 🩻
- **[Cognitively Biased Prompt Effects on Large Language Model Accuracy for Radiology Board-style Examination Questions](https://doi.org/10.1148/ryai.250585)**<br/>Dietrich NT et al. · *Radiology: Artificial Intelligence* · 2026-05-01 🩻
- **[Fine-Tuned Large Language Model for Automated Radiology Impression Generation: A Multicenter Evaluation](https://doi.org/10.1148/ryai.250714)**<br/>Li M et al. · *Radiology: Artificial Intelligence* · 2026-05-01 🩻
- **[Impact of Label Noise from Large Language Model-generated Annotations on Evaluation of Diagnostic Model Performance](https://doi.org/10.1148/ryai.250477)**<br/>Chavoshi M et al. · *Radiology: Artificial Intelligence* · 2026-03-01
- **[A Taxonomy of Machine Hallucination in Radiology](https://doi.org/10.1148/ryai.250203)**<br/>Brooks FJ et al. · *Radiology: Artificial Intelligence* · 2026-03-01 🩻
- **[Agentic AI in Radiology: Evolution from Large Language Models to Future Clinical Integration](https://doi.org/10.1148/ryai.250651)**<br/>Khosravi B et al. · *Radiology: Artificial Intelligence* · 2026-03-01 🩻
- **[Visualizing Radiologic Connections: An Explainable Coarse-to-Fine Foundation Model with Multiview Mammograms and Associated Reports](https://doi.org/10.1148/ryai.240646)**<br/>Gao Y et al. · *Radiology: Artificial Intelligence* · 2026-01-01 🩻🎗️
- **[Collaborative Integration of AI and Human Expertise to Improve Detection of Chest Radiograph Abnormalities](https://doi.org/10.1148/ryai.240277)**<br/>Awasthi A et al. · *Radiology: Artificial Intelligence* · 2025-09-01 🩻
- **[Retrieval-Augmented Generation with Large Language Models in Radiology: From Theory to Practice](https://doi.org/10.1148/ryai.240790)**<br/>Fink A et al. · *Radiology: Artificial Intelligence* · 2025-07-01 🩻
- **[RadioRAG: Online Retrieval-Augmented Generation for Radiology Question Answering](https://doi.org/10.1148/ryai.240476)**<br/>Tayebi Arasteh S et al. · *Radiology: Artificial Intelligence* · 2025-07-01 🩻
- **[Enhancing Large Language Models with Retrieval-Augmented Generation: A Radiology-Specific Approach](https://doi.org/10.1148/ryai.240313)**<br/>Weinert DA et al. · *Radiology: Artificial Intelligence* · 2025-05-01 🩻
- **[Performance of an Open-Source Large Language Model in Extracting Information from Free-Text Radiology Reports](https://doi.org/10.1148/ryai.230364)**<br/>Le Guellec B et al. · *Radiology: Artificial Intelligence* · 2024-07-01 🩻🚑
- **[Generative Large Language Models for Detection of Speech Recognition Errors in Radiology Reports](https://doi.org/10.1148/ryai.230205)**<br/>Schmidt RA et al. · *Radiology: Artificial Intelligence* · 2024-03-01 🩻
- **[Performance of ChatGPT on the Brazilian Radiology and Diagnostic Imaging and Mammography Board Examinations](https://doi.org/10.1148/ryai.230103)**<br/>Almeida LC et al. · *Radiology: Artificial Intelligence* · 2024-01-01 🩻🎓
- **[Risk of Bias in Chest Radiography Deep Learning Foundation Models](https://doi.org/10.1148/ryai.230060)**<br/>Glocker B et al. · *Radiology: Artificial Intelligence* · 2023-09-27 🩻🌍

</details>

<!-- PAPERS:END -->

## 补充与勘误

漏收、误收、链接失效，欢迎开 Issue 或提 PR。注意 README 是脚本生成的，改动请落在 [data/papers.json](data/papers.json)。

## License

CC0-1.0。论文元数据来自 Europe PMC。
