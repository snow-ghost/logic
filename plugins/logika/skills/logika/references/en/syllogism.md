# Syllogisms and deductive inference

## Structure

A categorical syllogism contains two premises, one conclusion, and three terms:

- **Major term P:** predicate of the conclusion.
- **Minor term S:** subject of the conclusion.
- **Middle term M:** occurs in both premises but not in the conclusion.
- The **major premise** contains P and M; the **minor premise** contains S and M.

The *dictum de omni et de nullo* states that what is affirmed or denied of an
entire class applies to its members. Applying it to an actual member requires
that the member belongs to the class.

## Eight rules

1. Exactly three terms with stable meanings; equivocation creates four terms.
2. Two premises and one conclusion.
3. M must be distributed in at least one premise.
4. No term may be distributed in the conclusion unless distributed in its premise.
5. Two negative premises yield no categorical conclusion.
6. A negative premise requires a negative conclusion, and vice versa.
7. Two particular premises yield no categorical conclusion.
8. A particular premise requires a particular conclusion.

These are the textbook's traditional rules. Separately check existence when
using a mood that draws a particular conclusion from universal premises.

## Figures

The position of M determines the figure. S is the subject and P the predicate
of the conclusion in every figure.

| Figure | Major premise | Minor premise | Typical use |
|---|---|---|---|
| 1 | M–P | S–M | Apply a general rule to a subordinate class |
| 2 | P–M | S–M | Exclude membership; a valid mood has a negative premise |
| 3 | M–P | M–S | Establish a particular connection or counterexample |
| 4 | P–M | M–S | Traditional fourth, or Galenic, arrangement |

## Nineteen traditional moods

Vowels encode major premise, minor premise, and conclusion, in that order.

| Figure | Moods |
|---|---|
| 1 | Barbara (AAA), Celarent (EAE), Darii (AII), Ferio (EIO) |
| 2 | Cesare (EAE), Camestres (AEE), Festino (EIO), Baroko (AOO) |
| 3 | Darapti (AAI), Disamis (IAI), Datisi (AII), Felapton (EAO), Bokardo (OAO), Ferison (EIO) |
| 4 | Bramantip (AAI), Camenes (AEE), Dimaris (IAI), Fesapo (EAO), Fresison (EIO) |

Baroko and Bokardo are also commonly spelled Baroco and Bocardo. Some lists
include five additional weakened moods whose particular conclusions follow
from stronger universal conclusions, given the relevant existence assumption.

Traditional mnemonic consonants describe reduction:

- **s:** simple conversion of the preceding proposition.
- **p:** conversion by limitation (*per accidens*).
- **m:** interchange premises (*mutatio praemissarum*).
- Initial **B, C, D, F:** the target first-figure mood.
- **k/c** in Baroko/Bokardo: indirect reduction by contradiction.

### Examples

**Barbara, AAA–1:** All M are P; all S are M; therefore all S are P.

**Celarent, EAE–1:** No M are P; all S are M; therefore no S are P.

**Cesare, EAE–2:** No P are M; all S are M; therefore no S are P.

**Baroko, AOO–2:** All P are M; some S are not M; therefore some S are not P.

Darapti and Felapton require M to exist, Bramantip requires P to exist, and Fesapo
requires M to exist. Make these assumptions explicit in modern-logic tasks.

## Reduction to figure 1

- **Cesare → Celarent:** simply convert the E major premise.
- **Camestres → Celarent:** interchange premises, convert the original E minor,
  and convert the resulting E conclusion.
- **Darapti → Darii:** convert the A minor by limitation, assuming M exists.
- **Bramantip → Barbara:** interchange premises, then convert the universal
  conclusion by limitation, assuming P exists.
- **Baroko/Bokardo:** assume the contradictory of the intended conclusion;
  Barbara then contradicts an accepted premise. Show the conflicting propositions.

## Conditional inferences

For “if A then B,” A is the antecedent and B the consequent.

| Form | Inference | Status |
|---|---|---|
| Modus ponens | A → B; A; therefore B | Valid |
| Modus tollens | A → B; not-B; therefore not-A | Valid |
| Affirming the consequent | A → B; B; therefore A | Invalid |
| Denying the antecedent | A → B; not-A; therefore not-B | Invalid |

For example, wet ground does not by itself establish rain: another cause could
produce it. A conditional must also be evaluated as a premise; a valid pattern
does not make an unreliable conditional true.

## Disjunctive inferences and dilemmas

**Modus tollendo ponens:** A or B; not-A; therefore B. The alternatives must be
exhaustive; they need not be exclusive for this inference.

**Modus ponendo tollens:** either A or B; A; therefore not-B. This requires an
exclusive disjunction. It fails for the ordinary inclusive “or.”

A triangle's acute/right/obtuse classification is both exhaustive and exclusive
within ordinary Euclidean geometry. An arbitrary list of business options need
not have either property.

Dilemmas combine conditional premises with a disjunction. For example,
A → C; B → D; A or B; therefore C or D. Check both conditionals and whether the
options exhaust the relevant possibilities. Trilemmas and longer cases follow
the same principle.

## Abbreviated and compound syllogisms

- **Enthymeme:** omits the major premise, minor premise, or conclusion. Restore
  the missing proposition and mark it as reconstructed, not as an observed fact.
- **Epicheirema:** a syllogism whose premises are themselves supported by
  abbreviated arguments. Expand and check those arguments too.
- **Polysyllogism:** a chain in which a conclusion of one syllogism becomes a
  premise of another. The preceding step is the prosyllogism; the following step
  is the episyllogism. The chain may proceed toward more particular or more general claims.
- **Aristotelian sorites:** starts with the particular end of a chain, such as
  Bucephalus → horse → animal → substance, omitting intermediate conclusions.
- **Goclenian sorites:** presents the corresponding chain in the reverse order,
  beginning from the more general end.

## Worked checks

“All French people are Europeans. All Parisians are Europeans. Therefore all
Parisians are French.” The middle term, Europeans, is an undistributed predicate
in both A premises. The conclusion is not established by those premises, whatever
its factual status.

“A bat is a mammal. This baseball bat is a bat. Therefore it is a mammal.” The
middle term changes meaning: *quaternio terminorum*.

“Avarice deserves blame because it is a vice.” Reconstruct “Every vice deserves
blame” as the major premise. The resulting inference has a valid form; whether
the reconstructed value premise is accepted is a separate issue.
