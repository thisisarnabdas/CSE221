def maximum_task(array):
    array.sort(key=lambda x: int(
        x[1]))  # sorting the array based on the second element[ending time] of each list inside the array
    new_array = []
    probable_start = -1
    for current_start, current_end in array:
        if int(current_start) >= int(probable_start):
            new_array.append([current_start, current_end])
            probable_start = current_end  # next tasks start will be greater or equal to currents end time
    return new_array


inp = open("input3.txt", "r")
out = open("output3.txt", "w")
n = int(inp.readline())
arr = []
for i in range(n):
    arr.append((inp.readline().split()))
output = maximum_task(arr)
out.write(f"{len(output)}\n")
for i, j in output:
    out.write(f"{i} {j}\n")
