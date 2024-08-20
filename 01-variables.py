# Intro to different variables in Python

# 1. THESE ARE PRIMITIVE DATA TYPES
# =================================================================
# Integer - it is a whole number
a = 1
print("Integer: ", a)

# Float - it is a decimal number
b = 1.0
print("Float: ", b)

# String - it is a sequence of characters
c = "Hello there"
print("String: ", c)

# Boolean - it is either True or False
d = True
# d = False
print("Boolean: ", d)

# 2. THESE ARE COLLECTIONS (USER DEFINED DATA TYPES)
# =================================================================
# List - it is a collection of items
e = ["a", 2, 0.45]
print("List: ", e)

# Tuple - it is a collection of items but unlike a list, it cannot be modified
g = (1, 2, 3)
print("Tuple: ", g)

# Set - it is a collection of unique items
h = {1, 2, 3}
print("Set: ", h)

# Dictionary - it is a collection of key-value pairs
f = {
        "a": 1, 
        "b": 2
    }  # {} is called curly braces
print("Dictionary: ", f)

# 3. THESE ARE SPECIAL DATA TYPES
# =================================================================
# None - it is a special value that represents the absence of a value
i = None
print("None: ", i)