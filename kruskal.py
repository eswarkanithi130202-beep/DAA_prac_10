def find(parent, vertex):
    while parent[vertex] != vertex:
        vertex = parent[vertex]
    return vertex

def union(parent, u, v):
    u = find(parent, u)
    v = find(parent, v)

    if u != v:
        parent[v] = u

def kruskal(edges, n):
    parent = list(range(n))

    # Sort edges by weight
    edges.sort()

    cost = 0

    print("\nEdges in Minimum Spanning Tree:")

    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            print(u, "--", v, "=", weight)
            cost += weight

    print("Minimum Cost =", cost)


# User input
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for i in range(e):
    u = int(input("Enter source vertex: "))
    v = int(input("Enter destination vertex: "))
    w = int(input("Enter weight: "))

    edges.append((w, u, v))

kruskal(edges, n)
