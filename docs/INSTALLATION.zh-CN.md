# 安装

[English](INSTALLATION.md)

本指南面向 Codex 用户；本项目仅在 Codex 中验证过。按推荐方式安装时，无须下载整个仓库，也无须运行 PowerShell 命令。

## 安装到个人 Codex（推荐）

1. 打开一个 Codex 对话。
2. 发送下面这条请求：

   ```text
   $skill-installer 请从 https://github.com/YLXOVO/resume-opportunity-match/tree/main/skills/resume-opportunity-match 安装这个 Skill
   ```

3. 等待安装器确认成功。它会把 `resume-opportunity-match` 安装到个人 Codex Skill 目录；你不需要手动创建或复制文件夹。
4. 开始下一轮对话。在 Codex 的 Skill 列表中查找 **Resume Opportunity Match**，或在新提示中输入 `$resume-opportunity-match`，确认 Codex 能识别它。如果没有出现，先重启 Codex 再检查，不必立即重复安装。

试用时，在对话中提供可读取的简历和职位描述，请 Codex 对比分析。你可以显式提到 `$resume-opportunity-match`，也可以让 Codex 根据请求自动选择。

## 仅安装到某个仓库（可选）

如果只希望在某个仓库中使用这个 Skill，可选择这种方式。除非明确需要两个副本，否则不要同时启用同名的个人安装：Codex 不会合并同名 Skill。

1. 在 [GitHub 仓库](https://github.com/YLXOVO/resume-opportunity-match)点击 **Code → Download ZIP** 并解压；如果已有本仓库的本地副本，可直接使用。
2. 用文件管理器找到解压后的 `skills/resume-opportunity-match` 文件夹，把**整个文件夹**复制到目标仓库的 `.agents/skills` 文件夹中。若目标仓库没有 `.agents/skills`，先在目标仓库中创建它。
3. 确认目标仓库中存在 `.agents/skills/resume-opportunity-match/SKILL.md`。安装不需要复制本仓库的 README、测试等其他文件。
4. 在 Codex 中打开目标仓库；如果 Skill 没有出现，请重启 Codex。

## 更新或卸载

安装器不会覆盖已存在的同名 Skill。更新前，先检查已安装文件夹是否为目录联接或符号链接：如果是，请更新它指向的源码仓库，不要删除源码。如果无法判断，请先让 Codex 检查该文件夹，不要贸然删除。对于普通的个人安装，先保存你对 Skill 所做的修改，只移除已安装的 `resume-opportunity-match` 文件夹，再重复推荐安装步骤。默认位置是 `~/.codex/skills/`（Windows 上为 `%USERPROFILE%\.codex\skills\`）。不要删除整个 `skills` 目录。

对于仓库级安装，只替换该目标仓库中的 `.agents/skills/resume-opportunity-match` 文件夹。卸载时，也只移除对应的 Skill 文件夹，不要删除整个 `.agents/skills` 目录；无需删除本项目的源码仓库。

维护者需要的命令行验证步骤请参阅[测试文档](TESTING.md)。
