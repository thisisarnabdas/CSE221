from collections import defaultdict


def detect_cycle(graph, num_cities):
    visited = [False] * (num_cities + 1)
    recur_stack = [False] * (num_cities + 1)

    def dfs(node):
        visited[node] = True
        recur_stack[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif recur_stack[neighbor]:
                return True
        recur_stack[node] = False
        return False

    for city in range(1, num_cities + 1):
        if not visited[city]:
            if dfs(city):
                return True
    return False


inp = open("input4.txt", "r")
out = open("output4.txt", "w")
num_cities, num_roads = [int(i) for i in inp.readline().split()]
graph = defaultdict(list)
for _ in range(num_roads):
    city1, city2 = [int(i) for i in inp.readline().split()]
    graph[city1].append(city2)
has_cycle = detect_cycle(graph, num_cities)
out.write("YES" if has_cycle else "NO")
