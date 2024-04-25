class DSU:
    def __init__(self, N):
        self.parent = list(range(N + 1))  # 1-based indexing for easier understanding
        self.size = [1] * (N + 1)  # Track the size of each set

    def find_set(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def union_sets(self, x, y):
        root_x = self.find_set(x)
        root_y = self.find_set(y)

        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]


def kruskal(edges, N):
    dsu = DSU(N)
    mst_cost = 0
    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if dsu.find_set(u) != dsu.find_set(v):
            dsu.union_sets(u, v)
            mst_cost += weight

    return mst_cost


inp = open("input2.txt", "r")
out = open("output2.txt", "w")
N, M = [int(i) for i in inp.readline().split()]
edges = []

for i in range(M):
    u, v, w = [int(i) for i in inp.readline().split()]
    edges.append((u, v, w))
min_cost = kruskal(edges, N)
out.write(str(min_cost) + "\n")
