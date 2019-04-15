from solver import Solver
from board import Board


""" 
Driver for the 8-puzzle solver, part of week 4's assignment of the 
Princeton Algorithms course (part I) on Coursera, see
http://coursera.cs.princeton.edu/algs4/assignments/8puzzle.html
"""


def main():
    # testing with 4 dimensions
    goal = Board([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]])

    initial_board = Board([
        [1, 2, 5, 4],
        [3, 6, 7, 8],
        [10, 9, 11, 12],
        [13, 14, 15, 0]], goal=goal)

    solver = Solver(initial_board)
    # solver.path is None if board is unsolvable
    if solver.path:
        print(f"Found a path in {solver.number_moves} moves.")
        for board in solver.path:
            print(board)
    else:
        print("This board is unsolvable.")


if __name__ == "__main__":
    main()
