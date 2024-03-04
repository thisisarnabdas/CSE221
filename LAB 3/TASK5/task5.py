import random


def quickSort(arr):
    if len(arr) < 2:
        return arr

    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    arr[pivot_idx], arr[-1] = arr[-1], arr[pivot_idx]
    less = [x for x in arr[:-1] if x < pivot]
    greater = [x for x in arr[:-1] if x >= pivot]

    return quickSort(less) + [pivot] + quickSort(greater)


inp = open("input5.txt", "r")
out = open("output5.txt", "w")

size = int(inp.readline())
unsorted = inp.readline().split()
unsorted = [int(numbers) for numbers in unsorted]  # converting string to int
sorted_numbers = quickSort(unsorted)

for i in sorted_numbers:
    out.write(f"{i} ")
