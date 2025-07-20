import json
import os
from student import Student

STORAGE = 'students.json'
def load_records():
    if os.path.exists(STORAGE):
        with open(STORAGE, 'r') as file:
            return json.load(file)
    return {}
def save_records(students):
    with open(STORAGE, 'w') as file:
        json.dump(students, file, indent=4)
def add_student():
    name = input("\nEnter student's name: ")
    subjects = {}
    while True:
        subject = input("\nEnter subject name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            mark = float(input(f"Enter marks for {subject}: "))
            subjects[subject] = mark
        except ValueError:
            print("\nInvalid input. Please enter a numeric value for marks.")
    student = Student(name, subjects)
    students = load_records()
    students[name] = student.to_rec()
    save_records(students)
    print(f"Student {name} added successfully.")
def view_students():
    students = load_records()
    if not students:
        print("\nNo students found.")
        return
    for name, record in students.items():
        print("-" * 40)
        print(f"Name: {name}, Marks: {record['marks']}, Average: {record['average']:.2f}, Grade: {record['grade']}")
def main():
    while True:
        print("\nStudent Report Card System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        in_req = int(input("Enter your choice: "))
        if in_req == 1:
            add_student()
        elif in_req == 2:
            view_students()
        elif in_req == 3:
            print("\nExiting system....")
            break
        else:
            print("Invalid entry. Please try again.")

main()