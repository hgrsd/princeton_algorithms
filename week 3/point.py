import math


class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"{(self.x, self.y)}"

    @property
    def coordinate(self):
        return [self.x, self.y]

    def compare_to(self, other):
        """Returns -1 if self < other, 0 if equal, 1 if self > other"""
        if not isinstance(other, Point):
            raise TypeError("Can only compare type Point to type Point")
        if self.y < other.y:
            return -1
        elif self.y > other.y:
            return 1
        elif self.x < other.x:
            return -1
        elif self.x > other.x:
            return 1
        else:
            return 0

    def slope_to(self, other):
        # points are identical
        if not self.compare_to(other):
            return -math.inf
        # slope is vertical
        elif self.x == other.x:
            return math.inf
        # slope is horizontal
        elif self.y == other.y:
            return 0
        else:
            return (other.y - self.y) / (other.x - self.x)

    def compare_slope(self, point_one, point_two):
        slope_1, slope_2 = self.slope_to(point_one), self.slope_to(point_two)
        if slope_1 < slope_2:
            return -1
        elif slope_1 > slope_2:
            return 1
        else:
            return 0
