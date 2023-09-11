import matplotlib.pyplot as plt
import numpy as np


def plot_circle(center_x, center_y, radius):
    theta = np.linspace(0, 2*np.pi, 100)
    x = center_x + radius * np.cos(theta)
    y = center_y + radius * np.sin(theta)

    plt.plot(x, y)
    plt.axis('equal')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Circle Using Polynomial Equation')
    plt.grid()
    plt.show()


# Circle parameters
center_x = 0
center_y = 0
radius = 5

plot_circle(center_x, center_y, radius)
