def bubbleSort(array):
    for i in range(n):
        for j in range(n - i - 1):
            tr1 = array[j].split(" ")
            tr2 = array[j + 1].split(" ")
            if (tr1[0] > tr2[0]) or (tr1[0] == tr2[0] and tr1[-1].replace(":", '') < tr2[-1].replace(":", '')):
                array[j], array[j + 1] = array[j + 1], array[j]


inp = open("input4.txt", "r")
out = open("output4.txt", "w")
n = int(inp.readline())
train_det = []
for i in range(n):
    train_det.append(inp.readline())
bubbleSort(train_det)
for i in train_det:
    out.write(i)
