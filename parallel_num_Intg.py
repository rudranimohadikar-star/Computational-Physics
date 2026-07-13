from mpi4py import MPI
import numpy as np

def func(x):
    return 4.0/(1.0 + x * x)

def trapezoidal_rule(a, b, n, h):
    est = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        x = a + i*h
        est += func(x)
    return est * h

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 1000
h = 1.0 / N

start = rank * N // size
end = (rank + 1) * N // size

local_sum = 0.0
for i in range(start, end):
    x = (i + 0.5) * h
    local_sum += 4.0 / (1.0 + x * x)

local_integral = local_sum * h
integral = comm.reduce(local_integral, op=MPI.SUM, root=0)

if rank == 0:
    print("Approximation:", integral)
    print("Error:", abs(integral - np.pi))