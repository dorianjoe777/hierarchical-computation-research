"""Check the novelty review's elementary closure formula by exact enumeration.

Run: python3 audit/check_boundary_closure.py
This is a reproduction of the classical lumpability criterion in our model.
It does not execute the full forecast/memory benchmark.
"""

from fractions import Fraction as F
from itertools import product

from check_sanity import closure_defect


def transition_matrix(coupling, noise):
    states = list(product((0, 1), repeat=3))
    index = {state: i for i, state in enumerate(states)}
    kernel = [[F(0) for _ in states] for _ in states]
    for i, (a, b, c) in enumerate(states):
        for gate, na, nb, nc in product((0, 1), repeat=4):
            probability = coupling if gate else 1 - coupling
            for flip in (na, nb, nc):
                probability *= noise if flip else 1 - noise
            target = (b ^ na, a ^ c ^ nb, (b if gate else c) ^ nc)
            kernel[i][index[target]] += probability
        assert sum(kernel[i]) == 1
        assert all(p >= 0 for p in kernel[i])
    return kernel, [c for _, _, c in states]


def main():
    count = 0
    for coupling, noise in product(
        (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)),
        (F(1, 32), F(1, 8), F(1, 4), F(1, 2)),
    ):
        kernel, projection = transition_matrix(coupling, noise)
        enumerated = closure_defect(kernel, projection)
        expected = coupling * abs(1 - 2 * noise)
        assert enumerated == expected, (coupling, noise, enumerated, expected)
        count += 1
    print(f"All {count} parameter pairs passed with exact rational arithmetic.")
    print("Verified: closure_defect = coupling * abs(1 - 2 * noise).")
    print("This elementary calculation is not a claim of scientific novelty.")


if __name__ == "__main__":
    main()
