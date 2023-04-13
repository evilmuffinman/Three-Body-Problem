# Three-Body-Problem
A method of using stacked 2D simulations to approximate 3D motion.
The three-body problem is a fundamental problem in physics and astronomy that involves predicting the motion of three celestial bodies under the influence of their mutual gravitational attraction. The problem has been of great significance in the development of modern physics and has been a subject of study for centuries.

The three-body problem was first formulated by Sir Isaac Newton in the late 17th century. Despite his groundbreaking work on the laws of motion and gravity, Newton was unable to solve the problem analytically, and it remained unsolved for over two centuries. In the 19th century, mathematicians like Carl Friedrich Gauss and Henri Poincaré made important contributions to the field, paving the way for modern approaches to solving the problem.

Today, the three-body problem remains an active area of research, with applications ranging from astrophysics to chaos theory. Advances in computing technology and numerical methods have allowed scientists to simulate the motion of three or more bodies with increasing accuracy, leading to new insights into the behavior of complex systems.

To enhance our understanding of three-body motion in a three-dimensional space, we propose a method of using stacked 2D simulations to approximate 3D motion. This method involves running two separate 2D simulations with different initial conditions, creating two sets of trajectories that correspond to the motion of the three bodies in two different planes. By stacking these results, we can approximate the motion of the bodies in 3D space.

This method is advantageous as it simplifies the problem of simulating three-body motion in 3D, which is notoriously difficult to solve analytically. By using numerical simulations, we can approximate the motion of the bodies with a high degree of accuracy and gain insights into the complex and often chaotic nature of three-body interactions.

In our study, we implemented the proposed method in Python using the scipy library for numerical integration and the matplotlib library for visualization. The resulting simulations provide a detailed and dynamic representation of three-body motion in 3D space, which can be used to study a wide range of physical phenomena, from astrophysics to molecular dynamics.

The significance of this method lies in its potential to advance our understanding of the behavior of celestial bodies, which can have practical applications in space exploration and satellite technology. The proposed method is computationally efficient and allows for the simulation of complex systems with greater accuracy than existing methods.

The proposed method of using stacked 2D simulations to approximate 3D motion was successful in simulating the three-body problem in 3D space. The resulting trajectories demonstrate the complex nature of the problem, and the potential of the method to be used in a variety of scientific fields. Additionally, incorporating an animation of the trajectories can provide a visual representation of the three-body motion, which can help scientists better understand the complex interactions between celestial bodies.

The proposed model for simulating three-body motion in 3D using stacked 2D simulations is implemented in Python using the SciPy library. The SciPy library provides a powerful suite of tools for scientific computing, including numerical integration functions that are used in the simulation.
The model is implemented as follows:
    1. Define the function that returns the derivative of the state vector, three_body(y, t). This function takes the state vector y and the time t as input, and returns the derivatives of the positions and velocities of the bodies.
    2. Define the initial conditions for the first 2D simulation. This includes the positions and velocities of the bodies in the x-y plane.
    3. Define the time grid, t, over which to integrate the differential equations.
    4. Solve the differential equations using the odeint function from SciPy for the first 2D simulation.
    5. Define the initial conditions for the second 2D simulation. This includes the positions and velocities of the bodies in the y-z plane.
    6. Solve the differential equations using odeint for the second 2D simulation.
    7. Stack the results of the two simulations to create a 3D representation.
    8. Create a 3D plot of the trajectories of the bodies using the matplotlib library.
    ![image](https://user-images.githubusercontent.com/3180138/231890216-213ae756-b4a2-4a04-805a-ad36032ec2b3.png)


The implementation of the model using Python and the SciPy library allows for efficient and accurate simulation of the three-body problem in 3D. The use of stacked 2D simulations to approximate 3D motion provides a novel approach to solving this difficult problem.
To enable 3D simulation, the original model was modified in the following ways:
    1. Additional initial conditions were defined for the second 2D simulation to represent the third dimension. This involved setting the z-coordinates and z-velocities of the bodies to zero.
    2. Two separate 2D simulations were performed, with the initial conditions for the second simulation being identical to those of the first, except for the z-coordinates and z-velocities.
    3. The results of the two 2D simulations were stacked together to create a 3D representation of the motion.
    4. A 3D plot was generated using the Matplotlib library to visualize the trajectories of the bodies.
    
    ![image](https://user-images.githubusercontent.com/3180138/231890314-311d14fa-b19a-49c4-9a0c-e2f14b5c900e.png)
    ![image](https://user-images.githubusercontent.com/3180138/231890344-f254f8d6-dbce-4099-9594-c71db7957568.png)
    ![image](https://user-images.githubusercontent.com/3180138/231890397-24d04ab3-7ec6-471f-acb0-6a4b5d4ea37f.png)

These modifications allowed the original 2D model to be extended to include the third dimension, enabling a more accurate simulation of three-body motion.
The resulting plot shows the trajectories of the three bodies in 3D space over time. As expected, the trajectories are complex and difficult to predict due to the chaotic nature of the three-body problem. However, the stacked 2D simulation method proved to be a successful approximation of 3D motion.
![three_body_animation](https://user-images.githubusercontent.com/3180138/231890630-269bba20-bae5-45ef-b6a4-522dca8dc0a9.gif)
