import json
import os
from student import Student

STORAGE = 'students.json'
def load_records():
    try:
        if os.path.exists(STORAGE):
            with open(STORAGE, 'r') as file:
                return json.load(file)
        return {}
    except json.JSONDecodeError:
        print("\nError reading the student records. The file may be corrupted.")
        return {}
    except Exception as e:
        print(f"\nAn error occurred while loading records: {e}")
        return {}
def save_records(students):
    try:
        with open(STORAGE, 'w') as file:
            json.dump(students, file, indent=4)
    except Exception as e:
        print(f"\nAn error occurred while saving records: {e}")
        return False
    return True
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
    try:
        students = load_records()
        if not students:
            print("\nNo students found.")
            return
        for i, name in enumerate(students, start=1):
            print("-" * 40)
            print(f"{i}. Name: {name}")
            print(f"Marks:")
            for subject, mark in students[name]['marks'].items():
                print(f"  {subject}: {mark}")
            print(f"Average: {students[name]['average']}; Grade: {students[name]['grade']}")
            print("-" * 40)
    except Exception as e:
        print(f"\nError displaying records: {e}")
        return
def main():
    while True:
        print("\n======== Student Records ========")
        print("-" * 40)
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        print("-" * 40)

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