import tempfile
import unittest
from pathlib import Path

from scripts.validate_skill import validate_skill


class ValidateSkillTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

    def make_skill(self, body: str, metadata: str | None = None) -> Path:
        root = Path(self.temp_dir.name) / "resume-opportunity-match"
        root.mkdir(parents=True)
        (root / "SKILL.md").write_text(body, encoding="utf-8")
        if metadata is not None:
            agent_dir = root / "agents"
            agent_dir.mkdir()
            (agent_dir / "openai.yaml").write_text(metadata, encoding="utf-8")
        return root

    def test_accepts_valid_skill_and_metadata(self) -> None:
        skill = self.make_skill(
            "---\nname: resume-opportunity-match\n"
            "description: Use when comparing a resume with a target opportunity.\n---\n\n# Instructions\n",
            'interface:\n  default_prompt: "Use $resume-opportunity-match to compare my resume."\n'
            "policy:\n  allow_implicit_invocation: true\n",
        )
        self.assertEqual([], validate_skill(skill))

    def test_requires_frontmatter_name_and_description(self) -> None:
        skill = self.make_skill("# Missing frontmatter\n")
        self.assertIn("SKILL.md must start with YAML frontmatter", validate_skill(skill))

    def test_requires_directory_and_name_to_match(self) -> None:
        skill = self.make_skill(
            "---\nname: different-name\n"
            "description: Use when comparing a resume with an opportunity.\n---\n"
        )
        self.assertIn("frontmatter name must match the skill directory", validate_skill(skill))

    def test_requires_default_prompt_to_name_the_skill(self) -> None:
        skill = self.make_skill(
            "---\nname: resume-opportunity-match\n"
            "description: Use when comparing a resume with a target opportunity.\n---\n",
            'interface:\n  default_prompt: "Compare my resume."\n',
        )
        self.assertIn(
            "openai.yaml default_prompt must mention $resume-opportunity-match",
            validate_skill(skill),
        )

    def test_rejects_default_prompt_with_skill_name_as_a_prefix(self) -> None:
        skill = self.make_skill(
            "---\nname: resume-opportunity-match\n"
            "description: Use when comparing a resume with a target opportunity.\n---\n",
            'interface:\n  default_prompt: "Use $resume-opportunity-match-wrong."\n',
        )
        self.assertIn(
            "openai.yaml default_prompt must mention $resume-opportunity-match",
            validate_skill(skill),
        )

    def test_does_not_accept_token_outside_default_prompt(self) -> None:
        skill = self.make_skill(
            "---\nname: resume-opportunity-match\n"
            "description: Use when comparing a resume with a target opportunity.\n---\n",
            'interface:\n  default_prompt: "Compare my resume."\n'
            'metadata: "$resume-opportunity-match"\n',
        )
        self.assertIn(
            "openai.yaml default_prompt must mention $resume-opportunity-match",
            validate_skill(skill),
        )

    def test_requires_token_in_interface_default_prompt(self) -> None:
        skill = self.make_skill(
            "---\nname: resume-opportunity-match\n"
            "description: Use when comparing a resume with a target opportunity.\n---\n",
            'metadata:\n  default_prompt: "$resume-opportunity-match"\n'
            'interface:\n  default_prompt: "Compare my resume."\n',
        )
        self.assertIn(
            "openai.yaml default_prompt must mention $resume-opportunity-match",
            validate_skill(skill),
        )

    def test_requires_default_prompt_to_be_direct_interface_child(self) -> None:
        skill = self.make_skill(
            "---\nname: resume-opportunity-match\n"
            "description: Use when comparing a resume with a target opportunity.\n---\n",
            'interface:\n  metadata:\n    default_prompt: "$resume-opportunity-match"\n',
        )
        self.assertIn(
            "openai.yaml default_prompt must mention $resume-opportunity-match",
            validate_skill(skill),
        )


if __name__ == "__main__":
    unittest.main()
