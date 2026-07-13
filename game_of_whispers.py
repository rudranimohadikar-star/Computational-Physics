from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

rng = np.random.default_rng(seed=100+rank*10)
co_op = rng.choice([0,1], size=1)[0]

if rank == 0:
    whisper = {
        "round": 0,
        "message": "MPI lets many processes cooperate.",
        "history": ["rank 0 created the message"],
    }
    comm.send(whisper, dest=1, tag=11)
    final_whisper = comm.recv(source=size - 1, tag=22)
    print("Final object:", final_whisper)

elif rank < size - 1:
    whisper = comm.recv(source=rank - 1, tag=11)
    if co_op == 1:
        whisper["message"] = whisper["message"] + f" Rank {rank} cooperated."
    else:
        whisper["message"] = whisper["message"] + f" Rank {rank} ain't co-op-ing."
    whisper["history"].append(f"rank {rank} changed the text")
    comm.send(whisper, dest=rank + 1, tag=11)

else:
    whisper = comm.recv(source=rank - 1, tag=11)
    if co_op == 1:
        whisper["message"] = whisper["message"] + f" Rank {rank} cooperated."
    else:
        whisper["message"] = whisper["message"] + f" Rank {rank} ain't co-op-ing."
    whisper["history"].append(f"rank {rank} ended the chain")
    comm.send(whisper, dest=0, tag=22)