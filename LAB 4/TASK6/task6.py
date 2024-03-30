def diamondSrc(graph, row, col, visited, rowSize, colSize):
    if row < 0 or row >= rowSize or col < 0 or col >= colSize or graph[row][col] == "#" or visited[row][col]:
        return 0
    visited[row][col] = True
    diamond = 0
    if graph[row][col] == "D":
        diamond += 1
    diamond += diamondSrc(graph, row - 1, col, visited, rowSize, colSize)
    diamond += diamondSrc(graph, row + 1, col, visited, rowSize, colSize)
    diamond += diamondSrc(graph, row, col - 1, visited, rowSize, colSize)
    diamond += diamondSrc(graph, row, col + 1, visited, rowSize, colSize)
    return diamond


inp = open("input6.txt", "r")
out = open("output6.txt", "w")
row, col = [int(i) for i in inp.readline().split()]
arr = [["" for _ in range(col)] for _ in range(row)]
for i in range(row):
    x = inp.readline()
    for j in range(col):
        arr[i][j] = x[j]
total = 0
for x in range(row):
    for y in range(col):
        if arr[x][y] == ".":
            visited = [[False for _ in range(col)] for _ in range(row)]
            total = max(total, diamondSrc(arr, x, y, visited, row, col))
out.write(str(total))
