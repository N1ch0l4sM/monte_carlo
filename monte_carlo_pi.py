import random
import matplotlib.pyplot as plt

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

plt.plot(range(1, num_points + 1), pi_estimates)
plt.axhline(y=3.141592653589793, color='r', linestyle='--', label='Actual Value of Pi')
plt.xlabel('Number of Points')
plt.ylabel('Estimated Pi Value')
plt.title('Monte Carlo Estimation of Pi')
plt.legend()
plt.show()