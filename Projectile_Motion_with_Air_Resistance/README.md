# Projectile Motion Simulation with Air Resistance
This repository contains a numerical simulation of projectile motion, considering air resistance and altitude-dependent gravitational acceleration. The simulation is implemented in Julia and uses the Runge-Kutta 4th order (RK4) method for solving the system of differential equations.
## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [Output](#output)
- [License](#license)
---
## Overview
The simulation models the motion of a projectile launched at an initial velocity and angle. It accounts for:
- **Air resistance**: Drag force is calculated using a quadratic drag model, with air density decreasing exponentially with altitude.
- **Gravitational acceleration**: Gravity decreases with altitude according to the inverse-square law.
- **Numerical integration**: The RK4 method is used to solve the system of differential equations governing the projectile's motion.
---
## Features
- **Altitude-dependent air density**: Air density decreases exponentially with height, following the barometric formula.
- **Altitude-dependent gravity**: Gravitational acceleration decreases with altitude, based on the inverse-square law.
- **Quadratic drag model**: Drag force is proportional to the square of the velocity and the cross-sectional area of the projectile.
- **RK4 integration**: High-accuracy numerical integration for solving the equations of motion.
---
## Requirements
To run the simulation, you need:
- **Julia**: Download and install Julia from [julialang.org](https://julialang.org/).
- **No additional packages**: The simulation uses only base Julia functionality.
---
## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/projectile-motion-simulation.git
   cd projectile-motion-simulation
   ```
2. Run the simulation:
   ```bash
   julia simulation.jl
   ```
3. View the results:
   - The simulation outputs a CSV file (`simulation.csv`) containing the time, position, and velocity of the projectile at each time step.
   - You can visualize the results using your preferred data analysis tool (e.g., Python, MATLAB, or Julia's Plots.jl).
---
## Implementation Details
### Equations of Motion
The following differential equations govern the motion of the projectile:

$$\frac{dx}{dt} = v_x, \quad \frac{dy}{dt} = v_y$$

$$\frac{dv_x}{dt} = -\frac{F_{\text{drag}, x}}{m}, \quad \frac{dv_y}{dt} = -g(y) - \frac{F_{\text{drag}, y}}{m}$$

where:
- $F_{\text{drag}} = \frac{1}{2} c \rho(y) A v^2$ is the drag force,
- $\rho(y) = \rho_0 e^{-y/H_n}$ is the air density at altitude $y$,
- $g(y) = g_0 \left(1 + \frac{y}{r}\right)^{-2}$ is the gravitational acceleration at altitude $y$.
### Numerical Integration
The RK4 method is used to solve the system of differential equations. This method provides high accuracy by combining the results of four intermediate steps.
### Parameters
The following constants are used in the simulation:
- Initial velocity ($v_i$): 11.0 m/s
- Launch angle ($\theta$): 30°
- Drag coefficient ($c$): 0.5 (for a sphere)
- Air density at sea level ($\rho_0$): 1.293 kg/m³
- Scale height ($H_n$): 10,400 m
- Diameter of projectile ($D$): 2.0 m
- Mass of projectile ($m$): 0.001 kg
- Gravitational acceleration at sea level ($g_0$): 9.8 m/s²
- Radius of Earth ($r$): 6.4 × 10⁶ m
- Time step ($dt$): 1 × 10⁻⁴ s
---
## Output
The simulation generates a CSV file (`simulation.csv`) with the following columns:
- `t`: Time (in seconds)
- `x`: Horizontal position (in meters)
- `y`: Vertical position (in meters)
- `vx`: Horizontal velocity (in meters/second)
- `vy`: Vertical velocity (in meters/second)
You can use this data to analyze the projectile's trajectory, velocity, and other properties.
