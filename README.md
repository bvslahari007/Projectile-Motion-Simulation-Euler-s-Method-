# Projectile Motion Simulation (Euler’s Method)

This is a simple project where I simulated projectile motion in Python using the semi-implicit Euler method.  
The idea was to model a particle moving under gravity, see how the trajectory looks, and make an animation to visualize it.

Animation at dt = 0.1s

## Features
- Simulates 2D projectile motion using basic physics
- Implements the semi-implicit Euler method for numerical integration
- Static trajectory plot with Matplotlib
- Animated motion using FuncAnimation
- Particle class that keeps the motion logic clean and reusable

## How it Works
1. Define the initial position, velocity, and acceleration of the particle
2. Update velocity and position step by step with Euler’s method at each small time interval `dt`
3. Collect the trajectory points while the particle is in motion
4. Visualize the results:
   - Static plot of the trajectory  
   - Animated simulation of the motion

(Here the simulation uses a time step of `dt = 0.1` for updating the motion.  
Smaller `dt` values make the simulation more accurate but slower, while larger values make it faster but less precise.)

## What I Learned
- How to write and use classes in Python
- Working with Matplotlib for both plots and animations
- Basics of numerical simulation with Euler’s method
- How physics equations can be turned into actual code

