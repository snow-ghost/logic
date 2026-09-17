# Extended audit of technical writing

Use this mode when inaccuracies have a high cost or the text makes strong claims
about quality, safety, performance, causation, comparative advantage, or readiness.
The purpose is credible, reproducible claims.

## 1. Claim inventory

For every substantial assertion, identify:

| Field | Question |
|---|---|
| Subject | Which system, component, or participant acts? |
| Action | What happens? |
| Conditions | Under which configuration, load, or inputs? |
| Result | What observable change occurs? |
| Evidence | Code, measurement, log, operational experience, citation, or inference? |
| Status | Implemented, tested, deployed, designed, planned, or hypothesized? |

When support is missing, qualify the claim or request evidence. Do not invent it.

## 2. Implementation status

| Status | Appropriate wording |
|---|---|
| Implemented | “The component performs…”; “A handler was added…” |
| Tested | “Tested on…”; “The test showed…” |
| Deployed | “Used in…”; “Processes production traffic…” |
| Designed | “The design specifies…”; “The protocol has been defined…” |
| Planned | “We plan to add…”; “The next stage includes…” |
| Hypothesis | “We will test whether…”; “The hypothesis is…” |

Do not generalize one experiment to the whole system or describe a plan as a
present capability.

## 3. Comparisons and causation

For a comparison, establish the baseline, alternative, shared conditions,
measured quantity, sample size and composition, and calculation method.
If measurements are absent, replace a claim of superiority with an observed
architectural difference, when that difference is supported.

For a causal assertion, examine both mechanism and observations. Use “X reduced Y”
when a controlled comparison or adequate operational evidence supports the claim.
Otherwise describe the observed association or label the expected effect as a hypothesis.

## 4. Completeness of the system description

Check whether the reader can identify:

- Inputs and their origins.
- Transformations and decisions.
- Outputs and their consumers.
- Where state is stored.
- Conditions for reusing stored knowledge or rules.
- Handling of errors and incomplete data.
- Trust boundaries and access rights.
- Operations that can change a production environment.
- The human role in validation and publication.

Supply missing information only from available evidence; otherwise ask the author.

## 5. Terminology

Keep a short concept-to-term mapping. Distinguish data, information, knowledge,
rules, scripts, model conclusions, and operator decisions. A synonym is acceptable
only if it preserves the technical referent. Expand unfamiliar abbreviations
on first use and retain the established spelling of technology names.

## 6. Information density

Identify each paragraph's function: problem, constraint, mechanism, example,
result, or conclusion. Remove sentences that only announce the next point or
repeat the preceding point without a new condition, mechanism, or consequence.
Split paragraphs that mix unrelated functions; merge neighboring paraphrases.

## 7. Consistency across sections

- The title matches the subject and content.
- Each section develops the stated topic and has a clear purpose.
- The introduction explains purpose and scope without adding unsupported facts.
- Conclusions follow from the evidence presented.
- Repeated numbers, names, and implementation statuses agree.

## 8. Final pass

1. Read as a specialist who has not seen the source material.
2. Identify claims that require unsupported trust in the author.
3. Compare against the source for altered facts, conditions, negations, and status.
4. Run `python3 scripts/lint_technical_style.py PATH --language en --extended`
   from the skill directory, if Python is available.
5. Review every finding manually; the script does not verify technical truth.
6. Return the edited text and separately identify only gaps that editing cannot resolve.
