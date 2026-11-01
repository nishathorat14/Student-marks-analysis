# Student Marks Analysis

# Store student names and marks
students = {
    "Amit": [80, 75, 85],
    "Rahul": [70, 65, 75],
    "Priya": [90, 85, 95],
    "Sneha": [85, 80, 90],
    "Rohan": [60, 70, 65]
}

# Calculate total and average marks
print("Student Marks Analysis\n")

for name, marks in students.items():

    total = sum(marks)
    average = total / 3

    print("Student:", name)
    print("Total Marks:", total)
    print("Average Marks:", average)
    print()

# Find highest and lowest total marks
totals = []

for marks in students.values():
    totals.append(sum(marks))

print("Highest Marks:", max(totals))
print("Lowest Marks:", min(totals))