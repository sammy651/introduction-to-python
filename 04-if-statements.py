# If statements in Python

# They used to execute a block of code if a condition is true

# 1. if statement
a = 1
b = 2

if a > b:
    print("a is greater than b")

if a < b:
    print("a is less than b")

# 2. if-else statement
if a > b:
    print("a is greater than b")
else:
    print("a is less than b")

# 3. if-elif-else statement
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# 4. nested if statement
if a >= b:
    if a == b:
        print("a is equal to b")
    else:
        print("a is greater than b")
else:
    print("a is less than b")