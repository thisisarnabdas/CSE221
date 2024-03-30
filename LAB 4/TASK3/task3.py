def dfs(graph, start):
    visited = set()
    path = []

    def dfs_traverse(node):
        if node not in visited:
            visited.add(node)
            path.append(node)
            for neighbor in sorted(graph[node]):
                dfs_traverse(neighbor)

    dfs_traverse(start)
    return path


inp = open("input3.txt", "r")
out = open("output3.txt", "w")
num_cities, num_roads = [int(i) for i in inp.readline().split()]
graph = {city: [] for city in range(1, num_cities + 1)}
for _ in range(num_roads):
    city1, city2 = [int(i) for i in inp.readline().split()]
    graph[city1].append(city2)
    graph[city2].append(city1)
for city, neighbors in graph.items():
    graph[city] = sorted(neighbors)
traversal_path = dfs(graph, 1)
out.write(" ".join(map(str, traversal_path)))
