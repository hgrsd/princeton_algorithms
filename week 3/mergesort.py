"""
Generic merge sort implementation.
Use by calling sort(), passing in the sortable sequence, lo, hi and a pointer to the compare function to be used.
"""


def sort(sortable, lo, hi, compare_function):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    sort(sortable, lo, mid, compare_function)
    sort(sortable, mid + 1, hi, compare_function)
    merge(sortable, lo, mid, hi, compare_function)


def merge(sortable, lo, mid, hi, compare_function):
    sortable_copy = sortable.copy()
    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            sortable[k] = sortable_copy[j]
            j += 1
        elif j > hi:
            sortable[k] = sortable_copy[i]
            i += 1
        elif compare_function(sortable_copy[j], sortable_copy[i]):
            sortable[k] = sortable_copy[j]
            j += 1
        else:
            sortable[k] = sortable_copy[i]
            i += 1
