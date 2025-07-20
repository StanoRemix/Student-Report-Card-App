from student import Student
marks = {
    'Math': 85,
    'Science': 78,
    'English': 92,
    'History': 88
}
student = Student("John Doe", marks)
record = student.to_rec()
print(record)
# This will output the student's record with name, marks, average, and grade.