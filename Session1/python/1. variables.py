# Section 1: Variables
# ---------------------

# Assignment 1: Create two variables, one holding a number and the other holding your name. Then print both.
my_age = 23
my_name = "Nur Jahan Smrity"
print("Age: ", my_age, end="; ")
print("Name: ", my_name)
friends_age = 24
friends_name = "Lamia Muskan"
print("Age: ", friends_age)
print("Name: ", friends_name)

# Section 2: Data Types
# ---------------------

# Assignment 2: Create variables of different types and use the type() function to check their types.
a = 9                                # int
b = 3.141                      # float
c = "Learning Python"                # string
d = False                            # bool
e = {2,4,5}                          #set
g = 1+3j  

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(g))

# Section 3: Variable Naming Conventions and Industry Standards
# -------------------------------------------------------------

# 2bad = 42  # This will raise a SyntaxError because variable names cannot begin with a number.
# Assignment 3: Fix the bad variable name above and create three more variables with good naming practices.

bad_2 = 42
bad_1 = "bad_2"
print('After fixing 2bad variable name : ', bad_1, ' = ', bad_2)
#here is the 3 more variable name
weight = "55 kg"
salary = "50k"
height = "5 feet 4 inch"

print('weight : ',weight)
print('salary : ',salary)
print('height : ',height)

# Section 4: Python's Dynamic Typing
# ----------------------------------

var = "I am a string"
print(var)

var = 42
print(var)
# Assignment 4: Create a variable, assign it a value of one type, then reassign it to a different type and print both.

variable = 56.566
print(variable)

variable = "float variable is changed to a string"
print(variable)