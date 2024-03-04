def merge(a, b, inv_left, inv_right):
    arr = []
    inversions = inv_left + inv_right
    while (len(a) >= 1) and (len(b) >= 1):
        if a[0] > b[0]:
            arr.append(b[0])
            b.remove(b[0])
            inversions += len(a)
        else:
            arr.append(a[0])
            a.remove(a[0])
    while len(a) >= 1 and len(b) == 0:
        arr.append(a[0])
        a.remove(a[0])
    while len(b) >= 1 and len(a) == 0:
        arr.append(b[0])
        b.remove(b[0])
    return arr, inversions


def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0

    else:
        mid = len(arr) // 2
        a1, inv_left = mergeSort(arr[:mid])  # write the parameter
        a2, inv_right = mergeSort(arr[mid:])  # write the parameter
        return merge(a1, a2, inv_left, inv_right)


def countInversions(arr):
    _, inversions = mergeSort(arr)
    return inversions


inp = open("input3.txt", "r")
out = open("output3.txt", "w")

size = int(inp.readline())
line_of_aliens = inp.readline().split()
line_of_aliens = [int(heights) for heights in line_of_aliens]  # converting string to int

total_inversions = countInversions(line_of_aliens)

out.write(f"{total_inversions}")
