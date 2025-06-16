l1 = [[]] * 10
l1[0].append(1)
# print(l1)
# print(list(range(10)))
l2 = [[] for _ in range(10)]
l2[0].append(1)
# print(l2)

# printing the graph
class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def __repr__(self):
        return "\n".join(["{}: {}".format(n, neighbours) for n, neighbours in enumerate(self.data)])
    def __str__(self):
        return self.__repr__()
num_nodes = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
graph1 = Graph(num_nodes, edges)
print(graph1)

# Add an edge to the graph
class Graph2:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def add_edge(self, n1, n2):
        if n2 not in self.data[n1]:
            self.data[n1].append(n2)
        if n1 not in self.data[n2]:
            self.data[n2].append(n1)
    def __repr__(self):
        return "\n".join(["{}: {}".format(n, neighbours) for n, neighbours in enumerate(self.data)])
    def __str__(self):
        return self.__repr__()

num_nodes = 6
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
graph2 = Graph2(num_nodes, edges)
print(graph2)

graph2.add_edge(4, 5)
print(graph2)

# Remove an edge from the graph
class Graph3:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def remove_edge(self, n1, n2):
        if n2 in self.data[n1]:
            self.data[n1].remove(n2)
        if n1 in self.data[n2]:
            self.data[n2].remove(n1)
    def __repr__(self):
        return "\n".join(["{}: {}".format(n, neighbours) for n, neighbours in enumerate(self.data)])
    def __str__(self):
        return self.__repr__()

num_nodes = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
graph3 = Graph3(num_nodes, edges)
print(graph3)

graph3.remove_edge(3, 4)
print(graph3)