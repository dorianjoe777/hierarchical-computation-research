"""Exact finite controls for the research audit; these are established examples.

Run from the repository root:
    python3 audit/check_sanity.py

Probabilities and closure defects use rational arithmetic. Entropies use log2;
the controls here have exact integer entropy values, checked below.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import isclose, log2
import json


def closure_defect(kernel, projection):
    """Maximum total-variation distance between block rows in the same block."""
    labels = sorted(set(projection))
    rows = [
        [sum((row[j] for j, label in enumerate(projection) if label == b), F(0))
         for b in labels]
        for row in kernel
    ]
    return max(
        sum((abs(a - b) for a, b in zip(rows[i], rows[j])), F(0)) / 2
        for i, j in product(range(len(kernel)), repeat=2)
        if projection[i] == projection[j]
    )


def entropy(probabilities):
    return sum(-float(p) * log2(float(p)) for p in probabilities if p)


def conditional_entropy(joint):
    """joint[(predictor_state, target)] is the joint probability."""
    masses = defaultdict(F)
    for (state, _), probability in joint.items():
        masses[state] += probability
    # Conditional form avoids subtracting two almost equal entropies.
    return sum(
        -float(p) * log2(float(p / masses[state]))
        for (state, _), p in joint.items() if p
    )


def bayes_error(joint):
    """Minimum target classification error from this predictor state alone."""
    best = defaultdict(F)
    for (state, _), p in joint.items():
        best[state] = max(best[state], p)
    return F(1) - sum(best.values(), F(0))


def inspect_cycle(projection, stride):
    n = 4
    kernel = [[F(int(j == (i + stride) % n)) for j in range(n)] for i in range(n)]
    current_joint = defaultdict(F)
    history_joint = defaultdict(F)
    macro_mass = defaultdict(F)
    history_mass = defaultdict(F)
    for previous_x in range(n):
        current_x = (previous_x + stride) % n
        next_x = (current_x + stride) % n
        previous, current, target = (projection[x] for x in (previous_x, current_x, next_x))
        current_joint[(current, target)] += F(1, n)
        history_joint[((previous, current), target)] += F(1, n)
        macro_mass[current] += F(1, n)
        history_mass[(previous, current)] += F(1, n)
    h_current = conditional_entropy(current_joint)
    h_history = conditional_entropy(history_joint)
    return {
        "projection": projection,
        "sampling_stride": stride,
        "initial_law": "uniform on the four microstates (stationary)",
        "closure_defect_tv": str(closure_defect(kernel, projection)),
        "next_given_current_entropy_bits": h_current,
        "next_given_previous_and_current_entropy_bits": h_history,
        "conditional_memory_information_bits": h_current - h_history,
        "current_only_bayes_error": str(bayes_error(current_joint)),
        "one_lag_bayes_error": str(bayes_error(history_joint)),
        "current_state_entropy_bits": entropy(macro_mass.values()),
        "two_observation_state_entropy_bits": entropy(history_mass.values()),
        "microstate_entropy_bits": 2,
    }


def main():
    parity = inspect_cycle([0, 1, 0, 1], 1)
    hidden_phase = inspect_cycle([0, 0, 1, 1], 1)
    slower = inspect_cycle([0, 0, 1, 1], 2)
    assert parity["closure_defect_tv"] == "0"
    assert isclose(parity["next_given_current_entropy_bits"], 0, abs_tol=1e-12)
    assert hidden_phase["closure_defect_tv"] == "1"
    assert hidden_phase["current_only_bayes_error"] == "1/2"
    assert hidden_phase["one_lag_bayes_error"] == "0"
    assert isclose(hidden_phase["conditional_memory_information_bits"], 1, abs_tol=1e-12)
    assert isclose(hidden_phase["two_observation_state_entropy_bits"], 2, abs_tol=1e-12)
    assert slower["closure_defect_tv"] == "0"
    assert isclose(slower["next_given_current_entropy_bits"], 0, abs_tol=1e-12)

    fluctuations = [F(-1), F(1)]
    mean = sum(fluctuations) / len(fluctuations)
    second_moment = sum(w * w for w in fluctuations) / len(fluctuations)
    assert mean == 0 and second_moment == 1
    print(json.dumps({
        "status": "All analytical controls passed; no new scientific result claimed.",
        "cycle_rule": "X[t+1] = (X[t] + 1) mod 4",
        "controls": {"parity": parity, "hidden_phase": hidden_phase, "slower_sampling": slower},
        "zero_mean_control": {"mean": str(mean), "second_moment": str(second_moment)},
        "limitations": [
            "Parity and paired states are different observables; their scores are not a same-task comparison.",
            "Stride two changes the prediction horizon and skips intermediate observations.",
            "One-lag memory in the paired-state control recovers all two bits of the microstate.",
            "These calculations establish neither a new law nor a physical energy or complexity bound."
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
