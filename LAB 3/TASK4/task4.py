def find_max(arr):
    squared = [i ** 2 for i in arr]
    maximum = -99999
    for i in range(size - 1):
        temp = arr[:i + 1] + sorted(squared[i + 1:], reverse=True)
        if (temp[i] + temp[i + 1]) > maximum:
            maximum = temp[i] + temp[i + 1]
    return maximum

inp = open("input4.txt", "r")
out = open("output4.txt", "w")

size = int(inp.readline())
A = inp.readline().split()
A = [int(numbers) for numbers in A]  # converting string to int
maximum = find_max(A)
out.write(f"{maximum}")