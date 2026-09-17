# Resume Opportunity Match

[简体中文](README.zh-CN.md)

An evidence-first Agent Skill for comparing a resume with one specific job or professional opportunity. It identifies what the supplied materials demonstrate, what needs clarification, and how to organize an opportunity-focused resume without inventing facts.

**Verified host:** Codex. Other Agent Skills hosts may be compatible, but this project has not tested or supported them.

## Value and limits

The skill traces conclusions to the supplied resume and opportunity, labels evidence as **Evidence sufficient**, **Partially supported**, or **No evidence found**, and produces analysis plus a proposed structure.

It does not provide a match percentage, make a hiring decision, invent achievements or metrics, research a company by default, or rewrite an entire resume by default. A later rewrite may use only supplied facts.

## Install and invoke

The canonical source is [`skills/resume-opportunity-match/`](skills/resume-opportunity-match/). Choose a personal or repository-local installation in the [installation guide](docs/INSTALLATION.md) / [中文安装指南](docs/INSTALLATION.zh-CN.md).

Provide both a readable resume/CV/profile and a job description, vacancy, role, internship, project, or other target opportunity. Host-readable inputs include pasted text, images, PDF, and DOCX. Codex supports implicit skill invocation when both artifacts are in scope; this repository has not independently verified automatic discovery. You can also ask:

```text
Use $resume-opportunity-match to compare my resume with this opportunity.
```

See the [usage guide](docs/USAGE.md) / [中文使用指南](docs/USAGE.zh-CN.md) for unreadable inputs, evidence gaps, and fact-bound follow-up rewrites.

## Output and privacy

For readable inputs, the report has eleven stable sections: input quality, role and sector, relevance map, ten concepts, requested and inferred skills, hiring problems, supporting evidence, low-value content, missing information, proposed structure, and questions. See the [output contract](docs/OUTPUT-CONTRACT.md).

Do not commit or paste a real resume into this project. Analysis occurs in the current host and considers job-related evidence only; protected and sensitive traits are excluded. Read [privacy and fairness](docs/PRIVACY-AND-FAIRNESS.md) before using personal material.

## Synthetic demonstration

All public examples are fictional: [resume](examples/synthetic-resume.md), [opportunity](examples/synthetic-job-description.md), and [expected report outline](examples/expected-report-outline.md). They demonstrate format, not advice for a real candidate.

## Verify locally

```powershell
python -m unittest discover -s tests -v
python scripts/validate_skill.py skills/resume-opportunity-match
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills/resume-opportunity-match
git diff --check
```

The third command applies only in a Codex environment with the system `skill-creator` validator installed.

## Status, license, and feedback

Version 0.1.0 is local only: no remote repository, release, or other hosting destination has been created or verified. This project is licensed under the [MIT License](LICENSE). For feedback while it remains local, use the [feedback guidance](docs/USAGE.md#feedback) with synthetic or fully redacted material.
