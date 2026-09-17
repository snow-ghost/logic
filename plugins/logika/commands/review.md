---
description: Review argument logic without rewriting the source (English or Russian).
---

Review the following text using the logika skill.

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/logika/SKILL.md` and select the English or Russian instructions as directed there.
2. Read the relevant language-specific references, especially the error catalog.
3. Apply review mode: identify the thesis and premises, check the inference forms, and explain each logical or evidential issue.
4. Return the review format from the selected instructions. Use the user's requested response language, otherwise the language of their request, and keep source quotations in their original language.

Do not rewrite the source in this command. If the user subsequently requests a repair, switch to repair mode.

Text to review:
$ARGUMENTS
