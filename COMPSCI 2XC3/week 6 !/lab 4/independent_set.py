import random
import matplotlib.pyplot as plot

print("hello world")

class Graph:
    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def hasEdge(self, node1, node2):
        return node2 in self.adj[node1]

    def addEdge(self, node1, node2):
        if not self.hasEdge(node1, node2):
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def getSize(self):
        return len(self.adj)

def createRandomGraph(nodes, edges):
    G = Graph(nodes)
    for i in range(edges):
        start = random.randint(0, nodes - 1)
        end = random.randint(0, nodes - 1)
        while start == end or G.hasEdge(start, end):
            start = random.randint(0, nodes - 1)
            end = random.randint(0, nodes - 1)
        G.addEdge(start, end)
    return G

def addElement(sets, element):
    newSet = sets.copy()
    for set in newSet:
        set.append(element)

    return newSet

def powerSet(set):
    if set == []:
        return [[]]
    
    return powerSet(set[1:]) + addElement(powerSet(set[1:]), set[0])

def isVertexCover(graph, vertexCover):
    for startVertex in graph.adj.keys():
        for endVertex in graph.adj[startVertex]:
            if (not startVertex in vertexCover) and (not endVertex in vertexCover):
                return False
            
    return True

def MVC(graph):
    nodes = [i for i in range(graph.getSize())]
    subsets = powerSet(nodes)
    min_cover = nodes
    
    for subset in subsets:
        if isVertexCover(graph, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    
    return min_cover

def isIndependentSet(graph, independentSet):
    for startVertex in graph.adj.keys():
        for endVertex in graph.adj[startVertex]:
            if (startVertex in independentSet) and (endVertex in independentSet):
                return False
    
    return True

def MIS(graph):
    nodes = [i for i in range(graph.getSize())]
    subsets = powerSet(nodes)
    
    maxCover = []
    
    for subset in subsets:
        if isIndependentSet(graph, subset):
            
            if len(subset) > len(maxCover):
                maxCover = subset
    
    return maxCover

MISlength = []
MVClength = []
n = 20

for i in range(n):

    if i == 0:
        graph = createRandomGraph(0, 0)
    
    else:
        graph = createRandomGraph(i, i-1)

    MISlength.append(len(MIS(graph)))
    MVClength.append(len(MVC(graph)))

print(MISlength)
print(MVClength)
plot.plot(MISlength, label = "MIS")
plot.plot(MVClength, label = "MVC")
plot.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
plot.yticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
plot.xlabel("Number of Nodes in Graph")
plot.ylabel("Number of Nodes in Solution")
plot.legend()
plot.show()