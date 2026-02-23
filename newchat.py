# Store student names
students = ["Jon", "Kim", "Lee", "Sara", "Miko", "Lin", "Toby", "Ben", "Mark", "Xia",
            "Jake", "Markus", "Teri", "Leigh"]

# Store GPAs in the same order
gpas = [3.25, 2.25, 2.30, 4.00, 1.90, 2.10, 2.89, 2.75, 2.34, 3.53,
        2.75, 2.90, 3.15, 3.75]

# ---- Print all students and GPAs ----
print("Student GPA List:")
for i in range(len(students)):
    print(students[i], ":", gpas[i])

# ---- Calculate average GPA ----
total = 0
for gpa in gpas:
    total = total + gpa

average = total / len(gpas)
print("\nAverage GPA:", round(average, 2))

# ---- Print above-average students ----
print("\nStudents above average GPA:")
for i in range(len(students)):
    if gpas[i] > average:
        print(students[i], "-", gpas[i])

# ---- Predict scholarship students ----
# Rule: GPA 2.75 or higher earns scholarship (updated threshold)
print("\nScholarship predictions:")
for i in range(len(students)):
    if gpas[i] >= 3.5:
        print(students[i], "-", gpas[i])