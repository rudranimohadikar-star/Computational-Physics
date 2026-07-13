import math
import matplotlib.pyplot as plt

# Gravitational constant
G = 6.674e-11

class Body:
    def __init__(self, name, mass, x, y, vx, vy, color):
        """
        Initialize a celestial body.
        TODO: Store the provided parameters as instance variables (e.g., self.mass = mass).
        TODO: Create two empty lists, self.history_x and self.history_y, to store the trajectory.
        """
        pass
        
    def record_state(self):
        """
        TODO: Append the current x and y positions to self.history_x and self.history_y.
        """
        pass
        
    def update_velocity(self, fx, fy, dt):
        """
        TODO: Update the velocity based on the applied force and the time step dt.
        (Hint: F = m*a, and a = dv/dt)
        Note: This simulation uses the simple Euler method, which is easy to 
              implement but accumulates numerical error over long times.
        """
        pass
        
    def update_position(self, dt):
        """
        TODO: Update the position based on the current velocity and the time step dt.
        """
        pass

class Simulation:
    def __init__(self, dt):
        """
        Initialize the simulation.
        TODO: Store the time step `dt`.
        TODO: Initialize an empty list `self.bodies` to hold the Body objects.
        """
        pass
        
    def add_body(self, body):
        """
        TODO: Append the provided `body` to the `self.bodies` list.
        """
        pass
        
    def step(self):
        """
        Perform one simulation step.
        TODO: 
        1. Create a dictionary or lists to store the net forces (fx, fy) for each body.
           (Initialize forces to 0).
        2. Loop through all pairs of bodies (e.g., using a nested loop).
        3. If body 1 is not body 2, calculate the gravitational force between them.
        4. Add the force components to the net force of body 1.
        5. After all forces are calculated, loop through the bodies again and 
           call their `update_velocity`, `update_position`, and `record_state` methods.
        """
        pass

# --- MAIN SCRIPT ---
if __name__ == "__main__":
    # TODO: Create a Simulation instance with dt = 3600
    
    # TODO: Create Body instances for Sun, Earth, and Moon
    # Sun: mass=1.989e30, x=0, y=0, vx=0, vy=0, color='y', name='Sun'
    # Earth: mass=5.972e24, x=1.496e11, y=0, vx=0, vy=29780, color='b', name='Earth'
    # Moon: mass=7.348e22, x=1.496e11 + 3.844e8, y=0, vx=0, vy=29780 + 1022, color='gray', name='Moon'
    
    # TODO: Add the bodies to the simulation
    
    # TODO: Run the simulation loop for steps = 24 * 365 (1 year)
    
    # --- PLOTTING ---
    plt.figure(figsize=(8, 8))
    plt.style.use('dark_background')
    
    # TODO: Loop through the bodies in the simulation and plot their history
    # plt.plot(body.history_x, body.history_y, color=body.color, label=body.name)
    
    plt.title("N-Body Simulation (OOP)")
    plt.axis("equal")
    plt.legend()
    plt.show()
