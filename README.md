# Logic and Technical Style Editor

Two skills for **Codex, Claude Code, and OpenCode**, with instructions and reference material in **English and Russian**. Both skills are licensed under the [MIT License](LICENSE).

| Skill | Purpose | Version | Instructions |
|---|---|---|---|
| `logika` | Review and repair arguments; check syllogisms, definitions, induction, and fallacies using Chelpanov's classical logic | 2.1.0 | [English](plugins/logika/skills/logika/SKILL.en.md) · [Russian](plugins/logika/skills/logika/SKILL.ru.md) |
| `technical-style-editor` | Edit technical writing while preserving facts, terminology, constraints, and implementation status | 0.3.0 | [English](plugins/technical-style-editor/skills/technical-style-editor/SKILL.en.md) · [Russian](plugins/technical-style-editor/skills/technical-style-editor/SKILL.ru.md) |

## Language selection

Each skill has one installable entry point, `SKILL.md`, which selects the English or Russian instructions from the source text or the user's request. The skill names stay the same in both languages; there are no separate language plugins to install.

Editing preserves the source language unless you request a translation. You can specify a different language for the explanation. For mixed-language documents, the editor applies each language's rules to the corresponding passages.

The logic skill includes six reference guides in each language. The technical editor includes two reference guides in each language and a shared bilingual diagnostic script. An additional [26-chapter textbook digest](plugins/logika/skills/logika/docs/konspekt.md) is available in Russian as optional background; it is not required for the English workflow.

## Install both skills for all three clients

Requires Git, Node.js, and npm. Preview the available skills:

```bash
npx skills add snow-ghost/logic --list
```

Install both in your user profile:

```bash
npx skills add snow-ghost/logic \
  --skill logika technical-style-editor \
  --global --agent codex claude-code opencode
```

To target one client, keep only its name after `--agent`. To install one skill, keep only its name after `--skill`. Remove `--global` for a project installation. Add `--copy` to use copies instead of symbolic links.

These commands use [Skills CLI](https://github.com/vercel-labs/skills). Choose one installation method per client: installing the same skill both as a folder and as a plugin can create duplicates. Update Skills CLI installations with `npx skills update`.

## Codex plugins

```bash
codex plugin marketplace add snow-ghost/logic
codex plugin add logika@logic
codex plugin add technical-style-editor@logic
```

Select a skill through `/skills` or mention it in your prompt:

```text
$logika Review the logic: All cats are mammals. A whale is a mammal. Therefore a whale is a cat.

$technical-style-editor Edit the technical text in docs/design.md. Preserve its language and implementation status.
```

See the [Codex skills documentation](https://learn.chatgpt.com/docs/build-skills). Start a new session if newly installed skills do not appear.

## Claude Code plugins

Run in a terminal:

```bash
claude plugin marketplace add snow-ghost/logic
claude plugin install logika@logic
claude plugin install technical-style-editor@logic
```

Then use the namespaced commands in chat:

```text
/logika:logika Repair this argument: Sales rose after the website update, so the update must have caused the increase.

/logika:review All cats are mammals. A whale is a mammal. Therefore a whale is a cat.

/technical-style-editor:technical-style-editor Edit docs/design.md in clear, direct technical prose.
```

With Skills CLI or manual folder installation, use `/logika` and `/technical-style-editor`. The `/logika:review` command is included in the plugin; with a folder installation, ask the skill to review the logic.

See the Claude Code documentation for [plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) and [skills](https://code.claude.com/docs/en/skills).

## OpenCode

Install only for OpenCode:

```bash
npx skills add snow-ghost/logic \
  --skill logika technical-style-editor --global --agent opencode
```

Example prompts:

```text
Use the logika skill to review this argument: ...

Use the technical-style-editor skill to edit docs/design.md.
```

OpenCode loads the instructions through its built-in `skill` tool. See the [OpenCode skills documentation](https://opencode.ai/docs/skills/).

## Manual installation without Node.js

Clone the collection and copy the skill directories. For Codex:

```bash
git clone https://github.com/snow-ghost/logic.git
cd logic
mkdir -p "$HOME/.agents/skills"
cp -R plugins/logika/skills/logika "$HOME/.agents/skills/"
cp -R plugins/technical-style-editor/skills/technical-style-editor "$HOME/.agents/skills/"
```

Use the appropriate destination for your client:

| Client | User installation | Project installation |
|---|---|---|
| Codex | `~/.agents/skills/` | `.agents/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `.opencode/skills/` |

Keep the directory names `logika` and `technical-style-editor`, and copy their entire contents, including both language versions, references, scripts, and licenses. Save any local changes before replacing an existing installation.

OpenCode also discovers skills in `~/.agents/skills/` and `~/.claude/skills/`, so an additional copy is unnecessary if the skills are already there. To update a manual installation, run `git pull --ff-only` in this repository's clone and copy the skill directories again.

## Workflows

**Logic:** request a review for diagnosis without rewriting, a repair for diagnosis followed by a revised argument, or an exercise solution for a step-by-step explanation. Benchmark JSON is reserved for explicitly requested BQA/MCQA tasks. Validity and truth of premises are assessed separately.

**Technical editing:** basic mode edits style and structure. Extended mode checks evidence for comparisons, causal claims, quality, and implementation readiness. Findings from the diagnostic script require human or agent review; they neither prove an error nor establish machine authorship.

You can combine the skills:

```text
First use logika to check the argument. Then use technical-style-editor to revise the style while preserving the facts and addressing the logical issues.
```

## Run the style checker directly

The optional diagnostic script requires **Python 3.9+**, with no external Python dependencies. From the repository root:

```bash
python3 plugins/technical-style-editor/skills/technical-style-editor/scripts/lint_technical_style.py \
  path/to/document.md --language en --extended
```

Use `--language ru` for Russian, or `--language auto` (the default) to run both sets of phrase rules, including on mixed-language text. Phrase findings use the language of their rule; in auto mode, structural messages follow the predominant language of the passage and the summary follows the document.

Add `--json` for structured output. Use `-` as the path to read standard input. The script does not modify the source. Exit codes are `0` for no findings, `1` for passages requiring review, and `2` for an input or argument error. Enable `--forbid-yo` (Russian only) or `--forbid-long-dash` only when the author requests those restrictions.

## Repository layout and validation

```text
.agents/plugins/marketplace.json      # Codex catalog
.claude-plugin/marketplace.json       # Claude Code catalog
plugins/<name>/
  .codex-plugin/plugin.json
  .claude-plugin/plugin.json
  skills/<name>/
    SKILL.md                         # language selection and discovery metadata
    SKILL.en.md                      # English instructions
    SKILL.ru.md                      # Russian instructions
    references/                      # Russian reference guides
      en/                            # English reference guides
    LICENSE
```

Validate the package and the bilingual style checker:

```bash
python3 -m unittest discover -s tests -v
claude plugin validate .
claude plugin validate plugins/logika
claude plugin validate plugins/technical-style-editor
```

## Attribution and license

The entire collection is [MIT-licensed](LICENSE).

The logic skill is based on [EvilFreelancer/logika](https://github.com/EvilFreelancer/logika) 2.0.0 by Pavel Rykov. Its original [MIT license and copyright notice](plugins/logika/LICENSE) are preserved in both the plugin and the installable skill directory.

The technical editor is by Sergei Uskov ([snow-ghost](https://github.com/snow-ghost)). Its [MIT license](plugins/technical-style-editor/LICENSE) is also included in both locations.

See [SOURCES.md](SOURCES.md) for the component origins and adaptations.
