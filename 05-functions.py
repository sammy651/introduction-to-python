# Funtions in Python

#  Funtions are a block of code that performs a specific task
#NB:  They are used to perform repetitive tasks

# A function can have 0 or more parameters
# A function can have 0 or more return values
# In order to use a function, you need to call it

# 1. Defining a function
# =================================================================
def hello():
    print("Hello World")

# 2. Calling a function
# =================================================================
hello()

# 3. Parameters
# =================================================================
def hello(name):
    print("Hello " + name)

hello("Samuel")

# 4. Return values
# =================================================================
def hello(name):
    return "Hello " + name

print(hello("Samuel"))

# 5. Multiple parameters
# =================================================================
def hello(first_name, last_name):
    return "Hello " + first_name + " " + last_name

print(hello("Samuel", "Owusu"))

# 6. An example with conditional statements
# =================================================================
def hello(first_name, last_name):
    if first_name == "Samuel":
        return "Hello " + first_name
    else:
        return "Hello " + first_name + " " + last_name

print(hello("Samuel", "Owusu"))
print(hello("John", "Doe"))

# 7. An example with loops
# =================================================================
def hello(first_name, last_name):
    for i in range(5):
        print("Hello " + first_name + " " + last_name)

hello("Samuel", "Owusu")