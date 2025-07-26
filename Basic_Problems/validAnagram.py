# Comparing two strings for Anagram
str1 = "Showrav"
str2 = "Showrav"

str1 = str1.replace(" ","").upper() #Remove spaces and convert upper to accurate checking
str2 = str2.replace(" ","").upper()

print(str1==str2)