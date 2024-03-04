def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        if a1 > a2:
            return a1
    return a2


inp = open("input2.txt", "r")
out = open("output2.txt", "w")
size = int(inp.readline())
array = inp.readline().split()
array = [int(numbers) for numbers in array]  # converting to integer
max_value = mergeSort(array)
out.write(f"{max_value[0]}")
