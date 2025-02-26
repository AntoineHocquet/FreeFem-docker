import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from matplotlib.animation import FuncAnimation

# Load the CSV data
data = pd.read_csv('solution_data.csv')

# Extract unique time steps
time_steps = data['time'].unique()

# Extract mesh points from the first time step
mesh_points = data[data['time'] == time_steps[0]]
x = mesh_points['x'].values
y = mesh_points['y'].values

# Compute global min and max for color scale
u_min = data['u'].min()
u_max = data['u'].max()

# Prepare the triangulation
triang = tri.Triangulation(x, y)

# Initialize the plot
fig, ax = plt.subplots(figsize=(6, 5))
contour = ax.tricontourf(triang, mesh_points['u'], cmap='inferno',vmin=u_min,vmax=u_max)
cbar = plt.colorbar(contour)
cbar.set_label('Temperature')

ax.set_title("Heat Equation Simulation Over Time")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Update function for the animation
def update(frame):
    current_data = data[data['time'] == time_steps[frame]]
    ax.clear()
    contour = ax.tricontourf(triang, current_data['u'], cmap='inferno',vmin=u_min,vmax=u_max)
    ax.set_title(f"Heat Equation at Time = {time_steps[frame]:.2f}s")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    return contour.collections

# Create the animation
anim = FuncAnimation(fig, update, frames=len(time_steps), interval=100, repeat=False)

# Save the animation as a GIF
anim.save('heat_equation_simulation.gif', writer='imagemagick')

# Close the plot after saving
plt.close()
