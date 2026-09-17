# Resume Opportunity Match — Design Specification

Status: Approved in chat on 2026-09-16, implemented, reviewed, and integrated into local `main` for 0.1.0. No remote repository, release, or publication has been created.

## 1. Purpose

`resume-opportunity-match` is a portable Agent Skill for evidence-based comparison of a candidate's resume with a specific job or professional opportunity. It adopts the perspective of a senior recruiter familiar with the role and sector, while keeping every conclusion traceable to the supplied materials.

The skill helps a candidate decide what to retain, remove, clarify, or reorganize for one opportunity. It does not invent accomplishments, rewrite an entire resume by default, assign a fabricated match percentage, or make hiring judgments from protected or sensitive personal characteristics.

## 2. Intended audience and distribution

The repository is a personal-maintainer project intended for public sharing. Version 0.1.0 will be a direct, portable skill rather than a plugin. Codex is the verified host. Other hosts implementing the Agent Skills specification may be compatible, but the project will not claim support that has not been tested.

The canonical source will live in this repository under `skills/resume-opportunity-match/`. The personal Codex installation will point to that canonical source when Windows permissions allow; otherwise it will be copied with the synchronization limitation documented.

The repository will use the `main` branch and the MIT license. This work will create a local Git repository and commits. It will not install GitHub CLI, handle credentials, create a remote repository, push, tag, or publish a GitHub Release.

## 3. Trigger and inputs

The skill should be implicitly discoverable. It activates when a user supplies or refers to both:

1. a resume, CV, professional profile, or equivalent career-history artifact; and
2. a job description, vacancy, role description, internship, project opportunity, or equivalent target-opportunity artifact.

Supported host-readable forms include images, PDF, DOCX, and pasted text. The skill relies on the host's existing file and image-reading capabilities; version 0.1.0 will not add a bespoke parser, OCR service, network service, MCP server, or file-conversion script.

If either artifact is absent or materially unreadable, the skill identifies the missing or unreadable content and pauses the substantive comparison. If both artifacts are sufficiently readable, it completes all analysis supported by the available evidence before requesting optional missing details.

The sector and target position are inferred from the opportunity. The user is asked only when the opportunity is ambiguous.

## 4. Evidence model

Every conclusion about fit must cite a concrete part of the supplied resume or opportunity. Evidence is classified as:

- **Evidence sufficient**: the resume directly demonstrates the requirement or problem-solving capability.
- **Partially supported**: the resume provides relevant but incomplete evidence.
- **No evidence found**: the supplied resume does not substantiate the requirement.

Statements derived directly from the opportunity are separated from recruiter interpretations. Interpretations such as the likely business problem behind a hire are labeled as inferences and include the textual signals that support them.

The skill does not use a numeric or percentage match score. It does not convert missing evidence into negative claims about the candidate; it states only that the supplied material does not demonstrate the point.

## 5. Analysis workflow

The skill performs the following work in order:

1. Inventory the supplied artifacts and report unreadable, missing, or ambiguous portions.
2. Identify the target role and sector from the opportunity.
3. Extract the opportunity's most important ten words or concepts. If the source genuinely lacks ten meaningful concepts, state that limitation rather than pad the list.
4. Separate explicit requirements from reasonable recruiter inferences.
5. Map each material resume experience to the opportunity and label it relevant, partially relevant, or not relevant, with an explanation.
6. Identify the capabilities the employer is substantively seeking.
7. Infer the likely problems the hire is intended to solve, label them as inferences, and cite the signals behind each inference.
8. Map resume evidence that demonstrates the candidate can address those problems.
9. Identify resume content that consumes space without increasing credibility or relevance for this opportunity.
10. Identify important missing information and state exactly what the candidate should add or verify.
11. Propose a new resume structure tailored to the opportunity, including section order, emphasis, and placement of existing evidence.
12. List uncertainties and targeted follow-up questions.

The default deliverable is analysis plus structure, not a full rewritten resume. If the user later requests a rewrite, the skill may rewrite only from supplied facts and must preserve uncertainty rather than manufacture details.

## 6. Output contract

The report uses this stable order:

1. Input quality and reading limitations
2. Role and sector identified
3. Resume-to-opportunity relevance map
4. Ten priority words or concepts
5. Explicitly requested skills and inferred skills
6. Problems the hire may be intended to solve
7. Resume evidence that supports solving those problems
8. Low-value or space-consuming resume content
9. Missing information and exact additions to consider
10. Proposed resume structure
11. Uncertainties and questions for the candidate

The explanation follows the user's language. Proposed resume headings, keywords, and target-facing phrasing follow the opportunity's language unless the user asks otherwise.

## 7. Truthfulness and fairness constraints

The skill must not invent or inflate experience, skills, outcomes, metrics, dates, scope, responsibilities, employers, credentials, or tools. It must not advise the user to add claims that the supplied materials do not substantiate. Missing numbers may be framed as questions for the candidate, never supplied as placeholders that resemble facts.

The skill assesses only job-related experience, capability, evidence, and communication. It does not use or infer suitability from photographs, names, age, sex or gender, race or ethnicity, nationality, religion, disability or health, marital or family status, pregnancy, sexual orientation, or other protected or sensitive traits. Such information is ignored unless the user requests a lawful, non-selection-related formatting action.

No external company research is performed by default. If the user separately requests research, it must be clearly separated from the two-artifact analysis and sourced.

## 8. Repository structure

```text
resume-opportunity-match/
|-- skills/
|   `-- resume-opportunity-match/
|       |-- SKILL.md
|       `-- agents/openai.yaml
|-- docs/
|   |-- DESIGN.md
|   |-- INSTALLATION.md
|   |-- INSTALLATION.zh-CN.md
|   |-- USAGE.md
|   |-- USAGE.zh-CN.md
|   |-- OUTPUT-CONTRACT.md
|   |-- PRIVACY-AND-FAIRNESS.md
|   |-- TESTING.md
|   |-- RELEASING.md
|   `-- REFERENCES.md
|-- examples/
|   |-- synthetic-resume.md
|   |-- synthetic-job-description.md
|   `-- expected-report-outline.md
|-- evals/
|   |-- README.md
|   `-- cases.json
|-- scripts/validate_skill.py
|-- tests/test_validate_skill.py
|-- .github/
|   |-- workflows/validate.yml
|   |-- ISSUE_TEMPLATE/
|   `-- PULL_REQUEST_TEMPLATE.md
|-- README.md
|-- README.zh-CN.md
|-- CONTRIBUTING.md
|-- SECURITY.md
|-- CHANGELOG.md
|-- LICENSE
`-- .gitignore
```

Repository documentation stays outside the skill directory so it does not inflate the skill's execution context. The skill itself remains instruction-first and contains no runtime scripts because its analysis requires judgment rather than deterministic transformation.

## 9. UI metadata

`agents/openai.yaml` will provide:

- display name: `Resume Opportunity Match`
- a short description suitable for the Codex skill picker
- a default prompt that explicitly invokes `$resume-opportunity-match`
- implicit invocation enabled

No icon assets or external tool dependencies are included in version 0.1.0.

## 10. Examples and documentation

The public examples use only synthetic resumes and opportunities. They demonstrate the output shape without teaching the skill to fabricate user data. Real resumes, names, contact details, employers, or application materials are never committed.

The English README is the default international entry point. `README.zh-CN.md` is a complete Chinese counterpart. Installation and usage guides are also bilingual. Specialist governance and maintenance documents may be English-only when their content is not part of the end-user path.

Documentation covers purpose, non-goals, compatibility, installation, uninstallation, invocation, supported inputs, output contract, privacy and fair-use boundaries, testing, maintenance, and local-to-GitHub publication.

## 11. Validation strategy

Creation follows RED–GREEN–REFACTOR for behavioral instructions:

### RED

Run clean-context baseline scenarios without the skill. Include direct, indirect, incomplete, non-trigger, fabrication-pressure, unreadable-input, and protected-trait scenarios. Record observable failures and rationalizations.

### GREEN

Write the smallest skill that corrects observed failures. Run the same scenarios with the skill and verify both activation and output-contract compliance.

### REFACTOR

Close demonstrated loopholes, keep the instructions concise, and repeat the affected scenarios. Do not add rules for hypothetical failures that tests did not expose.

Structural validation consists of:

- the bundled Codex skill creator validator;
- a repository-local, standard-library Python validator written test-first;
- unit tests for valid and invalid skill fixtures;
- GitHub Actions running the validator and unit tests;
- manual checks of bilingual links, installation instructions, and the synthetic example.

Behavioral evaluation cases live in `evals/cases.json`. The repository documents results without claiming deterministic model behavior or universal host compatibility.

## 12. Completion criteria

Implementation is complete when all of the following are true:

- The skill and UI metadata validate structurally.
- Baseline and with-skill behavioral evaluations are recorded and reviewed.
- The skill respects the evidence, truthfulness, fairness, language, and output contracts.
- Repository validator tests and GitHub Actions configuration pass locally where applicable.
- Documentation contains no placeholders, broken local links, real personal data, or unsupported compatibility claims.
- The repository is initialized on `main` and contains clean, meaningful local commits.
- The personal skill installation resolves to the canonical tested skill directory.
- Publishing instructions are sufficient to create a public GitHub repository later without exposing credentials.

## 13. Authoritative references

- OpenAI, Build skills: https://learn.chatgpt.com/docs/build-skills
- Agent Skills specification: https://agentskills.io/specification
- Agent Skills reference repository: https://github.com/agentskills/agentskills
- OpenAI plugin build guidance for a possible future distribution step: https://developers.openai.com/plugins/build/plugins
