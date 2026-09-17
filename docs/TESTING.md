# Testing

This repository separates behavioral evaluation from deterministic structure checks. The behavioral record is evidence about the tested prompts and host, not a guarantee of deterministic behavior or support in untested hosts.

## Behavioral process

Instruction work follows RED–GREEN–REFACTOR:

1. **RED:** run fresh-context, no-skill controls using the synthetic cases in `evals/cases.json` and record observable failures in `evals/results/baseline.md`.
2. **GREEN:** make the smallest instruction change that addresses an observed failure, then run the same relevant synthetic treatment cases.
3. **REFACTOR:** remove duplication or close an observed loophole, and re-run the affected case before recording the result in `evals/results/with-skill.md`.

The initial evaluation includes five no-skill controls and five with-skill combined-pressure micro-tests, plus application cases for direct and indirect complete inputs, missing opportunity, unreadable input, protected-trait pressure, and a non-trigger. The revised treatment reran the five micro-tests and a focused indirect-complete application case. It did **not** rerun every application case after the revision; see `evals/results/with-skill.md` for that limitation.

Use synthetic or fully redacted materials only. For instruction changes, test the affected prompt in a fresh context and record whether activation, the input gate, evidence labels, truthfulness, fairness, and the report shape behaved as required.

## Local checks

Run from the repository root:

```powershell
python -m unittest discover -s tests -v
python scripts/validate_skill.py skills/resume-opportunity-match
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills/resume-opportunity-match
git diff --check
```

The first command runs the standard-library unit tests. The second validates repository-specific skill structure. The third is the Codex `skill-creator` validator and is available only in a Codex environment that provides it. `git diff --check` catches whitespace errors.

## Manual documentation checks

Before release, manually verify that English and Simplified Chinese links resolve, examples remain synthetic, installation instructions match the supported host behavior, public text does not claim untested host support, and no private data or local filesystem paths appear in public documentation.
