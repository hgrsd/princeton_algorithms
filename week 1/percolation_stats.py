import percolation
import sys
import random
from time import perf_counter

"""
Driver for percolation.py
Use: python percolation_stats.py <number of repeats> <grid size>
"""


def main():

    if len(sys.argv) < 3:
        print(f"Usage: python(3) {sys.argv[0]} <number of repeats> <grid size>")
        return False

    repeats = int(sys.argv[1])
    size = int(sys.argv[2])
    total_runtime = 0
    total_fraction = 0

    print(f"\n[+] Starting {repeats} runs with a {size}*{size} grid.\n")
    for i in range(repeats):
        perc = percolation.Percolation(size)
        start = perf_counter()
        for _ in range(int(0.535 * size ** 2)):
            perc.open(random.randint(0, size - 1), random.randint(0, size - 1))
        while not perc.percolates():
            perc.open(random.randint(0, size - 1), random.randint(0, size - 1))
        stop = perf_counter()
        elapsed = stop - start
        fraction = perc.open_sites / size ** 2
        total_runtime += elapsed
        total_fraction += fraction
        print(f"\trun {i + 1}:\t\tfraction: {fraction:.4f}.\truntime: {elapsed:.2f}")

    avg_runtime = total_runtime / repeats
    avg_fraction = total_fraction / repeats
    print(f"\n[+] Completed.\n\n"
          f"\t* avg fraction: \t{avg_fraction:.4f} ({avg_fraction * size**2}/{size**2})\n"
          f"\t* avg runtime: \t\t{avg_runtime:.2f}s\n")


if __name__ == "__main__":
    main()

