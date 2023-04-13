import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function that returns the derivative of the state vector
def three_body(y, t):
    # Unpack the state vector
    x1, y1, z1, x2, y2, z2, x3, y3, z3, vx1, vy1, vz1, vx2, vy2, vz2, vx3, vy3, vz3 = y

    # Compute the distances between the bodies
    d12 = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    d13 = np.sqrt((x1 - x3)**2 + (y1 - y3)**2 + (z1 - z3)**2)
    d23 = np.sqrt((x2 - x3)**2 + (y2 - y3)**2 + (z2 - z3)**2)

    # Compute the derivatives of the positions
    x1dot = vx1
    y1dot = vy1
    z1dot = vz1
    x2dot = vx2
    y2dot = vy2
    z2dot = vz2
    x3dot = vx3
    y3dot = vy3
    z3dot = vz3

    # Compute the derivatives of the velocities
    v1xdot = (-x1 + x2) / d12**3 + (-x1 + x3) / d13**3
    v1ydot = (-y1 + y2) / d12**3 + (-y1 + y3) / d13**3
    v1zdot = (-z1 + z2) / d12**3 + (-z1 + z3) / d13**3
    v2xdot = (-x2 + x1) / d12**3 + (-x2 + x3) / d23**3
    v2ydot = (-y2 + y1) / d12**3 + (-y2 + y3) / d23**3
    v2zdot = (-z2 + z1) / d12**3 + (-z2 + z3) / d23**3
    v3xdot = (-x3 + x1) / d13**3 + (-x3 + x2) / d23**3
    v3ydot = (-y3 + y1) / d13**3 + (-y3 + y2) / d23**3
    v3zdot = (-z3 + z1) / d13**3 + (-z3 + z2) / d23**3

    # Return the derivatives
    return [x1dot, y1dot, z1dot, x2dot, y2dot, z2dot, x3dot, y3dot, z3dot, v1xdot, v1ydot, v1zdot, v2xdot, v2ydot, v2zdot, v3xdot, v3ydot, v3zdot]

# Define the initial conditions for the first 2D simulation
x1, y1, z1 = 0, 0, 0	# Central massive body (planet)
x2, y2, z2 = 1, 0, 2
x3, y3, z3 = 0, 1, 1
v1x, v1y, v1z = 0, -0.5, 3
v2x, v2y, v2z = 0, 0.5, 4
v3x, v3y, v3z = 0.5, 0, 3.8
y0_2d_1 = [x1, y1, z1, x2, y2, z2, x3, y3, z3, v1x, v1y, v1z, v2x, v2y, v2z, v3x, v3y, v3z]

# Define the initial conditions for the second 2D simulation
x1, y1, z1 = 0, 0, 0
x2, y2, z2 = 1/2, np.sqrt(3)/2, 3
x3, y3, z3 = 0, 0, 4
v1x, v1y, v1z = 1/2, np.sqrt(3)/2, 6
v2x, v2y, v2z = -1/2, np.sqrt(3)/2, 1
v3x, v3y, v3z = 0, -np.sqrt(3), 2
y0_2d_2 = [x1, y1, z1, x2, y2, z2, x3, y3, z3, v1x, v1y, v1z, v2x, v2y, v2z, v3x, v3y, v3z]


# Define the time grid
t = np.linspace(0, 20, 1000)

# Solve the differential equations using odeint for the first 2D simulation
sol_2d_1 = odeint(three_body, y0_2d_1, t)

# Solve the differential equations using odeint for the second 2D simulation
sol_2d_2 = odeint(three_body, y0_2d_2, t)

# Stack the results of the two simulations to create a 3D representation
sol_3d = np.vstack((sol_2d_1.T, np.zeros_like(sol_2d_1.T[0]), sol_2d_2.T))

# Create a 3D plot of the trajectories of the bodies
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot(sol_3d[0], sol_3d[1], sol_3d[2], label="Central Planet")
ax.plot(sol_3d[3], sol_3d[4], sol_3d[5], label="Moon 1")
ax.plot(sol_3d[6], sol_3d[7], sol_3d[8], label="Moon 2")


# Set the labels for each axis
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# Add a legend to the plot
ax.legend()

# Show the plot
plt.show()


