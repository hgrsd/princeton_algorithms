class QuickUnion:

    def __init__(self, n):
        self.id = []
        self.sizes = []
        for i in range(0, n):
            self.id.append(i)
            self.sizes.append(1)

    def is_connected(self, a, b):
        return self._root(a) == self._root(b)

    def union(self, a, b):
        if self.is_connected(a, b):
            return False
        a_root = self._root(a)
        b_root = self._root(b)
        if self.sizes[a_root] > self.sizes[b_root]:
            self.id[b_root] = self.id[a_root]
            self.sizes[a_root] += self.sizes[b_root]
            self.sizes[b_root] = 1
        else:
            self.id[a_root] = self.id[b_root]
            self.sizes[b_root] += self.sizes[a_root]
            self.sizes[a_root] = 1
        return True

    def _root(self, index):
        while index != self.id[index]:
            index = self.id[index]
            self.id[index] = self.id[self.id[index]]
        return index

