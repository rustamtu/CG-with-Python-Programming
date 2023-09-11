import matplotlib.pyplot as plt


def findN(radius):
    for i in range(1, radius):
        if pow(2, i) > radius:
            print(pow(2, i))
            return i


def draw_circle_DDA(center_x, center_y, radius):
    y = radius
    x = 0
    points = []
    i = 0
    n = findN(radius)
    # 0.0156  # for r=50, n=6, 50<64 eps=2^(-n) s.t. 2^(n-1)<r<2^n
    eps = pow(2, -n)
    print([radius, n, eps])
    print("i\tx\ty\tnew_x\tnew_y")
    while x <= y:

        row = [i, x, y]
        # print(x, y)
        points.append((x + center_x, y + center_y))
        points.append((y + center_x, x + center_y))
        points.append((-x + center_x, y + center_y))
        points.append((-y + center_x, x + center_y))
        points.append((-x + center_x, -y + center_y))
        points.append((-y + center_x, -x + center_y))
        points.append((x + center_x, -y + center_y))
        points.append((y + center_x, -x + center_y))
        x += eps*y
        y -= eps*x
        i += 1
        row.append(x)
        row.append(y)
        print(row)

    x_coords, y_coords = zip(*points)
    plt.plot(x_coords, y_coords, 'bo')
    plt.axis('equal')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Circle Drawing using DDA1 Algorithm')
    plt.grid()
    plt.show()


# Set the circle's center and radius
center_x = 0
center_y = 0
radius = 10

# Draw the circle using DDA algorithm
draw_circle_DDA(center_x, center_y, radius)
# n = findN(radius)
# print(n)
