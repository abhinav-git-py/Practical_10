def kruskal(graph):
    edges = []

    # Get all edges
    for u in graph:
        for v, weight in graph[u]:
            if u < v:
                edges.append((weight, u, v))

    # Sort edges by weight
    edges.sort()

    parent = {vertex: vertex for vertex in graph}
    mst = []
    total_cost = 0

    def find(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)

        if root_u == root_v:
            return False

        parent[root_v] = root_u
        return True

    for weight, u, v in edges:
        if union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost


# Example graph
graph = {
    'A': [('B', 2), ('D', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('B', 1), ('D', 5)],
    'D': [('A', 3), ('B', 4), ('C', 5)]
}

mst, cost = kruskal(graph)

print("MST:")
for u, v, weight in mst:
    print(u, "--", v, ":", weight)

print("Total cost:", cost)
