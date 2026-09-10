# Mathematical scope: feedback, energy, clocks, and accessible detail

**Working revision: 10 September 2026.** Conceptual motivation: [@dorian_x10](https://x.com/dorian_x10). The mathematical choices and elementary deductions below are an assistant-developed proposal for testing the user's idea. They are not a derivation of that idea from established physics, or a claim of novelty.

**Implementation update:** [working model v0.1](models/feedback_null_v01/SPEC.md) now fixes all eight differential equations and initial parameters, translates the null-state/self-reference visualization into candidate observables, and supplies [executed deterministic controls](models/feedback_null_v01/RESULTS.md). The noisy observation experiment and broader hierarchy remain future work. The [foundations overview](FOUNDATIONS-OVERVIEW.md) consolidates the current position.

The core question is: **under what dynamics can internal interactions produce a persistent collective unit, and how does that organization change the microscopic detail an interacting observer can obtain at a specified cost?** Asymmetry, available potential, completion, and temporal organization are part of this question from the beginning.

The newest manuscript is preserved verbatim in the local research workspace; its [provenance record](manuscripts/2026-09-10-asymmetry-clock-ram-provenance.json) identifies the exact bytes. This document interprets it without replacing it. Read the [physical assessment](physics-frontier-assessment-2026-09-10.md) for the intended quantum and relativistic applications. The earlier finite-state prediction study remains an optional calibration, not the organizing center of this work.

## 1. Preserve the intended mechanism, then separate its claims

The transistor-table picture proposes fixed underlying relationships with changing internal states. A component may rotate in its state space while retaining its neighbors; another collective organization may influence its timing through those same relationships. “RAM” names a proposed resource or mode enabling transitions. “Implosion/explosion” names how an exchange might look different from the two participating levels. A larger observer may encounter a stable summary despite continuous internal activity.

These are useful modeling intentions. They do not yet fix the equations. The first model will use coupled oscillators because they expose phase, energy, interaction, and measurement in a small solvable system. They are an analogue of the proposed mechanism, not a claim that transistors or particles literally obey this oscillator model. Real switching circuits can be considered after a quantitative effect is identified.

Separate these candidate statements:

1. Feedback helps maintain a collective organization.
2. This organization has identifiable timescales or clock observables.
3. The same interactions affect access to internal details through physical probes.
4. The relation persists when one collective unit participates in another organization.
5. A suitable extension reproduces specified quantum or relativistic results.

One result does not establish the next. The direction of the coherence–accessibility relationship must remain open: coherence may hide, reveal, or selectively redistribute detail.

## 2. Give the central words distinct mathematical jobs

| Word | Initial mathematical meaning | What must not be inferred automatically |
|---|---|---|
| System | State space, interaction graph, dynamics, and declared boundary ports | Every chosen partition corresponds to a physical object |
| Internal/external level | Subsystem and a proposed collective description that interacts with other systems | An extra spacetime dimension |
| Asymmetry of a state | Departure from a specified symmetry-invariant set, in a stated metric | A force, energy source, or quantity that must decrease |
| Symmetry of a law | Equivariance: transforming a state and then evolving agrees with evolving and then transforming | Every state is symmetric or approaches symmetry |
| Potential | First distinguish potential energy, available work, and dynamically reachable states | These are interchangeable meanings of “potentiality” |
| Completion | A named target set and criterion for entering and remaining near it | Maximum symmetry, disappearance, or a universal terminal level |
| Clock | An observable with identifiable phase or repeatable events, plus a readout procedure | A separate universal drive or a derivation of time itself |
| RAM | Candidate internal storage/resource degrees of freedom; specify energy, memory, and transfer separately | A newly identified substance or region of space |
| Coherence | Initially classical phase organization and its persistence under perturbation | Quantum coherence or entanglement |
| Accessible detail | Information about a fixed target obtained using specified interactions and resources | Information missing from an analyst's chosen summary is physically inaccessible |

For two identical units, let the symmetry exchange their labels. A dimensionless state-asymmetry measure can be

\[
A_{\rm sym}(z)=\frac{(q_1-q_2)^2}{q_*^2}
 +\frac{(\phi_1-\phi_2)^2}{\phi_*^2},
\]

where the positive reference scales are fixed before comparison. It vanishes on the symmetric subspace. Whether its derivative is negative is a calculation, not a definition. A single-site probe breaks exchange symmetry of the full apparatus even if the unprobed pair is symmetric; record that separately.

“Maximum asymmetry” also requires an admissible set, such as a fixed energy budget. This quadratic measure is unbounded on unrestricted phase space. A reset to maximal asymmetry is not defined until those constraints and the reset dynamics are specified.

Energetic disequilibrium is another quantity. Under a specified thermal model with energy levels \(E_i\), temperature \(T\), and Gibbs reference \(p_i^{\rm eq}\),

\[
F[p]=\sum_i p_iE_i+k_BT\sum_i p_i\ln p_i,
\qquad F[p]-F[p^{\rm eq}]=k_BT D_{\rm KL}(p\Vert p^{\rm eq}).
\]

The right side has units of energy; it is not the geometric asymmetry above. Its interpretation as recoverable work requires allowed operations and reservoir assumptions. The equality follows directly by substituting the Gibbs distribution; monotonic relaxation requires additional dynamical conditions.

For completion, choose a target set \(\mathcal M\), tolerance \(\varepsilon\), and hold duration \(T_h\):

\[
\tau_{\varepsilon,T_h}=
\inf\{t:\operatorname{dist}(z(s),\mathcal M)\leq\varepsilon
\text{ for all }s\in[t,t+T_h]\}.
\]

The value may be infinite. If completion means a functioning synchronized unit, also require a nonzero activity or amplitude threshold. A motionless zero-energy state must not count as a functioning clock merely because all differences vanished. An asymptotic limit does not imply exact completion in finite time.

## 3. Specify a small model with an energy balance

Start with two coupled modes. Use charge \(q_i\) in coulombs and conjugate flux \(\phi_i\) in webers, with capacitance \(C>0\), inductance \(L>0\), and \(\kappa\geq0\) in inverse farads:

\[
H_{12}=\sum_{i=1}^2\left(\frac{q_i^2}{2C}+\frac{\phi_i^2}{2L}\right)
       +\frac{\kappa}{2}(q_1-q_2)^2.
\]

Every term is in joules. This is an effective positive quadratic circuit Hamiltonian; an experimental implementation will require a realizable capacitance matrix and calibrated components.

Add one finite resource/clock mode \((q_r,\phi_r)\) and one probe mode \((q_m,\phi_m)\):

\[
H=H_{12}+\sum_{j\in\{r,m\}}
\left(\frac{q_j^2}{2C_j}+\frac{\phi_j^2}{2L_j}\right)
 +\frac{\kappa_r}{2}(q_1-q_r)^2
 +\frac{\eta}{2}(q_1-q_m)^2.
\]

The resource mode is initially just another coupled degree of freedom. Calling it a higher-level clock must wait until a collective relation is demonstrated. Its initial stored energy is finite; its depletion and response to the pair are included. The probe coupling is reciprocal: it changes both the measured system and the meter.

For \(z=(q_1,q_2,q_r,q_m,\phi_1,\phi_2,\phi_r,\phi_m)\), use

\[
\dot z=(\mathbb J-\mathbb R)\nabla H+Bu,
\qquad
\mathbb J=\begin{pmatrix}0&I\\-I&0\end{pmatrix},
\quad \mathbb R=\mathbb R^T\succeq0,
\quad y=B^T\nabla H.
\]

The entries of \(\mathbb R,B,u\) must have the units appropriate to each coordinate; positive semidefiniteness is understood after consistent coordinate scaling. The energy identity is

\[
\boxed{\dot H=-\nabla H^T\mathbb R\nabla H+u^Ty.}
\]

Indeed, \(v^T\mathbb Jv=0\) for a skew-symmetric matrix. Conservative interactions redistribute energy; dissipation and external power have explicit terms. This follows the established [port-Hamiltonian framework](https://arxiv.org/abs/2412.19673). It supplies an accounting method, not evidence for the proposed universal hierarchy.

Begin without noise. Then add calibrated noise and baths consistently with fluctuation–dissipation and stochastic energy accounting; do not add noise while retaining the deterministic balance unchanged. If couplings vary with time, their work contributes \(\partial H/\partial t\). No clock, amplifier, reset, or control protocol is an unaccounted power supply.

This answers “what drives motion?” at the model level: for the isolated pair, \(\dot q_1=\phi_1/L\) and \(\dot\phi_1=-q_1/C-\kappa(q_1-q_2)\), with the analogous equation for unit 2. State-dependent gradients and the coupling law determine the motion. The existence of an asymmetry measure alone does not determine either equation.

Subsystem energies require a declared allocation of interaction energy. Compute exchanged power from that allocation and verify cancellation in the total balance. Summing “liberated energy” at every level would double count energy if the levels describe the same degrees of freedom.

## 4. Establish four analytical controls before a parameter sweep

### 4.1 Coupling alone does not select a coherent mode

For the isolated conservative pair, define

\[
Q_\pm=(q_1\pm q_2)/\sqrt2,\qquad
\Phi_\pm=(\phi_1\pm\phi_2)/\sqrt2.
\]

Then

\[
H=H_++H_-,\quad
H_+=\frac{\Phi_+^2}{2L}+\frac{Q_+^2}{2C},\quad
H_-=\frac{\Phi_-^2}{2L}+\frac{(1/C+2\kappa)Q_-^2}{2},
\]

\[
\omega_+^2=\frac1{LC},\qquad
\omega_-^2=\frac{1/C+2\kappa}{L}.
\]

Each mode energy is conserved. Increasing \(\kappa\) changes the differential mode's frequency; it does not remove its excitation. A result about synchronization therefore needs initial-state restrictions, suitable dissipation, driving, or another justified mechanism.

A useful comparison adds damping only to the differential mode:
\(\dot\Phi_-=-(1/C+2\kappa)Q_- -r\Phi_-/L\), \(r>0\), while \(\dot Q_-=\Phi_-/L\). Thus \(\dot H_-=-r(\Phi_-/L)^2\); the stable damped mode decays while the undamped common mode survives if initially excited. This reproduces a known selection mechanism. Selective damping is a stated model assumption, and the observed apparatus must justify it.

### 4.2 Ongoing motion does not require changing total energy

A nonzero normal mode has
\(Q=A\cos\theta\), \(\Phi=-L\omega A\sin\theta\), and \(\dot\theta=\omega\), even though its total energy is constant. Consequently **net total energy change cannot universally define clock progression**.

The user's proposal may concern gross internal exchange instead. Test that separately, for example with the dimensionless accumulated activity

\[
s(t)=\frac1{E_*}\int_0^t\sum_e|P_e(v)|\,dv,
\]

where \(P_e\) is an explicitly defined transfer power, each interface is counted once, and \(E_*\) is a fixed reference energy. Compare \(s\) with measured phase/ticks across states and parameter changes. This quantity depends on the chosen decomposition, can pause, and is not automatically a universal time coordinate. A signed imbalance and gross throughput are competing interpretations, not synonyms.

This stage uses laboratory time to derive physical clock observables. It therefore investigates clock formation, not the emergence of time from a timeless theory.

### 4.3 A dissipative reset needs an energy and entropy account

For the autonomous undriven model, integrate the energy identity over a supposed full-state period \(T\):

\[
0=H(T)-H(0)=-\int_0^T\nabla H^T\mathbb R\nabla H\,dt.
\]

A periodic orbit cannot have strictly positive integrated dissipation under these assumptions. Conservative recurrence is possible; repeated dissipative restoration of the same resource requires an input or a larger accounting boundary. A finite reservoir may drive transients without returning to its initial state. This is a restriction on this model, not a no-go theorem for every cosmological cycle.

### 4.4 Interaction can also reveal hidden detail

In the conservative pair, an ideal continuous noiseless record of \(q_1(t)\), with known parameters and \(\kappa>0\), determines

\[
q_2(t)=\frac{L\ddot q_1+(1/C+\kappa)q_1}{\kappa},
\qquad \phi_i=L\dot q_i.
\]

Thus the full state is reconstructible from this ideal single-site output. At \(\kappa=0\), the second oscillator is unobservable from it. Differentiation becomes unstable with finite precision and noise, especially for weak coupling. This is a structural identifiability control, not a physically free measurement protocol. It prevents a general argument that internal coupling alone must hide detail. The actual reciprocal probe is tested separately.

## 5. Define clocks and distinguish persistent objects from averaged appearances

Extract phase only where amplitude is appreciable. Define ticks by successive phase crossings, and measure period, variability, drift, entrainment, and disturbance from reading the clock. A phase oscillator is not yet a complete clock with a durable output record. Studies of [autonomous quantum clocks](https://arxiv.org/abs/1609.06704) explicitly connect a clock's resource supply, dissipation, and performance under stated assumptions; they motivate this accounting without identifying time with energy.

There is a genuine unresolved choice in the manuscript: some passages assign a higher level a faster clock, while others motivate stability through compressed internal activity. Keep three observer parameters separate: sampling interval \(h\), integration window \(\Delta\), and instrument bandwidth.

For a centered window applied to \(q(t)=A\cos\omega t\), direct integration gives

\[
\overline q_\Delta(t)=A\,\operatorname{sinc}(\omega\Delta/2)\cos\omega t,
\qquad \operatorname{sinc}x=\sin x/x.
\]

Long integration can suppress oscillations; exact stroboscopic sampling can make motion appear constant. Faster sampling alone generally offers more opportunity to resolve motion. None of these choices creates a physical barrier by itself.

Test the stronger proposal by measuring whether collective properties remain stable under perturbations and different admissible probes. Mathematically, \(D\Pi(z)f(z)=0\) with \(f(z)\ne0\) shows that a constant macro-observable can coexist with internal motion. Choosing \(\Pi=H\) in a conservative oscillator gives an elementary example. A conserved number is not by itself a bounded material object or autonomous macroscopic dynamics. A reliable bit additionally requires distinguishable preparations, a readout rule, lifetime, and an error rate.

“Time crystallizing as space” is retained as a hypothesis about stable external structure. Establishing an actual spatial boundary requires a spatial model and a measurable boundary observable; a filtered time series or phase-space curve does not supply them.

## 6. Formulate the coherence–accessibility experiment

Freeze a target before changing coupling. A first choice is \(\Xi\): one of four equally likely initial phases of the differential mode, at fixed mode energy. The pair's common-mode state and the initial resource and probe states are fixed. These preparations have the same mode-energy summary but different microscopic phase. Specify initialization work separately. Repeat with another target later to establish whether any effect is target-specific.

Define allowed protocols \(\mathcal P(\mathcal B)\) through accessible ports, observation duration, bandwidth, integration, sampling, probe coupling bounds, calibrated noise, and preparation/control/readout work. For the complete physical record \(\mathcal R_p\),

\[
I_{\rm acc}(\mathcal B)=\sup_{p\in\mathcal P(\mathcal B)}I(\Xi;\mathcal R_p),
\qquad 0\leq I_{\rm acc}\leq2\ \text{bits}.
\]

This is a definition. Evaluating a finite collection of protocols gives achieved information values; their maximum is only a lower bound on the supremum. Numerical estimates also need uncertainty and estimator-bias checks. A theorem claiming unavoidable inaccessibility would need an upper bound valid for all allowed protocols.

At first, use the probe's calibrated charge/voltage record with additive readout noise as an explicit effective channel. State what detector physics that approximation omits. Include the probe's backaction in the dynamics even when the final recording stage is treated phenomenologically. A claim about fundamental limits requires modeling or bounding the omitted detector resources too.

Measure coherence with nonzero-amplitude phase locking, mode-energy distribution, and persistence. For two phases, \(c(t)=|e^{i\theta_1}+e^{i\theta_2}|/2\) detects in-phase alignment; it does not classify stable antiphase locking as incoherent in every sense. Also report \(|\langle e^{i(\theta_1-\theta_2)}\rangle|\), mean phase difference, and amplitude thresholds. Declare the averaging interval. Do not use a single order parameter to equate all forms of organization.

Measure disturbance using matched probed/unprobed trajectories, normalized state differences, phase shifts, and transferred energy. With noise, specify the ensemble or common-noise comparison. Report information versus disturbance and work, not merely correlation versus coupling.

The proposed relationship to test is conditional: **for a specified mechanism that increases persistent organization, do microscopic details become harder to recover through the permitted interface, at a matched resource and disturbance budget?** No monotone formula between coherence and information is imposed.

Required controls:

- Conservative coupling versus selective damping versus resource-driven interaction; these change different mechanisms.
- Fixed differential-mode energy versus fixed charge amplitude. A stiffer mode has smaller displacement at equal energy, which can explain poorer sensing without a new information barrier.
- A single-site probe versus a sum-only probe. The sum \(q_1+q_2\) cancels the differential mode by construction; that is insufficient evidence of physical inaccessibility.
- Improved bandwidth, timing, duration, and another permitted probe protocol. Determine whether an apparent barrier is a resource tradeoff, spectral mismatch, or genuine non-observability within the chosen class.
- Pair coherence before and during observation. Distinguish information erased by prior damping from information still present but inaccessible without disruption.
- Reservoir backaction and depletion. A prescribed external sinusoid cannot stand in for a finite autonomous higher clock without qualification.

Begin with analytically solvable linear response and state-observability calculations. For noisy readout of the four preparations, compute record likelihoods or controlled numerical approximations before training an inference algorithm. Use independent held-out trajectories and convergence checks. Do not introduce machine learning as a prerequisite.

## 7. Give RAM and inter-level transfer operational meanings

The first RAM candidate is the resource mode already included in \(H\). A second interpretation is redistribution between storage modes of one system: even a single oscillator alternates energy between its charge and flux terms. Both show how an internal resource can have changing availability without requiring an external “RAM space.” Oscillation phase, thermodynamic phase, and spatial location remain distinct concepts.

For each candidate measure stored energy, extractable work under allowed operations, transfer rates, and depletion. If it is also memory, separately measure information about earlier states, retention lifetime, and readout reliability. Joules are not bits. “Available for a transition” needs a specified target set and allowed dynamics; a linear oscillator has no intrinsic phase-transition threshold to discover.

To study a higher organizational level, derive a collective map \(Z_\ell=\Pi_\ell(z)\) and an effective evolution, including memory or noise when needed. Compare states sharing \(Z_\ell\) but differing internally. Predict the same external responses under the same interventions and bound the error over a specified time interval. A closed observation history is a weaker claim than a physical unit that remains autonomous under intervention. [Computational hierarchical emergence](https://arxiv.org/abs/2402.09090) provides closely related definitions to compare, rather than novelty by renaming.

Use two or three levels first, with measured coupling and frequency ratios. Coarse-graining can yield memory; consult a concrete [Mori–Zwanzig reduction study](https://arxiv.org/abs/1810.08175) before assuming Markovian macro-laws. Different levels describing the same system do not contain independent copies of its energy.

For “implosion/explosion,” first test whether the two views describe the same accounted transfer with opposite signs or a change of representation. Derive any scale-resolved energy budget from the underlying energy before assigning a current between descriptions. A persistent upward current is another claim to test: graph adjacency and level labels do not determine its direction, and a sustained directed transfer needs compatible initial conditions or a maintained drive. Specify what reverses, replenishes, or stops that current.

The eleven-level proposal remains an intended hypothesis. Keep the level count \(N\) variable and ask whether the equations select a finite depth, recurrent structure, or neither. Setting \(N=11\) reproduces a chosen architecture; it does not derive eleven. Ordinary group symmetry can organize a hierarchy, as investigated in [Rosas's symmetry preprint](https://arxiv.org/abs/2512.00984), but this neither supplies an energetic drive toward symmetry nor singles out eleven spacetime dimensions.

## 8. Execution order and decisions

| Stage | Concrete deliverable | Decision criterion |
|---|---|---|
| 0. Definitions and assumptions | Units, graph, state space, target sets, claim ledger, verbatim source record | No central word is doing incompatible mathematical jobs |
| 1. Analytical model | Pair, finite resource, reciprocal probe; energy identity; exact modes and observability | Correct balances and counterexamples before simulation |
| 2. Temporal organization | Phase/tick definitions, damping/driving comparisons, averaging and aliasing controls | Identify what produces persistent organization and what only changes a reading |
| 3. Access experiment | Fixed phase target; bounded protocol family; information, disturbance, and energy accounting | A conditional relationship survives fair controls, or a documented failure narrows it |
| 4. Physical check | A realizable small oscillator apparatus with calibrated components, detector loading and noise | Held-out measurements agree with a preregistered quantitative prediction |
| 5. Hierarchical extension | Two-level effective model, memory/error assessment, cross-level power accounting | The collective unit predicts interactions beyond a fitted summary |
| 6. Physical frontier | One explicit quantum or relativistic target with quantitative recovery criteria | Proceed only with the additional mathematical structure that target needs |

Stages 4 and 5 may exchange order if a two-level analytical result is needed to design the apparatus; choose from the results, not a fixed calendar. Nonlinearity is added only when a specified phenomenon, such as multistability or self-sustained entrainment, requires it. The fluid-rescaling result remains a methodological reference for studying scale-dependent dynamics, not evidence for this mechanism or a prerequisite for these stages. General P versus NP and human–AI implications are boundary topics.

The first publishable outcome may be a precise conditional result or counterexample. Novelty requires comparison with observability theory, synchronization, thermodynamics of clocks, and hierarchical emergence. A relabeled oscillator effect is a reproduction. Failure in this model limits this realization of the hypothesis; it neither disproves every possible realization nor justifies changing assumptions until a desired result appears.

**Current executable model:** the two-mode/resource/probe equations and deterministic controls are implemented in v0.1. The next quantitative task is its specified four-preparation observation experiment. The hierarchical extension, internal logical-certification controller, and quantum/relativistic derivations have not been executed by writing this plan.
