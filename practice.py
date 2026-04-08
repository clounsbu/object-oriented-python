# Create a class called Student with the following attributes:
# name (string)
# email (string)
# grades (list of integers)
class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades
# Add the following methods:
# add_grade(self, grade): Adds a grade to the grades list.
    def add_grade(self, grade):
        self.grades.append(grade)
# average_grade(self): Returns the average of all grades.
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
# display_info(self): Prints the student’s name, email, and grades.
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade()}")

# Return grades as a tuple
    def grades_tuple(self):
        # tuple() converts list to a tuple
        return tuple(self.grades)

# Part 2: Working with Objects
# Create 3 student objects with different names, emails, and initial grades.
student1 = Student("Chris", "clounsbu514@gmail.com", [94, 72, 91])
student2 = Student("Tom", "tlo11@gmail.com", [97, 92, 74])
student3 = Student("Bob", "bobthehench@gmail.com", [54, 63, 55])
# Add 2 new grades to each student using the add_grade method.
student1.add_grade(87)
student2.add_grade(78)
student3.add_grade(56)
# Print the information and average grade for each student using display_info.
students = [student1, student2, student3]
print("----Student Info-----")
for student in students:
    student.display_info()
    print()
    
# Part 3: Dictionary & Set Integration
# Create a dictionary called student_dict that maps each student’s email to their corresponding Student object.
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

# Write a function get_student_by_email(email) that retrieves a student object from the dictionary safely using .get().
def get_student_by_email(email):
    return student_dict.get(email)

# Search for a student
print("-----Search by email-----")
student_lookup = get_student_by_email(input("Student email: "))
if student_lookup:
    print("Student found!")
    student_lookup.display_info()
    print()
else:
    print("Student not found.")
# Create a set of all unique grades across all students and print it.
unique_grades = set()

# loop through the students object
for student in students:
    # nested loop to get grades for each student
    for grade in student.grades:
        # Adds each grade to the inique set ignoring duplicates
        unique_grades.add(grade)
# Sort unique grades from lowest to highest
sorted_unique_grades = sorted(unique_grades)
print(f"Unique Grades: {sorted_unique_grades}")
print()

# Part 4: Tuple Practice
print("-----Tuples------")
# Add a method to the Student class called grades_tuple(self) that returns the grades as a tuple.
grades_as_tuple = student1.grades_tuple()
print(f"Grades as tuple: {grades_as_tuple}")
# Demonstrate that tuples are immutable by trying to change a value (catch the exception with try/except and print a message).
try:
    grades_as_tuple[0] = 100
except TypeError:
    print("Tuples are immutable")
    print()

# Part 5: List Operations
print("-----List Operations-----")
# Remove the last grade from each student’s grades list using .pop().
for student in students:
    remove_last_grade = student.grades.pop()
    print(f"Removed {student.name}'s last grade {remove_last_grade}")
# Access and print the first and last grade for each student.
    print(f"{student.name} first grade: {student.grades[0]}")
    print(f"{student.name} last grade: {student.grades[-1]}")
# Print the number of grades each student has using len().
    print(f"Number of grades per student: {len(student.grades)}")

# Grades above a 90
for student in students:
    grades_over_90 = 0

    for grade in student.grades:
        if(grade >= 90):
            grades_over_90 += 1
            
    print(grades_over_90)