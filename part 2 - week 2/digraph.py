import math
import heapq


class Digraph:
    """
    Part II, week 2, Princeton Algorithms course on Coursera.

    An implementation of a weighted directed graph, constructed from an input file. The implementation uses
    an array of edge lists.

    Supported operations:
        - DFS
        - BFS
        - Topological order
        - DAG check
        - Shortest Ancestral Path (for DAGs)
        - Dijkstra

    @TODO:
        - Bellman-Ford
        - Topological Sort Algorithm
    """

    class Edge:

        def __init__(self, v, w, weight):
            self.from_vertex = v
            self.to_vertex = w
            self.weight = weight

        def __str__(self):
            return f"{self.from_vertex}->{self.to_vertex} ({self.weight})"

    def __init__(self, file_in):
        self._edges = []
        self._n_vertices = 0
        self._n_edges = 0
        with open(file_in) as f:
            self._n_vertices = int(f.readline().rstrip())
            self._n_edges = int(f.readline().rstrip())
            for _ in range(self._n_vertices):
                self._edges.append([])
            for line in f:
                if line.strip() != "":
                    v, w, weight = int(line.split()[0]), int(line.split()[1]), float(line.split()[2])
                    self.add_edge(v, w, weight)
        self.is_dag = self._dag()

    def add_edge(self, v, w, weight):
        self._edges[v].append(self.Edge(v, w, weight))

    def adjacent(self, v):
        return [edge.to_vertex for edge in self._edges[v]]

    def edges(self, v):
        return self._edges[v]

    @property
    def n_edges(self):
        return self._n_edges

    @property
    def n_vertices(self):
        return self._n_vertices

    @property
    def topological(self):
        if not self.is_dag:
            raise TypeError("Digraph is not acyclic, topological sort impossible.")
        visited = [False] * self._n_vertices
        topo_stack = []
        for i in range(self._n_vertices):
            if not visited[i]:
                self._topo_recurse(i, visited, topo_stack)
        return topo_stack[::-1]

    def _topo_recurse(self, s, visited, topo_stack):
        visited[s] = True
        for vertex in self.adjacent(s):
            if not visited[vertex]:
                self._topo_recurse(vertex, visited, topo_stack)
        topo_stack.append(s)

    def _dag(self):
        """
        Iterates through all vertices and uses DFS, keeping track of recursion stack,
        to detect any cycles.
        """
        visited = [False] * self._n_vertices
        rec_stack = [False] * self._n_vertices
        for i in range(self._n_vertices):
            if not visited[i]:
                if self._has_cycle(i, visited, rec_stack):
                    return False
        return True

    def _has_cycle(self, s, visited, rec_stack):
        visited[s] = True
        rec_stack[s] = True
        for vertex in self.adjacent(s):
            if not visited[vertex]:
                if self._has_cycle(vertex, visited, rec_stack):
                    return True
            elif rec_stack[vertex]:
                return True
        rec_stack[s] = False
        return False


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
        self.bfs()

    def bfs(self):
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


class SAP:
    """
    Same as used in previous week.

    The assignment was to implement a mechanism to search for the closest common ancestor of two given vertices in a DAG.
    This solution uses interleaved BFS to find the closest common ancestor. 'length' returns the number of edges in total to
    get from the two vertices to their common ancestor. 'ancestor' returns the first common ancestor itself.
    """

    def __init__(self, digraph):
        self.digraph = digraph
        if not digraph.dag:
            raise TypeError("Digraph is not a DAG -- SAP does not work on graphs with cycles.")

    def length(self, v, w):
        v_queue = [v]
        w_queue = [w]
        v_count = 0
        w_count = 0
        v_ancestors = dict()
        w_ancestors = dict()
        if v == w:
            return 0
        while v_queue or w_queue:
            if v_queue:
                cur = v_queue.pop(0)
                if cur in w_ancestors:
                    return v_count + w_ancestors[cur]
                v_ancestors[cur] = v_count
                if self.digraph.adjacent(cur):
                    v_queue.append(*self.digraph.adjacent(cur))
                v_count += 1
            if w_queue:
                cur = w_queue.pop(0)
                if cur in v_ancestors:
                    return w_count + v_ancestors[cur]
                w_ancestors[cur] = w_count
                if self.digraph.adjacent(cur):
                    w_queue.append(*self.digraph.adjacent(cur))
                w_count += 1
        return None

    def ancestor(self, v, w):
        v_queue = [v]
        w_queue = [w]
        v_ancestors = set()
        w_ancestors = set()
        if v == w:
            return 0
        while v_queue or w_queue:
            if v_queue:
                cur = v_queue.pop(0)
                if cur in w_ancestors:
                    return cur
                v_ancestors.add(cur)
                if self.digraph.adjacent(cur):
                    for vertex in self.digraph.adjacent(cur):
                        v_queue.append(vertex)
            if w_queue:
                cur = w_queue.pop(0)
                if cur in v_ancestors:
                    return cur
                w_ancestors.add(cur)
                if self.digraph.adjacent(cur):
                    for vertex in self.digraph.adjacent(cur):
                        w_queue.append(vertex)
        return None


class DijkstraSP:

    def __init__(self, digraph, source):
        self.digraph = digraph
        self.source = source
        self._edgeto = [None] * self.digraph._n_vertices
        self._distto = [math.inf] * self.digraph._n_vertices
        self._distto[source] = 0
        self.min_pq = []
        heapq.heappush(self.min_pq, (self._distto[source], source))
        while self.min_pq:
            distance, vertex = heapq.heappop(self.min_pq)
            # Ignore obsolete entries (this avoids implementing priority-changing mechanism)
            if distance > self._distto[vertex]:
                continue
            for edge in self.digraph.edges(vertex):
                self.relax(edge)

    def relax(self, edge):
        if self._distto[edge.to_vertex] > self._distto[edge.from_vertex] + edge.weight:
            self._distto[edge.to_vertex] = self._distto[edge.from_vertex] + edge.weight
            self._edgeto[edge.to_vertex] = edge
            heapq.heappush(self.min_pq, (self._distto[edge.to_vertex], edge.to_vertex))

    def distance_to(self, vertex):
        return self._distto[vertex]

    def path_to(self, vertex):
        path = []
        while self._edgeto[vertex]:
            path.append(str(self._edgeto[vertex]))
            vertex = self._edgeto[vertex].from_vertex
        return path[::-1]
