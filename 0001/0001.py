#u 200 diffrent code

import random

listStr = []
codeSet = set("")
while len(codeSet) < 200:
    s = ""
    for i in range(6):
    #print random.randrange(65,90)
        listStr.append(chr(random.randrange(65,90)))
        s = "".join(listStr)
    codeSet.add(s)
    listStr=[]

print codeSet