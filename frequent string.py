def calc(inputstr):
    myDict = {}
    for char in inputstr:
        if char in myDict:
            myDict[char] += 1
        else:
            myDict[char] = 1
    return(sorted(myDict.items(),key=lambda x: x[1],reverse=True))

inputstr = input("enter the string you want to check:")
res = calc(inputstr)
for i in range(0,(len(res))):
    print(f'\n{res[i][0]} : {res[i][1]}')