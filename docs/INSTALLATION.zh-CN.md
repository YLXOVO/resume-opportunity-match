# 安装

[English](INSTALLATION.md)

本仓库的 `skills/resume-opportunity-match/` 是规范且经过测试的源码。Codex 是唯一已验证宿主；项目尚未测试其他 Agent Skills 宿主。

同一宿主请只选择一种启用安装方式，以免更新来源不清晰。

## 个人 Codex Skill 目录

将规范源码复制到个人 Codex Skill 目录：

```powershell
Copy-Item -Recurse -Force .\skills\resume-opportunity-match "$env:USERPROFILE\.codex\skills\resume-opportunity-match"
```

必要时重启或刷新宿主。复制安装是独立副本；更新仓库不会自动更新它。

## 仓库级 `.agents/skills`

如需项目级副本，请在本仓库中运行（或将源路径替换为规范位置）：

```powershell
New-Item -ItemType Directory -Force .\.agents\skills | Out-Null
Copy-Item -Recurse -Force .\skills\resume-opportunity-match .\.agents\skills\resume-opportunity-match
```

依赖前请确认目标宿主会读取仓库级 Skill；本项目只验证过 Codex。

## Windows 目录链接

确认目标尚不存在后，可用 Windows 目录联接让个人目录指向规范源码：

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.codex\skills\resume-opportunity-match" -Target (Resolve-Path .\skills\resume-opportunity-match)
```

目录联接能避免副本漂移。若本地策略不允许创建链接，请使用复制安装，并在源码更新后重复更新步骤。

## 更新和验证

对于复制安装，更新本仓库后替换副本：

```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\skills\resume-opportunity-match"
Copy-Item -Recurse -Force .\skills\resume-opportunity-match "$env:USERPROFILE\.codex\skills\resume-opportunity-match"
```

对于目录联接，请更新规范源码并核对链接目标；不要向该联接上覆盖复制。用以下命令验证源码或安装副本：

```powershell
python scripts/validate_skill.py skills/resume-opportunity-match
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills/resume-opportunity-match
```

第二条命令仅适用于已安装系统 `skill-creator` 验证器的 Codex 环境。

可使用 [`../examples/`](../examples/) 中的合成材料安全地进行显式调用检查。

## 卸载

删除个人副本或目录联接前，请先核对准确目标：

```powershell
Get-Item "$env:USERPROFILE\.codex\skills\resume-opportunity-match"
Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\skills\resume-opportunity-match"
```

仓库级安装只删除该仓库的 `.agents\skills\resume-opportunity-match`。卸载副本不会删除本仓库中的规范源码。
