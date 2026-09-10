# Initial numerical controls for working model v0.1

**Run: 10 September 2026.** The [specification](SPEC.md) fixes all equations, parameters, initial conditions and controls. Reproduce with `python3 models/feedback_null_v01/run.py` from the repository root. The [report](results/baseline-report.json) records the runtime and diagnostics; the [baseline trajectory](results/baseline-trajectory.csv) contains samples every 0.1 dimensionless time unit.

These are deterministic calculations in an illustrative classical model. No physical apparatus, quantum model, autonomous logical certification algorithm, or noisy information experiment was evaluated.

## What happened

| Case | Initial total energy | Final total energy at time 100 | Maximum local pair energy | Maximum absolute meter coordinate |
|---|---:|---:|---:|---:|
| Baseline with finite resource and reciprocal meter | 0.625 | 0.1336284 | 0.3364211 | 0.6488532 |
| Meter disconnected | 0.625 | 0.3016161 | 0.4656909 | 0 |
| No damping | 0.625 | 0.6250000 | 0.4412014 | 0.9098940 |
| Global null initial state | 0 | 0 | 0 | 0 |

All quantities are in the dimensionless units defined in the specification. The first three runs start with a locally null pair and stored energy in the resource/interface. Local pair energy crosses the declared activity threshold at sampled time 0.06. This illustrates activation from a resource missing from a pair-only description; it does not illustrate creation of energy from nothing.

Attaching the meter changes the pair's trajectory and routes energy through an additional damped mode. The maximum normalized-coordinate difference between the pair with and without the meter is approximately 0.70565 in the specified Euclidean metric. This is a loading/backaction effect in the selected circuit analogue; it does not establish a quantum measurement tradeoff.

The ideal noiseless meter-output observability matrix has numerical rank eight at the declared baseline parameters. Thus this model gives no structural information barrier in the ideal continuous, known-parameter limit. Finite duration, noise, sampling, conditioning and the allowed probe resources still matter. The specified four-preparation task is needed to evaluate achieved information in a restricted observation protocol; it has not yet been run.

## What did not happen

The global null state remained exactly zero in the numerical control, as the equations require. No nonzero trajectory satisfied the local-completion threshold for the required hold interval and subsequently restarted during this observation window. The threshold was fixed at local energy 0.0001 and the hold interval at one time unit; these are diagnostic choices, not universal definitions of completion.

The damped baseline's dynamics matrix has all eigenvalues with negative real part (largest approximately -0.005096). For these fixed parameters, its eventual behavior is decay toward zero, although finite-time exchange and oscillations occur. The conservative control retains energy and ongoing oscillations, using the supplied initial energy. Neither supplies the proposed inevitable completion/reset cycle or an origin of time.

The absence of the desired recurrence is a result for this realization. The next extension must identify a physical reason for any added controller, nonlinearity, delay, or maintained drive. An imposed toggle or reset would be an assumption and must be described as such.

## Numerical checks

- Maximum baseline error in total energy plus accumulated dissipation: approximately **4.54 × 10⁻¹¹**.
- Maximum conservative total-energy drift: approximately **2.40 × 10⁻¹⁰**.
- Maximum change in state or accumulated dissipation when the integration step is halved: approximately **1.34 × 10⁻⁸** over the full trajectory.
- Maximum residual in the independently evaluated local boundary-power identity: approximately **4.17 × 10⁻¹⁷**.
- The disconnected meter remains at zero; the global-null run remains zero; cumulative dissipation is nondecreasing.

These checks support numerical consistency for the stated runs. They do not establish a general theorem, scientific novelty, or the broader research hypothesis. The trajectory CSV is rounded for portability; reported errors are calculated from the internal full-precision arrays.

## Next use of this model

The explicit four-preparation measurement task in [SPEC.md](SPEC.md#6-a-completely-specified-first-information-task-ready-for-a-separate-run) supplies the next quantitative baseline. Its hypotheses, initial energy, observation times, noise law, likelihood, and optimal decoder are fixed. Then compare coupling and disturbance under the controls in the [mathematical scope](../../mathematical-plan-feedback-energy-clocks.md).

To investigate the stronger self-reference proposal, add a finite physical controller with a specified certification target that includes or excludes its own record. Its states, energy, coupling, update rule and completion predicate must be given before testing whether attempted certification regenerates a residual. The existing reciprocal analog meter does not by itself implement that logical task.
