class QuickFind:

    def __init__(self, n):
        self.id = [i for i in range(0, n)]

    def is_connected(self, a, b):
        return self.id[a] == self.id[b]

    def union(self, a, b):
        a_id, b_id = self.id[a], self.id[b]
        self.id = [b_id if x == a_id else x for x in self.id]



