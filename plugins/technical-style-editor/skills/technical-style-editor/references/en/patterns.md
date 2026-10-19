# Patterns in technical prose

Use these examples after identifying the document's purpose and recording its
claims. They illustrate editing choices, not mandatory sentence templates.
Use a mechanism or measurement in a revision only when the source supports it;
otherwise request the missing detail or keep the description appropriately limited.

## Rhetorical negation

“Not X but Y,” “not just,” and “more than just” can introduce an unnecessary dispute.

Before:

> This is not just another chatbot, but a system for retaining diagnostic knowledge.

After:

> The system retains diagnostic knowledge for use in recurring incidents.

Keep a necessary negation:

> The controller does not publish a rule until validation succeeds.

## Announcements of intent

“I would like to explain,” “in this document we will discuss,” and “it is important
to note” often describe the act of writing instead of its subject.

Before:

> I want to show how the collector retrieves data from several sources.

After:

> The collector retrieves data from several sources.

Keep a navigation paragraph when a long document needs one; describe the sections
and their content directly.

## Defensive disclaimers

Before:

> I am not suggesting that we deploy the rule immediately; it needs testing and approval.

After:

> Test and approve the rule before deployment.

Retain attribution if the author is making a proposal rather than stating an
existing requirement: “I propose testing and approving the rule before deployment.”

## Unmeasured improvement

Before:

> The system significantly speeds up incident diagnosis.

With a supporting measurement:

> Median initial diagnosis time fell from 40 to 12 minutes across 60 incidents.

With a documented mechanism but no measurement:

> The system reuses the saved diagnostic sequence without another model request.

Without either kind of evidence, flag the claim for clarification. Do not turn
an intended effect into a measured result.

## Convenience and approval presented as explanation

“Conveniently,” “fortunately,” “elegant,” “easy,” “better,” and “simpler” do not
establish a step of a proof. Remove the evaluation or state the known reason for
the choice. Do not invent a reason.

Before:

> It is convenient to denote the displacement of card i by u_i.

After:

> Denote the displacement of card i by u_i.

If the source establishes a benefit, name it: “Under x = t + 1, the coefficient
of t vanishes.” Preserve formal comparisons such as `a < b`, defined terms such
as “natural number” and “simple group,” and comparisons against a stated criterion.

## Figurative agency in a deduction

Before:

> The equality u_i = 0 forces the card to stay in place.

After, if u_i already denotes the displacement of card i:

> The equality u_i = 0 implies that card i does not move.

Also review “compels,” “dictates,” and “obliges us.” Identify the actual premise
and consequence. If the step is unsupported, mark the gap rather than concealing
it with a verb replacement. Preserve literal actions and established terms such
as “forced process termination” when that is what the source describes.

## Ambiguous reference in a quantity definition

Before:

> On the unrolled line, each card is assigned a target position. Let its displacement be 𝑢_𝑖.

“Its” can refer to either the card or the position. If the context establishes
that the card is meant:

> On the unrolled line, each card i is assigned a target position. Denote the displacement of card i by 𝑢_𝑖.

If the target position is meant, name that position instead. Do not silently
choose a mathematical interpretation from these two sentences alone.

Apply the same check to “their difference,” “this quantity,” “the latter,” and
“the corresponding index.” Repeat a precise noun or symbol when two referents
are possible. Keep an unambiguous phrase such as “card i and its target position.”
Do not change displacement into coordinate or displacement magnitude, and do not
add a coordinate-difference formula that the source has not established.

A pronoun finding is a prompt to inspect the context, not a proof of ambiguity.

## Promotional wording

Replace “unique,” “revolutionary,” “powerful,” “cutting-edge,” or “innovative” with
an established distinguishing property.

Before:

> Our innovative approach saves a validated sequence of actions as an executable rule.

After:

> The agent saves a validated sequence of actions as an executable rule.

## Bureaucratic wrappers and nominalizations

Before:

> Within the framework of the solution, collection of cluster state is performed by the collector.

After:

> The collector reads the cluster state.

Prefer a concrete verb to “perform an analysis” or “carry out the implementation”
when the shorter form preserves meaning. Do not replace an established technical
term merely because it is a noun.

## Comparisons without a baseline

Before:

> A saved rule is faster than the agent.

With measurements:

> Across 100 repeated requests, the rule returned a result in a median of 180 ms;
> the agent using the same model took 14 s.

Without measurements, state only an established difference:

> The saved rule executes locally without another model request.

Check that the sample, conditions, and measure support the comparison.

## Artificial symmetry

Repeated openings and three-item lists are useful when they reflect the subject.
They become filler when neighboring sentences merely restate one claim.

Before:

> The system collects data. The system analyzes data. The system stores knowledge.

Revise by identifying the stages and their relationship, but only when their
roles are known. Do not invent component boundaries to make the prose more concrete.

## Necessary negation and modality

Preserve:

- A prohibition: “The operator must not write a secret to the log.”
- An invariant: “The rule does not change cluster state.”
- A failure condition: “Without quorum, the node does not accept writes.”
- A conceptual boundary: “A failed node does not necessarily imply lost quorum.”
- A correction needed to remove a reader's factual misunderstanding.

If removing a negation changes permitted behavior, it has a technical function.
Likewise, “must,” “may,” “can,” “will,” and “is planned to” express different
requirements, permissions, capabilities, commitments, and statuses.
