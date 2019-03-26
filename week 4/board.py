from copy import deepcopy

class Board:
    """
    Implements the Board class, pursuant to the week 4 assignment of the Princeton
    Algorithms Course (Part I) on Coursera, see
    http://coursera.cs.princeton.edu/algs4/assignments/8puzzle.html
    """

    def __init__(self, board, goal=None, moves_made=0, previous=None):
        self._board = board
        self._moves_made = moves_made
        self._goal = goal
        self._dimension = len(self._board)
        self._previous = previous

    def __eq__(self, other):
        for row in range(self._dimension):
            for col in range(self._dimension):
                if self._board[row][col] != other._board[row][col]:
                    return False
        return True

    def __str__(self):
        """ Pretty print function """

        ret_str = f"dimensions: {self._dimension}\n"
        ret_str += " "
        for _ in range(self._dimension * 3 + 1):
            ret_str += "-"
        ret_str += " \n"
        for row in range(self._dimension):
            ret_str += "|"
            for col in range(self._dimension):
               ret_str += str.rjust(f" {self._board[row][col] if self._board[row][col] != 0 else ' '}", 3, " ")
            ret_str += " |\n"
        ret_str += " "
        for _ in range(self._dimension * 3 + 1):
            ret_str += "-"
        ret_str += "\n"
        return ret_str

    # compares manhattan functions of self and other, for use in min pq
    def __lt__(self, other):
        return self.manhattan() < other.manhattan()

    def coordinates(self, number):
        """ Returns (row, col) tuple of the index of the number sought """

        for row in range(self._dimension):
            for col in range(self._dimension):
                if self._board[row][col] == number:
                    return row, col
        return None

    def hamming(self):
        """ Returns hamming score of a board compared to the goal board, plus one for every move made """

        if not self._goal:
            raise AttributeError("This Board does not point to a goal. Are you running "
                                 "the hamming() method of the goal Board itself?")
        total_score = 0
        for row in range(self._dimension):
            for col in range(self._dimension):
                if self._board[row][col] != 0 and self._board[row][col] != self._goal._board[row][col]:
                    total_score += 1
        return total_score + self._moves_made

    def manhattan(self):
        """ Returns manhattan score of a board compared to the goal board, plus one for every move made """

        if not self._goal:
            raise AttributeError("This Board does not point to a goal. Are you running "
                                 "the manhattan() method of the goal Board itself?")
        total_score = 0
        for row in range(self._dimension):
            for col in range(self._dimension):
                if self._board[row][col] != 0:
                    goal_row, goal_col = self._goal.coordinates(self._board[row][col])
                    total_score += abs(row - goal_row) + abs(col - goal_col)
        return total_score + self._moves_made

    def is_goal(self):
        return self == self._goal

    @property
    def neighbours(self):
        neighbours = []
        zero_row, zero_col = self.coordinates(0)
        if zero_col != 0:
            # exchange left
            board_new = deepcopy(self._board)
            board_new[zero_row][zero_col], board_new[zero_row][zero_col - 1] = board_new[zero_row][zero_col - 1], \
                                                                               board_new[zero_row][zero_col]
            neighbour = Board(board_new, goal=self._goal, moves_made=self._moves_made + 1, previous=self)
            # make sure neighbour isn't the same as the previous board
            if not self._previous or neighbour != self._previous:
                neighbours.append(neighbour)
        if zero_col != self._dimension - 1:
            # exchange right
            board_new = deepcopy(self._board)
            board_new[zero_row][zero_col], board_new[zero_row][zero_col + 1] = board_new[zero_row][zero_col + 1], \
                                                                               board_new[zero_row][zero_col]
            neighbour = Board(board_new, goal=self._goal, moves_made=self._moves_made + 1, previous=self)
            if not self._previous or neighbour != self._previous:
                neighbours.append(neighbour)
        if zero_row != 0:
            # exchange above
            board_new = deepcopy(self._board)
            board_new[zero_row][zero_col], board_new[zero_row - 1][zero_col] = board_new[zero_row - 1][zero_col], \
                                                                               board_new[zero_row][zero_col]
            neighbour = Board(board_new, goal=self._goal, moves_made=self._moves_made + 1, previous=self)
            if not self._previous or neighbour != self._previous:
                neighbours.append(neighbour)
        if zero_row != self._dimension - 1:
            # exchange below
            board_new = deepcopy(self._board)
            board_new[zero_row][zero_col], board_new[zero_row + 1][zero_col] = board_new[zero_row + 1][zero_col], \
                                                                               board_new[zero_row][zero_col]
            neighbour = Board(board_new, goal=self._goal, moves_made=self._moves_made + 1, previous=self)
            if not self._previous or neighbour != self._previous:
                neighbours.append(neighbour)
        return neighbours

    @property
    def previous(self):
        return self._previous

    @property
    def dimension(self):
        return self._dimension

    @property
    def moves_made(self):
        return self._moves_made

    @property
    def twin(self):
        """ Returns a 'twin' of this board, with a single swap (not involving the 0 element) made. """

        new_board = deepcopy(self._board)
        zero_row = self.coordinates(0)[0]
        if zero_row != 0:
            new_board[0][0], new_board[0][1] = new_board[0][1], new_board[0][0]
        else:
            new_board[1][0], new_board[1][1] = new_board[1][1], new_board[1][0]
        return Board(new_board, self._goal, self._moves_made, self._previous)


