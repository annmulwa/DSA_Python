def adj_matrix(num_nodes, edges):
    matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    for n1, n2 in edges:
        matrix[n1][n2] = 1
        matrix[n2][n1] = 1
    return matrix

num_nodes = 4
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
print(adj_matrix(num_nodes, edges))

undirected_matrix = adj_matrix(num_nodes, edges)
for row in undirected_matrix:
    print(row)