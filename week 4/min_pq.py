class MinPQ:
    """
    Implementation of a generic minimum priority queue using a min heap data structure. Part of the
    programming assignment of week 4, Princeton Algorithms course on Coursera:
    http://coursera.cs.princeton.edu/algs4/assignments/8puzzle.html

    Objects used as elements in this min pq must implement __lt__().
    """

    def __init__(self):
        self._size = 0
        self._queue = [None]

    def __len__(self):
        return self._size

    def del_min(self):
        if len(self) < 1:
            raise IndexError("Priority queue is empty.")
        min_item = self._queue[1]
        self.exchange(1, len(self))
        del(self._queue[len(self)])
        self._size -= 1
        self.sink(1)
        return min_item

    def insert(self, item):
        self._size += 1
        self._queue.append(item)
        self.swim(len(self))

    def swim(self, index):
        while index > 1 and self._queue[index] < self._queue[index//2]:
            self.exchange(index, index//2)
            index = index // 2

    def sink(self, index):
        while index * 2 <= len(self):
            scan = index * 2
            if scan < len(self) and self._queue[scan + 1] < self._queue[scan]:
                scan += 1
            if self._queue[scan] < self._queue[index]:
                self.exchange(index, scan)
                index = scan
            else:
                break

    def exchange(self, a, b):
        self._queue[a], self._queue[b] = self._queue[b], self._queue[a]
