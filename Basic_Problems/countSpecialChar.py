# Counting special characters
str = "Hello! how are you?"

sp_char = "!~@#$%^&*()-_+={}[]\|<>`?/"

count =0
for i in str:
    if i in sp_char:
        count +=1

print(count)