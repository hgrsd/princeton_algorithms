import sys
import randomised_queue

"""
Part of week 2's assignment of the Princeton Algorithm (Part I) course on Coursera,
see http://coursera.cs.princeton.edu/algs4/assignments/queues.html.

To be used as a driver for randomised_queue.py.

This programme reads in a number of strings and, after user input stops, prints out a number of
strings at random, dequeue-ing them from the randomised queue.
"""


def main():
    rq = randomised_queue.RandomisedQueue()
    # default of 5 repeats, if no command-line argument is given
    repeats = 5 if len(sys.argv) == 1 else sys.argv[1]
    while True:
        string = input("Enter string: ")
        if not string:
            break
        else:
            rq.enqueue(string)
    for _ in range(repeats):
        print(rq.dequeue())


if __name__ == "__main__":
    main()

