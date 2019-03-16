import point
from matplotlib import pyplot as plt

"""
This is an implementation of week 3's 'brute force collinear' programming assignment of the Princeton
Algorithms course (Part I). See http://coursera.cs.princeton.edu/algs4/assignments/collinear.html.

Intead of using a sorting algorithm, like fast_collinears.py, it has three nested loops to cycle through
all points and compare them to all other points. This means that the programme operates in O(N^3). 
"""

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


points = []
while True:
    print(f"Current points: ", points)
    user_input = input("Enter x, y to add new point, empty string to find collinears for current points: ")
    if user_input == "":
        plot_points(points, find_segments(points, 4))
    else:
        x, y = user_input.split(",")
        points.append(point.Point(int(x), int(y)))

