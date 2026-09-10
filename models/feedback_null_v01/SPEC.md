# Working model v0.1: null states, feedback, measurement, and finite resources

**10 September 2026.** This is a fully specified initial-value model that can be calculated and run. It translates the user's visualization into candidate mathematical and physical counterparts. It is a classical analogue, with explicit limits; it does not identify physical null states with absolute nonexistence or claim to explain the origin of the universe.

The [foundations overview](../../FOUNDATIONS-OVERVIEW.md) gives the research context. The [translation of the self-reference frontier](../../self-reference-frontier-2026-09-10.md) distinguishes logical self-certification from physical feedback. This specification supplies a concrete starting model instead of leaving those terms only as philosophical descriptions.

## 1. All variables, units and parameters

The system contains two local modes, one internal resource mode, and one meter mode. Their fixed interaction graph has edges \(1\leftrightarrow2\), \(1\leftrightarrow r\), and \(1\leftrightarrow m\). Internal coordinates change while graph adjacency remains fixed.

Start from charge/flux variables and positive reference capacitance \(C_*\), inductance \(L_*\), and energy \(E_*\). Use

\[
t_*=\sqrt{L_*C_*},\quad q_*=\sqrt{C_*E_*},\quad
\phi_*=\sqrt{L_*E_*},\qquad \tau=t/t_*.
\]

Every coordinate below is dimensionless charge or flux divided by its reference. Every mode uses the reference capacitance and inductance. The full state is

\[
z=(q_1,q_2,r,m,p_1,p_2,p_r,p_m)^T\in\mathbb R^8.
\]

The meter coordinate \(m\) is a finite-energy analog record of its interaction with unit 1. It is part of the system and influences that unit in return. A general-purpose internal algorithm that reasons about its own certificate is not represented by this single analog coordinate; that distinction must be retained when interpreting results.

Parameters are fixed before the runs:

\[
\kappa=0.8,\qquad \rho=0.25,\qquad \eta=0.2,
\qquad (\gamma_1,\gamma_2,\gamma_r,\gamma_m)=(0.01,0.01,0.005,0.04).
\]

The three couplings are dimensionless inverse-capacitance coefficients; a physical coefficient is the dimensionless value divided by \(C_*\). The \(\gamma_i\) are dimensionless damping rates in the equations below. These numbers are illustrative choices, not fitted constants of nature or a proposed universal hierarchy.

## 2. Null state, energy, asymmetry, and potential

Define the nonnegative dimensionless stored energy

\[
\mathcal H(z)=\tfrac12\sum_{i\in\{1,2,r,m\}}(q_i^2+p_i^2)
 +\tfrac\kappa2(q_1-q_2)^2
 +\tfrac\rho2(q_1-r)^2
 +\tfrac\eta2(q_1-m)^2,
\]

where \(q_r=r\) and \(q_m=m\). Physical energy is \(E_*\mathcal H\). All terms are nonnegative and

\[
\mathcal H(z)\geq\tfrac12\|z\|^2,\qquad
\boxed{\mathcal H=0\iff z=0.}
\]

Thus **0 is the model's global null state**, a precise reference state. It is still a state in an existing mathematical model. It does not mean that state space, laws, or reference structure cease to exist.

Local energy and local asymmetry are

\[
E_{12}=\tfrac12(q_1^2+q_2^2+p_1^2+p_2^2)
 +\tfrac\kappa2(q_1-q_2)^2,
\qquad A=(q_1-q_2)^2+(p_1-p_2)^2.
\]

Local nullity \(E_{12}=0\) does not imply global nullity: resource, meter, or interface energy may remain. Local symmetry \(A=0\) also permits an active common oscillation, so symmetry, quiescence and nonexistence cannot be identified by one zero.

“Potential” receives three explicit counterparts: stored energy \(\mathcal H\); the coordinate-dependent potential \(V=\mathcal H-\sum_i p_i^2/2\); and the reachable states from an initial condition under the declared dynamics. This initial undriven model has no freely selectable control inputs. Thermodynamic available work requires an additional protocol and reservoir specification.

For \(\mathcal H(0)>0\), define local energy occupancy \(f=E_{12}/\mathcal H(0)\). It lies between 0 and 1 here. This is one candidate for “fullness”; it is not informational completeness or maximum symmetry. Neither \(f=1\) nor a preferred final stage is guaranteed to be reachable.

## 3. The complete dynamics

There is no external drive, no noise, and no imposed restart:

\[
\begin{aligned}
\dot q_1&=p_1,&\dot q_2&=p_2,&\dot r&=p_r,&\dot m&=p_m,\\
\dot p_1&=-(1+\kappa+\rho+\eta)q_1+\kappa q_2+\rho r+\eta m-\gamma_1p_1,\\
\dot p_2&=\kappa q_1-(1+\kappa)q_2-\gamma_2p_2,\\
\dot p_r&=\rho q_1-(1+\rho)r-\gamma_rp_r,\\
\dot p_m&=\eta q_1-(1+\eta)m-\gamma_mp_m.
\end{aligned}
\]

Dots mean derivatives with respect to \(\tau\). These are linear ordinary differential equations \(\dot z=Mz\); they have a unique solution for every initial state and finite time. They instantiate the earlier energy-based model without unspecified evolution functions.

The balance follows by differentiation:

\[
\frac{d\mathcal H}{d\tau}=-\mathcal D,
\qquad \mathcal D=\gamma_1p_1^2+\gamma_2p_2^2+\gamma_rp_r^2+\gamma_mp_m^2.
\]

Define dissipated energy \(Q(\tau)=\int_0^\tau\mathcal D(s)ds\). Then \(\mathcal H+Q=\mathcal H(0)\). Damping represents energy leaving the eight-mode description into an unmodeled passive environment; \(Q\) records that transfer. The model is undriven but thermodynamically open when damping is nonzero. No equilibrium thermal-noise claim is made.

Energy entering the local pair through its declared boundary obeys

\[
\frac{dE_{12}}{d\tau}
=\underbrace{\rho(r-q_1)p_1}_{P_{r\to12}}
 +\underbrace{\eta(m-q_1)p_1}_{P_{m\to12}}
 -\gamma_1p_1^2-\gamma_2p_2^2.
\]

These are powers across the chosen pair boundary. Their opposites need not equal the instantaneous change of the bare auxiliary-mode energies: the interfaces also store energy. All three coupling energies remain in \(\mathcal H\).

The pair can become active from local zero if an auxiliary mode initially stores energy. Conversely, at global zero every derivative is zero. The model therefore permits **locally unobserved resources driving activity**, but predicts no spontaneous departure from its global null state. Adding fluctuations or a drive would change assumptions and require their physical accounting.

## 4. Mathematical counterparts of the visualization

| Visualization | Explicit counterpart in v0.1 | Interpretation/test |
|---|---|---|
| Nonexistence / emptiness | Global \(z=0\), or a separately named local null set \(E_{12}=0\) | These have different dynamical consequences |
| Fullness | Local energy occupancy \(f\); alternatively a defined information criterion in §6 | Do not switch meanings during an argument |
| Asymmetry | \(A\), relative to exchange of the local units | Calculate its derivative; monotone decay is not imposed |
| Internal coherence | Common/differential mode energies and phase organization | Persistence and nonzero amplitude must accompany a high score |
| Fixed transistor with internal rotation | Fixed graph with rotating charge/flux coordinates | Internal phase-space motion does not change graph neighbors |
| RAM / hidden resource | \((r,p_r)\), its stored energy, and its boundary power | Finite internal storage; no new substance is asserted |
| Measurement / analog memory | \((m,p_m)\), with output \(y=m\) | A dynamically filtered, disturbing sensor, not perfect access to the full state |
| Self-involving feedback | \(q_1\) affects \(m\), which affects \(q_1\); the meter belongs to the whole being described | A physical analogue; logical self-certification requires an explicit further target/controller |
| Mask / phantom boundary | Meter response \(y\) and interface energy \(B_m=\eta(q_1-m)^2/2\) | Measurable boundary activity, not an established spacetime surface |
| Failed measurement | Tracking residual \(e=q_1-m\), or target inference loss in §6 | Tracking error is not quantum uncertainty |
| Implosion/explosion | Signed boundary powers and redistribution among mode energies | Opposite descriptions must use the same energy account |
| Completion | Entry into a declared target for a hold interval; use thresholds below | A local threshold can be left again through accounted coupling |
| Renewed activity | Later exit from the local completion set | Measured from trajectories, never forced by a reset command |
| Clock | Phase and positive-going zero crossings of an active collective coordinate | Physical rate comes from the dynamics and the reference scale |
| Time as accumulated unresolved activity | Compare clock events with integrated tracking residual and gross energy throughput | This is a hypothesis test, not a definition equating them |
| Higher stable object | A collective observable with persistence under admissible probing | A small or averaged output alone does not establish such an object |
| Eleven levels | Future variable-depth hierarchy \(N\), with \(N=11\) a candidate | Eight state coordinates here are not eight organizational levels or spacetime dimensions |

For the local pair, let \(Q_\pm=(q_1\pm q_2)/\sqrt2\), \(P_\pm=(p_1\pm p_2)/\sqrt2\). Define

\[
E_+=\tfrac12(P_+^2+Q_+^2),\quad
E_-=\tfrac12[P_-^2+(1+2\kappa)Q_-^2],\qquad
c=E_+/(E_++E_-).
\]

Here \(E_++E_-=E_{12}\). The score \(c\) measures common-mode energy fraction, not all forms of coherence. It is undefined at local zero, and is used only above an activity threshold. With auxiliaries attached these are useful coordinates, not independent normal modes of the entire system.

Use \(\varepsilon=10^{-4}\) and a hold interval of 1 dimensionless time unit for the initial local-completion diagnostic. Define a certificate in the data analysis only after observing the full hold interval; it cannot claim future persistence. The internal meter alone is not assumed to know \(E_{12}\). An autonomous certificate-producing controller remains a separately specified extension.

Define the collective phase \(\theta=\operatorname{atan2}(-P_+,Q_+)\) where its amplitude is nonzero; it need not increase uniformly with the auxiliary couplings. Use observable positive-going \(Q_+=0\) crossings with an amplitude threshold for the initial event counter. An event counter is not a proof of clock accuracy or of time's origin.

For candidate carga-tiempo diagnostics, compare event times with

\[
S_E(\tau)=\int_0^\tau(|P_{r\to12}|+|P_{m\to12}|)ds,
\qquad S_e(\tau)=\int_0^\tau e(s)^2ds.
\]

The first is a dimensionless transferred-energy measure for this boundary; the second is an integrated normalized tracking residual. Their units and physical meanings differ. Similar-looking curves would not establish an identity. Neither supplies a universal upward direction or explains the preexisting parameter \(\tau\).

## 5. Initial conditions and executable controls

The initial demonstration uses

\[
z(0)=(0,0,1,0,0,0,0,0),\qquad \mathcal H(0)=(1+\rho)/2=0.625.
\]

The pair initially has zero local energy; the resource and its interface contain all initial energy. Run four declared cases to \(\tau=100\): baseline, meter disconnected (\(\eta=0\)), all damping removed, and global null initialization. Use fourth-order Runge–Kutta with step 0.01, and repeat the baseline with step 0.005 to check numerical convergence.

The executable checks null-state invariance, the energy-plus-dissipation budget, conservative energy conservation, the meter's response, the local-power identity, and agreement between step sizes. It reports local-completion intervals rather than assuming they recur. Trajectories, diagnostics and a report are written under `results/`.

Run from the repository root:

```sh
python3 models/feedback_null_v01/run.py
```

Requires Python 3 and NumPy; [requirements.txt](requirements.txt) pins the NumPy version used, and the report records the runtime. These are baseline consistency checks of a selected analogue. They are not a test of quantum uncertainty, a derivation of all hierarchy levels, or evidence for a cosmic origin. See [RESULTS.md](RESULTS.md) for the recorded outcome and limitations.

## 6. A completely specified first information task, ready for a separate run

To test accessible detail, retain the same dynamics but prepare one of four equally likely initial vectors:

\[
v_0=(1,-1,0,0,0,0,0,0),\quad
v_1=(0,0,0,0,1,-1,0,0),\quad v_2=-v_0,\quad v_3=-v_1,
\]

\[
z_j(0)=\sqrt{E_0/\mathcal H(v_j)}\,v_j,\qquad E_0=0.625.
\]

The target is the preparation label \(\Xi\in\{0,1,2,3\}\). These four preparations have equal total modeled energy. They differ from the resource-initialized control in §5 and are not mixed with it.

Record \(Y_k=m(0.1k)+\sigma\xi_k\), \(k=1,\ldots,200\), with \(\sigma=0.01\) and independent standard normal \(\xi_k\). This is an explicitly idealized readout-noise channel; physical costs of the final logger are not derived by the oscillator model. Meter backaction itself remains in the dynamics.

For a record \(Y\), the exactly specified likelihood is

\[
p(Y\mid j)=(2\pi\sigma^2)^{-100}
\exp\left[-\frac1{2\sigma^2}\sum_{k=1}^{200}(Y_k-m_j(0.1k))^2\right].
\]

With the uniform prior, Bayes' rule fixes the optimal preparation decoder. Define the actual task uncertainty as \(H(\Xi\mid Y)\) and achieved information as \(2-H(\Xi\mid Y)\) bits. Information is not identified with \(e^2\), energy, or \(A\). Compute this task separately after reviewing the baseline trajectories; the current executable does not claim to have run this inference experiment.

A later coupling comparison needs fixed observation resources, amplitude controls, and apparatus-loading accounting from the larger mathematical scope. No finite set of tested protocols proves a universal information barrier.

## 7. Exactly what remains to be derived

This v0.1 fixes the state space, equations, energy account, null/completion definitions, boundary observables, clock candidates, initial conditions, solver controls, and one future information task. It is a complete working analogue at that scope.

An internal logical self-certification algorithm, nonlinear sustained cycles, emergent spatial geometry, a preferred eleven-level structure, and quantum laws are not implemented by naming their analogues. Each needs a further explicit model or derivation. The baseline is intentionally able to settle, retain predictable detail, or leave a locally quiet state using finite stored energy. Those outcomes are part of testing the visualization faithfully.
