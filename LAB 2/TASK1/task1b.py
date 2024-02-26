def targetFinder(arr, n, target):
    left_pointer, right_pointer = 0, n - 1

    for i in range(n):
        if left_pointer == right_pointer:
            return "IMPOSSIBLE"
        if arr[left_pointer] + arr[right_pointer] == target:
            return f"{left_pointer + 1} {right_pointer + 1}"
        elif arr[left_pointer] + arr[right_pointer] < target:
            left_pointer += 1
        elif arr[left_pointer] + arr[right_pointer] > target:
            right_pointer -= 1


inp = open("input1b.txt", "r")
out = open("output1b.txt", "w")
parameters = inp.readline().split()
parameters = [int(i) for i in parameters]
n = parameters[0]
target = parameters[1]
arr = inp.readline().split()
arr = [int(i) for i in arr]
return_position = targetFinder(arr, n, target)
out.write(return_position)
