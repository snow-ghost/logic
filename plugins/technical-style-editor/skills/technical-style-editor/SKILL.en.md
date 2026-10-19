# Technical Style Editor

Revise English technical writing so that each substantial claim identifies its
subject, action, conditions, and verifiable result. Preserve the author's meaning
and the actual implementation status of the system described.

## Choose a mode

Use **basic mode** by default for technical writing of any genre or length when
style and structure can be improved without a deeper audit of the evidence.

Use **extended mode** when inaccuracies have a high cost or the text makes claims
about quality, safety, performance, causation, comparative advantage, or readiness.
Read [the extended audit](references/en/extended-audit.md) for that mode.

## Workflow

1. Identify the purpose, audience, and required format.
2. Read the entire source. Treat facts, numbers, names, constraints, links, and
   implementation status as fixed unless the author confirms a change. In
   mathematical writing, also preserve definitions, notation, indices, quantifiers,
   hypotheses, and the direction of implications.
3. If a file is available and Python is installed, run
   `python3 scripts/lint_technical_style.py PATH --language en`. Add `--extended`
   for extended mode. Use `--language auto` for mixed English/Russian text.
   Apply `--forbid-long-dash` only at the author's request; `--forbid-yo` concerns
   Russian text only. If the script cannot run, perform the same review manually.
4. Privately track the subject, action, object, conditions, result, evidence, and
   status of each claim. Do not print this inventory unless requested.
5. Arrange paragraphs around the subject or fact, mechanism, conditions, result,
   and supporting evidence, in the order that best explains the material.
6. Remove rhetorical contrasts, announcements of intent, promotional evaluations,
   filler, bureaucratic phrasing, arbitrary three-part lists, and repeated openings.
7. Preserve negations that express prohibitions, invariants, limitations, failure
   conditions, or necessary distinctions.
8. When patterns recur, consult [editing patterns](references/en/patterns.md).
9. In extended mode, check implementation status, comparisons, causation, inputs,
   outputs, errors, measurable results, and consistency across sections.
10. Rerun the diagnostic script and interpret each finding in context. A match
    identifies a passage for review; it does not require a replacement.
11. Read the revision on its own. Resolve each pronoun to its referent and each
    symbol to the quantity it denotes. Compare against the source to verify that
    facts, qualifications, mathematical meaning, and readiness claims are preserved.

## Editing rules

- Begin with the subject, action, or result when the context permits.
- Name the actor. Keep passive voice when the actor is unknown, irrelevant, or
  conventionally omitted in the document's genre.
- Replace evaluation with a mechanism or measurement. Without measurements, use
  a neutral description; do not manufacture a metric.
- Distinguish fact, inference, and plan. Mark proposed and future capabilities.
- Use one precise term for one concept. Do not vary technical terms for style.
- Expand unfamiliar abbreviations on first use and preserve standard names.
- Split a sentence when it mixes distinct claims or conditions.
- Use lists for meaningful sequence, membership, or comparison, not symmetry.
- Keep first person for the author's decisions or experience; remove “I would
  like to discuss” when the sentence can state the subject directly.
- Preserve modal force: “must,” “may,” “can,” “planned,” and “verified” are not
  interchangeable. Do not turn a permission into a requirement or a plan into a fact.

## Precision in explanations and mathematical proofs

Apply these rules in basic mode too, including when introducing notation or
describing a proof or algorithm.

- Remove unsupported evaluations such as “conveniently,” “fortunately,” “elegant,”
  “natural,” “easy,” “better,” and “simpler.” State the operation or an established
  property: “Define…” or “This substitution eliminates the term…”. Explain a
  choice when its reason is known and relevant; do not invent a benefit to replace
  an evaluation. Preserve defined terms such as “natural number” or “simple group,”
  and comparisons with a stated criterion or formula.
- Replace figurative agency (“the equality forces us,” “the condition compels,”
  “the bound dictates”) with the explicit relationship: “Equation (2) implies…”
  or “Condition (3) excludes…”. Name both the grounds and the consequence. If the
  source does not justify the step, mark the gap rather than making it sound proved.
  Preserve literal coercion or specified system behavior when that is the actual claim.
- Resolve “its,” “their,” “this,” “that,” “the former/latter,” and “corresponding.”
  When two objects could be meant, repeat the object's name or symbol, even if
  this repeats a noun. A quantity definition should name its subject: “the
  displacement of card i” or “the coordinate of the target position.” Unambiguous
  pronouns are acceptable. If context does not determine the referent, ask for
  clarification or mark `[unclear referent]`.
- Distinguish an object, its position, coordinate, displacement, and displacement
  magnitude. Preserve signs, domains, and index meanings. Do not introduce a new
  formula, replace displacement with distance, or add premises to repair the prose.

See [editing patterns](references/en/patterns.md) for examples. The linter flags
phrases for review; independently check referents and mathematical implications
in context even when no pattern matches.

## Constraints

- Do not add facts, numbers, test results, production experience, or causal
  relationships absent from the source.
- Do not promote a design to a prototype, a prototype to a deployed system, or
  one observation to a general rule.
- Do not remove conditions, exceptions, risks, prohibitions, or qualifications
  that change meaning.
- Do not add deliberate errors, random details, or syntactic noise to evade
  automated authorship detection.
- A stylistic pattern is not proof that a text was machine-generated.
- Do not replace a technical term with a familiar word if precision would suffer.

## Output

By default, return the edited text without a preamble or a report on every change.

If the user requests a review, return a brief assessment, passages that affect
meaning or credibility, a revised version, and the evidence still needed to
support strong claims. For forms, preserve field names and their order.
