# Counting vowels in an given word
vowels = ['a','e','i','o','u']
word = "Programming"

count =0
for char in word:
    if char in vowels:
        count+=1
print(count)