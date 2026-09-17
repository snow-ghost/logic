#!/usr/bin/env python3
"""Find phrases that deserve manual review in Russian technical prose."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


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


SENTENCE_RE = re.compile(r"[^.!?\n]+[.!?]?", re.UNICODE)
WORD_RE = re.compile(r"[A-Za-zА-Яа-яЁё0-9]+(?:[-'][A-Za-zА-Яа-яЁё0-9]+)*", re.UNICODE)


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


def optional_findings(lines: list[str], forbid_yo: bool, forbid_long_dash: bool) -> list[Finding]:
    findings: list[Finding] = []
    for number, line in enumerate(lines, start=1):
        if forbid_yo and re.search(r"[Ёё]", line):
            findings.append(Finding(number, "letter-yo", "По требованию текста замените букву ё на е.", excerpt(line, 0)))
        if forbid_long_dash and "—" in line:
            findings.append(Finding(number, "long-dash", "По требованию текста замените длинное тире.", excerpt(line, line.index("—"))))
    return findings


def extended_structure_findings(text: str) -> list[Finding]:
    findings: list[Finding] = []
    seen: dict[str, int] = {}
    offset = 0
    for match in SENTENCE_RE.finditer(text):
        sentence = " ".join(match.group().strip().split())
        line = text.count("\n", 0, match.start()) + 1
        words = WORD_RE.findall(sentence)
        if len(words) > 45:
            findings.append(
                Finding(line, "long-sentence", f"В предложении {len(words)} слов; проверьте, не смешаны ли разные утверждения и условия.", sentence[:150] + ("…" if len(sentence) > 150 else ""))
            )
        normalized = sentence.casefold().strip(" .!?")
        if len(words) >= 8:
            if normalized in seen:
                findings.append(Finding(line, "repeated-sentence", f"Предложение повторяет строку {seen[normalized]}.", sentence))
            else:
                seen[normalized] = line
        offset = match.end()
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Диагностирует речевые признаки в русском техническом тексте без автоматической правки.")
    parser.add_argument("path", nargs="?", default="-", help="Файл UTF-8 или - для стандартного ввода")
    parser.add_argument("--extended", action="store_true", help="Включить проверку сравнений, слабых формулировок и структуры")
    parser.add_argument("--forbid-yo", action="store_true", help="Сообщать о букве ё")
    parser.add_argument("--forbid-long-dash", action="store_true", help="Сообщать о длинном тире")
    parser.add_argument("--json", action="store_true", help="Вывести результат в JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        text = read_text(args.path)
    except (OSError, UnicodeError) as error:
        print(f"Не удалось прочитать текст: {error}", file=sys.stderr)
        return 2

    lines = text.splitlines()
    rules = BASE_RULES + (EXTENDED_RULES if args.extended else ())
    findings = pattern_findings(lines, rules)
    findings.extend(optional_findings(lines, args.forbid_yo, args.forbid_long_dash))
    if args.extended:
        findings.extend(extended_structure_findings(text))
    findings.sort(key=lambda item: (item.line, item.rule, item.excerpt))

    if args.json:
        print(json.dumps([asdict(item) for item in findings], ensure_ascii=False, indent=2))
    elif findings:
        for item in findings:
            print(f"{item.line}: [{item.rule}] {item.message}")
            print(f"    {item.excerpt}")
        print(f"Найдено мест для ручной проверки: {len(findings)}")
    else:
        print("Срабатываний нет.")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
