# Hierarchical Computation Research

**Founding scope:** v1. **Current direction:** reassessed on 10 September 2026.

**Provenance marker:** `DORIAN_X10::HCT-SKELETON::2026-09-08::V1`

This repository records a research program developed from the hypothesis that internal feedback can organize components into collective units, with characteristic timing and constrained but useful access to their internal details. It investigates the proposed relation among asymmetry, energy exchange, clocks, and interacting observation, and whether that relation can recur across levels of organization.

**Start with the [mathematical scope](mathematical-plan-feedback-energy-clocks.md) and [active execution plan](NEXT-STEPS.md).** Following the user's latest manuscript, the current priority is a small energy-consistent oscillator model with a finite internal resource and an interacting probe. The [scientific reassessment](research-audit-2026-09-10.md) retains its evidence corrections; the earlier predictive-compression benchmark is now an optional calibration. The broad physical hypotheses remain unvalidated, with no claim of a new theorem or experimental discovery.

The [original research intention](RESEARCH-INTENT.md) places that benchmark within a broader hypothesis: internal feedback, coherent organization and scale-relative uncertainty may be related across the user's proposed eleven-dimensional structure. Investigating a possible connection to quantum uncertainty is an explicit medium- to long-term objective; it has not yet been derived.

The first version is a disciplined program of work rather than a completed theory. Its central questions are:

- When does a coarse-graining map produce a closed or approximately closed effective dynamics?
- How do unresolved fluctuations reappear as effective stress, memory, noise, or feedback?
- Can asymmetry, timing, and self-reference be expressed as testable mathematical structures?
- What can rescaled dynamical systems and finite-time concentration teach us about hierarchical organization?
- Which claims survive formal proof, simulation, and physical measurement?

## Contents

- [`RESEARCH-INTENT.md`](RESEARCH-INTENT.md): the user's clarified physical motivation and its relationship to the narrower first experiments.
- [`research-audit-2026-09-10.md`](research-audit-2026-09-10.md): evidence audit, corrections, source comparison, and the status of each hypothesis.
- [`novelty-review-2026-09-10.md`](novelty-review-2026-09-10.md): nearest prior work, an elementary exact calculation, and candidate contributions whose novelty remains to be established.
- [`NEXT-STEPS.md`](NEXT-STEPS.md): the current order of work, deliverables, and decision criteria.
- [`mathematical-plan-feedback-energy-clocks.md`](mathematical-plan-feedback-energy-clocks.md): definitions of asymmetry, potential, completion, clocks and RAM; energy-consistent equations; observer experiment; analytical controls.
- [`physics-frontier-assessment-2026-09-10.md`](physics-frontier-assessment-2026-09-10.md): specific quantum/relativistic intersections and a qualitative assessment of present evidence.
- [`claim-ledger-feedback-energy-clocks.md`](claim-ledger-feedback-energy-clocks.md): assumptions, deductions, physical hypotheses, and conditions for revising them.
- [`manuscripts/README.md`](manuscripts/README.md): the preservation record for the user's latest verbatim manuscript, which is retained locally.
- [`archive/predictive-benchmark-plan-2026-09-10.md`](archive/predictive-benchmark-plan-2026-09-10.md): the previous finite-state benchmark plan, retained as an optional study.
- [`audit/check_energy_clock_controls.py`](audit/check_energy_clock_controls.py): exact rational spot checks of elementary mode, energy-balance, and observability calculations.
- [`audit/check_sanity.py`](audit/check_sanity.py) and [`audit/sanity-results.json`](audit/sanity-results.json): reproducible elementary closure, memory, sampling, and quadratic-averaging controls.
- [`scope-hierarchical-computation-v1.tex`](scope-hierarchical-computation-v1.tex): the LaTeX edition, with numbered equations, the seven hypotheses, research-effort tables, notation clarifications, and a P versus NP appendix.
- [Compiled scope PDF](output/pdf/scope-hierarchical-computation-v1.pdf): the typeset reading edition.
- [`scope-build.md`](scope-build.md): compilation and verification instructions.
- [`research-program-hierarchical-computation.md`](research-program-hierarchical-computation.md): the historical v1 research plan, including the Navier–Stokes intersection and earlier workstream weights; read the reassessment for current priorities and corrections.
- [`provenance-dorian-x10-hct-skeleton-v1.json`](provenance-dorian-x10-hct-skeleton-v1.json): a machine-readable version marker and SHA-256 record.
- [`ORIGIN.md`](ORIGIN.md): source and attribution context for this public v1 release.

The founding Markdown plan is preserved. The September 9 LaTeX edition adds explicitly labeled clarifications and the subsequent P versus NP discussion. Neither typesetting nor those additions constitute an independent verification of the external fluid proof or new experimental results. The original `v1` and `scope-v1` tags retain their original contents; consult `main` for the current edition.

## Current scientific boundary

The working hypothesis is exploratory. The repository does not claim that fluid turbulence, consciousness, quantum theory, computation, or cosmology have already been unified. Established results and proposed extensions are marked separately in the plan. In particular, a Navier–Stokes construction showing finite-time blow-up under carefully designed forcing is evidence about what the equations permit under stated hypotheses; it is not evidence that generic physical fluids or unforced fluids must blow up.

## Attribution and provenance

The public source account associated with this hypothesis is [@dorian_x10](https://x.com/dorian_x10). The marker above is intended to make this version easy to identify and cite. A marker and a hash support public version tracking; they do not independently prove identity, ownership, or priority.

## Suggested next step

Specify and derive the two-mode/resource/probe model in the [active plan](NEXT-STEPS.md#next-deliverable-the-smallest-inspectable-physical-model). Establish energy accounting, clocks, and observer response before testing the proposed coherence–accessibility relation. Reproduce the elementary new controls with `python3 audit/check_energy_clock_controls.py`; the older prediction controls remain available with `python3 audit/check_sanity.py`.
