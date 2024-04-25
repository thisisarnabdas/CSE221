import heapq as hq
import math


def djikstra(graph, source):
    distance = [math.inf] * len(graph)
    visited = [False] * len(graph)
    prev = [None] * len(graph)
    distance[source] = 0
    q = []
    hq.heappush(q, (distance[source],
                    source))  # The reason for using tuple the heapq module compares the elements based on their first value (priority value) when ordering the heap.

    while q:
        num, u = hq.heappop(q)
        if visited[u] == True:
            continue
        visited[u] = True
        for v, cost in graph[u]:
            new_cost = distance[u] + cost
            if new_cost < distance[v]:
                distance[v] = new_cost
                prev[v] = u  # updates when the shortest path is found
                hq.heappush(q, (distance[v], v))

    distance.pop(0)
    while math.inf in distance:
        idx = distance.index(math.inf)
        distance[idx] = -1  # Unreachable nodes(nodes that can't be reached from source node)
    return distance


inp = open("input1.txt", "r")
out = open("output1.txt", "w")
inputs = inp.read().split("\n")
line1 = inputs[0].split(" ")
num_of_node = int(line1[0])
num_of_edges = int(line1[1])
source_node = int(inputs[-1])

my_dict = {i: [] for i in range(num_of_node + 1)}
for i in range(1, len(inputs) - 1, 1):
    line = inputs[i].split(" ")
    node1 = int(line[0])
    node2 = int(line[1])
    cost = int(line[2])
    my_dict[node1].append((node2, cost))

main = djikstra(my_dict, source_node)
out.write(" ".join(list(map(str, main))))
