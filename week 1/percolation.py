import quickunion

class Percolation:
    """
    This class is a Python implementation of the week 1 programming assignment of the Princeton Algorithms course
    on Coursera. See http://coursera.cs.princeton.edu/algs4/assignments/percolation.html

    A 2d grid of n*n "sites" is initialised, consisting of only "closed" sites. Then, an increasing amounts of
    sites are opened and connected to up to four adjacent open sites (left, up, right, down), if any.

    Sites are opened until the grid "percolates", that is, until there is a route of connected sites from the top of the
    grid to the bottom. The user can then calculate the fraction of open sites, using the open_sites property.
    This means that this class may be used in the Monte Carlo method to run a large volume of simulations,
    in an attempt to converge upon a fraction of open sites at which percolation becomes (nearly) guaranteed.
    """

    def __init__(self, gridsize):
        self.gridsize = gridsize
        self._grid = [[0 for _ in range(gridsize)] for _ in range(gridsize)]
        self._open_sites = 0
        self.quickunion = quickunion.QuickUnion(gridsize ** 2)

    def _flatten(self, row, col):
        return row * self.gridsize + col

    def open(self, row, col):
        if not self.is_open(row, col):
            self._grid[row][col] = 1
            self._open_sites += 1
            # if left is open, make connection
            if col > 0 and self.is_open(row, col - 1):
                self.quickunion.union(self._flatten(row, col), self._flatten(row, col - 1))
            # if right is open, make connection
            if col < self.gridsize - 1 and self.is_open(row, col + 1):
                self.quickunion.union(self._flatten(row, col), self._flatten(row, col + 1))
            # if up is open, make connection
            if row > 0 and self.is_open(row - 1, col):
                self.quickunion.union(self._flatten(row, col), self._flatten(row - 1, col))
            # if down is open, make connection
            if row < self.gridsize - 1 and self.is_open(row + 1, col):
                self.quickunion.union(self._flatten(row, col), self._flatten(row + 1, col))
            return True
        else:
            return False

    def is_open(self, row, col):
        return bool(self._grid[row][col])

    def is_full(self, row, col):
        open_top = [(0, y) for y in range(self.gridsize) if self.is_open(0, y)]
        for x, y in open_top:
            if self.quickunion.is_connected(self._flatten(x, y), self._flatten(row, col)):
                return True
        return False

    @property
    def open_sites(self):
        return self._open_sites

    def percolates(self):
        open_bottom = [(self.gridsize - 1, y) for y in range(self.gridsize) if self.is_open(self.gridsize - 1, y)]
        for x, y in open_bottom:
            if self.is_full(x, y):
                return True
        return False

    def print_grid(self):
        for row in self._grid:
            for col in row:
                print(" " if col == 0 else "o", end="")
            print("")
