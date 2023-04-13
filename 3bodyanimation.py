import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, PillowWriter

def three_body(y, t):
    x1, y1, z1, x2, y2, z2, x3, y3, z3, vx1, vy1, vz1, vx2, vy2, vz2, vx3, vy3, vz3 = y

    d12 = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    d13 = np.sqrt((x1 - x3)**2 + (y1 - y3)**2 + (z1 - z3)**2)
    d23 = np.sqrt((x2 - x3)**2 + (y2 - y3)**2 + (z2 - z3)**2)

    x1dot = vx1
    y1dot = vy1
    z1dot = vz1
    x2dot = vx2
    y2dot = vy2
    z2dot = vz2
    x3dot = vx3
    y3dot = vy3
    z3dot = vz3

    v1xdot = (-x1 + x2) / d12**3 + (-x1 + x3) / d13**3
    v1ydot = (-y1 + y2) / d12**3 + (-y1 + y3) / d13**3
    v1zdot = (-z1 + z2) / d12**3 + (-z1 + z3) / d13**3
    v2xdot = (-x2 + x1) / d12**3 + (-x2 + x3) / d23**3
    v2ydot = (-y2 + y1) / d12**3 + (-y2 + y3) / d23**3
    v2zdot = (-z2 + z1) / d12**3 + (-z2 + z3) / d23**3
    v3xdot = (-x3 + x1) / d13**3 + (-x3 + x2) / d23**3
    v3ydot = (-y3 + y1) / d13**3 + (-y3 + y2) / d23**3
    v3zdot = (-z3 + z1) / d13**3 + (-z3 + z2) / d23**3

    return [x1dot, y1dot, z1dot, x2dot, y2dot, z2dot, x3dot, y3dot, z3dot, v1xdot, v1ydot, v1zdot, v2xdot, v2ydot, v2zdot, v3xdot, v3ydot, v3zdot]

x1, y1, z1 = 0, 0, 0
x2, y2, z2 = 1, 0, 2
x3, y3, z3 = 0, 1, 1
v1x, v1y, v1z = 0, -0.5, 1.3
v2x, v2y, v2z = 0, 0.5, 1
v3x, v3y, v3z = 0.5, 0, 1.6
y0_2d_1 = [x1, y1, z1, x2, y2, z2, x3, y3, z3, v1x, v1y, v1z, v2x, v2y, v2z, v3x, v3y, v3z]

t = np.linspace(0, 20, 1000)
sol_2d_1 = odeint(three_body, y0_2d_1, t)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Initialize lines for each body
line1, = ax.plot([], [], [], label="Central Planet")
line2, = ax.plot([], [], [], label="Moon 1")
line3, = ax.plot([], [], [], label="Moon 2")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()

# Set axis limits
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)

# Animation update function
def update(frame):
    line1.set_data(sol_2d_1[:frame, 0], sol_2d_1[:frame, 1])
    line1.set_3d_properties(sol_2d_1[:frame, 2])
    line2.set_data(sol_2d_1[:frame, 3], sol_2d_1[:frame, 4])
    line2.set_3d_properties(sol_2d_1[:frame, 5])
    line3.set_data(sol_2d_1[:frame, 6], sol_2d_1[:frame, 7])
    line3.set_3d_properties(sol_2d_1[:frame, 8])
    return line1, line2, line3,

# Create animation
ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)

# Set up the writer
writer = PillowWriter(fps=30)

# Save the animation as a GIF
ani.save("three_body_animation.gif", writer=writer)

# Show the animation (optional)
plt.show()
