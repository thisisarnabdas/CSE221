def sort_by_order_of_n(arr1, arr2):
    sorted_list = []
    arr1_pointer, arr2_pointer = 0, 0
    while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):
        if arr1[arr1_pointer] < arr2[arr2_pointer]:
            sorted_list.append(arr1[arr1_pointer])
            arr1_pointer += 1
        elif arr1[arr1_pointer] > arr2[arr2_pointer]:
            sorted_list.append(arr2[arr2_pointer])
            arr2_pointer += 1
        else:
            sorted_list.append(arr1[arr1_pointer])
            sorted_list.append(arr2[arr2_pointer])
            arr1_pointer += 1
            arr2_pointer += 1
    sorted_list.extend(arr1[arr1_pointer:])
    sorted_list.extend(arr2[arr2_pointer:])
    return sorted_list


inp = open("input2b.txt", "r")
out = open("output2b.txt", "w")
arr1_len = int(inp.readline())
arr1 = inp.readline().split()
arr1 = [int(i) for i in arr1]
arr2_len = int(inp.readline())
arr2 = inp.readline().split()
arr2 = [int(i) for i in arr2]
sorted_list = sort_by_order_of_n(arr1, arr2)
for i in sorted_list:
    out.write(f"{i} ")
