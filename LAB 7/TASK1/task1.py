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


inp = open("input1.txt", "r")
out = open("output1.txt", "w")
N, K = [int(i) for i in inp.readline().split()]
dsu = DSU(N)
for i in range(K):
    A, B = [int(i) for i in inp.readline().split()]
    dsu.union_sets(A, B)
    root_A = dsu.find_set(A)
    circle_size = dsu.size[root_A]
    out.write(str(circle_size) + "\n")
