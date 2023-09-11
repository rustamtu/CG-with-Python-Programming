import matplotlib.pyplot as plt


def drawBresenhamCircle(radius):
    x = 0
    y = radius
    d = 3 - 2 * radius

    points = []  # List to store the circle points
    i = 0
    print("i\tx\ty\td\tnew_x\tnew_y")
    while x <= y:
        points.append((x, y))
        points.append((-x, y))
        points.append((x, -y))
        points.append((-x, -y))
        points.append((y, x))
        points.append((-y, x))
        points.append((y, -x))
        points.append((-y, -x))

        row = [i, x, y, d]
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1
        i += 1
        row.append(x)
        row.append(y)
        print(row)

    return points


def plotCircle(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    plt.scatter(x_coords, y_coords, color='red')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linewidth=0.5, linestyle='--', color='gray')
    plt.title("Bresenham's Circle Drawing Algorithm")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == "__main__":
    # radius = int(input("Enter the radius of the circle: "))
    radius = 10
    points = drawBresenhamCircle(radius)
    plotCircle(points)

# circle_midPoint.py
# d = 1 - radius
# if d < 0:
#     d = d + 2 * x + 3
# else:
#     d = d + 2 * (x - y) + 5
#     y -= 1

# i	x	y	d	new_x	new_y
# [0, 0, 10, -9, 1, 10]
# [1, 1, 10, -6, 2, 10]
# [2, 2, 10, -1, 3, 10]
# [3, 3, 10, 6, 4, 9]
# [4, 4, 9, -3, 5, 9]
# [5, 5, 9, 8, 6, 8]
# [6, 6, 8, 5, 7, 7]
# [7, 7, 7, 6, 8, 6]


# circle_Bresenham
# d = 3 - 2 * radius
# if d < 0:
# 	d = d + 4 * x + 6
# else:
# 	d = d + 4 * (x - y) + 10
# 	y -= 1

# i	x	y	d	new_x	new_y
# [0, 0, 10, -17, 1, 10]
# [1, 1, 10, -11, 2, 10]
# [2, 2, 10, -1, 3, 10]
# [3, 3, 10, 13, 4, 9]
# [4, 4, 9, -5, 5, 9]
# [5, 5, 9, 17, 6, 8]
# [6, 6, 8, 11, 7, 7]
# [7, 7, 7, 13, 8, 6]
