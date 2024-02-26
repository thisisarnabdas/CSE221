inp = open("input1a.txt", "r")
out = open("output1a.txt", "w")
s = inp.readline()
for i in range(int(s)):
    a = int(inp.readline())
    if a % 2 == 0:
        out.write(str(a) + " is an even number.\n")
    else:
        out.write(str(a) + " is an odd number.\n")
