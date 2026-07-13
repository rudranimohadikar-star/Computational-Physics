# ==============================================================================
# MISSION CONTROL: EXOPLANET KEPLER-A (OOP Edition)
# Python Data & Visualization Workshop - Student Template
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import savgol_filter
from scipy.optimize import minimize
from matplotlib.widgets import Slider


class KeplerMission:
    def __init__(self):
        # Initialize the core mission parameters.
        print("Initializing Mission Control...")

        # Task: Create a time array from -10 to 10 days (e.g., 500 points).
        # Assign it to self.time
        ### YOUR CODE HERE ###
        # self.time = ...

        # Initialize attributes we will fill in later phases
        self.flux_clean = None
        self.flux_noisy = None
        self.flux_filtered = None
        self.path = []

    # ==========================================================================
    # PHASE 1: The Clean Signal
    # ==========================================================================
    def phase_1_clean_signal(self):
        print("Starting Phase 1...")
        # Task: Create a flux array that is 1.0 everywhere, but dips down to 0.98
        # between time -1 and 1. Assign to self.flux_clean.
        ### YOUR CODE HERE ###

        # Task: Plot self.time vs self.flux_clean.
        # Add labels, title, grid, and save as PNG (dpi=300).
        plt.figure(figsize=(10, 4))
        ### YOUR CODE HERE ###

        # plt.show() # Uncomment to view, close window to continue script

    # ==========================================================================
    # PHASE 2: Piercing the Cosmic Noise & The Ringing Artifact
    # ==========================================================================
    def phase_2_cosmic_noise(self):
        print("Starting Phase 2...")
        # Task: Add Gaussian noise (np.random.normal) and a low-freq drift
        # (e.g. a sine wave) to self.flux_clean. Assign to self.flux_noisy.
        ### YOUR CODE HERE ###

        # Task: Apply a Savitzky-Golay filter to self.flux_noisy.
        # Hint: savgol_filter(data, window_length, polyorder)
        # Try window_length=41 and polyorder=3.
        # Assign to self.flux_filtered.
        ### YOUR CODE HERE ###

        # Task: Plot self.flux_noisy (alpha=0.4) and overlay self.flux_filtered.
        # Add a legend! Notice how well the polynomial fits the smooth Gaussian dip.
        plt.figure(figsize=(10, 4))
        ### YOUR CODE HERE ###

        # plt.show()

    # ==========================================================================
    # PHASE 3: Weighing the Cosmos (Linear vs. Log)
    # ==========================================================================
    def phase_3_weigh_cosmos(self):
        print("Starting Phase 3...")
        import streamlit as st

        # Task: Load the 'planets' dataset from seaborn and drop missing values
        # for 'orbital_period' and 'distance'.
        ### YOUR CODE HERE ###
        # df = ...

        # Task: Create a Streamlit title "Kepler Mission Dashboard"
        # and display the dataframe using st.dataframe()
        ### YOUR CODE HERE ###

        # Task: Create a seaborn scatterplot of orbital_period vs distance in LINEAR scale.
        # Color points by 'method'. Notice how squished and unreadable it is.
        plt.figure(figsize=(8, 6))
        ### YOUR CODE HERE ###

        # plt.show()

        # Task: Create the exact same scatterplot, but set x and y scales to 'log'.
        plt.figure(figsize=(8, 6))
        ### YOUR CODE HERE ###

        # Task: Use np.polyfit to find the slope of log(period) vs log(distance).
        # Overlay this fit line on your log-log plot.
        ### YOUR CODE HERE ###

        # plt.show()

    # ==========================================================================
    # PHASE 4: Mapping the Gravity Well
    # ==========================================================================
    def _error_surface(self, vars):
        # A simple 2D mathematical surface representing an optimization landscape.
        x, y = vars
        # Task: Return Rosenbruck function value at (x, y).
        pass

    def _tracker_callback(self, xk):
        # Callback to track the optimization path.
        # Task: Append a copy of the current coordinates (xk) to self.path
        ### YOUR CODE HERE ###
        pass

    def phase_4_gravity_well(self):
        print("Starting Phase 4...")

        # --------------------------------------------------------
        # Task 1:
        # Create a meshgrid of X and Y values from -3 to 3.
        # --------------------------------------------------------
        ### YOUR CODE HERE ###

        # --------------------------------------------------------
        # Task 2:
        # Compute the Rosenbrock surface using:
        # self._error_surface((X, Y))
        # --------------------------------------------------------
        ### YOUR CODE HERE ###

        # --------------------------------------------------------
        # Task 3:
        # Create a list of optimization methods to compare.
        # --------------------------------------------------------
        ### YOUR CODE HERE ###

        # --------------------------------------------------------
        # Task 4:
        # Choose a starting point:
        # x0 = [-2, 2]
        # --------------------------------------------------------
        ### YOUR CODE HERE ###

        # --------------------------------------------------------
        # Task 5:
        # Create a figure with plt.contourf.
        # Add a colorbar.
        # --------------------------------------------------------
        plt.figure(figsize=(10, 8))
        ### YOUR CODE HERE ###

        # --------------------------------------------------------
        # Task 6:
        # Loop over each optimization method.
        #
        # Inside the loop:
        #   - Reset self.path
        #   - Add the initial point
        #   - Run scipy.optimize.minimize
        #   - Use callback=self._tracker_callback
        #   - Store the result
        # --------------------------------------------------------

        ### YOUR CODE HERE ###



        # ----------------------------------------------------
        # Task 7:
        # Extract path coordinates from self.path.
        # ----------------------------------------------------
        ### YOUR CODE HERE ###

        # ----------------------------------------------------
        # Task 8:
        # Overlay the optimization trajectory.
        # Use plt.plot().
        # ----------------------------------------------------
        ### YOUR CODE HERE ###

        # ----------------------------------------------------
        # Task 9:
        # Print:
        #   - final coordinates
        #   - iteration count
        #   - function evaluations
        # ----------------------------------------------------
        ### YOUR CODE HERE ###

        # --------------------------------------------------------
        # Task 10:
        # Finalize the plot:
        #   - title
        #   - axis labels
        #   - legend
        # --------------------------------------------------------
        ### YOUR CODE HERE ###

        # plt.show()

    # ==========================================================================
    # PHASE 5: The Interactive Dashboard
    # ==========================================================================
    def _calc_dip(self, t, depth, width):
        # Helper to calculate a parametric Gaussian dip.
        return 1.0 - depth * np.exp(-0.5 * (t / width) ** 2)

    def phase_5_dashboard(self):
        print("Starting Phase 5...")
        # Setup figure
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.subplots_adjust(bottom=0.3)  # Make room for sliders

        init_depth = 0.02
        init_width = 2.0

        # Plot initial line
        line, = ax.plot(self.time, self._calc_dip(self.time, init_depth, init_width), lw=2, color='darkred')
        ax.set_ylim(0.9, 1.05)

        # Task: Create the slider axes and the Slider objects.
        # ax_depth = plt.axes([0.2, 0.15, 0.65, 0.03])
        # ax_width = plt.axes([0.2, 0.1, 0.65, 0.03])
        ### YOUR CODE HERE ###

        # Task: Create an update function that takes a value (val),
        # recalculates the dip using self._calc_dip, and updates line.set_ydata().
        def update(val):
            ### YOUR CODE HERE ###
            # fig.canvas.draw_idle() # Redraws the canvas dynamically
            pass

        # Task: Connect the update function to both sliders.
        ### YOUR CODE HERE ###

        # plt.show()


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
if __name__ == "__main__":
    mission = KeplerMission()

    # Students: Uncomment each phase as you complete it!
    # mission.phase_1_clean_signal()
    # mission.phase_2_cosmic_noise()
    # mission.phase_3_weigh_cosmos()
    mission.phase_4_gravity_well()
    # mission.phase_5_dashboard()