# 使用指南

[English](USAGE.md)

## 提供两份可读取材料

请同时提供简历、CV 或职业档案，以及具体职位、角色、实习、项目或其他机会。只要宿主可读取，粘贴文本、图片、PDF 和 DOCX 都可使用；Skill 不增加解析器、OCR 或网络服务。

可使用合成[简历](../examples/synthetic-resume.md)和[机会](../examples/synthetic-job-description.md)安全体验流程。

## 自动和显式调用

当两份材料已提供或被清楚引用来进行匹配分析或定制时，Skill 可以自动调用。为避免歧义，可明确请求：

```text
Use $resume-opportunity-match to compare my resume with this opportunity. Keep conclusions tied to the supplied material.
```

解释跟随用户语言。建议的标题、关键词和面向目标的措辞跟随机会描述的语言，除非另有要求。

## 输入缺失或不可读

任一必需材料缺失或实质不可读时，Skill 只输出 **Input quality and reading limitations**，说明具体缺口，请求可读副本，然后停止。它不猜测文字，也不生成空的十一节报告。

## 证据缺口

- **Evidence sufficient** — 简历直接证明了要求或能力。
- **Partially supported** — 存在相关证据但有重要缺口，包括日期、范围、符合条件的职责或连续性尚未确认。
- **No evidence found** — 所提供简历没有证实该点；这不是关于候选人的负面断言。

若年限或范围不清楚，请提供准确月份和符合条件的职责。不要要求以看似合理的指标、职责或事实化措辞填补缺口。

## 可选的后续改写

默认结果为分析加建议结构。审阅后可提出聚焦改写：

```text
Rewrite only the Northstar experience using the facts already supplied. Preserve uncertainty and do not add outcomes or metrics.
```

改写只能使用已提供事实。默认不开启外部公司研究；单独请求研究时，应将其与两份材料的分析分开，并提供来源。

## 反馈

项目没有已配置或已验证的远程问题追踪器。请通过本地协作渠道反馈，并提供简洁的合成或完全脱敏复现：宿主、输入类型、提示、期望行为、实际行为和相关报告章节。不要包含真实简历、联系方式、凭据或其他个人数据。
