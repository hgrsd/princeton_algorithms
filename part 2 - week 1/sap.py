class SAP:
    """
    Part II, week 1, Princeton Algorithms course on Coursera.
    Assignment:
    http://coursera.cs.princeton.edu/algs4/assignments/wordnet.html

    The assignment was to implement a mechanism to search for the closest common ancestor of two given vertices in a DAG.
    This solution uses interleaved BFS to find the closest common ancestor. 'length' returns the number of edges in total to
    get from the two vertices to their common ancestor. 'ancestor' returns the first common ancestor itself.
    """

    def __init__(self, digraph):
        self.digraph = digraph

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

