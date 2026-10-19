import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "plugins/technical-style-editor/skills/technical-style-editor/scripts/lint_technical_style.py"
)


def run_lint(text, *options):
    return subprocess.run(
        [sys.executable, str(SCRIPT), "-", "--json", *options],
        input=text, text=True, encoding="utf-8", capture_output=True, check=False,
    )


class BilingualLinterTests(unittest.TestCase):
    def test_english_phrases_and_localized_messages(self):
        result = run_lint(
            "It is important to note that the system significantly improves throughput.",
            "--language", "en",
        )
        self.assertEqual(result.returncode, 1)
        findings = json.loads(result.stdout)
        self.assertEqual({item["rule"] for item in findings}, {"importance-marker", "unmeasured-improvement"})
        for item in findings:
            self.assertEqual(item["line"], 1)
            self.assertNotRegex(item["message"], r"[А-Яа-яЁё]")

    def test_russian_rules_remain_available(self):
        result = run_lint(
            "Важно отметить, что система значительно ускоряет обработку.",
            "--language", "ru",
        )
        self.assertEqual(result.returncode, 1)
        findings = json.loads(result.stdout)
        self.assertEqual({item["rule"] for item in findings}, {"importance-marker", "unmeasured-improvement"})
        self.assertTrue(all(any("а" <= char.lower() <= "я" for char in item["message"]) for item in findings))

    def test_auto_checks_both_languages_and_preserves_line_numbers(self):
        result = run_lint("This is an innovative approach.\nЭто инновационный подход.")
        self.assertEqual(result.returncode, 1)
        findings = json.loads(result.stdout)
        self.assertEqual([(item["line"], item["rule"]) for item in findings], [
            (1, "promotional-adjective"), (2, "promotional-adjective"),
        ])
        for language, expected_line in (("en", 1), ("ru", 2)):
            selected = run_lint("This is an innovative approach.\nЭто инновационный подход.", "--language", language)
            self.assertEqual([item["line"] for item in json.loads(selected.stdout)], [expected_line])

    def test_contractions_and_capitalization(self):
        for text in ("This isn't just a cache.", "This isn’t just a cache.", "This is NOT JUST a cache."):
            with self.subTest(text=text):
                result = run_lint(text, "--language", "en")
                self.assertEqual(result.returncode, 1)
                self.assertIn("not-just", {item["rule"] for item in json.loads(result.stdout)})

    def test_extended_checks_are_opt_in_for_both_languages(self):
        for language, text in (("en", "The service responds faster."), ("ru", "Сервис отвечает быстрее.")):
            with self.subTest(language=language):
                self.assertEqual(run_lint(text, "--language", language).returncode, 0)
                result = run_lint(text, "--language", language, "--extended")
                self.assertEqual(result.returncode, 1)
                self.assertEqual({item["rule"] for item in json.loads(result.stdout)}, {"comparison-without-baseline"})

    def test_plain_text_and_necessary_negation_are_preserved(self):
        for language, text in (
            ("en", "The controller does not publish a rule until validation succeeds."),
            ("ru", "Контроллер не публикует правило до успешного прохождения проверок."),
        ):
            with self.subTest(language=language):
                result = run_lint(text, "--language", language)
                self.assertEqual(result.returncode, 0)
                self.assertEqual(json.loads(result.stdout), [])

    def test_optional_typography_restrictions(self):
        text = "Отчёт — текст."
        self.assertEqual(run_lint(text).returncode, 0)
        result = run_lint(text, "--forbid-yo", "--forbid-long-dash")
        self.assertEqual(result.returncode, 1)
        self.assertEqual({item["rule"] for item in json.loads(result.stdout)}, {"letter-yo", "long-dash"})

    def test_structure_findings_use_the_requested_language(self):
        sentence = "The worker reads the input and stores the result."
        result = run_lint(sentence + "\n\n" + sentence, "--language", "en", "--extended")
        self.assertEqual(result.returncode, 1)
        repeated = [item for item in json.loads(result.stdout) if item["rule"] == "repeated-sentence"]
        self.assertEqual(len(repeated), 1)
        self.assertEqual(repeated[0]["line"], 3)
        self.assertIn("line 1", repeated[0]["message"])
        long_result = run_lint(" ".join(["word"] * 46) + ".", "--language", "en", "--extended")
        self.assertEqual({item["rule"] for item in json.loads(long_result.stdout)}, {"long-sentence"})

    def test_file_input_is_read_only_and_errors_return_two(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.md"
            original = b"This is an innovative approach.\n"
            path.write_bytes(original)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(path), "--language", "en", "--json"],
                capture_output=True, text=True, encoding="utf-8", check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual(json.loads(result.stdout), json.loads(run_lint(original.decode(), "--language", "en").stdout))
            path.unlink()
            missing = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True)
            self.assertEqual(missing.returncode, 2)
            path.write_bytes(b"\xff")
            invalid = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True)
            self.assertEqual(invalid.returncode, 2)

    def test_evaluations_are_reviewed_in_basic_mode(self):
        for language, samples in (
            ("ru", ("Здесь удобно ввести t.", "Это удачный выбор обозначения.", "Сумма удачно сокращается.", "Теперь проще выбрать i.")),
            ("en", ("It is convenient to introduce t.", "This is an elegant choice.", "The terms cancel nicely.", "This choice is simpler.")),
        ):
            for text in samples:
                with self.subTest(language=language, text=text):
                    result = run_lint(text, "--language", language)
                    self.assertEqual(result.returncode, 1)
                    self.assertIn("unsupported-evaluation", {item["rule"] for item in json.loads(result.stdout)})

    def test_figurative_agency_and_explicit_inference(self):
        for language, source, revised in (
            ("ru", "Равенство u_i = 0 вынуждает карточку остаться на месте.", "Из равенства u_i = 0 следует, что карточка i не перемещается."),
            ("en", "The equality u_i = 0 forces the card to stay in place.", "The equality u_i = 0 implies that card i does not move."),
        ):
            with self.subTest(language=language):
                flagged = run_lint(source, "--language", language)
                self.assertEqual(flagged.returncode, 1)
                self.assertIn("figurative-agency", {item["rule"] for item in json.loads(flagged.stdout)})
                clean = run_lint(revised, "--language", language)
                self.assertEqual(clean.returncode, 0)

    def test_quantity_references_flag_both_russian_spellings_and_english(self):
        prefix = "На развёрнутой прямой каждой карточке назначается целевая позиция.\n"
        for language, source, revised in (
            ("ru", prefix + "Обозначим её перемещение через 𝑢_𝑖.", prefix + "Обозначим перемещение карточки i через 𝑢_𝑖."),
            ("ru", prefix + "Обозначим ее перемещение через 𝑢_𝑖.", prefix + "Обозначим перемещение карточки i через 𝑢_𝑖."),
            ("en", "Each card has a target position.\nLet its displacement be 𝑢_𝑖.", "Each card has a target position.\nDenote the displacement of card i by 𝑢_𝑖."),
        ):
            with self.subTest(language=language, source=source):
                flagged = run_lint(source, "--language", language)
                self.assertEqual(flagged.returncode, 1)
                findings = [item for item in json.loads(flagged.stdout) if item["rule"] == "pronoun-reference"]
                self.assertEqual(len(findings), 1)
                self.assertEqual(findings[0]["line"], 2)
                self.assertIn("𝑢_𝑖", findings[0]["excerpt"])
                self.assertEqual(run_lint(revised, "--language", language).returncode, 0)

    def test_formal_comparisons_and_defined_terms_are_preserved(self):
        for language, text in (
            ("ru", "Пусть n — естественное число, а G — простая группа. Для всех i ∈ I имеем u_i ≤ v_i. При n > 2 оценка содержит на один член меньше."),
            ("en", "Let n be a natural number and G a simple group. For all i ∈ I, u_i ≤ v_i. When n > 2, the bound contains one fewer term."),
        ):
            with self.subTest(language=language):
                result = run_lint(text, "--language", language)
                self.assertEqual(result.returncode, 0)
                self.assertEqual(json.loads(result.stdout), [])


if __name__ == "__main__":
    unittest.main()
