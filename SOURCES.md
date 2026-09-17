# Component origins

The entire collection is distributed under the [MIT License](LICENSE).

| Component | Author and source | Version | License |
|---|---|---|---|
| `logika` | Pavel Rykov, [EvilFreelancer/logika](https://github.com/EvilFreelancer/logika); bilingual adaptation by Sergei Uskov | Based on 2.0.0; current version 2.1.0 | [MIT](plugins/logika/LICENSE) |
| `technical-style-editor` | Sergei Uskov ([snow-ghost](https://github.com/snow-ghost)) | 0.3.0 | [MIT](plugins/technical-style-editor/LICENSE) |
| Plugin catalogs and package checks | Sergei Uskov ([snow-ghost](https://github.com/snow-ghost)) | 0.2.0 | [MIT](LICENSE) |

## Contents

- `logika`: English and Russian instructions, six reference guides per language, an optional Russian digest of the 26 chapters of Chelpanov's textbook, an MIT license, and a Claude Code review command.
- `technical-style-editor`: English and Russian instructions and reference guides, a bilingual diagnostic script, interface metadata, and an MIT license.
- Plugin manifests and catalogs install the same skill directories from `snow-ghost/logic`.

## Logic adaptations

- Version metadata uses the standard `metadata` mapping, with the upstream version retained separately.
- The MIT license is included in the plugin and the standalone skill directory.
- The review workflow works with all clients; `/logika:review` is an additional Claude Code plugin command.
- The full textbook is not bundled. The optional Russian chapter digest is retained without a dependency on an absent source file.
- English instructions and reference guides adapt the source terminology and examples. They distinguish the traditional nonempty-class assumptions from modern predicate logic and distinguish missing evidence from a false premise. The original Russian reference guides remain available.
- One `SKILL.md` selects the language-specific instructions, so installing both languages does not create duplicate skills.

## Technical editor adaptations

- Both instruction languages preserve the constraints on facts, terminology, modality, and implementation status.
- English editing examples and phrase rules cover English rhetorical contrasts, filler, promotional wording, comparisons, and bureaucratic phrasing.
- The diagnostic script retains the Russian rules and adds `--language en`, `--language ru`, and `--language auto`. Auto mode runs both rule sets, including on mixed-language text.
- The script only reports passages for review; it does not rewrite files or determine their authorship.
