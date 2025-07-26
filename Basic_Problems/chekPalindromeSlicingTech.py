# Checking for palindrome using extended  slicing technique
str ="Ana"
str=str.lower()

if str == str[::-1]:
    print(True)
else:
    print(False)