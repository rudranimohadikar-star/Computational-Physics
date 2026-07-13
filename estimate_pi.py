import numpy as np

rng = np.random.default_rng(5)

n_trials = 100
sample_sizes = [50, 10**2, 10**3, 10**4, 10**5]

print(f"{'N':>8} {'mean_pi':>12} {'std_pi':>12} {'abs_error':>12}")

for N in sample_sizes:
    x = rng.uniform(-1, 1, size=(n_trials, N))
    y = rng.uniform(-1, 1, size=(n_trials, N))

    inside = (x**2 + y**2) <= 1
    counts_inside = np.sum(inside, axis=1)

    pi_estimates = 4 * counts_inside / N

    mean_pi = np.mean(pi_estimates)
    std_pi = np.std(pi_estimates)
    abs_error = abs(mean_pi - np.pi)

    print(f"{N:8d} {mean_pi:12.6f} {std_pi:12.6f} {abs_error:12.6f}")