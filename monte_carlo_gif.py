import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import PIL

def estimate_pi(num_points):
    points_inside_circle = 0
    points_inside_square = 0
    pi_estimates = []
    
    for i in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        distance = x**2 + y**2
        
        if distance <= 1:
            points_inside_circle += 1
        
        points_inside_square += 1
        
        pi_estimate = 4 * (points_inside_circle / points_inside_square)
        pi_estimates.append(pi_estimate)
        
    return pi_estimates

num_points = 1000
pi_estimates = estimate_pi(num_points)

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.axhline(y=3.141592653589793, color='r', linestyle='--', label='Actual Value of Pi')
ax.set_xlabel('Number of Points')
ax.set_ylabel('Estimated Pi Value')
ax.set_title('Monte Carlo Estimation of Pi')
ax.legend()

x_data = list(range(1, num_points + 1))
y_data = pi_estimates

def update(frame):
    line.set_data(x_data[:frame], y_data[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(x_data), interval=200, blit=True)
ani.save('pi_estimation.gif', writer='pillow')