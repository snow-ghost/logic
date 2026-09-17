---
name: technical-style-editor
license: MIT
metadata:
  version: "0.3.0"
  languages: "en,ru"
description: >
  Edit English or Russian technical writing into clear, direct, evidence-based
  prose. Remove rhetorical contrasts, filler, promotional claims, bureaucratic
  wording, and repetitive structure while preserving facts, terminology,
  constraints, and implementation status. Use for technical documents of any
  genre or length, editorial reviews, and checks for formulaic writing.
  Русские запросы: «отредактируй технический текст», «убери канцелярит»,
  «проверь технический стиль», «проверь на признаки машинного текста».
---

# Technical Style Editor / Редактор технического стиля

Choose the editing language from the source text. If no source text is present,
use the user's requested language, otherwise the language of their request.

- **English:** read [SKILL.en.md](SKILL.en.md) and use the English style references.
- **Русский:** прочитай [SKILL.ru.md](SKILL.ru.md) и используй русские справочники.

Load one instruction version. Preserve the text's language unless the user asks
for a translation. If the explanation must be in another language, keep the
editing rules appropriate to the source and write the explanation as requested.
For a bilingual document, apply each language's rules to its own passages.

The shared diagnostic script supports `--language en`, `--language ru`, and
`--language auto` (the default, which checks both languages in mixed text).
Script and reference paths are relative to this skill directory. Use Python 3.9
or newer to run the script; the editorial instructions also work without it.
