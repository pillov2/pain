from collections import deque
from tqdm import tqdm
import random
import matplotlib.pyplot as plot


#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

#Use the methods below to determine minimum vertex covers

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.number_of_nodes())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover

def approx1(G):
    cover = []
    edges = {}
    for node in G.adj.keys():
        edges[node] = G.adj[node].copy()
    while not is_vertex_cover(G, cover):
        node = highest_degree_node(edges)
        cover.append(node)
        remove_incident_edges(edges, node)
    return cover

def highest_degree_node(edges):
    return max(edges, key=lambda x: len(set(edges[x])))

def random_node(edges):
    return random.choice(list(edges.keys()))

def remove_incident_edges(edges, node_to_remove):
    edges.pop(node_to_remove)
    for e in edges.values():
        if node_to_remove in e:
            e.remove(node_to_remove)
    
## Check this ?
def approx2(G):
    cover = []
    edges = {}
    for node in G.adj.keys():
        edges[node] = G.adj[node].copy()

    node = random_node(edges)
    while not is_vertex_cover(G, cover):
        while node in cover:
            node = random_node(edges)
        cover.append(node)
    return cover

def approx3(G):
    cover = []
    edges = {}
    for node in G.adj.keys():
        edges[node] = G.adj[node].copy()
    while not is_vertex_cover(G, cover):
        node = random_node(edges)
        cover.append(node)
        remove_incident_edges(edges, node)
    return cover

def create_random_graph(nodes, edges):
    G = Graph(nodes)
    for i in range(edges):
        start = random.randint(0, nodes - 1)
        end = random.randint(0, nodes - 1)
        while start == end or G.are_connected(start, end):
            start = random.randint(0, nodes - 1)
            end = random.randint(0, nodes - 1)
        G.add_edge(start, end)
    return G

def experiment(nodes, edges, graphs):
    total_opt = 0
    total_approx1 = 0
    total_approx2 = 0
    total_approx3 = 0
    for i in tqdm(range(graphs)):
        G = create_random_graph(nodes, edges)
        total_opt += len(MVC(G))
        total_approx1 += len(approx1(G))
        total_approx2 += len(approx2(G))
        total_approx3 += len(approx3(G))
    return [total_approx1/total_opt, total_approx2/total_opt, total_approx3/total_opt]

def worstCase(nodes):
    total_opt = 0
    worst_approx1 = 0
    worst_approx2 = 0
    worst_approx3 = 0
    graphList = create_all_graphs(nodes)
    for i in tqdm(range(1000)):
        for G in graphList:
            total_opt += len(MVC(G))
            worst_approx1 += len(approx1(G))
            worst_approx2 += len(approx2(G))
            worst_approx3 += len(approx3(G))
    return [worst_approx1/total_opt, worst_approx2/total_opt, worst_approx3/total_opt]

def create_all_graphs(nodes):
    edges = getEdges(nodes)
    graphs = []
    for eList in edges:
        G = Graph(nodes)
        for edge in eList:
            G.add_edge(edge[0], edge[1])
        graphs.append(G)
    return graphs

def getEdges(nodes, i=None, j=None):
    edges = []

    if i is None:
        edges = [[[0,1]] + r for r in getEdges(nodes=nodes, i=0, j=1)]
    
    elif j<nodes-1:
        edges += [[[i,j+1]] + r for r in getEdges(nodes=nodes, i=i, j=j+1)]
        edges += [r for r in getEdges(nodes=nodes, i=i, j=j+1)]

    elif i<nodes-1:
        edges = getEdges(nodes=nodes, i=i+1, j=i+1)

    else:
        edges = [[]]

    return edges

results1 = []
results2 = []
results3 = []
for i in range(2,6,1):
    e = worstCase(i)
    results1.append(e[0]-1)
    results2.append(e[1]-1)
    results3.append(e[2]-1)
plot.plot([2,3,4,5], results1, label='Approx 1')
plot.plot([2,3,4,5], results2, label='Approx 2')
plot.plot([2,3,4,5], results3, label='Approx 3')
plot.title("Worst Case Difference v.s. Number of Nodes")
plot.xlabel("Number Of Nodes")
plot.ylabel("Worst Case Difference")
plot.legend()
plot.show()