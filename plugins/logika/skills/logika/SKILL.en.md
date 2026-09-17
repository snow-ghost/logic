# Logika

Analyze reasoning using classical formal logic as presented in G. Chelpanov's
*Textbook of Logic*. Check whether conclusions follow from premises, concepts
remain consistent, and definitions and divisions are sound.

Distinguish **validity of inference** from **truth of premises**. A valid argument
can have false premises, and an invalid argument can reach a true conclusion.
Identify which issue is at stake. An unverified premise is not thereby false.

## Modes

**Review** — requests such as “check the logic,” “review this argument,” or “find
logical fallacies.” Diagnose the reasoning without rewriting the source. Name
each error in English and give its conventional Latin name when one exists.
Explain why it is an error and how to correct it. Use the review format below.

**Repair** — requests such as “fix the logic” or “repair the argument.” Give a brief
diagnosis, then a revised text and a list of changes.

- Preserve the author's style, vocabulary, and approximate length; change only
  what the reasoning requires.
- Do not introduce facts. Qualify an unsupported conclusion only as far as the
  available premises justify. Changing “all” to “some” still requires evidence
  that at least one case exists. Otherwise mark the claim `[evidence needed]`.
- Make disputed hidden premises explicit or remove the conclusions relying on
  them. Distinguish a proposed check from evidence already obtained.
- Explain which error each change addresses.

**Exercises** — check a syllogism, convert a proposition, identify a figure or
mood, identify a method of induction, or reconstruct an enthymeme. Provide a
step-by-step solution using the relevant references.

**Benchmark** — only when the user explicitly requests a BQA/MCQA benchmark or
machine-graded response. Return one JSON object without surrounding prose or
Markdown: `{"reasoning": "brief step-by-step explanation", "answer": "yes|no or A|B|C|D"}`.
An ordinary yes/no question does not by itself request benchmark mode.

## Analysis procedure

1. Identify the thesis, premises, intermediate conclusions, and final conclusion.
2. Identify each inference: categorical syllogism, conditional or disjunctive
   inference, immediate inference, square of opposition, induction, or analogy.
   Reconstruct missing premises in enthymemes before evaluating them.
3. Check concepts for shifts in meaning, circular or disproportionate
   definitions, mixed criteria of division, overlap, and omitted cases.
4. Check the applicable inference rules. For induction and analogy, evaluate
   evidential strength rather than demanding deductive certainty.
5. Locate and name errors using [the error catalog](references/en/errors.md).
6. Return the output for the requested mode.

## Review format

```text
Verdict: no logical errors found / N issues found (K invalid inferences, M evidential concerns).

Argument structure: thesis, premises, and how the conclusion is reached (2–4 sentences).

| # | Passage (quotation) | Error | Why it matters | Suggested correction |

Hidden premises: unstated assumptions the argument requires and which are disputed.

Strength of non-deductive conclusions: assess inductions and analogies, if present.
```

An invalid inference fails to establish its conclusion from its premises. An
evidential concern involves insufficient support, a weak induction, or an
analogy whose relevance has not been established. Do not label every omitted
premise a fallacy: explain whether it is acceptable in context.

## Reference selection

- [Concepts](references/en/concepts.md): classifications, definitions, divisions,
  genus and differentia, and dichotomy.
- [Judgments](references/en/judgments.md): A/E/I/O, distribution, the square of
  opposition, obversion, conversion, and contraposition.
- [Syllogisms](references/en/syllogism.md): figures, moods, reduction, conditional
  and disjunctive reasoning, enthymemes, sorites, and dilemmas.
- [Induction](references/en/induction.md): Mill's methods, hypotheses, analogy,
  classification, and approximate generalizations.
- [Errors](references/en/errors.md): logical fallacies, sophisms, and paralogisms.
- [Laws](references/en/laws.md): the four traditional laws of thought.

For a prose argument, usually read errors and syllogisms first. Load the other
references when the text calls for them. The optional Russian chapter digest
is background material; it is not required for English analysis.

## Laws of thought

1. **Identity:** keep the meaning of a term stable throughout an argument.
2. **Non-contradiction:** A and not-A cannot both be true at the same time and in
   the same respect.
3. **Excluded middle:** A or not-A; no third alternative between contradictories.
4. **Sufficient reason:** provide grounds for assertions. Distinguish a reason
   for knowing (*ratio cognoscendi*) from an event's cause (*ratio fiendi*).

These are used in the textbook's traditional framework. When a task uses modern
predicate logic, state any existence assumptions needed to move from universal
to particular propositions; do not infer existence from an empty class.

## Eight checks for a categorical syllogism

1. Exactly three terms, with no equivocation (*quaternio terminorum*).
2. Exactly two premises and one conclusion.
3. The middle term is distributed in at least one premise.
4. No term is distributed in the conclusion unless distributed in its premise.
5. Two negative premises yield no categorical conclusion.
6. A negative premise requires a negative conclusion, and a negative conclusion
   requires a negative premise.
7. Two particular premises yield no categorical conclusion.
8. A particular premise requires a particular conclusion.

Distribution: A distributes S only; E distributes both S and P; I distributes
neither; O distributes P only. Identify the rule violated when a syllogism fails.

## Quick error catalog

| Error | Typical form |
|---|---|
| Irrelevant conclusion (*ignoratio elenchi*) | Proving something other than the thesis |
| Begging the question (*petitio principii*) | Assuming the disputed conclusion in a premise |
| Circular proof (*circulus in demonstrando*) | A supports B and B supports A |
| *Ad hominem* | Attacking the person in place of addressing the argument |
| *Post hoc ergo propter hoc* | Treating temporal succession as proof of causation |
| Hasty generalization | Generalizing from inadequate or biased observations |
| False analogy | Transferring properties based on superficial similarity |
| Affirming the consequent | If A then B; B; therefore A |
| Denying the antecedent | If A then B; not-A; therefore not-B |
| Four terms (*quaternio terminorum*) | A term changes meaning between premises |
| *A dicto secundum quid ad dictum simpliciter* | Dropping essential qualifications |
| Composition or division | Moving a property between parts and whole without warrant |
| False dilemma | Presenting alternatives as exhaustive when others exist |

## Examples

### Valid syllogism

“All metals are elements. Some bodies are metals. Therefore, some bodies are elements.”

Major: all M are P (A). Minor: some S are M (I). Conclusion: some S are P (I).
The middle term is the subject of the major and predicate of the minor: figure 1,
AII, Darii. M is distributed in the major. The inference is valid; the truth of
the supplied premises is a separate question.

### Invalid syllogism

“All historians are impartial. No natural scientists are historians. Therefore,
no natural scientists are impartial.”

All M are P; no S are M; therefore no S are P. P is undistributed in the A premise
but distributed in the E conclusion. This is illicit major.

### Conversion

“All squares are rectangles” converts by limitation to “Some rectangles are
squares,” given that squares exist. Simple conversion to “All rectangles are
squares” is invalid.

### Mill's method

Three factories use different machines but the same lubricant and show the same
gear wear. This suggests the method of agreement. The causal conclusion is
tentative: compare otherwise similar conditions with and without that lubricant.

### Review and repair

Source: “Sales fell 10% after we introduced the new framework. Obviously the
framework caused the fall. All successful companies use the old stack, so we
must return to it.”

The sequence does not establish causation. The universal claim about successful
companies lacks evidence, and copying their stack requires an additional
premise about its relevance to this business. A possible repair is:

> Sales fell 10% after we introduced the new framework. Before deciding whether
> to roll back, we need to test whether the framework contributed to the fall.
> The claim about successful companies also needs evidence and a reason their
> experience would apply here. A rollback would be justified if the relevant
> evidence supports it.

Changes: qualify the causal claim, flag the unsupported generalization, and
make the recommendation conditional on evidence. No new observations are added.

### Explicit benchmark

Request: “BQA benchmark: if ‘All planets orbit the Sun’ is true, is ‘Some planets
do not orbit the Sun’ true? Return the benchmark JSON.”

`{"reasoning": "A and O are contradictories. If A is true, O is false.", "answer": "no"}`
