# Section 1: Dictionary Basics
# ----------------------------

# Assignment 1: Create a dictionary representing a student with keys like 'name', 'roll_number', 'grades' (a list of subjects and marks).
# Perform various operations like adding, removing, and modifying elements.

# Initial dictionary 
student = { 
    'name': 'Smrity', 
    'roll_number': 'C193254', 
    'grades': { 
        'Math': 85, 
        'Science': 90, 
        'English': 88 
        } 
    } 
print("Initial Dictionary:") 
print(student)
# Adding a new subject and grade 
student['grades']['History'] = 92 
print("\nAfter Adding History:") 
print(student)
# Removing a subject and grade 
del student['grades']['Math'] 
print("\nAfter Removing Math:") 
print(student) 
# Modifying a grade 
student['grades']['Science'] = 95 
print("\nAfter Modifying Science Grade:") 
print(student)


# Section 2: Integrating Dictionaries with Lists and Tuples
# ---------------------------------------------------------

# Assignment 2: Create a dictionary where keys are student names and values are lists of grades. Calculate the average grade for each student.

# Initial dictionary with student names and their grades 
students_grades = { 
    'Smrity': [85, 90, 88], 
    'Nurjahan': [78, 82, 79], 
    'Mariya': [92, 88, 91], 
    'Sumaiya': [76, 85, 80], 
    'Rozina': [89, 94, 90] 
} 
# Function to calculate the average grade 
def calculate_average(grades): 
    return sum(grades) / len(grades) 
# Dictionary to store the average grades 
students_averages = {} 
# Calculating the average grade for each student 
for student, grades in students_grades.items(): 
    average = calculate_average(grades) 
    students_averages[student] = average 
print("Average Grades:") 
for student, average in students_averages.items(): 
    print(f"{student}: {average:.2f}")
