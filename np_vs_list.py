import time
import numpy as np

N = 10000000

# Python lists
x_list = list(range(N))
z_list = list(range(N))

t0 = time.perf_counter()
y_list = [3*x + 2*(z**2) for x, z in zip(x_list, z_list)]
total_list = sum(y_list)
mean_list = total_list / len(y_list)
t1 = time.perf_counter()

# NumPy arrays
x_arr = np.arange(N)
z_arr = np.arange(N)

t2 = time.perf_counter()
y_arr = 3*x_arr + 2*(z_arr**2)
total_arr = np.sum(y_arr)
mean_arr = np.mean(y_arr)
t3 = time.perf_counter()

print("List time:", t1 - t0)
print("NumPy time:", t3 - t2)