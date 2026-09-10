"""Exact rational checks of elementary controls in the mathematical scope.

Run from the repository root: python3 audit/check_energy_clock_controls.py
Uses only the Python standard library. Prints a report; does not modify files.
These are finite algebraic spot checks, not simulations, general proofs,
physical experiments, or evidence that the research hypothesis is true.
"""

import json
from fractions import Fraction as F
from itertools import product


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def mv(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def determinant(a):
    a = [list(row) for row in a]
    result = F(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            result = -result
        value = a[i][i]
        result *= value
        for j in range(i + 1, len(a)):
            ratio = a[j][i] / value
            for k in range(i + 1, len(a)):
                a[j][k] -= ratio * a[i][k]
            a[j][i] = F(0)
    return result


def matrices(capacitances, inductances, edges, damping=None):
    """H=z^T K z/2 with charge-difference couplings; A=(J-R)K."""
    n = len(capacitances)
    size = 2 * n
    k = [[F(0) for _ in range(size)] for _ in range(size)]
    j = [[F(0) for _ in range(size)] for _ in range(size)]
    r = damping or [[F(0) for _ in range(size)] for _ in range(size)]
    for i in range(n):
        k[i][i] = 1 / capacitances[i]
        k[n+i][n+i] = 1 / inductances[i]
        j[i][n+i], j[n+i][i] = F(1), F(-1)
    for i, h, coupling in edges:
        k[i][i] += coupling
        k[h][h] += coupling
        k[i][h] -= coupling
        k[h][i] -= coupling
    a = multiply([[j[i][h] - r[i][h] for h in range(size)]
                  for i in range(size)], k)
    return k, a, r


def check_balance(k, a, r):
    left1 = multiply(transpose(a), k)
    left2 = multiply(k, a)
    krk = multiply(multiply(k, r), k)
    for i, h in product(range(len(k)), repeat=2):
        assert left1[i][h] + left2[i][h] == -2 * krk[i][h]


def main():
    # State coordinates are q1,q2,phi1,phi2, in consistent chosen units.
    states = [(F(1), F(2), F(-1), F(3)),
              (F(0), F(1), F(2), F(-2)),
              (F(3, 2), F(-1, 3), F(2, 5), F(1, 7))]
    pairs = 0
    for c, l, coupling in product((F(1), F(2)), (F(1), F(3)),
                                  (F(0), F(1, 4), F(1), F(4))):
        k, a, r = matrices([c, c], [l, l], [(0, 1, coupling)])
        check_balance(k, a, r)
        a2 = multiply(a, a)
        for sign, omega2 in ((1, 1/(l*c)),
                             (-1, (1/c + 2*coupling)/l)):
            for v in ([F(1), F(sign), F(0), F(0)],
                      [F(0), F(0), F(1), F(sign)]):
                assert mv(a2, v) == [-omega2*x for x in v]

        row = [[F(1), F(0), F(0), F(0)]]
        obs = []
        for _ in range(4):
            obs.append(row[0])
            row = multiply(row, a)
        assert determinant(obs) == -coupling**2/l**4

        damp = [[F(0) for _ in range(4)] for _ in range(4)]
        rate = F(2, 3)
        damp[2][2] = damp[3][3] = rate/2
        damp[2][3] = damp[3][2] = -rate/2
        kd, ad, rd = matrices([c, c], [l, l], [(0, 1, coupling)], damp)
        check_balance(kd, ad, rd)
        for z in states:
            q1, q2, p1, p2 = z
            total = sum(x*y for x, y in zip(z, mv(k, z)))/2
            common = (p1+p2)**2/(4*l) + (q1+q2)**2/(4*c)
            differential = ((p1-p2)**2/(4*l)
                            + (1/c + 2*coupling)*(q1-q2)**2/4)
            assert total == common + differential
            grad_minus = [(1/c + 2*coupling)*(q1-q2)/2,
                          -(1/c + 2*coupling)*(q1-q2)/2,
                          (p1-p2)/(2*l), -(p1-p2)/(2*l)]
            assert sum(x*y for x, y in zip(grad_minus, mv(a, z))) == 0
            assert sum(x*y for x, y in zip(grad_minus, mv(ad, z))) == (
                -rate*(p1-p2)**2/(2*l**2))
            if coupling:
                reconstructed = (l*mv(a2, z)[0] + (1/c + coupling)*q1)/coupling
                assert reconstructed == q2
        pairs += 1

    # Four-mode pair/resource/probe: reciprocal gradients and energy balance.
    n = 8
    damp4 = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(4, 8):
        damp4[i][i] = F(i-3, 10)
    k, a, r = matrices([F(1), F(1), F(2), F(3)],
                       [F(2), F(2), F(3), F(4)],
                       [(0, 1, F(1, 2)), (0, 2, F(1, 3)),
                        (0, 3, F(1, 5))], damp4)
    check_balance(k, a, r)
    assert k[0][2] == k[2][0] == -F(1, 3)
    assert k[0][3] == k[3][0] == -F(1, 5)
    print(json.dumps({
        "status": "passed",
        "arithmetic": "exact rational",
        "pair_parameter_fixtures": pairs,
        "state_fixtures_per_pair": len(states),
        "four_mode_balance_fixtures": 1,
        "observability_determinant": "-kappa^2/L^4",
        "checked": ["quadratic energy balance", "normal-mode frequencies",
                    "mode energy decomposition and conservation",
                    "selective damping energy decay", "single-site reconstruction",
                    "reciprocal resource and probe coupling"],
        "limits": "Algebraic spot checks only; no noisy observer experiment or physical validation."
    }, indent=2))


if __name__ == "__main__":
    main()
