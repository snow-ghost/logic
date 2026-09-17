#!/usr/bin/env python3
"""Find phrases that deserve manual review in English or Russian technical prose."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import english_rules


@dataclass(frozen=True)
class Finding:
    line: int
    rule: str
    message: str
    excerpt: str


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    message: str


def compile_rule(name: str, pattern: str, message: str) -> Rule:
    return Rule(name, re.compile(pattern, re.IGNORECASE | re.UNICODE), message)


BASE_RULES = (
    compile_rule(
        "rhetorical-negation",
        r"\bне\s+[^.!?\n]{1,80},?\s+(?:а|но)\s+",
        "Проверьте риторическое противопоставление; начните с прямого утверждения, если отрицание не задает ограничение.",
    ),
    compile_rule(
        "not-just",
        r"\bне\s+(?:просто|только|столько)\b",
        "Проверьте усиление через отрицание и назовите свойство прямо.",
    ),
    compile_rule(
        "negative-opening",
        r"^\s*(?:[-*]\s+|\d+[.)]\s+)?не\b",
        "Проверьте начало с отрицания; сохраните его только для запрета, инварианта или существенной границы.",
    ),
    compile_rule(
        "author-intent",
        r"\b(?:я|мы)\s+(?:хочу|хотим|постараюсь|постараемся|собираюсь|собираемся)\s+(?:рассказать|показать|объяснить|рассмотреть|поделиться)\b",
        "Замените объявление намерения содержанием.",
    ),
    compile_rule(
        "document-announcement",
        r"\b(?:в\s+(?:этом|данном)\s+(?:докладе|тексте|разделе|документе)|далее)\s+(?:мы\s+)?(?:рассмотрим|расскажу|покажем|будет\s+рассмотрен[аоы]?)\b",
        "Проверьте мета-описание текста; назовите предмет раздела прямо.",
    ),
    compile_rule(
        "importance-marker",
        r"\b(?:важно|следует|стоит)\s+(?:отметить|подчеркнуть|понимать|учитывать)\b",
        "Уберите указание на важность и сформулируйте сам факт.",
    ),
    compile_rule(
        "stance-adverb",
        r"\b(?:безусловно|несомненно|очевидно|безусловно|разумеется|естественно)\b",
        "Проверьте оценочное наречие; оно редко добавляет техническое основание.",
    ),
    compile_rule(
        "promotional-adjective",
        r"\b(?:уникальн\w*|революционн\w*|передов\w*|инновационн\w*|мощн\w*|прорывн\w*)\b",
        "Замените рекламную оценку проверяемым отличием.",
    ),
    compile_rule(
        "inflated-claim",
        r"\b(?:кардинально|радикально|принципиально|качественно)\s+(?:улучш\w*|ускор\w*|снижа\w*|повыша\w*|меня\w*)\b",
        "Сильное утверждение требует меры, условий и основания.",
    ),
    compile_rule(
        "unmeasured-improvement",
        r"\b(?:значительно|существенно|заметно|эффективно)\s+(?:улучш\w*|ускор\w*|снижа\w*|сокраща\w*|повыша\w*|увеличива\w*)\b",
        "Добавьте измерение или опишите механизм без оценочного усилителя.",
    ),
    compile_rule(
        "bureaucratic-wrapper",
        r"\b(?:в\s+рамках|с\s+целью|посредством)\b|\b(?:осуществляется|производится|выполняется)\s+(?:сбор|обработка|анализ|проверка|формирование)\b",
        "Упростите канцелярскую оболочку и назовите исполнителя действия.",
    ),
    compile_rule(
        "passive-result",
        r"\b(?:было|были|будет|будут)\s+(?:проведен[аоы]?|выполнен[аоы]?|реализован[аоы]?|осуществлен[аоы]?|сделан[аоы]?)\b",
        "Проверьте пассивную форму и назовите исполнителя, если он известен.",
    ),
    compile_rule(
        "assistant-meta",
        r"\b(?:конечно[,!]?|безусловно[,!]?|вот\s+(?:переработанный|улучшенный|готовый)\s+вариант|надеюсь[, ]+это\s+поможет)\b",
        "Удалите служебную реплику помощника из готового текста.",
    ),
)


EXTENDED_RULES = (
    compile_rule(
        "comparison-without-baseline",
        r"\b(?:лучше|быстрее|дешевле|точнее|надежнее|надёжнее)\b",
        "Проверьте объект сравнения, одинаковые условия и измеряемую величину.",
    ),
    compile_rule(
        "weak-copula",
        r"\bявля(?:ется|ются|лся|лась|лось|лись)\b",
        "Проверьте, можно ли заменить связку точным действием или определением.",
    ),
    compile_rule(
        "vague-enablement",
        r"\bпозволя(?:ет|ют|л|ла|ло|ли)\b",
        "Уточните механизм и наблюдаемый результат вместо общей возможности.",
    ),
    compile_rule(
        "demonstrative-bureaucracy",
        r"\b(?:данн(?:ый|ая|ое|ые)|указанн(?:ый|ая|ое|ые))\s+(?:подход|решение|система|метод|механизм)\b",
        "Назовите предмет непосредственно.",
    ),
    compile_rule(
        "weak-assertion",
        r"\bможно\s+(?:сказать|отметить|сделать\s+вывод)\b|\bпредставляется\s+(?:важным|целесообразным|возможным)\b",
        "Сформулируйте утверждение прямо и укажите основание.",
    ),
)


EN_BASE_RULES = tuple(compile_rule(*spec) for spec in english_rules.BASE_RULES)
EN_EXTENDED_RULES = tuple(compile_rule(*spec) for spec in english_rules.EXTENDED_RULES)


SENTENCE_RE = re.compile(r"[^.!?\n]+[.!?]?", re.UNICODE)
WORD_RE = re.compile(r"[A-Za-zА-Яа-яЁё0-9]+(?:[-'’][A-Za-zА-Яа-яЁё0-9]+)*", re.UNICODE)


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def excerpt(line: str, start: int, width: int = 150) -> str:
    compact = " ".join(line.strip().split())
    if len(compact) <= width:
        return compact
    raw_prefix = line[:start]
    compact_start = len(" ".join(raw_prefix.strip().split()))
    left = max(0, compact_start - width // 3)
    right = min(len(compact), left + width)
    piece = compact[left:right]
    if left:
        piece = "…" + piece
    if right < len(compact):
        piece += "…"
    return piece


def pattern_findings(lines: list[str], rules: Iterable[Rule]) -> list[Finding]:
    findings: list[Finding] = []
    for number, line in enumerate(lines, start=1):
        for rule in rules:
            for match in rule.pattern.finditer(line):
                findings.append(Finding(number, rule.name, rule.message, excerpt(line, match.start())))
    return findings


def message_language(text: str, language: str) -> str:
    """Choose labels only; auto mode always runs both sets of phrase rules."""
    if language != "auto":
        return language
    russian = len(re.findall(r"[А-Яа-яЁё]", text))
    english = len(re.findall(r"[A-Za-z]", text))
    return "ru" if russian > english else "en"


def optional_findings(lines: list[str], forbid_yo: bool, forbid_long_dash: bool, language: str = "auto") -> list[Finding]:
    findings: list[Finding] = []
    for number, line in enumerate(lines, start=1):
        russian = message_language(line, language) == "ru"
        if forbid_yo and re.search(r"[Ёё]", line):
            message = "По требованию текста замените букву ё на е." if russian else "Replace ё with е only as requested by the author."
            findings.append(Finding(number, "letter-yo", message, excerpt(line, 0)))
        if forbid_long_dash and "—" in line:
            message = "По требованию текста замените длинное тире." if russian else "Replace the em dash only as requested by the author."
            findings.append(Finding(number, "long-dash", message, excerpt(line, line.index("—"))))
    return findings


def extended_structure_findings(text: str, language: str = "auto") -> list[Finding]:
    findings: list[Finding] = []
    seen: dict[str, int] = {}
    for match in SENTENCE_RE.finditer(text):
        sentence = " ".join(match.group().strip().split())
        start = match.start() + len(match.group()) - len(match.group().lstrip())
        line = text.count("\n", 0, start) + 1
        words = WORD_RE.findall(sentence)
        russian = message_language(sentence, language) == "ru"
        if len(words) > 45:
            message = (
                f"В предложении {len(words)} слов; проверьте, не смешаны ли разные утверждения и условия."
                if russian else
                f"This sentence has {len(words)} words; check for mixed claims or conditions."
            )
            findings.append(Finding(line, "long-sentence", message, sentence[:150] + ("…" if len(sentence) > 150 else "")))
        normalized = sentence.casefold().strip(" .!?")
        if len(words) >= 8:
            if normalized in seen:
                message = (
                    f"Предложение повторяет строку {seen[normalized]}." if russian else
                    f"This sentence repeats line {seen[normalized]}."
                )
                findings.append(Finding(line, "repeated-sentence", message, sentence))
            else:
                seen[normalized] = line
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Review English or Russian technical prose without changing the text.")
    parser.add_argument("path", nargs="?", default="-", help="UTF-8 file, or - for standard input")
    parser.add_argument("--language", choices=("auto", "en", "ru"), default="auto", help="Phrase rules to use; auto checks both languages (default)")
    parser.add_argument("--extended", action="store_true", help="Also review comparisons, weak wording, and structure")
    parser.add_argument("--forbid-yo", action="store_true", help="Report Russian ё when the author forbids it")
    parser.add_argument("--forbid-long-dash", action="store_true", help="Report em dashes when the author forbids them")
    parser.add_argument("--json", action="store_true", help="Output findings as JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        text = read_text(args.path)
    except (OSError, UnicodeError) as error:
        label = "Не удалось прочитать текст" if args.language == "ru" else "Could not read text"
        print(f"{label}: {error}", file=sys.stderr)
        return 2

    lines = text.splitlines()
    rules = ()
    if args.language in ("ru", "auto"):
        rules += BASE_RULES + (EXTENDED_RULES if args.extended else ())
    if args.language in ("en", "auto"):
        rules += EN_BASE_RULES + (EN_EXTENDED_RULES if args.extended else ())
    findings = pattern_findings(lines, rules)
    findings.extend(optional_findings(lines, args.forbid_yo, args.forbid_long_dash, args.language))
    if args.extended:
        findings.extend(extended_structure_findings(text, args.language))
    findings.sort(key=lambda item: (item.line, item.rule, item.excerpt))

    if args.json:
        print(json.dumps([asdict(item) for item in findings], ensure_ascii=False, indent=2))
    elif findings:
        for item in findings:
            print(f"{item.line}: [{item.rule}] {item.message}")
            print(f"    {item.excerpt}")
        if message_language(text, args.language) == "ru":
            print(f"Найдено мест для ручной проверки: {len(findings)}")
        else:
            print(f"Passages to review: {len(findings)}")
    else:
        print("Срабатываний нет." if message_language(text, args.language) == "ru" else "No findings.")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
