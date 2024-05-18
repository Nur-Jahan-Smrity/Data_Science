# Section 1: Python Lists
# -----------------------

# Copy a list(This part is very much important . be careful while doing so .)
simple_list = [8, 2, 9, 4, 5]
duplicate_list = simple_list
duplicate_list.append(7)
print("simple_list id", id(simple_list), "duplicate_list id: ", id(duplicate_list))
print("Duplicate List: ", duplicate_list)
print("Simple List: ", simple_list)
list_copy = simple_list.copy()
list_copy.append(8)
print("List Copy: ", list_copy)
print("Simple List: ", simple_list)

# Assignment 1: Create a 2D list representing a 3x3 matrix and perform operations like accessing, modifying, and iterating through it.

matrix = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
#accessing matrix
print(matrix[1][2])
#modifying the matrix
matrix[1][2] = 60006
print(matrix[1][2])
#iterating elements 
for row in matrix:
    for element in row:
        print(element,end=" ")
    print()

# Section 2: Python Tuples
# ------------------------

# Assignment 2: Create a tuple with mixed data types and demonstrate its potential use cases in data structures like dictionaries.
#tuple with mixed data type

smrity_info =("Smrity",23,"Female",["python","data science"])
another_example_of_key = 10
#dictionary using tuple
my_info = {
    "name": smrity_info[0],
    "age": smrity_info[1],
    "gender": smrity_info[2],
    "my_interest": smrity_info[3]
}
#print the dictionary value 
print(my_info)
#print specific key value of the dictionary 
print("interest : ",my_info["my_interest"])
print("age : ",my_info["age"])


# Section 3: Advanced Applications
# --------------------------------

simple_list.sort()
print(simple_list)
even_numbers = [x for x in simple_list if x % 2 ==0]
print("even numbers are : ",even_numbers)
odd_numbers = [x for x in simple_list if x % 2 !=0]
print("odd numbers are : ",odd_numbers)

even_odd_numbers = [("even", x) if x % 2 == 0 else ("odd", x) for x in simple_list]
for category, number in even_odd_numbers: 
    print(f"{number} is {category}")

another_matrix = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
print("Initial matrix : ")
for row in another_matrix:
    for cell in row:
        print(cell,end=" ")
    print()
incremented_matrix = [[cell + 1 for cell in row] for row in another_matrix]
print("Incremented matrix : ")
for row in incremented_matrix:
    for cell in row:
        print(cell,end=" ")
    print()
       
# Assignment 3: Create a list of tuples, where each tuple contains a student's name and their grade. Sort this list by grades.

students_info = [("smrity", 10), ("mariya", 90), ("sumaiya", 20), ("elsa", 30), ("ena", 11), ("jupiter", 22)]
# Sorted
students_info.sort(key=lambda x: x[1])
for student in students_info: 
    print(student)
