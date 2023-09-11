import matplotlib.pyplot as plt


def drawMidPointCircle(radius):
    x = 0
    y = radius
    d = 1 - radius
    # print("d = 1 - radius")
    points = []  # List to store the circle points
    print("i\tx\ty\td\tnew_x\tnew_y")
    i = 0
    while x <= y:
        # print("{}\t{}\t\t{}\t{}".format(i, d, x, y))
        row = [i, x, y, d]
        points.append((x, y))
        points.append((-x, y))
        points.append((x, -y))
        points.append((-x, -y))
        points.append((y, x))
        points.append((-y, x))
        points.append((y, -x))
        points.append((-y, -x))

        if d < 0:
            d = d + 2 * x + 3
            # print("d = d + 2 * x + 3")
        else:
            d = d + 2 * (x - y) + 5
            # print("d = d + 2 * (x - y) + 5")
            y -= 1
        x += 1
        i += 1
        # print("\t{}\t{}".format(x, y))
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
    plt.title("Mid Point Circle Drawing Algorithm")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == "__main__":
    # radius = int(input("Enter the radius of the circle: "))
    radius = 7
    points = drawMidPointCircle(radius)
    plotCircle(points)
