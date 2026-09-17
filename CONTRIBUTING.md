# Contributing

Thanks for helping improve Resume Opportunity Match. Contributions should keep the skill evidence-first, fact-bound, and limited to job-related evidence.

## Feedback and issues

Use only synthetic or fully redacted material in issues and examples. Describe the host, skill version or commit, input type, expected behavior, actual behavior, and a minimal synthetic reproduction. Do not submit a real resume, contact details, credentials, or other personal data.

## Pull requests

Focused pull requests are welcome. Explain the problem and scope, keep unrelated changes out, and update documentation and `CHANGELOG.md` when appropriate.

Before opening a pull request, run:

```powershell
python -m unittest discover -s tests -v
python scripts/validate_skill.py skills/resume-opportunity-match
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills/resume-opportunity-match
git diff --check
```

The third command applies when the Codex system `skill-creator` validator is installed. Changes to the skill instructions also need a behavior evaluation using the documented synthetic cases: compare the affected behavior with the recorded baseline or treatment results, record the observed outcome, and change only the instruction needed to address a demonstrated gap.
