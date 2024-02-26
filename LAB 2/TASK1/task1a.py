def targetFinder(arr, n, target):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return f"{i + 1} {j + 1}"
    return "IMPOSSIBLE"


inp = open("input1a.txt", "r")
out = open("output1a.txt", "w")
parameters = inp.readline().split()
parameters = [int(i) for i in parameters]
n = parameters[0]
target = parameters[1]
arr = inp.readline().split()
arr = [int(i) for i in arr]
return_position = targetFinder(arr, n, target)
out.write(return_position)
