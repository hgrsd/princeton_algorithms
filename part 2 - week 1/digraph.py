class Digraph:

    def __init__(self, file_in):
        self._vertices = []
        self._n_vertices = 0
        self._n_edges = 0
        with open(file_in) as f:
            self._n_vertices = int(f.readline().rstrip())
            self._n_edges = int(f.readline().rstrip())
            for _ in range(self._n_vertices):
                self._vertices.append([])
            for line in f:
                if line.strip() != "":
                    v, w = [int(x) for x in line.split()]
                    self.add_edge(v, w)

    def add_edge(self, v, w):
        self._vertices[v].append(w)

    @property
    def adjacent(self, v):
        return self._vertices[v]

    @property
    def n_edges(self):
        return self._n_edges

    @property
    def n_vertices(self):
        return self._n_vertices
