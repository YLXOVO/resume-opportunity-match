# Installation

[中文](INSTALLATION.zh-CN.md)

The canonical, tested source is `skills/resume-opportunity-match/` in this repository. Codex is the only verified host. Other Agent Skills hosts have not been tested by this project.

Choose one active installation for a host so updates are unambiguous.

## Personal Codex skill directory

Copy the canonical skill into your personal Codex skills directory:

```powershell
Copy-Item -Recurse -Force .\skills\resume-opportunity-match "$env:USERPROFILE\.codex\skills\resume-opportunity-match"
```

Restart or refresh the host if necessary. A copied installation is independent; repository updates do not update it automatically.

## Repository-local `.agents/skills`

For a project-specific copy, run from this repository (or replace the source path with its canonical location):

```powershell
New-Item -ItemType Directory -Force .\.agents\skills | Out-Null
Copy-Item -Recurse -Force .\skills\resume-opportunity-match .\.agents\skills\resume-opportunity-match
```

Confirm that the target host reads repository-local skills before relying on it. This project has only verified Codex.

## Windows directory link

After confirming the destination does not already exist, a Windows junction can point the personal directory at the canonical source:

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.codex\skills\resume-opportunity-match" -Target (Resolve-Path .\skills\resume-opportunity-match)
```

The junction avoids copy drift. If local policy blocks links, use a copied installation and repeat the update step after source changes.

## Update and verify

For a copied installation, replace it after updating this repository:

```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\skills\resume-opportunity-match"
Copy-Item -Recurse -Force .\skills\resume-opportunity-match "$env:USERPROFILE\.codex\skills\resume-opportunity-match"
```

For a junction, update the canonical source and verify the link target; do not copy over the junction. Validate the source or installed copy with:

```powershell
python scripts/validate_skill.py skills/resume-opportunity-match
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills/resume-opportunity-match
```

The second command applies only in a Codex environment with the system `skill-creator` validator installed.

Use the synthetic examples in [`../examples/`](../examples/) for a safe explicit-invocation check.

## Uninstall

Check the exact target before removing a personal copy or junction:

```powershell
Get-Item "$env:USERPROFILE\.codex\skills\resume-opportunity-match"
Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\skills\resume-opportunity-match"
```

For a repository-local installation, remove only that repository's `.agents\skills\resume-opportunity-match`. Uninstalling a copy does not delete this repository's canonical source.
