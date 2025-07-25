#Counting consonants in a given word
vowel = ['a','e','i','o','u']
word = "Showrav"

count =0
for char in word:
    if char not in vowel:
        count +=1
print(count)