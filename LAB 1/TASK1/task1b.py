inp = open("input1b.txt", "r")
out = open("output1b.txt", "w")
s = inp.readline()
for i in range(int(s)):
    text = inp.readline()
    text = text.replace("calculate", "")
    text = text.replace("\n", "")
    out.write("The result of"+text+" is "+str(eval(text))+"\n")
