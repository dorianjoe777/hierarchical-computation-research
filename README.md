# Hierarchical Computation Research

**Founding scope:** v1. **Current direction:** reassessed on 10 September 2026.

**Provenance marker:** `DORIAN_X10::HCT-SKELETON::2026-09-08::V1`

This repository records a research program developed from the hypothesis that complex systems may implement computation through interacting levels of description. The program studies whether coarse-grained states can preserve mathematically useful information about finer-scale dynamics, and whether repeated rescaling can turn apparent physical complexity into a simpler trajectory in scale/state space.

**Start with the [scientific reassessment](research-audit-2026-09-10.md) and [active execution plan](NEXT-STEPS.md).** They supersede the original effort weights and seven-day schedule. The current priority is a finite-state study of predictive coarse-graining, retained memory, and sampling cost. The broad physical hypotheses remain unvalidated; the repository now includes small exact controls, with no claim of a new theorem or experimental discovery.

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
- [`NEXT-STEPS.md`](NEXT-STEPS.md): the active finite-model specification and milestones, baselines, and stopping rules.
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

Derive the eight-state transition table and freeze the boundary-prediction task in [Milestone 1](NEXT-STEPS.md#milestone-1--freeze-one-model-and-one-task). Then establish exact prediction/storage baselines before extending the model. Reproduce the completed audit controls with `python3 audit/check_sanity.py`.
