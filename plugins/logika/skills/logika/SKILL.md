---
name: logika
license: MIT
metadata:
  version: "2.1.0"
  upstream-version: "2.0.0"
  languages: "en,ru"
description: >
  Review and repair arguments in English or Russian using classical formal logic
  from G. Chelpanov's textbook. Check inferences, syllogisms, definitions, divisions,
  induction, and analogies; identify fallacies and solve logic exercises.
  Use for logical review, argument repair, and logic problems.
  Русские запросы: «проверь логику», «найди логические ошибки», «исправь логику»,
  «поправь аргументацию», «проверь силлогизм».
---

# Logika / Логика

Choose the instruction language from the text or exercise being analyzed. If no
source text is present, use the user's requested language, otherwise the language
of their request. Explicit language instructions take precedence.

- **English:** read [SKILL.en.md](SKILL.en.md), then its English references as needed.
- **Русский:** прочитай [SKILL.ru.md](SKILL.ru.md), затем нужные русские справочники.

Load one instruction version. For mixed-language material, use the references
needed for each passage. Preserve the source language when repairing a text;
translate only when requested. Write the analysis in the user's requested
response language, or the language of their request by default.

Both versions provide review, repair, exercise, and explicit BQA/MCQA benchmark
modes. Reference and script paths are relative to this skill directory.
