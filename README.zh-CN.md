# Resume Opportunity Match

[English](README.md)

这是一个以证据为先的 Agent Skill：将简历与具体职位或职业机会比较，识别已有材料能证明什么、还需澄清什么，以及如何在不编造事实的前提下组织针对该机会的简历。

**已验证宿主：** Codex。其他 Agent Skills 宿主可能兼容，但本项目尚未测试或支持它们。

## 价值与边界

Skill 将结论追溯到所提供的简历和机会，使用 **Evidence sufficient**（证据充分）、**Partially supported**（部分支持）和 **No evidence found**（未发现证据）标签，输出分析及建议结构。

它不会给出匹配百分比、做录用判断、编造经历或指标、默认研究公司，也不会默认整份重写简历。之后的改写只能使用已提供事实。

## 安装和调用

规范源码位于 [`skills/resume-opportunity-match/`](skills/resume-opportunity-match/)。可在[英文安装指南](docs/INSTALLATION.md)或[中文安装指南](docs/INSTALLATION.zh-CN.md)中选择个人或仓库级安装。

请同时提供可读取的简历/CV/职业档案，以及职位描述、空缺职位、角色、实习、项目或其他目标机会。宿主可读取的输入包括粘贴文本、图片、PDF 和 DOCX。两份材料都在上下文中时，Codex 支持隐式调用 Skill；本项目尚未独立验证自动发现。也可明确请求：

```text
Use $resume-opportunity-match to compare my resume with this opportunity.
```

关于不可读输入、证据缺口和基于事实的后续改写，请阅读[英文使用指南](docs/USAGE.md)或[中文使用指南](docs/USAGE.zh-CN.md)。

## 输出与隐私

对于可读取输入，报告有稳定的十一节：输入质量、角色与行业、相关性映射、十个概念、明确与推断技能、招聘问题、支持证据、低价值内容、缺失信息、建议结构和问题。完整定义见[输出契约](docs/OUTPUT-CONTRACT.md)。

请不要向本项目提交或粘贴真实简历。分析在当前宿主中进行，只评估与工作相关的证据；受保护和敏感特征不会用于匹配分析。使用个人材料前请阅读[隐私与公平说明](docs/PRIVACY-AND-FAIRNESS.md)。

## 合成演示

所有公开示例均为虚构：[简历](examples/synthetic-resume.md)、[机会](examples/synthetic-job-description.md)和[预期报告大纲](examples/expected-report-outline.md)。它们展示格式，不构成对真实候选人的建议。

## 本地验证

```powershell
python -m unittest discover -s tests -v
python scripts/validate_skill.py skills/resume-opportunity-match
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills/resume-opportunity-match
git diff --check
```

第三条命令仅适用于已安装系统 `skill-creator` 验证器的 Codex 环境。

## 状态、许可证与反馈

0.1.0 目前仅是本地状态：未创建或验证远程仓库、发布版本或其他托管目的地。本项目采用 [MIT License](LICENSE)。在项目仍为本地状态时，请按[反馈说明](docs/USAGE.zh-CN.md#反馈)通过本地协作渠道反馈，并只提供合成或完全脱敏的材料。
