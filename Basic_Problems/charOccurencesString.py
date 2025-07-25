# Counting the number of occurrences of a character in a string
str = "Programming"
char = 'g'
count =0
for i in str:
    if i in char:
        count+=1
print(count)