import ast
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGINS = {
    "logika": "2.1.0",
    "technical-style-editor": "0.3.0",
}
FRONTMATTER_NAME = re.compile(r"^name:\s*([^\s]+)\s*$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def load_json(path: Path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


class RepositoryLayoutTests(unittest.TestCase):
    def test_marketplaces_expose_the_same_plugins(self):
        codex = load_json(ROOT / ".agents/plugins/marketplace.json")
        claude = load_json(ROOT / ".claude-plugin/marketplace.json")

        self.assertEqual(codex["name"], "logic")
        self.assertEqual(claude["name"], "logic")
        self.assertEqual(
            [entry["name"] for entry in codex["plugins"]],
            list(PLUGINS),
        )
        self.assertEqual(
            [entry["name"] for entry in claude["plugins"]],
            list(PLUGINS),
        )

        for entry in codex["plugins"]:
            name = entry["name"]
            self.assertEqual(entry["source"], {
                "source": "local",
                "path": f"./plugins/{name}",
            })
            self.assertEqual(entry["policy"]["installation"], "AVAILABLE")
            self.assertEqual(entry["policy"]["authentication"], "ON_INSTALL")

        for entry in claude["plugins"]:
            name = entry["name"]
            self.assertEqual(entry["source"], f"./plugins/{name}")
            self.assertEqual(entry["version"], PLUGINS[name])

    def test_plugin_manifests_and_skill_entrypoints_agree(self):
        for name, version in PLUGINS.items():
            with self.subTest(plugin=name):
                plugin_root = ROOT / "plugins" / name
                codex = load_json(plugin_root / ".codex-plugin/plugin.json")
                claude = load_json(plugin_root / ".claude-plugin/plugin.json")

                self.assertEqual(codex["name"], name)
                self.assertEqual(claude["name"], name)
                self.assertEqual(codex["version"], version)
                self.assertEqual(claude["version"], version)
                self.assertEqual(codex["skills"], "./skills/")
                self.assertEqual(claude["skills"], "./skills/")

                skills = list((plugin_root / "skills").glob("*/SKILL.md"))
                self.assertEqual(skills, [plugin_root / "skills" / name / "SKILL.md"])

                text = skills[0].read_text(encoding="utf-8")
                self.assertTrue(text.startswith("---\n"))
                match = FRONTMATTER_NAME.search(text)
                self.assertIsNotNone(match)
                self.assertEqual(match.group(1), name)
                self.assertRegex(text, r"(?m)^description:")

    def test_skill_relative_links_resolve_inside_each_skill(self):
        for name in PLUGINS:
            skill_root = ROOT / "plugins" / name / "skills" / name
            for document in skill_root.rglob("*.md"):
                for raw_target in MARKDOWN_LINK.findall(document.read_text(encoding="utf-8")):
                    target = raw_target.strip().split("#", 1)[0]
                    if not target or target.startswith(("http://", "https://", "mailto:")):
                        continue
                    with self.subTest(skill=name, document=document.name, target=target):
                        resolved = (document.parent / target).resolve()
                        self.assertTrue(resolved.is_file(), f"{document}: missing link {target}")
                        self.assertTrue(resolved.is_relative_to(skill_root.resolve()))

    def test_bundled_python_scripts_parse(self):
        for script in ROOT.glob("plugins/*/skills/*/scripts/*.py"):
            with self.subTest(script=script.relative_to(ROOT)):
                ast.parse(script.read_text(encoding="utf-8"), filename=str(script))

    def test_required_license_notices_are_bundled(self):
        for name in PLUGINS:
            with self.subTest(plugin=name):
                license_text = (ROOT / "plugins" / name / "LICENSE").read_text(
                    encoding="utf-8"
                )
                self.assertIn("MIT License", license_text)

    def test_logika_review_command_is_bundled(self):
        self.assertTrue((ROOT / "plugins/logika/commands/review.md").is_file())


if __name__ == "__main__":
    unittest.main()
