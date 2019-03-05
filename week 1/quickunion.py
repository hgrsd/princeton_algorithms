class QuickUnion:

    def __init__(self, n):
        self.id = list(range(n))
        self.sizes = [1] * n

    def is_connected(self, a, b):
        return self._root(a) == self._root(b)

    def union(self, a, b):
        a_root = self._root(a)
        b_root = self._root(b)
        if a_root == b_root:
            return False
        if self.sizes[a_root] > self.sizes[b_root]:
            self.id[b_root] = self.id[a_root]
            self.sizes[a_root] += self.sizes[b_root]
        else:
            self.id[a_root] = self.id[b_root]
            self.sizes[b_root] += self.sizes[a_root]
        return True

    def _root(self, index):
        while index != self.id[index]:
            self.id[index] = self.id[self.id[index]]
            index = self.id[index]
        return index

