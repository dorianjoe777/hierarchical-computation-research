# Novelty assessment — 10 September 2026

**Conclusion:** there is scope to investigate an original, limited contribution, but this project has not yet demonstrated one. The current broad concepts and the proposed first experiment substantially overlap established research. No confirmed literature gap has been identified by this targeted search.

This assessment follows the [scientific audit](research-audit-2026-09-10.md) and sharpens the novelty gate in [NEXT-STEPS.md](NEXT-STEPS.md). The conceptual motivation remains attributed to [@dorian_x10](https://x.com/dorian_x10); the finite-state formalization is a modeling choice made in this project. Independently reaching a useful question is different from establishing scientific priority for its mathematical answer.

## What the closest work already covers

| Our proposed idea | Closest primary work | Consequence for novelty |
|---|---|---|
| A small “skeleton” retains the information needed to predict | [Shalizi–Crutchfield, *Computational Mechanics*](https://arxiv.org/abs/cond-mat/9907176), published 2001 | Minimal predictive representations are established; renaming one a skeleton adds no result |
| A coarse description may need retained history | [Geiger–Temmel, *Lumpings of Markov chains…*](https://arxiv.org/abs/1212.4375), published 2014; [Geiger–Wu, *Higher-Order Kullback–Leibler Aggregation*](https://arxiv.org/abs/1608.04637), 2016 preprint | Memory effects, higher-order aggregation and information-theoretic objectives already exist |
| Trade predictive accuracy against compression | [Marzen–Crutchfield, *Causal Rate-Distortion for Infinite-Order Markov Processes*](https://arxiv.org/abs/1412.2859), 2014 preprint / 2016 publication | A prediction–compression curve alone is not a new framework |
| Update the summary recursively as observations arrive | [Still, *Information Bottleneck Approach to Predictive Inference*](https://www.mdpi.com/1099-4300/16/2/968), 2014, Section 4.2 | Recursive predictive compression under a memory/coding constraint is explicit prior work |
| Pass progressively reduced information through several levels | [*Exact and Soft Successive Refinement of the Information Bottleneck*](https://pmc.ncbi.nlm.nih.gov/articles/PMC10528077/), 2023 | Multistage processing and loss of information optimality already have formal treatments |
| Link retained information to physical scales and renormalization | [Koch-Janusz–Ringel, *Mutual Information, Neural Networks and the Renormalization Group*](https://arxiv.org/abs/1704.06279), 2017 preprint / 2018 publication; [Gordon et al., *Relevance in the Renormalization Group and in Information Theory*](https://arxiv.org/abs/2012.01447), 2020 preprint | The information-theory/RG bridge is already developed in specified physical settings |
| Link predictive memory to thermodynamic efficiency | [Still, Sivak, Bell and Crooks, *The thermodynamics of prediction*](https://arxiv.org/abs/1203.3271), 2012 | This is a real established connection under physical assumptions; our metaphor supplies no new energy law |
| Learn predictions from compressed observations of a hidden process | [Han–Jiang–Wu, *Prediction from compression for models with infinite memory*](https://proceedings.mlr.press/v247/han24a.html), 2024 | There are already strong learning-theoretic results; a trained predictor needs the appropriate statistical baselines |

These works solve different problems; the table does not assert that one paper already solves our entire proposed benchmark. It establishes that its main ingredients, and several combinations of those ingredients, have substantial precedent. A publication date cannot be inferred from the search engine's crawl date; the dates above distinguish preprints from journal publications where relevant.

The strongest correction to the previous plan is the recursive-information-bottleneck comparison. Still's Section 4.2 explicitly optimizes state updates from the previous state and current input, trading predictive information against an information-theoretic coding cost. Consequently, **adding an online update rule is not by itself an original contribution**. The exact hardware storage and implementation costs in our proposed study need separate definitions; they must not be silently identified with that information-theoretic cost.

Likewise, successive refinement studies whether staged representations preserve information optimality. This makes it a necessary comparison for the original inter-level idea, although a feed-forward compression hierarchy and a temporally recurrent observer are different mathematical objects.

For continuous dynamics, [Hudson–Li's Mori–Zwanzig study](https://arxiv.org/abs/1810.08175) already supplies a concrete reduced-dynamics example in which memory matters. Finding a similar effect in a new toy system would initially be a reproduction or application.

## An immediate calculation shows how modest our first result is

In the proposed three-node model, the observed boundary is \(Y_t=c_t\). Conditional on the full state \(x=(a,b,c)\), the probability of the next boundary bit being one is

\[
q_x=\Pr(c_{t+1}=1\mid X_t=x)
=\epsilon+(1-2\epsilon)\big[(1-\gamma)c+\gamma b\big].
\]

This follows directly by averaging the Bernoulli selector and then applying the independent bit-flip noise. For two microstates with the same visible bit \(c\), only their differing \(b\) values change this probability. The total-variation distance between two Bernoulli laws is the absolute difference between their success probabilities. Therefore the strong-lumpability defect is exactly

\[
\boxed{\Delta(\Pi,K)=\gamma|1-2\epsilon|.}
\]

Thus the projection onto the boundary bit is strongly lumpable precisely when \(\gamma=0\) or \(\epsilon=1/2\), over \(0\le\gamma\le1\) and \(0\le\epsilon\le1/2\). This is a short application of the classical criterion, not a discovery claim. The internal \(a,b\) dynamics can still affect longer-history predictions and stationary averages; this one-step calculation does not determine them.

Independent enumeration of all transition probabilities matched the formula at all 20 planned parameter pairs using exact rational arithmetic. Reproduce with `python3 audit/check_boundary_closure.py`; the [script](audit/check_boundary_closure.py) checks this identity only. The full forecast/memory benchmark has not been run.

It also exposes a useful conceptual distinction. At \(\epsilon=1/2\), the observed next bit is an independent fair bit: closure is exact, while forecasting information is absent. Hence “more autonomous coarse dynamics” and “more predictable dynamics” are not equivalent. Nonzero strong-lumpability defect, in turn, does not prove that a particular stationary observer benefits from one chosen lag.

The eight-state model is valuable because these distinctions can be inspected fully. Choosing a previously unused set of eight transitions would not, by itself, make a substantial scientific contribution.

## Where a contribution might still be developed

### 1. A certified prediction–memory frontier for a defined observer class

This is the most manageable candidate to investigate first. Observe \(Y_{nd}\), where \(d\) is a sampling stride, and predict the same physical target \(Y_{nd+1}\). Require an online observer with \(m\) possible internal states:

\[
M_n=g(M_{n-1},Y_{nd}),\qquad
\widehat p_n=q(M_n).
\]

Specify deterministic updates, fixed initialization, observation access, and a time-independent probability decoder. One possible objective is

\[
\mathcal L^*_{m,d}(\gamma,\epsilon)=
\inf_{g,q}\limsup_{N\to\infty}\frac1N
\sum_{n=0}^{N-1}\mathbb E[-\log_2 q(M_n)(Y_{nd+1})].
\]

The expectation must use the stated microstate law and observer initialization. The source's unique stationary distribution does not imply the joint source–observer chain is irreducible: an observer may have several closed classes. Handle initialization and long-run occupation weights explicitly.

This is a **candidate specification**, not a proposed new information theory. It constrains observer state cardinality, rather than just an entropy or mutual-information quantity. Report its storage ceiling \(\lceil\log_2m\rceil\) separately from update-table storage, decoder precision, computation and sampling costs. It is not yet a total physical-resource optimum.

For binary observations there are \(m^{2m}\) labeled deterministic update tables. Small cases can be exhausted; a global optimum should be claimed only over the explicitly enumerated class, with reliable numerical bounds on log-loss comparisons. Randomized, time-dependent, or externally clocked observers are outside that class unless added and costed.

**A possible contribution:** prove a nontrivial characterization of the optimum, an unavoidable memory requirement, or a robust change in optimal observer structure over a meaningful model family, and establish that the result is not already implied by the closest theory.

**Insufficient by itself:** a plot where more memory helps, an optimality claim based on one heuristic, or a new notation for a known objective. The literature gap for the stated frontier is currently **unconfirmed**.

### 2. A better constructive method with the same information access

A method that finds a compact, recursively maintainable summary might be useful if it has a proved guarantee or a reproducible advantage in construction cost, online memory or forecast quality against relevant methods. It must count any history buffer or auxiliary state used to construct the apparent summary.

Candidate comparisons include fixed-history predictors, exact finite-history grouping, recursive bottleneck methods where their assumptions match, and a known-model Bayesian filter using the same observations. The latter's probability vector and arithmetic precision have a cost; it is different from the privileged full-microstate oracle. [Predictive state representations](https://arxiv.org/abs/1207.4167) are also an established comparison if the project introduces actions or interventions.

**A possible contribution:** a specified algorithm with an advantage that persists beyond the system used to design it. No such algorithm exists in this repository yet. Restricting the first experiment to eight states helps verification but cannot establish scalable performance.

### 3. A useful physical application

A calibrated electronic system could test when sampling and retained history improve a boundary forecast at a measured resource cost. A useful application would connect an identified physical mechanism to a model that predicts held-out measurements and survives competing explanations.

This is a possible route to empirical novelty after the mathematical baseline. Repeating expected memory effects in an arbitrary circuit is not automatically a research contribution. Demonstrating an energy relation requires a physical energy model and measurements; the Boolean noise parameter is not a temperature and the coupling parameter is not an energy.

## What would change this assessment

Before claiming novelty, write a single sentence specifying the claimed addition, then attach:

1. The closest paper and the exact result or assumption that it does not cover.
2. A complete derivation, exhaustive certificate, reproducible comparison, or physical measurement establishing the addition.
3. A reason it matters beyond renaming concepts or selecting different parameters.
4. The conditions and counterexamples limiting the claim.

The next decision should be whether the finite baseline exposes an interesting problem of type 1 or 2. It should not be a promise to solve a major open problem. If the outputs are all straightforward consequences of known results, release them as a clear reproduction and revise the research question before enlarging the project.

The fluid result remains relevant background on multiscale dynamics, not evidence that our combination is original. Quantum coordinates, a universal number of levels, and cosmological interpretations have no derived predictions in this project, so scientific novelty cannot currently be assessed through comparison of their mathematical consequences.

## Search scope and limits

This was a targeted primary-literature check of predictive states, finite/higher-order Markov aggregation, predictive rate-distortion, recursive information bottlenecks, successive refinement, information-based renormalization, thermodynamics of prediction, and recent HMM prediction theory. Sources were examined through available abstracts, indexed publisher text and selected sections. In particular, the recursive update objective was checked in indexed text of Still's Section 4.2; direct retrieval of that publisher PDF was blocked.

This is not an exhaustive systematic review or a proof that no matching result exists. The evidence supports substantial prior overlap and several plausible research targets; it does not yet support a claim of a newly identified open problem, a publication-ready result, or a numerical probability of discovery.
