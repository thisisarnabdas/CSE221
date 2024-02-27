def maximum_task(array):
    # sorting the array based on the second element[ending time] of each list inside the array
    array.sort(key=lambda x: int(x[1]))
    new_array = []
    probable_start = -1
    for current_start, current_end in array:
        if int(current_start) >= int(probable_start):
            new_array.append([current_start, current_end])
            probable_start = current_end  # next tasks start will be greater or equal to currents end time
    return new_array


inp = open("input4.txt", "r")
out = open("output4.txt", "w")
n, manpower = inp.readline().split()
arr = [inp.readline().split() for i in range(int(n))]
sum = 0
for i in range(int(manpower)):
    output = maximum_task(arr)
    sum += len(output)
    arr = [sublist for sublist in arr if sublist not in output]
out.write(f"{sum}")
