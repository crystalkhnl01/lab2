students = {}
n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    students[name] = marks

print("\nAverage Marks of Each Student:")
for name in students:
    marks = students[name]
    avg = (marks[0] + marks[1] + marks[2]) / 3
    print(f"{name}: {avg:.2f}")
highest_avg = -1
topper = ""
for name in students:
    marks = students[name]
    avg = (marks[0] + marks[1] + marks[2]) / 3
    if avg > highest_avg:
        highest_avg = avg
        topper = name
print(f"\nTopper: {topper} with average marks {highest_avg:.2f}")
name_to_update = input("\nEnter the name of the student to update marks: ")
if name_to_update in students:
    print(f"Current marks: {students[name_to_update]}")
    new_marks = []
    for i in range(1, 4):
        new_mark = float(input(f"Enter new marks for subject {i}: "))
        new_marks.append(new_mark)
    students[name_to_update] = new_marks
    print(f"Updated marks for {name_to_update}: {students[name_to_update]}")
else:
    print("Student not found.")
