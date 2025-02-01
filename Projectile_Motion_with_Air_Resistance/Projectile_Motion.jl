# Constants
const vi = 11.0  # meters/second
const theta = 30.0  # degrees
const c = 0.5  # drag coefficient for sphere
const row_o = 1.293  # density kg/m^3
const H_n = 10400.0  # scale height in meters
const D = 2.0  # Diameter of projectile cross-section
const R = D/2  # Radius of projectile cross-section
const A = π*R^2  # Area of cross-section
const g_o = 9.8  # gravitational acceleration meter/second^2
const x_o = 0.0  # starting x position
const y_o = 0.0  # starting y position
const r = 6.4e6  # radius of Earth in meters
const m = 0.001  # mass of projectile in kg
const dt = 1e-4  # time step in seconds

# Initial conditions
const vx_o = vi*cos(deg2rad(theta))
const vy_o = vi*sin(deg2rad(theta))

# Function to calculate air density at given height
function air_density(y)
    return row_o * exp(-y/H_n)  # Fixed: removed extra parentheses
end

# Function to calculate gravitational acceleration at given height
function grav_accel(y)
    return g_o * (1 + y/r)^(-2)
end

# Define the system of differential equations
function derivatives(state)
    x, y, vx, vy = state
    
    # Calculate current air density
    row = air_density(y)
    
    # Calculate velocity magnitude
    v_mag = sqrt(vx^2 + vy^2)
    
    # Common drag term
    drag_factor = 0.5 * c * row * A * v_mag / m
    
    # Return derivatives [dx/dt, dy/dt, dvx/dt, dvy/dt]
    return [
        vx,  # dx/dt
        vy,  # dy/dt
        -drag_factor * vx,  # dvx/dt
        -grav_accel(y) - drag_factor * vy  # dvy/dt
    ]
end

# RK4 step function
function rk4_step(state, dt)
    k1 = derivatives(state)
    k2 = derivatives(state .+ 0.5 * dt * k1) 
    k3 = derivatives(state .+ 0.5 * dt * k2)
    k4 = derivatives(state .+ dt * k3) 
    
    return state .+ (dt/6.0) * (k1 .+ 2k2 .+ 2k3 .+ k4)
end

# Simulation
function run_simulation()
    # Initial state vector [x, y, vx, vy]
    state = [x_o, y_o, vx_o, vy_o]
    
    # Added: Time variable for output
    t = 0.0
    
    # Open file for writing
    open("simulation.csv", "a") do file
        # Write header
        println(file, "t,x,y,vx,vy")
        
        # Run simulation until y becomes negative
        while state[2] >= y_o
            # Write current state to file
            println(file, "$(t),$(join(state, ','))")
            
            # Calculate next state using RK4
            state = rk4_step(state, dt)
            t += dt
        end
    end
end

# Run the simulation
run_simulation()
