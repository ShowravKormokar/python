# Building a top half pyramid

#       *
#      * *
#     * * *
#    * * * *

num = 5
for i in range(1, num):
    for j in range(num - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()