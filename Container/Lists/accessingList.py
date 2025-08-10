# Initialization List, using []
list = [1,2,3,4,5] # Index start at 0

#Access element, listName[position]
print(list[2])

#Access element from back
print(list[-2])

# Access element between range
print(list[2:4])

# Default beginning to the range
print(list[:4]) #Including 4th element

# Default ending to the range
print(list[2:])

#Check if exist
if 4 in list:
    print(f"Yes, position is: {list.index(4)}")
else:
    print("No")