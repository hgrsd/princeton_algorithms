class Digraph:
    """
    Part II, week 2, Princeton Algorithms course on Coursera.

    An implementation of a weighted directed graph, constructed from an input file.

    Supported operations:
        - DFS
        - BFS
        - DAG check
        - Shortest Ancestral Path (for DAGs)
        - Dijkstra
        - Bellman-Ford
        - Topological Sort Algorithm
    """

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
                    v, w, weight = int(line.split()[0]), int(line.split()[1]), float(line.split()[2])
                    self.add_edge(v, w, weight)

    def add_edge(self, v, w, weight):
        self._vertices[v].append(Edge(v, w, weight))

    def adjacent(self, v):
        return [edge.to_vertex for edge in self._vertices[v]]

    @property
    def n_edges(self):
        return self._n_edges

    @property
    def n_vertices(self):
        return self._n_vertices


class Edge:

    def __init__(self, v, w, weight):
        self.from_vertex = v
        self.to_vertex = w
        self.weight = weight


class DFS:

    def __init__(self, digraph, source):

        self._seen = [False] * digraph.n_vertices
        self._edge_to = [None] * digraph.n_vertices
        self._digraph = digraph
        self._seen[source] = True
        self._edge_to[source] = source
        self.dfs(source)

    def dfs(self, source):
        for vertex in self._digraph.adjacent(source):
            if not self._seen[vertex]:
                self._seen[vertex] = True
                self._edge_to[vertex] = source
                self.dfs(vertex)

    def visited(self, vertex):
        return self._seen[vertex]

    def edge_to(self, vertex):
        return self._edge_to[vertex]

class BFS:

    def __init__(self, digraph, source):
        self._seen = [False] * digraph.n_vertices
        self._steps_to = [None] * digraph.n_vertices
        self._digraph = digraph
        self._seen[source] = True
        self._steps_to[source] = 0
        self._queue = [source]
        self.BFS()

    def BFS(self):
        while self._queue:
            cur = self._queue.pop()
            for vertex in self._digraph.adjacent(cur):
                if not self._seen[vertex]:
                    self._queue.append(vertex)
                    self._seen[vertex] = True
                    self._steps_to[vertex] = self._steps_to[cur] + 1

    def visited(self, vertex):
        return self._seen[vertex]

    def steps_to(self, vertex):
        return self._steps_to[vertex]
