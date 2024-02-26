inp = open("input2.txt", "r")
out = open("output2.txt", "w")
array_size = inp.readline()
array = inp.readline()
array = array.split(" ")
final_array = []
for i in array:
    final_array.append(int(i))


def bubbleSort(arr):
    flag = False
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break
    arr = " ".join(map(str, arr))  # Converting each number to a string using map()
    out.write(arr)


bubbleSort(final_array)
