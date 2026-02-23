# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]

# add two more students after the initial list is created
students.append("Sara")
students.append("Miko")

# function to print ‘Hi name’ for each student in the list
# and then display the total number of students
def greet_students(students):
    for student in students:
        print(f"Hi {student}")
    print(f"Total students: {len(students)}")

# call the function to greet the students
greet_students(students)

# change Jon to John (first element at index 0)
students[0] = "John"

print("\nUpdated student list:")
print(students)

# ---------- GPA COLLECTION PROGRAM ----------

# Create new empty lists for GPA analysis
student_names = []
gpas = []

# Input 25 students and GPAs
for i in range(25):
    name = input(f"Enter name of student {i+1}: ")
    gpa = float(input(f"Enter GPA of {name}: "))
    
    student_names.append(name)
    gpas.append(gpa)

# Display stored data
print("\nStudent GPA List:")
for i in range(25):
    print(f"{student_names[i]} : {gpas[i]}")

    # Store student names
students = ["Jon", "Kim", "Lee", "Sara", "Miko", "Lin", "Toby", "Ben", "Mark", "Xia"]

# Store GPAs (same order as names)
gpas = [3.25, 2.25, 2.30, 4.00, 1.90, 2.10, 2.89, 2.75, 2.34, 3.53]

# ---- Calculate average GPA ----
total = 0
for gpa in gpas:
    total = total + gpa

average = total / len(gpas)

print("Average GPA:", round(average, 2))

# ---- Print above-average students ----
print("\nStudents above average GPA:")
for i in range(len(students)):
    if gpas[i] > average:
        print(students[i], "-", gpas[i])

# ---- Predict scholarship students ----
# (Example rule: GPA >= 3.5 gets scholarship)
print("\nScholarship predictions:")
for i in range(len(students)):
    if gpas[i] >= 3.5:
        print(students[i], "-", gpas[i])