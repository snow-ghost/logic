# Induction, hypotheses, analogy, and classification

## Deduction and induction

**Deduction:** a valid inference makes its conclusion necessary if its premises
are true. Applying a general rule to a particular case is one important form.

**Induction:** extends observations to unobserved cases or a wider class. Assess
how strongly the evidence supports the extension, not as though every inductive
conclusion claimed deductive certainty.

### Complete and incomplete induction

- **Complete:** enumerate every member of a finite class. Checking all twelve
  calendar months establishes that none has more than 31 days. The conclusion
  summarizes the checked class and depends on its being exhaustive.
- **Incomplete:** infer a generalization from only some members. The conclusion
  extends beyond the observations and remains open to counterexamples.

### Popular and scientific induction

Simple enumeration (*per enumerationem simplicem*) generalizes because no
counterexample has been noticed. “Every swan observed was white” does not justify
“All swans are white.”

Scientific induction investigates relevant conditions, distinguishes incidental
from explanatory features, and checks consistency with other established
knowledge. More observations alone do not remove systematic selection bias.

## Laws and causal investigation

In the traditional framework, a law expresses a stable property or necessary
relation within specified conditions. A counterexample challenges either the
proposed law or the adequacy of those conditions; it must not simply be ignored.

Distinguish observation of events as they occur from experiments that intervene
to isolate, vary, and repeat conditions. Mill's methods organize causal inquiry;
their conclusions depend on the adequacy of the comparison and control of
alternative explanations.

## Mill's five methods

### Agreement

Several instances of a phenomenon share one relevant circumstance despite
different surroundings:

```text
ABC → abc
ADE → ade
Shared A is a candidate explanation for a.
```

Example: fires under different conditions all involve a particular chemical.
The shared factor is a causal candidate, not proof that an unnoticed common
factor or selection effect is absent.

### Difference

Compare a case where the phenomenon occurs with an otherwise comparable case
where it does not:

```text
ABC → abc
 BC →  bc
The difference A is a candidate cause or necessary part of the cause of a.
```

For a software failure, compare revisions under the same input and environment.
Locating the first failing change helps identify a cause only to the extent that
the observations are reproducible and other relevant conditions are controlled.

### Joint method of agreement and difference

Combine positive cases sharing a circumstance with comparable negative cases
lacking it. A plant repeatedly flourishing in one soil type but not in the
comparison soils illustrates this arrangement. Check other differences before
attributing the effect to soil composition.

### Residues

Subtract effects already explained by known causes and investigate the remainder:

```text
ABC → abc
A explains a; B explains b.
Investigate C as the explanation for residual c.
```

The traditional astronomical example is investigating unexplained perturbations
of Uranus after accounting for known influences. The inference depends on the
accuracy and completeness of the subtraction model.

### Concomitant variation

Changes in A accompany changes in a. Investigate whether A causes a, is an effect
of a, or shares a cause with it. This is useful when a factor cannot be wholly
removed, such as temperature in studies of thermal expansion. Covariation alone
does not establish causal direction or eliminate confounding.

## Analogy

An analogy transfers a property from one case to another on the basis of shared
features. Its strength depends on:

1. How numerous and relevant the similarities are.
2. How substantial the dissimilarities are.
3. Whether the shared features are connected with the property being inferred.

Superficial resemblance is weak support. Comparing a state with a biological
organism does not establish that states must undergo a fixed biological lifespan.
Likewise, sharing a user interface does not establish that two systems have the
same failure modes.

## Hypotheses

A hypothesis proposes an explanation to be tested. Check that it:

- Is coherent and compatible with relevant established evidence.
- Explains the observations for which it was introduced.
- Has consequences that can be checked.
- Does not multiply unsupported assumptions merely to evade contrary results.

Derive observable consequences, test them, and compare rival explanations.
If H implies C and C occurs, H is supported only to the extent that the evidence
distinguishes it from rivals; H is not thereby deductively proved. An
*experimentum crucis* is a discriminating test between competing explanations.
If C fails, check the auxiliary assumptions and test conditions as well as H.

Example: a metal dissolving in aqua regia does not by itself establish that it
is gold; the observed consequence is not unique to that hypothesis.

## Deductive explanation of laws

An **empirical law** is established observationally without derivation from a
more general account. A **derived law** follows from such an account. Explanation
can take three forms:

1. Subsumption under a more general law, as orbital regularities are connected
   with laws of motion and gravitation.
2. Identification of intermediate mechanisms in a causal chain A → B → C.
3. Unification of several regularities under a shared process or concept.

Explaining an empirical regularity also clarifies its limits. For example, an
account of pumping in terms of atmospheric pressure identifies conditions under
which a fixed-height rule would no longer apply.

## Approximate generalizations

“Most S are P,” “S usually have P,” and statistical tendencies concern a class
or distribution. They do not guarantee a property of a particular individual.
Retain the probability, scope, conditions, and uncertainty in the conclusion.

“This treatment helped most observed patients, so it will help this patient”
overstates the evidence if offered as a certainty. Presented as a qualified
prediction with the appropriate evidence, it is not automatically a formal fallacy.

## Classification

Classification groups objects by attributes useful for understanding or finding
them. In the textbook's distinction:

- **Natural classification** uses relevant structural or explanatory properties
  and supports further justified inferences.
- **Artificial classification** uses a convenient lookup feature, such as an
  author's initial. It can be useful without supporting claims about deeper properties.

**Nomenclature** names classes; **terminology** supplies the terms used to
describe attributes. Do not infer unverified properties solely from a label.

## Quick identification

- Several positive cases with one common factor: agreement.
- Comparable cases differing in one relevant factor: difference.
- Positive and negative case patterns combined: joint method.
- Subtracting known contributions: residues.
- Quantities changing together: concomitant variation.
- A prediction matching a hypothesis: corroboration to evaluate, not proof by
  affirming the consequent.
