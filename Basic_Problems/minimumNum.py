# Finding minimum number in a list
numList = [1,57,38,1,8,9]
minNum =numList[0]

for num in numList:
    if minNum > num:
        minNum = num
print(minNum)