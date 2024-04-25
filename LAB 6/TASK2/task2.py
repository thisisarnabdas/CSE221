import heapq


def find_distance(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


def find_safest_path(graph, source, target):
    distances_from_source = find_distance(graph, source)
    distances_from_target = find_distance(graph, target)

    min_time = float('inf')
    meet_node = None

    for node in range(1, len(graph)):
        if distances_from_source[node] != float('inf') and distances_from_target[node] != float('inf'):
            time_to_meet = max(distances_from_source[node], distances_from_target[node])
            if time_to_meet < min_time:
                min_time = time_to_meet
                meet_node = node

    return min_time, meet_node


inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')
n, m = [int(i) for i in inp.readline().split()]
graph = {i: [] for i in range(1, n + 1)}  # Start indexing from 1

for _ in range(m):
    s, d, w = [int(i) for i in inp.readline().split()]
    graph[s].append((d, w))

s, t = [int(i) for i in inp.readline().split()]

min_time, meet_node = find_safest_path(graph, s, t)

if min_time == float('inf'):
    out.write('Impossible')
else:
    out.write(f"Time {min_time} \nNode {meet_node}")
