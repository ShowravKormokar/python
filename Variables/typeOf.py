# Type of
x=20
str = "Showrav"

print(type(x))


# List type
l = ["A", "B", "C"]
l1,l2,l3 = l
print(l1) # A

# Tuple type
t = ("D","E","F")
t1,t2,t3 = t
print(t2) # E

# Dict type
d = {"Name":"Showrav", "Age":23}
print(d)
print(d["Name"])

for key, value in d.items():
    print(key,":",value)

# Print JSON file
import json
print(json.dumps(d,indent=4))