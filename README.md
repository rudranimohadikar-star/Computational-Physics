# Computational Physics

A collection of Python scripts and exercises from the **CP1** (Computational Physics 1) course, covering Monte Carlo methods, parallel computing with MPI, N-body simulations, data analysis, and scientific visualization.

---

## Repository Structure

### Monte Carlo & Stochastic Simulations

| File | Description |
|------|-------------|
| `estimate_pi.py` | Estimates π using Monte Carlo sampling (random points in a unit square) across multiple sample sizes, reporting mean, std deviation, and absolute error. |
| `galton_board.py` | Simulates a Galton board with 10 000 beads and 20 rows, demonstrating the emergence of a binomial (≈ normal) distribution. |
| `rw_monte_carlo.py` | 1D random walk with absorbing boundaries at ±10. Computes first-passage times and hitting probabilities for 100 000 walkers. |

### Parallel Computing (MPI)

| File | Description |
|------|-------------|
| `parallel_dot_prod.py` | Parallel dot product using `MPI.Scatter` / `MPI.Reduce` for evenly divisible arrays. |
| `parallel_dot_prod_uneven.py` | Same as above but handles arrays whose length is **not** evenly divisible by the number of ranks, using `Scatterv` with explicit counts and displacements. |
| `parallel_num_Intg.py` | Parallel numerical integration of 4/(1+x²) over [0, 1] (≈ π) using the midpoint rule and `MPI.Reduce`. |
| `parallel_randomWalk_dataDecomp.py` | Data-decomposed parallel random walk on a periodic lattice. Gathers final positions and tracked trajectories (kymograph) on rank 0 for plotting. |
| `game_of_whispers.py` | MPI ring-communication demo: a message dictionary is passed around all ranks, each one appending to it based on a random cooperate/defect choice. |

### N-Body Simulations

| File | Description |
|------|-------------|
| `three_body_switchable.py` | Procedural 3-body gravitational simulation with two modes: **STABLE** (Sun–Earth–Moon) and **CHAOTIC** (three equal-mass stars). Uses Euler integration. |
| `three_body_skeleton (1).py` | OOP skeleton/template for an N-body simulation with `Body` and `Simulation` classes — meant to be completed as an exercise. |

### Data Analysis & Visualization (Exercises)

| File | Description |
|------|-------------|
| `Exercise1` | Parses LAMMPS thermo output logs (`.sec` files) into Pandas DataFrames. |
| `Ex1plot` | Extends `Exercise1` with stress–strain curve plotting (raw + rolling average) for single files and entire folders. Generates `stress_strain_single.png` and `stress_strain_all.png`. |
| `templateex4.py` | Student template for the "Mission Control: Exoplanet Kepler-A" workshop (OOP edition). Contains guided `### YOUR CODE HERE ###` sections for signal processing, Kepler's third law, Rosenbrock optimization, and an interactive slider dashboard. |
| `Exercise5.py` | Full solution for the Kepler-A workshop: transit signal generation, Savitzky-Golay filtering, log-log exoplanet scatter plots, multi-method Rosenbrock optimization comparison, and a Matplotlib slider dashboard. |

### Performance Benchmarks

| File | Description |
|------|-------------|
| `np_vs_list.py` | Benchmarks Python list comprehensions vs NumPy vectorized operations on 10⁷ elements. |

### Data Files

| File | Description |
|------|-------------|
| `log140-1.sec`, `log140-2.sec` | LAMMPS molecular dynamics log files used by `Exercise1` and `Ex1plot`. |
| `stress_strain_single.png` | Pre-generated stress–strain plot (single log file). |
| `stress_strain_all.png` | Pre-generated stress–strain plot (combined log files). |

---

## Prerequisites

- **Python 3.8+**
- Core packages: `numpy`, `matplotlib`, `pandas`
- Exercise 5 / template: `scipy`, `seaborn`
- MPI scripts: `mpi4py` (+ an MPI implementation such as OpenMPI or MPICH)

Install dependencies:

```bash
pip install numpy matplotlib pandas scipy seaborn mpi4py
```

---

## Usage

### Standard scripts

```bash
python estimate_pi.py
python galton_board.py
python rw_monte_carlo.py
python np_vs_list.py
python three_body_switchable.py
python Exercise5.py
```

### MPI scripts

```bash
mpirun -np 4 python parallel_dot_prod.py
mpirun -np 4 python parallel_dot_prod_uneven.py
mpirun -np 4 python parallel_num_Intg.py
mpirun -np 4 python parallel_randomWalk_dataDecomp.py
mpirun -np 4 python game_of_whispers.py
```

### LAMMPS log analysis

```bash
python Exercise1
python Ex1plot
```

---

## License

This project is for educational purposes as part of the CP1 course.
