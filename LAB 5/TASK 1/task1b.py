from collections import deque
result = []
queue = deque()
visited = set()


def bfs(G, v, visited, Indeg):  # Here indeg means no. of pre-req course
    visited.add(v)
    queue.append(v)

    while queue:
        x = queue.popleft()
        result.append(x)

        for neighbour in G[x]:
            Indeg[neighbour] -= 1

            if neighbour not in visited and Indeg[neighbour] == 0:
                visited.add(neighbour)
                queue.append(neighbour)


inp = open('input1b.txt', 'r')
out = open('output1b.txt', 'w')

n, m = [int(i) for i in inp.readline().split()]

my_dict = {}
for i in range(1, n + 1):
    my_dict[i] = []

track = [0] * (n + 1)
for i in range(m):
    pre_req, course = [int(i) for i in inp.readline().split()]
    my_dict[pre_req].append(course)
    track[course] += 1

for i in range(1, n + 1):
    if track[i] == 0 and i not in visited:
        bfs(my_dict, i, visited, track)

if len(result) < n:
    out.write('IMPOSSIBLE')
else:
    out.write(str(result).strip('[]').replace(',', ''))
