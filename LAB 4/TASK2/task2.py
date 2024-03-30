from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    path = []
    while queue:
        current_city = queue.popleft()
        path.append(current_city)
        for neighbor in graph[current_city]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return path


inp = open("input2.txt", "r")
out = open("output2.txt", "w")
num_cities, num_roads = [int(i) for i in inp.readline().split()]
graph = {city: [] for city in range(1, num_cities + 1)}
for _ in range(num_roads):
    city1, city2 = [int(i) for i in inp.readline().split()]
    graph[city1].append(city2)
    graph[city2].append(city1)
traversal_path = bfs(graph, 1)
out.write(" ".join(str(x) for x in traversal_path))
