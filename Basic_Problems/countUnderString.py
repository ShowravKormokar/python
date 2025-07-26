# Counting digits, letters, and spaces in a string
str = "Is price $35?"

import re #Importing regular expression library

digitCount = re.sub("[^0-9]","",str)
letterCount = re.sub("[^a-zA-Z]","",str)
spaceCount = re.findall("[ \S]",str)

print(len(digitCount))
print(len(letterCount))
print(len(spaceCount))