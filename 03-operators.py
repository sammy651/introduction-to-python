# Operators in Python

# Operators are symbols that are used to perform specific operations
# They are used to perform mathematical operations, logical operations, etc.

# Types of Operators

# 1. Arithmetic Operators - they perform mathematical operations like addition, subtraction, multiplication, division
print("Addition: ", 1 + 2)
print("Subtraction: ", 1 - 2)
print("Multiplication: ", 1 * 2)
print("Division: ", 1 / 2)
print("Modulus: ", 11 % 4) # Returns the remainder

# 2. Assignment Operators - they are used to assign values to variables
a = 1
b = 2
c = a + b
first_name = "Samuel"
last_name = "Owusu"

print("Assignment: ", c)
print("Full name: ", first_name + " " + last_name)

# 3. Comparison Operators - they are used to compare two value. They return True or False
a = 1
b = 2
print("a greater than b: ", a > b)
print("a greater than or equal to b: ", a >= b)
print("a less than b: ", a < b)
print("a less than or equal to b: ", a <= b)
print("a equal to b: ", a == b)
print("a not equal to b: ", a != b)

# 4. Logical Operators - they are used to perform logical operations. They return True or False
print("a and b: ", a and b)
print("a or b: ", a or b)

# Unique to Python
# 5. Identity Operators - they are used to check if two objects are identical
a = 1
b = 2
print("a is b: ", a is b)
print("a is not b: ", a is not b)

# 6. Membership Operators - they are used to check if a value is present in a sequence
a = [1, 2, 3]
print("1 in a: ", 1 in a)
print("4 in a: ", 4 in a)

# 7. Bitwise Operators - they are used to perform bitwise operations. Bitwise operations are used to perform operations on binary numbers. They return True or False
a = 10
b = 20
print("a & b: ", a & b) # AND
print("a | b: ", a | b) # OR
print("a ^ b: ", a ^ b) # XOR