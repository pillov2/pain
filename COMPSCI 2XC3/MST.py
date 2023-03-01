import min_heap

class WeightedGraph:

    def __init__(self, n):
        self.adj = {}
        self.w = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        for node in self.adj[node1]:
            if node == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2, weight):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)
            self.w[(node1, node2)] = weight
            self.w[(node2, node1)] = weight

    def number_of_nodes(self):
        return len(self.adj)

g = WeightedGraph(5)
g.add_edge(0,1,1)
g.add_edge(0,2,2)
g.add_edge(0,3,3)
g.add_edge(1,2,4)
g.add_edge(1,3,5)
g.add_edge(2,4,100)


def prim(G):
    MST = WeightedGraph(G.number_of_nodes())
    marked = {}
    for i in range(G.number_of_nodes()):
        marked[i] = False
    marked[0] = True
    for i in range(G.number_of_nodes()-1):
        current_edge = (0, 0, 9999999)
        for start_node in G.adj:
            for end_node in G.adj[start_node]:
                if marked[start_node] and not marked[end_node]:
                    if G.w[(start_node, end_node)] < current_edge[2]:
                        current_edge = (start_node, end_node, G.w[(start_node, end_node)])
        marked[current_edge[1]] = True
        MST.add_edge(current_edge[0], current_edge[1], current_edge[2])
    return MST

def prim2(G):
    MST = WeightedGraph(G.number_of_nodes())
    marked = {}
    for i in range(G.number_of_nodes()):
        marked[i] = False
    Q = min_heap.MinHeap([])
    v = 0
    for end_node in G.adj[v]:
        Q.insert(min_heap.Element((v,end_node), G.w[(v,end_node)]))
    while not Q.is_empty():
        min_edge = Q.extract_min().value
        v = min_edge[1]
        if not marked[v]:
            MST.add_edge(min_edge[0], v, G.w[min_edge])
            for end_node in G.adj[v]:
                Q.insert(min_heap.Element((v, end_node), G.w[(v, end_node)]))
            marked[v] = True
    return MST

def prim3(G):
    MST = WeightedGraph(G.number_of_nodes())
    marked = {}
    pred = {}
    for i in range(G.number_of_nodes()):
        marked[i] = False
    Q = min_heap.MinHeap([])
    for i in range(1, G.number_of_nodes()):
        Q.insert(min_heap.Element(i, 999999))
    Q.insert(min_heap.Element(0,0))
    while not Q.is_empty():
        v = Q.extract_min().value
        marked[v] = True
        if v != 0:
            MST.add_edge(v, pred[v], G.w[(v, pred[v])])
        for end_node in G.adj[v]:
            if not marked[end_node]:
                if G.w[(v, end_node)] < Q.get_element_from_value(end_node).key:
                    Q.decrease_key(end_node, G.w[(v, end_node)])
                    pred[end_node] = v
    return MST







"""
def prim2(G):
    MST = WeightedGraph(G.number_of_nodes())
    marked = {}
    for i in range(G.number_of_nodes()):
        marked[i] = False
    Q = min_heap.MinHeap([])
    v = 0
    for end_node in G.adj[v]:
        Q.insert(min_heap.Element((v,end_node), G.w[(v,end_node)]))
    while not Q.is_empty():
        min_edge = Q.extract_min().value
        v = min_edge[1]
        if not marked[v]:
            MST.add_edge(min_edge[0], v, G.w[min_edge])
            for end_node in G.adj[v]:
                Q.insert(min_heap.Element((v, end_node), G.w[(v, end_node)]))
            marked[v] = True
    return MST

def prim3(G):
    MST = WeightedGraph(G.number_of_nodes())
    marked = {}
    pred = {}
    for i in range(G.number_of_nodes()):
        marked[i] = False
    Q = min_heap.MinHeap([])
    for i in range(1, G.number_of_nodes()):
        Q.insert(min_heap.Element(i, 99999))
    Q.insert(min_heap.Element(0,0))
    while not Q.is_empty():
        v = Q.extract_min().value
        marked[v] = True
        if v != 0:
            MST.add_edge(v, pred[v], G.w[(v,pred[v])])
        marked[v] = True
        for end_node in G.adj[v]:
            if not marked[end_node]:
                if G.w[(v, end_node)] < Q.get_element_from_value(end_node).key:
                    Q.decrease_key(end_node, G.w[(v, end_node)])
                    pred[end_node] = v
    return MST



def prim1(G):
    MST = WeightedGraph(G.number_of_nodes())
    marked = {}
    for i in range(G.number_of_nodes()):
        marked[i] = False
    marked[0] = True
    for _ in range(G.number_of_nodes() - 1):
        current_edge = (0, 0, 99999)
        for start_node in G.adj:
            if marked[start_node]:
                for end_node in G.adj[start_node]:
                    if G.w[(start_node, end_node)] < current_edge[2] and not marked[end_node]:
                        current_edge = (start_node, end_node, G.w[(start_node, end_node)])
        MST.add_edge(current_edge[0], current_edge[1], current_edge[2])
        marked[current_edge[1]] = True
    return MST


def kruskal(G):
    MST = WeightedGraph()
    nodes = list(G.adj.keys())
    Q = min_heap.MinHeap([])
    ds = disjoint_set.DisjointSet(nodes)

    for node in nodes:
        MST.add_node(node)
    for node in nodes:
        for neighbour in G.adj[node]:
            Q.insert(min_heap.Element((node, neighbour), G.w(node, neighbour)))

    while not Q.is_empty():
        current_edge = Q.extract_min().value
        if ds.find(current_edge[0]) != ds.find(current_edge[1]): #Nodes are not connected
            MST.add_edge(current_edge[0], current_edge[1], G.w(current_edge[0], current_edge[1]))
            ds.union(current_edge[0], current_edge[1])

    return MST

"""










