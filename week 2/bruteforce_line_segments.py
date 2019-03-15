import point
from matplotlib import pyplot as plt


def find_segments(points, length):
    """ Finds and returns a list of line segments that connect four collinear points """
    segments = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            collinears = [points[i].coordinates, points[j].coordinates]
            for k in range(j + 1, len(points)):
                if points[i].slope_to(points[j]) == points[i].slope_to(points[k]) \
                        and points[j].compare_to(points[k]) != 0:
                    collinears.append(points[k].coordinates)
            if len(collinears) > length - 1:
                segments.append(collinears)
    return segments


def plot_points(points, segments):
    for point in points:
        plt.scatter(*point.coordinates)
    for segment in segments:
        for coordinate in segment:
            print(coordinate)
        x = sorted([coordinate[0] for coordinate in segment])
        y = sorted([coordinate[1] for coordinate in segment])
        plt.plot(x, y)
    plt.show()


a = point.Point(0, 9)
b = point.Point(0, 14)
c = point.Point(0, 19)
d = point.Point(12, 20)
e = point.Point(0, 23)
f = point.Point(-1, 0)
g = point.Point(3, 5)
h = point.Point(6, 10)
i = point.Point(9, 15)
j = point.Point(4, 15)
points = [a, b, c, d, e, f, g, h, i, j]

plot_points(points, find_segments(points, 4))
