import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(5)

n_beads = 10000
n_rows = 20

steps = rng.integers(0, 2, size=(n_beads, n_rows))
final_bins = np.sum(steps, axis=1)

counts = np.bincount(final_bins, minlength=n_rows + 1)
mean_bin = np.mean(final_bins)
var_bin = np.var(final_bins)

print("Bin counts:")
for i, c in enumerate(counts):
    print(f"Bin {i}: {c}")

print("\nMean final bin:", mean_bin)
print("Variance of final bin:", var_bin)

plt.hist(final_bins, bins=np.arange(n_rows + 2) - 0.5, edgecolor="black")
plt.xlabel("Bin")
plt.ylabel("Number of beads")
plt.title("Galton Board Simulation")
plt.show()