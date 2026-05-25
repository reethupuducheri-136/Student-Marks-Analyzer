print("===================================")
print("     STUDENT MARKS ANALYZER")
print("===================================")

# Student Name
student_name = input("Enter student name: ")

# Subject Marks
math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

# Display Marks
print("\n========== RESULT ==========")

print("Student Name:", student_name)

print("\nSubject Marks")
print("----------------------")
print("Math:", math)
print("Science:", science)
print("English:", english)

# Total
total = math + science + english

# Average
average = round(total / 3, 2)

# Grade System
if average >= 90:
    grade = "A"

elif average >= 75:
    grade = "B"

elif average >= 50:
    grade = "C"

else:
    grade = "Fail"

# Highest & Lowest
marks = [math, science, english]

highest = max(marks)
lowest = min(marks)

# Final Result
print("\n========== ANALYSIS ==========")

print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)

print("Highest Mark:", highest)
print("Lowest Mark:", lowest)

# Subject Pass/Fail
print("\n========== SUBJECT STATUS ==========")

if math >= 35:
    print("Math: Pass")
else:
    print("Math: Fail")

if science >= 35:
    print("Science: Pass")
else:
    print("Science: Fail")

if english >= 35:
    print("English: Pass")
else:
    print("English: Fail")

print("\n===================================")
print("   ANALYSIS COMPLETED SUCCESSFULLY")
print("===================================")
