import ctypes
import random


class RandomisedQueue:
    """
    This class implements a randomised queue of dynamic size, containing arbitrary types.
    The implementation follows the specification given by the week 2 programming assignment
    of the Princeton Algorithms course (Part I), at http://coursera.cs.princeton.edu/algs4/assignments/queues.html

    The specifications stipulated that the operation of the randomised queue must take amortised constant time.
    This means that, in contrast to the deque class in this same week, it does not use a linked list (which
    operates in worst-case constant time, rather than amortised constant time), but a dynamically-sized array.

    Given that the assignment was in large part about implementing such a dynamically-sized array, using repeated
    doubling, it was pointless to use any of the Python built-in types such as a list. Therefore, I have used
    a fixed-length array of py_objects, using the ctypes library. This is, of course, a slightly contrived use case,
    but it is justified by the educational value of the assignment.
    """

    def __init__(self):
        self._n_elements = 0
        self._array_size = 1
        self._array = (1 * ctypes.py_object)()

    def __iter__(self):
        # create a shuffled copy of the array to iterate over
        items = sorted(list(self._array[0:self._n_elements]), key=lambda *args: random.random())
        while items:
            yield items.pop()

    def __len__(self):
        return self._n_elements

    def is_empty(self):
        return not self._n_elements

    def enqueue(self, item):
        # check if array has sufficient capacity, else double in size
        if self._n_elements == self._array_size:
            self._resize(self._array_size * 2)
            self._array[self._n_elements] = item
            self._n_elements += 1
        else:
            self._array[self._n_elements] = item
            self._n_elements += 1

    def dequeue(self):
        if not self._n_elements:
            raise LookupError("Queue is empty.")
        idx = random.randint(0, self._n_elements - 1)
        # swap last element and randomly chosen element
        self._array[idx], self._array[self._n_elements - 1] = self._array[self._n_elements - 1], self._array[idx]
        # check if remaining elements are less than 25% of capacity; if so, half capacity
        if self._n_elements - 1 < self._array_size / 4:
            self._resize(self._array_size // 2)
        self._n_elements -= 1
        return self._array[self._n_elements]  # return the dequeue-ed value

    def sample(self):
        if not self._n_elements:
            raise LookupError("Queue is empty.")
        else:
            return self._array[random.randint(0, self._n_elements - 1)]

    def _resize(self, new_capacity):
        new_array = (ctypes.py_object * new_capacity)()
        # copy elements from old to new array
        new_array[:self._n_elements] = self._array[:self._n_elements]
        self._array = new_array
        self._array_size = new_capacity

