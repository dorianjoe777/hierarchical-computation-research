# Active execution plan

**Adopted:** 10 September 2026. Read the [reassessment](research-audit-2026-09-10.md) for evidence and corrections. This plan replaces the old percentage allocations, seven-day schedule, fluid-proof-first dependency, and parallel SAT/quantum experiments. Historical scope files remain unchanged.

## The question we will actually investigate

For a small interacting system, **which information must a limited observer retain to predict a fixed boundary observable, and what accuracy is lost when storage or observation frequency is reduced?**

The first stage is a reproduction and characterization study. Existing theories already show that useful coarse-graining and memory can occur. We will claim novelty only after identifying a specific addition relative to those theories.

The immediate mathematical deliverable is a finite-state benchmark with exact probabilities, known failure cases, and complete accounting of the information given to each predictor. The immediate physical deliverable is a clearly specified observable and sampling procedure that could later be implemented in a controlled digital apparatus. A continuum theory is not needed to start.

## Milestone 1 — Freeze one model and one task

Use three binary nodes \(X_t=(a_t,b_t,c_t)\in\{0,1\}^3\), updated synchronously at integer ticks:

\[
\begin{aligned}
a_{t+1}&=b_t\oplus\eta^a_t,\\
b_{t+1}&=a_t\oplus c_t\oplus\eta^b_t,\\
c_{t+1}&=((1-G_t)c_t+G_t b_t)\oplus\eta^c_t.
\end{aligned}
\]

Here \(\oplus\) is XOR, the noises \(\eta^a_t,\eta^b_t,\eta^c_t\) are independent Bernoulli variables with probability \(\epsilon\), and \(G_t\) is independently Bernoulli with probability \(\gamma\). Draw all these variables independently across ticks and independently of past states. The arithmetic expression inside the last XOR selects either \(c_t\) or \(b_t\) and is itself binary.

This is an **explicit new modeling choice for testing the question**, not a physical law derived from the transcript. It gives internal feedback and a controlled influence on the observable boundary node. It contains eight states, so its full transition matrix can be enumerated without simulation error.

- Primary observation: \(Y_t=c_t\).
- Primary target: the distribution of \(Z=Y_{t+1}\). Additional horizons \(Y_{t+2}\) and \(Y_{t+4}\) are separately labeled tasks.
- Parameter grid: \(\gamma\in\{0,1/4,1/2,3/4,1\}\), \(\epsilon\in\{1/32,1/8,1/4,1/2\}\). These are coverage choices, not fitted physical constants.
- Primary law: the unique stationary distribution of the full chain. Because every next-state probability is positive for these noise values, the chain has a unique stationary distribution. Compute and verify it from the exact rational matrix.
- Robustness law: separately start at each of the eight microstates and report time-dependent predictions; do not mix these results with stationary averages.
- Primary observation schedule: every tick. For a secondary sampling test, observe every second or fourth tick but predict the same one-tick-ahead target at the observed time. This avoids improving the score merely by changing the target horizon.

Document the noise convention, time unit, state order, observation access, and loss in `experiments/finite_boundary/spec.md` before building a sweep. An actual physical delay or a change to the update rule would be a later experiment; sampling is not equivalent to changing the system's clock.

**Completion condition:** the eight-state transition table is derived; rows sum to one; the stationary law is verified; the observation and target are fixed. No experiment should introduce preferred hierarchy depth, quantum coordinates, or an assumed energy interpretation of coupling.

## Milestone 2 — Establish exact baselines and failure cases

Begin from the [four-state controls already checked](audit/sanity-results.json), then evaluate the eight-state model. Compute joint probabilities by enumeration and matrix powers before fitting any predictor to sampled data.

| Predictor | Information available at prediction time | Role |
|---|---|---|
| Constant probability forecast | Stationary target frequency | Detect apparent gains caused only by an imbalanced target |
| Current observation | \(Y_t\) | Memoryless coarse baseline |
| One-lag history | \((Y_{t-d},Y_t)\) at sampling stride \(d\) | Measure useful retained memory |
| Two-lag history | \((Y_{t-2d},Y_{t-d},Y_t)\) | Check whether improvement continues with more memory |
| Full microstate oracle | \(X_t\) and the known transition matrix | Best prediction with privileged access; not a fair equal-access competitor |
| Exact predictive grouping of a finite history | Group histories only when their target distributions agree | Known sufficient-statistic construction; candidate compression reference |

For the last row, count the memory needed to compute and update the grouping. A small group label does not guarantee a small online predictor: it may still require storing the full history. Prove a recursive update if claiming the label alone can be maintained. Grouping for one forecast horizon need not preserve longer-horizon predictions or define an autonomous macro dynamics.

Report:

1. Strong lumpability defect \(\Delta(\Pi,K)\), distinguishing it from a stationary average error.
2. Conditional target entropy and Bayes classification error for each representation.
3. Predictive information supplied by each added lag. A zero single-lag value is not a proof that all older history is irrelevant.
4. Representation entropy, maximum number of states, actual retained bits, transition/decoder-table size, and construction/update work as separate quantities.
5. Excess optimal log loss \(H(Z\mid S)-H(Z\mid X_t)\), in bits per forecast. This is nonnegative here because the full Markov state screens the future from the observation history. It does not count model-estimation error.

**Required controls:** at \(\gamma=0\), the boundary is a closed noisy two-state chain. At \(\epsilon=1/2\), future boundary bits are independent fair bits: memory should supply no forecasting gain. Pair these with the audit's deterministic hidden-phase counterexample. Exact closure and intrinsic predictability are different properties.

**Completion condition:** analytical controls match enumeration; all 20 parameter combinations have exact reference values; each result names its law and target. If a baseline fails, fix the calculation before proceeding. This milestone is not yet a novelty claim.

## Milestone 3 — Decide whether there is a useful contribution

First make a compact plot/table of prediction loss against actual storage, with coupling and noise shown separately. Do not combine bits, latency and joules into one score without a justified conversion. Do not compare predictors with extra sensors as though they have the same information budget.

Then choose **one** limited extension justified by the baseline results: for example, a recursively updateable summary with fewer states than the available history, or a precise counterexample showing why a proposed summary cannot work. State its rule before evaluation.

Compare directly with the applicable results in [predictive-state theory](https://arxiv.org/abs/cond-mat/9907176), [higher-order lumpability](https://arxiv.org/abs/1212.4375), and [higher-order Markov aggregation](https://arxiv.org/abs/1608.04637). A change of vocabulary or an expected memory effect is not a new theorem.

If a learned method is introduced, use independent trajectories for training, validation and test; freeze its choices before testing; report several independent seeds and uncertainty intervals. Avoid overlapping history windows across data splits. Keep the exact matrix calculation as the reference. Report encoder/training cost as well as inference cost, and show performance away from the parameters used to select the method.

**Continue if:** there is a reproducible equal-access advantage at a stated cost, a proved characterization within a stated class, or a useful counterexample that changes the hypothesis.

**Stop or revise if:** the gain vanishes against the exact baseline; it requires hidden-state access unavailable to competitors; bookkeeping consumes the claimed compression; it depends on changing the forecast task; or it merely reproduces an existing result. A negative outcome should be written up as a limitation, not rescued by changing the interpretation after seeing the data.

## Milestone 4 — Choose one extension after the finite result

| Direction | Entry requirement | Observable result and stopping rule |
|---|---|---|
| Continuous dynamics with memory | Finite pipeline works and a question requires continuous variables | Reproduce one established reduced-dynamics benchmark, such as [Hudson–Li](https://arxiv.org/abs/1810.08175); check numerical convergence and compare memoryless and memoryful models. Stop if apparent benefit is a solver artifact. |
| Controlled physical realization | A simulator predicts a specific measurable effect under calibrated conditions | Implement observable digital nodes or a small coupled electronic system; log boundary states, sampling times, interventions and noise. Compare held-out data with the preregistered model and baselines. Stop generalizing if the apparatus does not implement the assumed dynamics. |
| Rescaling study | There is a defined rescaling, observable, norm and reason it addresses a result from this project | Reproduce a tractable known self-similar example and distinguish exact profile, asymptotic limit and attraction. A full Navier–Stokes/Lean reproduction remains a separate specialist project. |

Choose one row, not all three. In an apparatus, prediction gains test the particular model and measurement scheme. Inferring an energy law requires actual calibrated energy measurements and a thermodynamic derivation; neither information entropy nor a software counter supplies that automatically. A finite-resolution fluid experiment cannot directly demonstrate an actual infinity.

Quantum modifications, cosmological depth, human–AI ontology, and general P versus NP remain outside this cycle. They need their own operational models and evidence before resources are assigned.

## Publication and decision record

Maintain a small claim ledger with: statement, assumptions, provenance, nearest prior result, evidence file, failure condition, and current status. Use statuses **established reference**, **reproduction**, **proved within model**, **numerical evidence**, **physical measurement**, or **interpretation**. None of the current elementary examples should be labeled a new discovery.

The next release should contain the specification, exact baseline code/results, one cost–accuracy figure, failures, and a short comparison with prior work. Publish a technical research claim only after its novelty and correctness have been checked. A useful reproduction report is also a legitimate outcome.

Progress is gated by these deliverables, not the former seven-day promise. The next executable step is **Milestone 1's transition-table derivation and specification**, followed by the exact baseline. This is small enough to inspect fully and informative enough to decide whether the broader project has a productive mathematical path.
