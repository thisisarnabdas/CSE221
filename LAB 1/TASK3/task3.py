inp = open("input3.txt", "r")
out = open("output3.txt", "w")
initial_size = int(inp.readline())
sid = inp.readline()  # String input from txt file
sid = sid.split(" ")  # Makes a list from the string
final_sid = []
for i in sid:
    final_sid.append(int(i))  # Converts the string components to integer
mark = inp.readline()  # String input from txt file
mark = mark.split(" ")  # Makes a list from the string
final_mark = []
for i in mark:
    final_mark.append(int(i))  # Converts the string components to integer
my_dict = {}
for i in range(initial_size):  # Links marks with student id
    if final_mark[i] not in my_dict:
        my_dict[final_mark[i]] = [final_sid[i]]
    else:
        my_dict[final_mark[i]] += [final_sid[i]]


def selection_sort(data, size):  # Selection sorting algorithm
    for i in range(size):
        max_index = i  # Assuming First index=max
        for j in range(i + 1, size):  # Comparing the first index with all the other indexes
            if data[j] > data[max_index]:
                max_index = j
        data[i], data[max_index] = data[max_index], data[i]  # Swap the maximum element with the current element

    return data


order = list(set(final_mark))  # Removes duplicate marks using set
final_size = len(order)  # Size of list after removing duplicates
order = selection_sort(order, final_size)  # Sorting the marks in descending order

for x in order:  # Get the students with that mark
    my_dict[x].sort()  # Sorting the IDs in ascending order
    students = my_dict[x]  # IDs that got X marks
    for y in students:
        out.write(f"ID: {y} Mark: {x}\n")
