import matplotlib.pyplot as plt


def draw_circle_DDA(center_x, center_y, radius):
    y = radius
    x = 0
    # points = [(x + center_x, y + center_y)]
    points = []
    # print(x, y)
    i = 0
    print("i\tx\ty\td\tnew_x\tnew_y")
    while x <= y:
        d = x**2 + y**2 - radius**2
        row = [i, x, y, d]
        if d >= 0:
            y -= 1
        # print(x, y)
        points.append((x + center_x, y + center_y))
        points.append((y + center_x, x + center_y))
        points.append((-x + center_x, y + center_y))
        points.append((-y + center_x, x + center_y))
        points.append((-x + center_x, -y + center_y))
        points.append((-y + center_x, -x + center_y))
        points.append((x + center_x, -y + center_y))
        points.append((y + center_x, -x + center_y))
        x += 1
        i += 1
        row.append(x)
        row.append(y)
        print(row)

    x_coords, y_coords = zip(*points)
    plt.plot(x_coords, y_coords, 'bo')
    plt.axis('equal')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Circle Drawing using DDA Algorithm')
    plt.grid()
    plt.show()


# Set the circle's center and radius
center_x = 0
center_y = 0
radius = 10

# Draw the circle using DDA algorithm
draw_circle_DDA(center_x, center_y, radius)
