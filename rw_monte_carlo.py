import numpy as np

rng = np.random.default_rng(1002)

n_walkers = 100000
left_boundary = -10
right_boundary = 10

positions = np.zeros(n_walkers, dtype=int)
first_passage_times = np.zeros(n_walkers, dtype=int)
hit_boundary = np.zeros(n_walkers, dtype=int)   # -1 for left, +1 for right
active = np.ones(n_walkers, dtype=bool) # Once absorbed, becomes False

t = 0

while np.any(active):
    t += 1

    steps = rng.choice([-1, 1], size=active.sum())
    positions[active] += steps

    hit_left = active & (positions <= left_boundary)
    hit_right = active & (positions >= right_boundary)

    absorbed = hit_left | hit_right

    first_passage_times[absorbed] = t
    hit_boundary[hit_left] = -1
    hit_boundary[hit_right] = 1

    active[absorbed] = False

p_right_first = np.mean(hit_boundary == 1)
p_left_first = np.mean(hit_boundary == -1)

mean_fpt = np.mean(first_passage_times)
std_fpt = np.std(first_passage_times, ddof=1)

print("Probability of hitting +10 first:", p_right_first)
print("Probability of hitting -10 first:", p_left_first)
print("Mean first-passage time:", mean_fpt)
print("Std. dev. of first-passage time:", std_fpt)