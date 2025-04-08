# 2 Student Grades
# Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
# Add a new student and grade.
# Update an existing student’s grade.
# Print all student grades.

def add_student(students):
    name = input("Enter the student's name: ")
    grade = input("Enter the student's grade: ")
    students[name] = grade
    print(f"Added {name} with grade {grade}.")
def update_student(students):
    name = input("Enter the student's name to update: ")
    if name in students:
        grade = input(f"Enter the new grade for {name}: ")
        students[name] = grade
        print(f"Updated {name}'s grade to {grade}.")
    else:
        print(f"{name} not found in the records.")
def print_students(students):
    if students:
        print("Student Grades:")
        print(students)
        for name, grade in students.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")

def main():
    students = {}
    while True:
        # Display menu
        print("\n1. Add Student" )
        print("2. Update Student Grade")
        print("3. Print All Students")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            update_student(students)
        elif choice == '3':
            print_students(students)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()