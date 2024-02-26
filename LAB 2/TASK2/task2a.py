def merge(a, b):
    arr = []

    while (len(a) >= 1) and (len(b) >= 1):
        if a[0] > b[0]:
            arr.append(b[0])
            b.remove(b[0])
        else:
            arr.append(a[0])
            a.remove(a[0])
    while len(a) >= 1 and len(b) == 0:
        arr.append(a[0])
        a.remove(a[0])
    while len(b) >= 1 and len(a) == 0:
        arr.append(b[0])
        b.remove(b[0])
    return arr


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        return merge(a1, a2)


inp = open("input2a.txt", "r")
out = open("output2a.txt", "w")
arr1_len = int(inp.readline())
arr1 = inp.readline().split()
arr1 = [int(i) for i in arr1]
arr2_len = int(inp.readline())
arr2 = inp.readline().split()
arr2 = [int(i) for i in arr2]
final_arr = arr1 + arr2
sorted_arr = mergeSort(final_arr)
for i in sorted_arr:
    out.write(f"{i} ")
