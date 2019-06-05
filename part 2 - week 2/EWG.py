import quickunion
import heapq

class Graph:
    """
    Implements an undirected weighted graph. Part II, week 2, Princeton Algorithms course on Coursera.
    Operations:
        - Kruskal (MST)
        - @TODO: Prim (MST)
    """

    class Edge:

        def __init__(self, v, w, weight):
            self.v = v
            self.w = w
            self.weight = weight

        def __str__(self):
            return f"{self.v}<->{self.w} ({self.weight})"

        def __lt__(self, other):
            return self.weight < other.weight

        def either(self):
            return self.v

        def other(self, vertex):
            if vertex == self.v:
                return self.w
            else:
                return self.v

    def __init__(self, file_in=None, n_vertices=None):
        self._edges = []
        if file_in:
            with open(file_in) as f:
                self._n_vertices = int(f.readline().rstrip())
                self._n_edges = int(f.readline().rstrip())
                for _ in range(self._n_vertices):
                    self._edges.append([])
                for line in f:
                    if line.strip() != "":
                        v, w, weight = int(line.split()[0]), int(line.split()[1]), float(line.split()[2])
                        edge = self.Edge(v, w, weight)
                        self.add_edge(edge)
        else:
            self._n_vertices = n_vertices
            self._n_edges = 0
            for _ in range(self._n_vertices):
                    self._edges.append([])

    def add_edge(self, edge):
        self._edges[edge.v].append(edge)
        self._edges[edge.w].append(edge)

    def adjacent(self, v):
        """ Returns v's adjacent vertices by index """
        return [edge.other(v) for edge in self._edges[v]]

    def edges(self, v):
        """ Returns all Edge objects for vertex v """
        return self._edges[v]

    @property
    def all_edges(self):
        return self._edges

    @property
    def n_edges(self):
        return self._n_edges

    @property
    def n_vertices(self):
        return self._n_vertices

    def kruskal(self):
        queue = []
        mst = []
        uf = quickunion.QuickUnion(self.n_vertices)
        for vertex in self.all_edges:
            for edge in vertex:
                heapq.heappush(queue, edge)
        while queue and len(mst) < self.n_vertices:
            cur = heapq.heappop(queue)
            v = cur.either()
            w = cur.other(v)
            if not uf.is_connected(v, w):
                mst.append(cur)
                uf.union(v, w)
        return mst
