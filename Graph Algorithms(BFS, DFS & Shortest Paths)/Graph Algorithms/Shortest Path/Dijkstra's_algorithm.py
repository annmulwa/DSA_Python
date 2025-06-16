# printing the graph
class Graph:
    def __init__(self, num_nodes, edges, weighted=False, directed=False):
        self.num_nodes = num_nodes
        self.weighted = weighted
        self.directed = directed

        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]

        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}: {}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{}: {}\n".format(i, nodes)
        return result

# shortest path from the source node to the target node
def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    parent = [None] * len(graph.data)
    queue = []

    distance[source] = 0
    queue.append(source)
    idx = 0

    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx += 1

        # update the distances of all the neighbours
        update_distances(graph, current, distance, parent)

        # find the first unvisited node with the smallest distance
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)

    return distance[current], parent

def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbours"""
    neighbours = graph.data[current]
    weights = graph.weight[current]

    for i, node in enumerate(neighbours):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current

def pick_next_node(distance, visited):
    """Pick the next unvisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node

num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
graph7 = Graph(num_nodes7, edges7, weighted=True, directed=True)
print(graph7)

print(shortest_path(graph7, 0, 5))

num_nodes2 = 9
edges2 =[(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2),
         (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]
graph2 = Graph(num_nodes2, edges2, weighted=True)
print(graph2)

print(shortest_path(graph2, 0, 8))
