import point
import mergesort

from matplotlib import pyplot as plt

"""
This is an implementation of week 3's 'fast collinears' programming assignment of the Princeton
Algorithms course (Part I). See http://coursera.cs.princeton.edu/algs4/assignments/collinear.html.

The programme iterates through all points, generating a sorted list of the slopes to all other points,
using Merge Sort. This operates in O(N log N).

It then loops through the sorted list to find the required number of collinear points.
"""


def find_segments(points, length):
    """
    Finds and returns a list of line segments that connect at least length collinear points

    TODO: Implement sliding window technique rather than for loop for further performance gain
    """
    segments = []
    # Loop through all points
    for i in range(len(points) - 1):
        # Set origin to the current point
        collinears = []
        origin = points[i]
        # Create a list of tuples (slope from origin, point) for all points
        slopes = [(origin.slope_to(point), point) for point in points]
        # Sort the tuples by slope from origin using Merge Sort
        mergesort.sort(slopes, 0, len(points) - 1, lambda a, b: a[0] < b[0])
        # Loop through all points, apart from origin, in the sorted list of slopes
        for j in range(1, len(slopes) - 1):
            found = 0
            k = 0
            # Check the slopes at j and j + k, and increment number of collinears found if equal
            # Because the list of slopes is sorted, we can simply stop looping if the next slope
            # doesn't match the current slope, and go to the next point.
            while j + k < len(slopes) and slopes[j][0] == slopes[j+k][0]:
                found += 1
                k += 1
            # If we have found at least length - 1 collinears, we loop through them
            # and add each one to our list
            if found >= length - 1:
                collinears = [origin]
                for x in range(0, found):
                    collinears.append(slopes[j+x][1])
        # If we have found enough collinears, collinears won't be None and we append them to our found segments
        if collinears:
            segments.append(collinears)

    return segments


def plot_points(points, segments):
    """
    Plots all points and line segments between them.
    """
    for point in points:
        plt.scatter(*point.coordinates)
    for segment in segments:
        # Sort all x and y values in ascending order so that we can plot the line segments
        x = sorted([coordinate.coordinates[0] for coordinate in segment])
        y = sorted([coordinate.coordinates[1] for coordinate in segment])
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
