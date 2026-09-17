from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values


def _default_prompt(text: str) -> str:
    in_interface = False
    interface_indent = -1
    interface_child_indent: int | None = None
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        if indent == 0 and stripped == "interface:":
            in_interface = True
            interface_indent = indent
            interface_child_indent = None
            continue
        if not in_interface:
            continue
        if indent <= interface_indent:
            in_interface = False
            continue
        if interface_child_indent is None:
            interface_child_indent = indent
        if indent != interface_child_indent:
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        if key.strip() != "default_prompt":
            continue
        value = value.strip()
        if value.startswith(('"', "'")):
            quote = value[0]
            end = value.find(quote, 1)
            return value[1:end] if end != -1 else value[1:]
        return value.split("#", 1)[0].strip()
    return ""


def _mentions_skill_token(prompt: str, name: str) -> bool:
    token = re.escape("$" + name)
    return re.search(rf"(?<![A-Za-z0-9_-]){token}(?![A-Za-z0-9_-])", prompt) is not None


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return ["SKILL.md is required"]
    text = skill_file.read_text(encoding="utf-8")
    data = _frontmatter(text)
    if not data:
        return ["SKILL.md must start with YAML frontmatter"]
    name = data.get("name", "")
    description = data.get("description", "")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append("frontmatter name must use lowercase letters, digits, and hyphens")
    if name != skill_dir.name:
        errors.append("frontmatter name must match the skill directory")
    if not description or len(description) > 1024:
        errors.append("frontmatter description must contain 1 to 1024 characters")
    metadata = skill_dir / "agents" / "openai.yaml"
    if metadata.is_file():
        metadata_text = metadata.read_text(encoding="utf-8")
        if not _mentions_skill_token(_default_prompt(metadata_text), name):
            errors.append("openai.yaml default_prompt must mention $" + name)
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_skill.py PATH_TO_SKILL", file=sys.stderr)
        return 2
    errors = validate_skill(Path(argv[1]))
    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
