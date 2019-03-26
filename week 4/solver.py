from board import Board
from min_pq import MinPQ


class Solver:
    """
    Implementation of the Solver class, pursuant to the week 4 assignment of the Princeton
    Algorithms Course (Part I) on Coursera, see
    http://coursera.cs.princeton.edu/algs4/assignments/8puzzle.html
    """

    def __init__(self, initial):
        self._initial = initial
        self.path = None
        self._final_board = self._solve(initial)
        if self._final_board:
            self.path = self._path()
            self.number_moves = len(self.path) - 1

    def _path(self):
        """
        Returns a list containing the path found.
        Simply starts at the final board (the solution), and follows each Board's
        previous property until the initial board is reached.
        """

        board = self._final_board
        path = [board]
        while board.previous is not None:
            path.append(board.previous)
            board = board.previous
        return path[::-1]

    @classmethod
    def _solve(cls, board):
        queue = MinPQ()
        queue_twin = MinPQ()
        twin = board.twin
        while not board.is_goal():
            # get the neighbours
            neighbours = board.neighbours
            # insert neighbours in the min pq
            for neighbour in neighbours:
                queue.insert(neighbour)
            # pop min (= lowest manhattan score) board from the min pq
            board = queue.del_min()

            # run through the same steps for twin board and check if it's solved
            twin_neighbours = twin.neighbours
            for neighbour in twin_neighbours:
                queue_twin.insert(neighbour)
            twin = queue_twin.del_min()
            if twin.is_goal():
                # twin is solved, which means that our actual board is unsolvable
                return None
        # return the final board
        return board
