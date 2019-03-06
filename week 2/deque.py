class Deque:
    """
    This is a Python implementation of part one of the week 2 programming assignment for the course "Algorithms I"
    (Princeton) on Coursera. (see http://coursera.cs.princeton.edu/algs4/assignments/queues.html)

    This deque is implemented using a doubly linked list. While this is slightly slower due to the increased overhead
    compared to using a dynamic array, the assignment specified that it needed worst case constant time per operation;
    a dynamic array uses amortised constant time.
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def add_first(self, item):
        if not item:
            raise TypeError("None cannot be added to the deque.")
        old_head = self._head
        new_head = Node()
        new_head.item = item
        new_head.next = old_head
        self._head = new_head
        if self._size > 0:
            old_head.prev = new_head
        else:
            self._tail = self._head
        self._size += 1
        return True

    def add_last(self, item):
        if not item:
            raise TypeError("None cannot be added to the deque.")
        old_tail = self._tail
        new_tail = Node()
        new_tail.item = item
        self._tail = new_tail
        if self._size > 0:
            old_tail.next = new_tail
            new_tail.prev = old_tail
        else:
            self._head = self._tail
        self._size += 1
        return True

    def remove_first(self):
        if self._size == 0:
            raise LookupError("Deque is empty")
        to_remove = self._head
        self._head = self._head.next
        self._size -= 1
        if self._size == 0:
            self._tail = self._head
        else:
            self._head.prev = None
        return to_remove.item

    def remove_last(self):
        if self._size == 0:
            raise LookupError("Deque is empty")
        to_remove = self._tail
        self._tail = self._tail.prev
        self._size -= 1
        if self._size == 0:
            self._head = self._tail
        else:
            self._tail.next = None
        return to_remove.item

    def is_empty(self):
        return self._size == 0

    @property
    def size(self):
        return self._size

    def __iter__(self):
        index = self._head
        while index:
            yield index.item
            index = index.next


class Node:

    def __init__(self):
        self.item = None
        self.next = None
        self.prev = None
