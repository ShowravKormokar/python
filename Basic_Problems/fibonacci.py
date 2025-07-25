# Write fibonacci series

# Type- 01
def fibonacci_nth(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b, a+b
    return a

# Print 5th fibonacci number
print(fibonacci_nth(10))

# Type- 02
def fib_series(n):
    a,b = 0,1
    for _ in range(n):
        print(a, end=" ")
        a,b= b, a+b
fib_series(10)