from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 10000000
local_n = N // size

if rank == 0:
    rng = np.random.default_rng(100)
    a = rng.uniform(0.0, 1.0, N)
    b = rng.uniform(1.0, 10.0, N)
else:
    a = None
    b = None

local_a = np.empty(local_n, dtype=np.float64)
local_b = np.empty(local_n, dtype=np.float64)

comm.Scatter(a, local_a, root=0)
comm.Scatter(b, local_b, root=0)

local_dotProd = np.dot(local_a, local_b)
global_dotProd = comm.reduce(local_dotProd, op=MPI.SUM, root=0)

if rank == 0:
    print("Parallel dot:", global_dotProd)
    print("Serial dot:", np.dot(a, b))