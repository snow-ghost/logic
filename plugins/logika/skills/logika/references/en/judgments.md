# Judgments: forms, opposition, and distribution

## Structure and categorical forms

A categorical proposition has a **subject** S, a **predicate** P, and a **copula**
joining or separating them (“is” / “is not”).

| Form | Quantity and quality | Formula | Example |
|---|---|---|---|
| A | Universal affirmative | All S are P | All humans are mortal |
| E | Universal negative | No S are P | No insects are vertebrates |
| I | Particular affirmative | Some S are P | Some metals are precious |
| O | Particular negative | Some S are not P | Some people are not wise |

Mnemonic: *affIrmo* supplies A and I; *nEgO* supplies E and O. “Some” means at least
one and does not by itself exclude “all.”

## Other classifications

By relation:

- **Categorical:** an unconditioned assertion, S is P.
- **Hypothetical:** if A, then B. A is the antecedent (*antecedens*); B is the
  consequent (*consequens*).
- **Disjunctive:** A or B, possibly with more alternatives. State whether the
  disjunction is inclusive or exclusive. Exhaustiveness is needed when ruling
  out alternatives to establish the remaining one.
- **Hypothetical-disjunctive:** combines conditionals and alternatives, as in a dilemma.

By modality:

- **Problematic:** possible or probable.
- **Assertoric:** asserted as actual.
- **Apodictic:** asserted as necessary.

Do not treat a possibility as an established fact or a fact as a necessity.

## Distribution

A term is **distributed** when the proposition refers to its entire extension.

| Proposition | Subject S | Predicate P |
|---|---|---|
| A | Distributed | Undistributed |
| E | Distributed | Distributed |
| I | Undistributed | Undistributed |
| O | Undistributed | Distributed |

Negative propositions distribute their predicates; affirmative propositions do
not. Universal propositions distribute their subjects. Independently established
coextension can justify additional inferences, but it is extra information and
does not change the standard distribution table for an A-form statement.

## Square of opposition

The traditional square below assumes a nonempty subject class. In modern
predicate logic, universals alone do not assert existence: retain the
contradictories but check existence before using the other relations.

1. **Contradictories** (*contradictoriae*): A–O and E–I. Exactly one is true.
2. **Contraries** (*contrariae*): A–E. They cannot both be true, but can both be false.
3. **Subalterns** (*subalternae*): A–I and E–O. Truth passes from universal to
   particular; falsity passes from particular to universal. The converses fail.
4. **Subcontraries** (*subcontrariae*): I–O. They can both be true, but cannot both
   be false under the nonempty-subject assumption.

To refute “all,” a counterexample establishing O suffices; there is no need to
prove the stronger claim E.

| Given | A | E | I | O |
|---|---|---|---|---|
| A true | — | False | True | False |
| E true | False | — | False | True |
| I true | Unknown | False | — | Unknown |
| O true | False | Unknown | Unknown | — |
| A false | — | Unknown | Unknown | True |
| E false | Unknown | — | True | Unknown |
| I false | False | True | — | True |
| O false | True | False | True | — |

## Immediate inferences

### Obversion (*obversio*)

Change the quality and replace the predicate with its complement. Quantity and
meaning are preserved.

| Original | Obverse |
|---|---|
| A: All S are P | E: No S are non-P |
| E: No S are P | A: All S are non-P |
| I: Some S are P | O: Some S are not non-P |
| O: Some S are not P | I: Some S are non-P |

Example: “Some metals are precious” becomes “Some metals are not nonprecious.”

### Conversion (*conversio*)

Exchange subject and predicate.

- **A → I**, by limitation (*per accidens*), provided S exists: “All birds are
  animals” gives “Some animals are birds.” Simple conversion to A needs separate
  evidence that the terms are coextensive.
- **E → E**, simple conversion: “No S are P” gives “No P are S.”
- **I → I**, simple conversion: “Some S are P” gives “Some P are S.”
- **O does not convert:** it would distribute a term not distributed in the premise.

### Obversion followed by conversion

Chelpanov's presentation of opposition by predicate uses obversion followed by
conversion. State the resulting form rather than relying on terminology alone:

| Original | Result |
|---|---|
| A: All S are P | E: No non-P are S |
| E: No S are P | I: Some non-P are S, provided S exists |
| O: Some S are not P | I: Some non-P are S |
| I: Some S are P | No result by this procedure |

In the familiar modern formulation, contraposition of “All S are P” is “All
non-P are non-S,” equivalent to the E result above by obversion. Do not confuse
the different surface forms.

## Examples

“All birds fly” is false. Its contradictory, “Some birds do not fly,” is true;
the truth of “No birds fly” and “Some birds fly” is undetermined by that premise alone.

“No honest witnesses are bribed” converts to “No bribed people are honest witnesses.”

A dilemma says a student either loves or hates learning, making rewards either
unnecessary or useless. The disjunction needs justification: indifference is an
omitted possibility.
