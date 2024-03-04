def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == k - 1:  # Check if pivot is the k-th smallest
            return arr[pivot_index]
        elif pivot_index < k - 1:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return quickselect(arr, low, pivot_index - 1, k)


# Example usage
inp = open("input6.txt", "r")
out = open("output6.txt", "w")
N = int(inp.readline().split()[0])
arr = inp.readline().split()
arr = [int(i) for i in arr]
queries = int(inp.readline().split()[0])
query_list = []
for i in range(queries):
    query_list.append(int(inp.readline()))

for k in query_list:
    kth_smallest = quickselect(arr.copy(), 0, N - 1, k)  # Copy array to avoid modification
    out.write(f"{kth_smallest}\n")
