from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 933199  # 23

if rank == 0:
    rng = np.random.default_rng(100)
    a = rng.uniform(0.0, 1.0, N)
    b = rng.uniform(1.0, 10.0, N)
else:
    a = None
    b = None

# counts for each rank
base = N // size
remainder = N % size
counts = np.array([base + 1 if r < remainder else base for r in range(size)], dtype=int)

# starting offsets
displs = np.zeros(size, dtype=int)
displs[1:] = np.cumsum(counts[:-1])

local_n = counts[rank]
local_a = np.empty(local_n, dtype=np.float64)
local_b = np.empty(local_n, dtype=np.float64)

comm.Scatterv([a, counts, displs, MPI.DOUBLE], local_a, root=0)
comm.Scatterv([b, counts, displs, MPI.DOUBLE], local_b, root=0)

local_dot = np.dot(local_a, local_b)
global_dot = comm.reduce(local_dot, op=MPI.SUM, root=0)

if rank == 0:
    print("Parallel dot product:", global_dot)
    print("Serial dot product:", np.dot(a, b))