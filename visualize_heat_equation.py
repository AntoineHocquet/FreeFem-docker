import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from matplotlib.animation import FuncAnimation

# Load the CSV data
data = pd.read_csv('solution_data.csv')

# Extract unique time steps
time_steps =data['time'].unique()

# Extract mesh points
x = data['x'].unique()
y = data['y'].unique()

# Prepare the triangulation of the mesh for plotting
# Assuming mesh structure stays constant over time
mesh_points = data[data['time'] == time_steps[0]]
triang = tri.Triangulation(mesh_points['x'], mesh_points['y'])

# Initialize the plot
fig, ax = plt.subplots(figsize=(6, 5))
contour = ax.tricontourf(triang, mesh_points['u'], cmap='inferno')
cbar = plt.colorbar(contour)
cbar.set_label('Temperature')

ax.set_title("Heat Equation Simulation Over Time")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Function to update the animation at each time step
def update(frame):
    current_data = data[data['time'] == time_steps[frame]]
    ax.clear()
    contour = ax.tricontourf(triang, current_data['u'], cmap='inferno')
    ax.set_title(f"Heat Equation at Time = {time_steps[frame]:.2f}s")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    return contour.collections

# Create the animation
anim = FuncAnimation(fig, update, frames=len(time_steps), interval=100, repeat=False)

# Save the animation as an MP4 file
anim.save('heat_equation_simulation.mp4', writer='ffmpeg')

# Show the animation (if running interactively)
plt.show()
