# Finding maximum number in a list
numlist = [1,8,3,7,9,0,21,5]
maxNum = numlist[0]

for num in numlist:
    if maxNum < num:
        maxNum = num
print(maxNum)