from collections import deque, defaultdict


def shortest_path(graph, start, destination):
    queue = deque([(start, 0, [start])])
    visited = set()
    while queue:
        node, time, path = queue.popleft()
        if node == destination:
            return time, path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append((neighbor, time + 1, new_path))
    return -1, []


inp = open("input5.txt", "r")
out = open("output5.txt", "w")
num_cities, num_roads, destination = [int(i) for i in inp.readline().split()]
graph = defaultdict(list)
for _ in range(num_roads):
    city1, city2 = [int(i) for i in inp.readline().split()]
    graph[city1].append(city2)
    graph[city2].append(city1)
time, path = shortest_path(graph, 1, destination)
if time != -1:
    out.write(f"Time: {time}\nShortest Path: {" ".join(str(x) for x in path)}")
else:
    out.write("Destination not reachable")
