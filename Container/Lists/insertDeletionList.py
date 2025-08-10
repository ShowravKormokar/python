# Insertion in List
list =[1,2,3,4,5]
list.append(6)
print(list)

# Insert by position
list.insert(0,0) #Insert value 0 in position 0(begin)
print(list)

#Extended list by adding another list
list2=[7,8,9]
list.extend(list2)
print(list)


# Deletion in List
list.remove(9) # Remove element from last
print(list)

#Remove element by specific position
list.pop(0)
print(list)

#Remove another way
del list[5] #Remove value 6
print(list)

# Clear list
list.clear()
print(list) #Show empty

#Delete List completely
del list
print(list)