import heapq


def djikstra(graph, N, start):
    danger = [float('inf')] * N
    danger[start] = 0

    pq = [(0, start)]

    while pq:
        current_danger, node = heapq.heappop(pq)

        if node == N - 1:
            return current_danger

        for neighbor, weight in graph[node]:
            new_danger = max(current_danger, weight)

            if new_danger < danger[neighbor]:
                danger[neighbor] = new_danger
                heapq.heappush(pq, (new_danger, neighbor))

    return "Impossible"


inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')
n, m = [int(i) for i in inp.readline().split()]
graph = [[] for i in range(n)]

for i in range(m):
    u, v, w = [int(i) for i in inp.readline().split()]
    graph[u - 1].append((v - 1, w))

result = djikstra(graph, n, 0)  # Start from node 1 (index 0)

out.write(str(result) + '\n')
