# Research reassessment — 10 September 2026

> Direction update, 10 September 2026: this document retains its original evidence assessment. Following the user's later asymmetry/clock/RAM manuscript, the [mathematical scope](mathematical-plan-feedback-energy-clocks.md) and [active roadmap](NEXT-STEPS.md) supersede its task ordering. Energy exchange, asymmetry, clocks, and interacting observation are now central; the predictive benchmark remains optional.

**Status:** scientific scope audit and reproducible elementary checks. This document and [NEXT-STEPS.md](NEXT-STEPS.md) supersede the priorities and seven-day schedule in the v1 scope. The original Markdown, LaTeX, PDF, hashes, and tags remain historical records.

**Conceptual source:** [@dorian_x10](https://x.com/dorian_x10). This audit distinguishes the user's questions and hypotheses from AI-proposed formalizations. Attribution records a contribution to this project; scientific novelty requires a separate literature comparison.

## Assessment

We have an organized research proposal, a typeset scope, and provenance records. Before this audit, the repository contained no research implementation, simulation results, physical measurements, or new proved theorem. The LaTeX appendix correctly established an elementary conditional gradient-flow identity and clarified several earlier ambiguities. Successful PDF compilation did not validate the proposed theory.

The most defensible direction is **predictive coarse-graining in interacting systems**: determine which internal details can be discarded while retaining a specified prediction, and when memory or additional measured variables are necessary. This preserves a central idea in the original conversation while giving it a finite, checkable meaning.

The previous AI-assisted plan overreached in its breadth and in treating several analogies as support for a common physical mechanism. The fluid announcement should not have made a full proof audit the first dependency of this project. The effort percentages had no quantitative basis for their relative values; they were planning suggestions, not evidential weights. The seven-day schedule combined too many unrelated research programs to support reliable conclusions.

No current result establishes a unified theory, a new physical law, a necessary number of hierarchy levels, or a route to resolving P versus NP. This is a statement about the evidence currently available, not a proof that all broader ideas are impossible.

## What was checked

- The original private transcript, with particular attention to the 21 user turns. Repeated pasted prompts were deduplicated for reading. User quotations of Gemini were distinguished from the user's own assertions.
- The founding Markdown scope, LaTeX and its clarification/P versus NP appendices, README, build notes, provenance records, and repository history through commit `39e7354778afc26becccd3304e6ffbf213eb512c`.
- The OpenAI announcement, the fluid paper's theorem statement, introductory mechanism and scaling discussion, selected theorem references, and public Lean entry points/build instructions. This was a source-and-scope check, **not** a line-by-line verification of the 166-page proof or a Lean/Comparator build.
- Primary literature on predictive states, information bottlenecks, Markov aggregation and retained memory.
- New exhaustive four-state controls and a quadratic averaging check, supplied in [audit/check_sanity.py](audit/check_sanity.py), with [recorded output](audit/sanity-results.json).

All four publication-file hashes in `scope-provenance.json` and the private transcript digest in the founding provenance record matched their local files. No physical experiment, external expert review, full novelty search, or independent formal proof verification was performed in this audit.

## Recovering the original questions faithfully

These are paraphrases of the user's ideas, not claims that the formal candidates have been derived from them.

| Original thread of thought | Faithful mathematical candidate | What must remain separate |
|---|---|---|
| Internal interactions and feedback leave an aggregate result usable by the next level | A projection, predictive state, or boundary summary with a defined target | A summary need not be binary, autonomous, or sufficient |
| Timing and arrangement affect what a system can do | Sampling interval, update schedule, propagation delay and coupling | A rescaled time parameter is not evidence of a higher physical observer |
| Internal “boundness” limits accessible detail | Separate measures of coupling, observability, predictive loss and measurement budget | No universal information-protection or “Shannon tax” law has been derived |
| Asymmetry drives transitions or organization | A model-specific imbalance, potential, or Lyapunov function | These quantities are not interchangeable; the universe optimizing one objective is an interpretation |
| Apparent separation could reflect a different relational description | A proposed state-space mapping with measurement and causal rules | Relabeling coordinates does not derive quantum correlations or spacetime physics |
| Self-prediction and coevolving human–AI interaction have limits | Separate finite prediction, feedback/adaptation, and computability questions | Logical undecidability is different from slow computation or observational limits |
| A hierarchy might have a preferred depth | A model-selection question after specifying levels and a cost | A fitted depth is not the number of spacetime dimensions |

The transcript contains shifts between resolving asymmetry, symmetry, physical energy, and philosophical interpretation. It does not specify a unique functional or dynamics for these ideas. Choosing one now would be a modeling decision by this project, not recovery of an already complete theory. The clearest present anchor is the user's request to explain local feedback becoming a usable aggregate at the next level.

## Reclassification of the seven hypotheses

| Item | Correct present status | Decision |
|---|---|---|
| H1: some coarse descriptions preserve prediction | Established in many specified systems; the existential wording is too weak to be novel | Replace with a fixed-target, costed comparison in one model family |
| H2: observability has resource tradeoffs | A plausible research question, but the proposed quantities do not define one universal tradeoff | Specify access, units, time window, noise and budget before testing |
| H3: asymmetry organizes systems | The chosen gradient-flow example has a standard dissipation identity; a universal claim does not follow | Keep as an optional later mechanism, not a foundational axiom |
| H4: rescaling simplifies some singular trajectories | An established mathematical phenomenon in specified models | Use as a separate calibration example; prove stability separately |
| H5: self-reference limits prediction | Universal undecidability is established; a new model-specific boundary is unspecified | Retain the distinction, defer new work |
| H6: compatibility with quantum mechanics | A requirement on a future model, not an experimentally supported hypothesis in this project | Defer until a model gives actual probabilities and observables |
| H7: a preferred number of levels | No derivation or data support eleven or twelve | Remove preferred depth from active assumptions |

Predictive minimal representations already have a substantial theory; see [Shalizi and Crutchfield, *Computational Mechanics*](https://arxiv.org/abs/cond-mat/9907176). The scientific opportunity must be a specific improvement, characterization, application, or useful failure case beyond that foundation.

## Mathematical corrections that change the direction

### A projection does not automatically define a higher-level dynamics

For a deterministic system with fine-state update \(F\) and projection \(\Pi\), an exact macro update \(G\) requires

\[
\Pi F=G\Pi.
\]

Equivalently, whenever \(\Pi x=\Pi x'\), we must have \(\Pi F(x)=\Pi F(x')\). Otherwise the same visible state can have different visible futures. Information discarded by the projection can return through the dynamics. A hierarchy diagram alone does not establish this condition at any level.

For a finite Markov chain with transition matrix \(K\), define

\[
q_i(b)=\sum_{j:\Pi(j)=b}K_{ij},\qquad
\Delta(\Pi,K)=\max_{\Pi(i)=\Pi(j)}\frac12\sum_b|q_i(b)-q_j(b)|.
\]

The condition \(\Delta=0\) is strong lumpability: the projected chain has the same autonomous transition rule for every initial distribution. This is established theory, not a new theorem of our hypothesis. Necessity follows by starting at either microstate in a block; sufficiency follows because every mixture within that block has the same next-block distribution. See [Wolfer and Watanabe, *Geometric Aspects of Data-Processing of Markov Chains*](https://arxiv.org/abs/2203.04575), Section 3.4, for the classical criterion and context.

If \(\Delta>0\), the particular projection fails this universal criterion. It can still give useful approximate or distribution-specific predictions. For any single proposed macro row, the triangle inequality gives a worst-case one-step total-variation error of at least \(\Delta/2\) on a maximally separated pair. This is an elementary bound, not a lower bound on every possible representation or prediction algorithm.

### Memory is an explicit candidate, with an explicit cost

Let \(Y_t=\Pi(X_t)\). Under a specified probability law,

\[
I(Y_{t+1};Y_{t-1}\mid Y_t)>0
\]

proves that the current macrostate alone misses predictive information present in the preceding observation. Zero for this single lag does not prove the full Markov property; longer history can matter. Finite history need not suffice in every system.

Higher-order lumpability and its information-theoretic characterization are already studied by [Geiger and Temmel](https://arxiv.org/abs/1212.4375). Approximation by smaller, higher-order chains is also treated by [Geiger and Wu](https://arxiv.org/abs/1608.04637). Merely showing that memory helps would reproduce known ideas. Our eventual contribution would need a narrower result or an advantage over appropriate baselines.

### Preserve a fixed task, not just information in general

A constant summary is small but usually uninformative; the full microstate is sufficient but may save nothing. Specify the target \(Z\), horizon, available observations, and loss before selecting a summary \(S\). Compare forecasting distributions or task error, not just \(I(X;S)\). Ordinary reconstruction rate-distortion is not automatically the same objective as preserving future prediction. The [information bottleneck method](https://arxiv.org/abs/physics/0004057) is an existing formulation for compression that retains relevance to another variable.

Count summary construction, online update, decoder storage, training data and measurement access. Entropy in bits is not runtime, channel capacity in bits per second, or dissipated energy in joules. The appendix's units correction to the proposed boundness ratio is valid, but dimensional consistency alone does not give it a physical law or a bound of one. Mutual information also does not by itself identify causal direction.

### A decreasing functional proves only what its assumptions imply

For differentiable, time-independent \(A\), symmetric \(M\succeq0\), antisymmetric \(J\), and smooth solutions of

\[
\dot x=-M\nabla A+J\nabla A,
\qquad
\frac{dA}{dt}=-\nabla A^{\mathsf T}M\nabla A\le0.
\]

The appendix's derivation is correct. It does not prove convergence to a unique/global optimum, useful computation, or an efficient algorithm. Added forcing, explicit time dependence, delay, or stochastic noise needs its own calculation. Calling \(A\) “asymmetry” does not establish its equivalence to physical potential energy or thermodynamic free energy.

### “Computation” needs a task-level meaning

A dynamical system has state transitions. To claim it implements a computation, specify inputs, their encoding, a rule or task, outputs and readout. To claim a resource advantage, compare implementations of the same task. Otherwise nearly any motion can be redescribed as computation without gaining an explanatory or predictive result.

## The fluid intersection, correctly weighted

The OpenAI announcement is dated **8 September 2026**. It reports a forced three-dimensional viscous construction starting from rest, with bounded kinetic energy and unbounded velocity near a finite time, and claims alternatives C and D of the Clay formulation. The [announcement](https://openai.com/index/navier-stokes-solution/) and [paper, Theorem 1.1](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) match the central description in our scope. As checked on 10 September, Clay's page labels the problem [“Active”](https://www.claymath.org/millennium/navier-stokes-equation/); that label alone establishes neither acceptance nor rejection of the released proof.

The reviewed Lean snapshot is [`f9e8bc5b38b6e212696e8a30e3e91517af887bbd`](https://github.com/openai/NavierStokesAndEuler/tree/f9e8bc5b38b6e212696e8a30e3e91517af887bbd). Its whole-space and periodic entry points and Comparator instructions are present. Reading them is not a build or a dependency/axiom audit. Existing discussion of `sorry` in challenge files must not be used by itself to establish either failure or success of the proof.

The distinct Chen–Walsh–Wheeler hollow-vortex paper was published **23 July 2026**. It concerns two-dimensional Euler free boundaries, gas-filled cores, and collapse with divergent absolute pressure. It is not the same theorem or announcement. [Published article](https://link.springer.com/article/10.1007/s00208-026-03541-2)

| Intersection | What carries over to our project | What does not follow |
|---|---|---|
| Nonlinear averaging | A hidden fluctuation can contribute to a retained quadratic quantity; this motivates closure tests | Every microscopic detail reduces to a sufficient binary skeleton |
| Rescaled profiles | A change of variables can expose a simpler leading structure | Stability, attraction of nearby solutions, or convergence of the full corrected flow without a specified norm |
| Different spatial and temporal scales | Ratios of transport, diffusion and observation times can matter | A universal hierarchy of clocks or observers |
| Concentrated amplitude with bounded energy | Global integral bounds and local maxima constrain different properties | Infinite readable information, infinite energy generation or unlimited computation |

The paper's scales \(\ell_r\asymp\tau^{1/2}\), \(\ell_z\asymp\tau^{1/2-h}\), and the differing angular/radial Reynolds-number behavior agree with our transcription. The essential correction is that fixed-shape language concerns the **leading profile**, not an independently established attractor for all nearby full solutions. [Paper, Sections 2–3](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)

Our inference is that closure and rescaling supply useful methods to borrow. They supply no new evidence for the project's quantum, cosmological, or computational universality claims. The primary direction remains viable even if the external theorem is revised. A full proof reproduction should be a separately scoped specialist project, not the admission requirement for beginning ours.

For continuous dynamics later, a closer initial comparison is a modest model with eliminated variables and memory. [Hudson and Li's Mori–Zwanzig benchmark](https://arxiv.org/abs/1810.08175) explicitly studies the importance of memory in reduced dynamics.

## Exact controls completed during this audit

Take \(X_{t+1}=X_t+1\pmod4\), with uniform initial phase. Enumerating all four states gives:

| Observable and sampling | Closure defect \(\Delta\) | Next-state uncertainty from current observation | With one preceding observation |
|---|---:|---:|---:|
| Parity: labels `0,1,0,1`; every tick | 0 | 0 bits | 0 bits |
| Paired states: labels `0,0,1,1`; every tick | 1 | 1 bit | 0 bits |
| Paired states; every second tick | 0 | 0 bits | 0 bits |

For paired states at every tick, the best current-only predictor makes errors with probability \(1/2\); one lag determines the next observation exactly. But that two-observation state has **two bits**, the full microstate entropy. Memory restores prediction here without delivering compression of the fine state. At stride two the target horizon changes and intermediate behavior is skipped. The parity row is a different observable, not a fair competitor for predicting the paired-state target.

These controls show why the new experiment must hold the target and time horizon fixed. They support no novelty claim. Likewise, an equal mixture of \(w=-1,+1\) has mean zero and second moment one: a mean can lose information needed for a nonlinear observable. This does not reproduce the fluid PDE.

Reproduce with `python3 audit/check_sanity.py`; the script uses exact rational probabilities and asserts the analytical values. It requires only Python's standard library.

## Deferred claims and corrected expectations

- **P versus NP:** the appendix's definitions and polynomial construction/readout obligations are sound. The problem remains [listed as unsolved](https://www.claymath.org/millennium/p-vs-np/). A SAT boundary-summary experiment is a separate algorithm project and is deferred to avoid splitting this one. A useful summary for dynamics does not solve arbitrary SAT. A bad summary does not prove a lower bound against all algorithms.
- **Singularities as computers:** the time change \(t=T_*(1-e^{-s})\) maps infinite rescaled time into finite physical time but supplies no finite-resource encoding, reliable steps, or readout. The broader resource problem is discussed in [Aaronson, *NP-complete Problems and Physical Reality*](https://www.scottaaronson.com/papers/npcomplete.pdf).
- **Quantum and relational coordinates:** there is presently no model deriving measurement probabilities. Existing [Bell experiments](https://arxiv.org/abs/1508.05949) constrain explanations; repeating standard quantum predictions without a distinct model would not test this hypothesis. No change to quantum mechanics is implied by the classical controls.
- **Preferred depth, cosmology and consciousness:** retain these as labeled exploratory interpretations. Numerical preferences within one toy model cannot establish a universal depth. Coinciding announcements, feeds or service interruptions do not establish a causal mechanism.
- **Authorship:** preserve the user's contribution and public version history without treating a marker as proof of worldwide priority or guaranteed future attribution. The private transcript remains private.

The older sentence saying a theory “becomes physics only when it predicts an observable difference” is too restrictive. A reformulation can contribute understanding or calculation while matching established predictions. It must nevertheless show what it adds; a claim of new physical behavior requires a discriminating prediction and evidence.

## Direction from here

Replace parallel workstreams with one milestone sequence: **define a prediction task → establish exact baselines → test costed summaries and memory → assess a limited extension**. The immediate output is a finite-model benchmark, not a unification paper. Success can mean a useful representation, a well-defined limitation, or a clear reproduction identifying where the original intuition already belongs in existing mathematics.

The [execution plan](NEXT-STEPS.md) specifies the model, measures, baselines and stopping rules. Expanding the interpretation becomes justified only after a particular result gives a reason to do so.
