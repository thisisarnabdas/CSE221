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


inp = open("input1.txt", "r")
out = open("output1.txt", "w")

size = int(inp.readline())
unsorted = inp.readline().split()
unsorted = [int(numbers) for numbers in unsorted]  # converting string to int

sorted_numbers = mergeSort(unsorted)

for i in sorted_numbers:
    out.write(f"{i} ")
