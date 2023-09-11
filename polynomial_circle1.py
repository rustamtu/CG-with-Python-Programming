import matplotlib.pyplot as plt
import math


def plot_circle_polynomial(radius):
    x = 0
    y = radius

    points = []  # List to store the circle points

    while x <= y:
        points.append((x, y))
        points.append((-x, y))
        points.append((x, -y))
        points.append((-x, -y))
        points.append((y, x))
        points.append((-y, x))
        points.append((y, -x))
        points.append((-y, -x))
        print(x, y)
        x += 1
        y = abs(math.sqrt(radius * radius-x * x))
        print(x, y)

    return points


def plotCircle(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    plt.scatter(x_coords, y_coords, color='red')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linewidth=0.5, linestyle='--', color='gray')
    plt.title("Polynomial Circle Drawing Algorithm")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == "__main__":
    # radius = int(input("Enter the radius of the circle: "))
    radius = 20
    points = plot_circle_polynomial(radius)
    plotCircle(points)
