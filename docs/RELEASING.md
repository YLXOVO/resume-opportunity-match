# Releasing

Version 0.1.0 is local-only. This document describes a future GitHub publication workflow; it does not create a remote repository, install GitHub CLI, handle credentials, push changes, create a tag, or create a release.

## Prepare locally

1. Confirm `CHANGELOG.md` has the intended version and date.
2. Run the commands in [TESTING.md](TESTING.md), including `git diff --check`.
3. Review the staged diff for synthetic-only examples, no personal data, accurate documentation, and the intended version.
4. Commit the release-ready changes on `main`.

## GitHub web flow

1. Create an empty GitHub repository in the desired account or organization. Do not initialize it with conflicting files.
2. Add that repository as `origin` in the local clone, then push `main` using the authenticated GitHub-provided instructions.
3. From the reviewed local commit, create and push an annotated tag before opening the release page:

   ```powershell
   git tag -a v0.1.0 -m "Release v0.1.0"
   git push origin v0.1.0
   ```

4. On GitHub, create a Release and select the existing `v0.1.0` tag. Copy only the matching version section from `CHANGELOG.md` into the release notes; do not include `Unreleased` or prior version sections. Mark pre-release status if applicable.

## Optional GitHub CLI flow

If `gh` is already installed and authenticated by the maintainer, equivalent commands may be:

```powershell
git remote add origin https://github.com/OWNER/REPOSITORY.git
git push -u origin main
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0
# Create release-notes-v0.1.0.md with only the [0.1.0] section from CHANGELOG.md.
gh release create v0.1.0 --title "v0.1.0" --notes-file release-notes-v0.1.0.md
```

Replace `OWNER/REPOSITORY` with the actual future repository. The temporary notes file must contain only the target version's notes; alternatively, paste that section manually into the GitHub release form. Inspect each command before running it. Do not install `gh`, authenticate, or publish from this repository without an explicit maintainer decision.
