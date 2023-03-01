from collections import deque
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

    def has_edge(self, start, end):
        if end in self.adj[start]:
            return True 
        return False

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

# Breadth First Search returning path
def BFS2(G, node1, node2):
    Q = deque([(node1, [node1])])
    marked = {node1: True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node, current_path = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return current_path + [node]
            if not marked[node]:
                Q.append((node, current_path + [node]))
                marked[node] = True
    return []

# Breadth First Search 3
def BFS3(G, node):
    Q = deque([node])
    marked = {node: True}
    pred = {}
    for n in G.adj:
        if n != node:
            marked[n] = False
            pred[n] = None
    while len(Q) != 0:
        current_node = Q.popleft()
        for n in G.adj[current_node]:
            if not marked[n]:
                marked[n] = True
                Q.append(n)
                pred[n] = current_node
    return pred






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

#Depth First Search returning path
def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    currentPath = []
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            currentPath.append(current_node)
            if current_node == node2:
                return currentPath
            if len(G.adj[current_node]) == 1 and current_node != (node1 or node2):
                while len(currentPath) > 0 and len(G.adj[currentPath[-1]]) <= 2:
                    currentPath.pop()
            for node in G.adj[current_node]:
                if not marked[node]:
                    S.append(node)
                    if node == node2:
                        currentPath.append(node)
                        return currentPath
    return []

# Depth First Search returning 
def DFS3(G, node):
    S = [node]
    marked = {node: True}
    predecessor = {}
    for n in G.adj:
        if n != node:
            marked[n] = False
            predecessor[n] = None
    while len(S) != 0:
        current_node = S.pop()
        for neighbor in G.adj[current_node]:
            if not marked[neighbor]:
                S.append(neighbor)
                marked[neighbor] = True
                predecessor[neighbor] = current_node
    return predecessor

# Has Cycle
def has_cycle(G):
    S = [0]
    marked = {0: True}
    predecessor = {}
    for n in G.adj:
        if n != 0:
            marked[n] = False
            predecessor[n] = None
    while len(S) != 0:
        current_node = S.pop()
        for neighbor in G.adj[current_node]:
            if not marked[neighbor]:
                S.append(neighbor)
                marked[neighbor] = True
                predecessor[neighbor] = current_node
            elif predecessor[current_node] != neighbor:
                return True
    return False


# Returns false if there exist any two nodes that do not have a path between them
def is_connected(G):
    # path between node and itself does not count as a path between two nodes
    # By that assumption, you need atleast 2 nodes in a graph for it to be connected
    if G.number_of_nodes() < 2:
        return False
    Q = deque([0])
    marked = {0 : True}
    for node in G.adj:
        if node != 0:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    for nodes in marked:
        if not marked[nodes]:
            return False
    return True
    
# Generate Random Graph
def create_random_graph(nodes, edges):
    G = Graph(nodes)
    for i in range(edges):
        start = random.randint(0, nodes - 1)
        end = random.randint(0, nodes - 1)
        while start == end or G.has_edge(start, end):
            start = random.randint(0, nodes - 1)
            end = random.randint(0, nodes - 1)
        G.add_edge(start, end)
    return G

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
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover

def exp1Prob(graph_number, nodes, edges):
    cycle_count = 0
    for i in range(graph_number):
        G = create_random_graph(nodes, edges)
        if has_cycle(G):
            cycle_count += 1
    return float(cycle_count/graph_number) * 100.0

def exp1(size, runs, edges):
    probs = []
    for i in range(edges):
        print(i, "out of", edges)
        probs.append(exp1Prob(runs, size, i))
    plot.plot(probs)
    plot.xlabel("Number of edges")
    plot.ylabel("Cycle Probability")
    plot.show()

def exp1v2(size, runs, edges, label=""):
    probs = []
    proportion = []
    for i in range(edges):
        print(i, "out of", edges)
        probs.append(exp1Prob(runs, size, i))
        proportion.append(float(i/size))
    plot.plot(proportion, probs, label=label)

# #Experiment1 Edge Num vs Cycle Prob
# exp1(100,1000,300)


# #Experiment1 Edge Proportion vs Cycle Prob (with multiple node nums)
# exp1v2(1000,100,2000,"1000 Nodes")
# exp1v2(100,100,200,"100 Nodes")
# exp1v2(10,100,20,"10 Nodes")
# plot.xlabel("Proportion of edges")
# plot.ylabel("Cycle Probability")
# plot.legend()
# plot.show()

def exp2Prob(graph_number, nodes, edges):
    cycle_count = 0
    for i in range(graph_number):
        G = create_random_graph(nodes, edges)
        if is_connected(G):
            cycle_count += 1
    return float(cycle_count/graph_number) * 100.0

def exp2(size, runs, edges):
    probs = []
    for i in range(edges):
        print(i, "out of", edges)
        probs.append(exp2Prob(runs, size, i))
    plot.plot(probs)
    plot.xlabel("Number of edges")
    plot.ylabel("Connected Probability")
    plot.show()

def exp2v2(size, runs, edges, label=""):
    probs = []
    proportion = []
    for i in range(edges):
        print(i, "out of", edges)
        probs.append(exp2Prob(runs, size, i))
        proportion.append(float(i/size))
    plot.plot(proportion, probs, label=label)

# Experiment2 Edge Num vs Connected Prob
# exp2(100,500,600)

# Experiment1 Edge Proportion vs Cycle Prob (with multiple node nums)
# exp2v2(100,100,600,"100 Nodes")
# exp2v2(200,100,1200,"200 Nodes")
# exp2v2(300,100,1800,"300 Nodes")
# plot.xlabel("Proportion of edges")
# plot.ylabel("Connected Probability")
# plot.legend()
# plot.show()