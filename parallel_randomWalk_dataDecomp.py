from mpi4py import MPI
import numpy as np
import matplotlib.pyplot as plt

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

L = 100
N = 1000
T = 100000
t_plot = 1000

assert N % size == 0, "N must be divisible by size for this example"

local_N = N // size
rng = np.random.default_rng(seed=100 + rank)
positions = rng.integers(0, L, size=local_N, dtype=np.int64)

tracked_RW = rng.integers(0, local_N, size=2, dtype=int)

pos_all_time = np.empty((2, T+1), dtype=np.int64)
pos_all_time[:, 0] = positions[tracked_RW]

for t in range(1, T+1):
    steps = rng.choice([-1, 0, 1], size=local_N)
    positions = (positions + steps) % L
    pos_all_time[:, t] = positions[tracked_RW]

if rank == 0:
    all_positions = np.empty(N, dtype=np.int64)
    all_tracked_RW = np.empty((size, 2, T+1), dtype=np.int64)
else:
    all_positions = None
    all_tracked_RW = None

comm.Gather(positions, all_positions, root=0)
comm.Gather(pos_all_time, all_tracked_RW, root=0)

if rank == 0:
    plt.figure()
    plt.hist(all_positions, bins=100, alpha=0.7, range=(0, L), density=True)
    plt.xlabel('x')
    plt.ylabel('pdf')
    plt.title('Distribution of RWs')
    
    plt.figure()
    all_tracked_RW = all_tracked_RW.reshape(2*size, T+1)
    for i in range(2*size):
        plt.scatter(all_tracked_RW[i,:t_plot], np.arange(t_plot), label=f'RW {i}', marker='.', s=1)
    plt.xlabel('Position')
    plt.ylabel('Time')
    plt.title('Kymograph of tracked RWs')
    plt.show()