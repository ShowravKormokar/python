# Create Global variable
global x

x = 20

def myFunc1():
    print("X is under func: ",x) #Access anywhere

def myFunc2():
    global y 
    y=90
    print("Y is under function= ", y)

#Call func
myFunc1()
myFunc2()

#print(y) #it cannot be access because y is declare under function
print("X is outside function= ", x)
