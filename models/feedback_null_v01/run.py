"""Run the fully specified classical analogue in SPEC.md.

Requires NumPy. Writes deterministic baseline/control diagnostics and a sampled
baseline trajectory. No inference experiment, quantum model, or autonomous
logical certificate is implemented by these consistency checks.
"""

import csv
import json
import platform
from dataclasses import asdict, dataclass, replace
from pathlib import Path

import numpy as np


@dataclass(frozen=True)
class Parameters:
    kappa: float = 0.8
    rho: float = 0.25
    eta: float = 0.2
    gamma: tuple = (0.01, 0.01, 0.005, 0.04)


def stiffness(p):
    k = np.eye(4)
    for j, coefficient in ((1, p.kappa), (2, p.rho), (3, p.eta)):
        k[0, 0] += coefficient
        k[j, j] += coefficient
        k[0, j] -= coefficient
        k[j, 0] -= coefficient
    return k


def dynamics_matrix(p):
    return np.block([[np.zeros((4, 4)), np.eye(4)],
                     [-stiffness(p), -np.diag(p.gamma)]])


def diagnostics(z, p):
    q, momentum = z[..., :4], z[..., 4:8]
    bare = np.sum(q*q + momentum*momentum, axis=-1)/2
    internal = p.kappa*(q[..., 0]-q[..., 1])**2/2
    resource_interface = p.rho*(q[..., 0]-q[..., 2])**2/2
    meter_interface = p.eta*(q[..., 0]-q[..., 3])**2/2
    energy = bare + internal + resource_interface + meter_interface
    pair = np.sum(q[..., :2]**2 + momentum[..., :2]**2, axis=-1)/2 + internal
    resource_power = p.rho*(q[..., 2]-q[..., 0])*momentum[..., 0]
    meter_power = p.eta*(q[..., 3]-q[..., 0])*momentum[..., 0]
    dissipation = np.sum(np.asarray(p.gamma)*momentum**2, axis=-1)
    qplus = (q[..., 0]+q[..., 1])/np.sqrt(2)
    pplus = (momentum[..., 0]+momentum[..., 1])/np.sqrt(2)
    eplus = (qplus**2 + pplus**2)/2
    asymmetry = (q[..., 0]-q[..., 1])**2 + (momentum[..., 0]-momentum[..., 1])**2
    return dict(energy=energy, pair=pair, resource_power=resource_power,
                meter_power=meter_power, dissipation=dissipation,
                qplus=qplus, pplus=pplus, eplus=eplus, asymmetry=asymmetry,
                meter_interface=meter_interface, error=q[..., 0]-q[..., 3])


def solve(p, z0, step=0.01, duration=100):
    matrix = dynamics_matrix(p)
    gamma = np.asarray(p.gamma)

    def rhs(w):
        z = w[:8]
        dq = matrix @ z
        dissipation = np.dot(gamma, z[4:8]**2)
        pr = p.rho*(z[2]-z[0])*z[4]
        pm = p.eta*(z[3]-z[0])*z[4]
        return np.concatenate((dq, [dissipation, abs(pr)+abs(pm), (z[0]-z[3])**2]))

    count = round(duration/step)
    assert np.isclose(count*step, duration)
    trajectory = np.zeros((count+1, 11))
    trajectory[0, :8] = z0
    for i in range(count):
        w = trajectory[i]
        k1 = rhs(w)
        k2 = rhs(w + step*k1/2)
        k3 = rhs(w + step*k2/2)
        k4 = rhs(w + step*k3)
        trajectory[i+1] = w + step*(k1+2*k2+2*k3+k4)/6
    times = np.linspace(0, duration, count+1)
    return times, trajectory


def quiet_intervals(t, pair, epsilon=1e-4, hold=1.0):
    quiet = pair <= epsilon
    transitions = np.diff(np.concatenate(([False], quiet, [False])).astype(int))
    starts, ends = np.flatnonzero(transitions == 1), np.flatnonzero(transitions == -1)-1
    return [(float(t[a]), float(t[b])) for a, b in zip(starts, ends)
            if t[b]-t[a] >= hold]


def summarize(t, w, p):
    d = diagnostics(w[:, :8], p)
    energy0 = float(d['energy'][0])
    budget_error = np.max(np.abs(d['energy']+w[:, 8]-energy0))
    assert budget_error < 1e-7*max(1.0, energy0), budget_error
    assert np.min(d['energy']) >= -1e-12
    assert np.all(np.diff(w[:, 8]) >= -1e-12)
    active = np.flatnonzero(d['pair'] > 1e-4)
    qp, pp = d['qplus'], d['pplus']
    tick_indices = np.flatnonzero((qp[:-1] < 0) & (qp[1:] >= 0)
                                  & (np.hypot(qp[1:], pp[1:]) > 1e-5))
    tick_times = [float(t[i]+(t[i+1]-t[i])*(-qp[i])/(qp[i+1]-qp[i]))
                  for i in tick_indices]
    quiet = quiet_intervals(t, d['pair'])
    return {
        'initial_energy': energy0,
        'final_energy': float(d['energy'][-1]),
        'dissipated_energy': float(w[-1, 8]),
        'max_energy_budget_error': float(budget_error),
        'max_local_pair_energy': float(np.max(d['pair'])),
        'first_local_activation_above_1e-4': float(t[active[0]]) if len(active) else None,
        'max_absolute_meter_record': float(np.max(np.abs(w[:, 3]))),
        'held_local_quiet_intervals': quiet,
        'reactivations_after_held_quiet': int(sum(end < t[-1] for _, end in quiet)),
        'collective_positive_crossing_times': tick_times,
        'gross_boundary_transfer_integral': float(w[-1, 9]),
        'tracking_residual_integral': float(w[-1, 10]),
        'largest_real_part_dynamics_eigenvalues': float(np.max(np.linalg.eigvals(dynamics_matrix(p)).real)),
    }


def main():
    p = Parameters()
    z0 = np.array([0., 0., 1., 0., 0., 0., 0., 0.])
    cases = {
        'baseline': (p, z0),
        'meter_disconnected': (replace(p, eta=0.), z0),
        'conservative': (replace(p, gamma=(0., 0., 0., 0.)), z0),
        'global_null': (p, np.zeros(8)),
    }
    summaries, runs = {}, {}
    for name, (params, initial) in cases.items():
        t, w = solve(params, initial)
        summaries[name] = summarize(t, w, params)
        runs[name] = (t, w)
    t, w = runs['baseline']
    _, fine = solve(p, z0, step=0.005)
    convergence_error = float(np.max(np.abs(w[:, :9]-fine[::2, :9])))
    assert convergence_error < 1e-7, convergence_error
    assert np.array_equal(runs['global_null'][1], np.zeros_like(w))
    assert np.all(runs['meter_disconnected'][1][:, 3] == 0)
    assert np.all(runs['conservative'][1][:, 8] == 0)
    assert summaries['baseline']['max_local_pair_energy'] > 0

    # Independent analytic gradient check of the local pair-power equation.
    sample = w[::137, :8]
    grad = np.zeros_like(sample)
    grad[:, 0] = sample[:, 0]+p.kappa*(sample[:, 0]-sample[:, 1])
    grad[:, 1] = sample[:, 1]-p.kappa*(sample[:, 0]-sample[:, 1])
    grad[:, 4:6] = sample[:, 4:6]
    direct = np.sum(grad*(sample @ dynamics_matrix(p).T), axis=1)
    d = diagnostics(sample, p)
    boundary = (d['resource_power']+d['meter_power']
                -p.gamma[0]*sample[:, 4]**2-p.gamma[1]*sample[:, 5]**2)
    power_error = float(np.max(np.abs(direct-boundary)))
    assert power_error < 1e-12, power_error

    sensor = np.zeros(8)
    sensor[3] = 1
    matrix = dynamics_matrix(p)
    observability = np.vstack([sensor @ np.linalg.matrix_power(matrix, j) for j in range(8)])
    pair_indices = [0, 1, 4, 5]
    disturbed = w[:, pair_indices]-runs['meter_disconnected'][1][:, pair_indices]
    report = {
        'model': 'feedback_null_v01',
        'runtime': {'python': platform.python_version(), 'numpy': np.__version__},
        'status': 'baseline consistency checks passed',
        'parameters': asdict(p),
        'duration': 100, 'primary_step': 0.01, 'refined_step': 0.005,
        'max_state_and_dissipation_step_refinement_error': convergence_error,
        'max_local_power_identity_error': power_error,
        'ideal_meter_output_observability_rank_numerical': int(np.linalg.matrix_rank(observability)),
        'max_pair_state_difference_due_to_meter': float(np.max(np.linalg.norm(disturbed, axis=1))),
        'cases': summaries,
        'limits': ['Dimensionless classical analogue; parameter choices are illustrative.',
                   'Damping exports energy to an unmodeled passive environment, recorded as Q.',
                   'No forced restart; no autonomous logical certificate controller.',
                   'Clock events use an already specified time parameter.',
                   'The four-preparation noisy inference task has not been executed.',
                   'No physical measurement, quantum derivation, or cosmological conclusion.'],
    }
    out = Path(__file__).resolve().parent/'results'
    out.mkdir(exist_ok=True)
    (out/'baseline-report.json').write_text(json.dumps(report, indent=2)+'\n')
    d = diagnostics(w[:, :8], p)
    columns = ['tau','q1','q2','resource','meter','p1','p2','p_resource','p_meter',
               'dissipated_energy','gross_transfer','integrated_tracking_residual',
               'total_energy','local_pair_energy','asymmetry','meter_interface_energy',
               'resource_to_pair_power','meter_to_pair_power','q_plus','p_plus','common_mode_energy']
    rows = np.column_stack([t, w, d['energy'], d['pair'], d['asymmetry'], d['meter_interface'],
                            d['resource_power'], d['meter_power'], d['qplus'], d['pplus'], d['eplus']])
    assert rows.shape[1] == len(columns)
    with (out/'baseline-trajectory.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(columns)
        writer.writerows([[format(float(x), '.10g') for x in row] for row in rows[::10]])
    print(json.dumps({key: value for key, value in report.items() if key != 'cases'}, indent=2))
    for name, result in summaries.items():
        print(name, json.dumps({key: result[key] for key in
              ['initial_energy','final_energy','max_local_pair_energy',
               'max_absolute_meter_record','reactivations_after_held_quiet']}))


if __name__ == '__main__':
    main()
