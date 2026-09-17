# Installation

[中文](INSTALLATION.zh-CN.md)

This guide is for Codex users. Codex is the only host this project has tested. You do not need to download the whole repository or run PowerShell commands for the recommended installation.

## Install for your account (recommended)

1. Open a Codex conversation.
2. Send this request:

   ```text
   $skill-installer Install the skill from https://github.com/YLXOVO/resume-opportunity-match/tree/main/skills/resume-opportunity-match
   ```

3. Wait for the installer to confirm success. It installs the `resume-opportunity-match` skill into your personal Codex skills directory; you do not need to create or copy folders yourself.
4. Start a new turn. Look for **Resume Opportunity Match** in Codex's Skills list, or type `$resume-opportunity-match` in a new prompt and check that Codex recognizes it. If it does not appear, restart Codex and check again before reinstalling.

To try it, provide a readable resume and a job description in a conversation and ask Codex to compare them. You can explicitly mention `$resume-opportunity-match`, or let Codex select the skill from your request.

## Install for one repository only (optional)

Use this option if the skill should be available only while working in a particular repository. Do not also keep a personal installation of the same skill active unless you intentionally want two copies: Codex does not merge same-named skills.

1. On [GitHub](https://github.com/YLXOVO/resume-opportunity-match), select **Code → Download ZIP** and extract it. If you already have a checkout, use that instead.
2. In your file manager, find the extracted `skills/resume-opportunity-match` folder. Copy that whole folder into the target repository's `.agents/skills` folder. Create `.agents/skills` in the target repository if it does not exist.
3. Check that the target repository now contains `.agents/skills/resume-opportunity-match/SKILL.md`. The repository's README, tests, and other files are not needed for installation.
4. Open the target repository in Codex. If the skill does not appear, restart Codex.

## Update or remove

The installer does not overwrite an existing skill with the same name. Before updating, check whether the installed folder is a junction or symbolic link: if it is, update its source checkout instead of deleting the source. If you cannot tell, ask Codex to inspect that folder before removing anything. For a regular personal installation, save any changes you made inside the skill, remove only the installed `resume-opportunity-match` folder, and repeat the recommended installation. By default, that folder is under `~/.codex/skills/` (on Windows, `%USERPROFILE%\.codex\skills\`). Do not remove the entire `skills` directory.

For a repository-only installation, replace only that repository's `.agents/skills/resume-opportunity-match` folder with a fresh copy. To uninstall, remove only the corresponding skill folder, never the entire `.agents/skills` directory. Neither action requires deleting this source repository.

Maintainers can find command-line validation steps in [Testing](TESTING.md).
