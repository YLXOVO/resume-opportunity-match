# Usage

[中文](USAGE.zh-CN.md)

## Provide two readable artifacts

Supply both a resume, CV, or professional profile and a specific job, role, internship, project, or other opportunity. Pasted text, images, PDFs, and DOCX files are usable when the host can read them; the skill adds no parser, OCR, or network service.

Explore safely with the synthetic [resume](../examples/synthetic-resume.md) and [opportunity](../examples/synthetic-job-description.md).

## Automatic and explicit invocation

The skill is eligible for automatic invocation when both artifacts are supplied or clearly referenced for fit analysis or tailoring. For an unambiguous request:

```text
Use $resume-opportunity-match to compare my resume with this opportunity. Keep conclusions tied to the supplied material.
```

Explanation follows the user's language. Proposed headings, keywords, and target-facing phrasing follow the opportunity's language unless requested otherwise.

## Missing or unreadable input

When either required artifact is absent or materially unreadable, the skill outputs only **Input quality and reading limitations**, identifies the exact gap, requests a readable copy, and stops. It does not guess text or create an empty eleven-section report.

## Evidence gaps

- **Evidence sufficient** — the resume directly demonstrates the requirement or capability.
- **Partially supported** — relevant evidence has a material gap, including unresolved dates, scope, qualifying duties, or continuity.
- **No evidence found** — the supplied resume does not substantiate the point; this is not a negative claim about the candidate.

Supply exact months and qualifying duties where duration or scope is unclear. Do not request plausible metrics, responsibilities, or fact-like wording to fill a gap.

## Optional follow-up rewrite

The default result is analysis plus structure. After review, a focused request is appropriate:

```text
Rewrite only the Northstar experience using the facts already supplied. Preserve uncertainty and do not add outcomes or metrics.
```

A rewrite uses supplied facts only. External company research is off by default; separately requested research should be distinct from the two-artifact analysis and sourced.

## Feedback

There is no configured or verified remote issue tracker. Use your local collaboration channel with a concise synthetic or fully redacted reproduction: host, input type, prompt, expected behavior, observed behavior, and relevant report section. Do not include real resumes, contact information, credentials, or other personal data.
