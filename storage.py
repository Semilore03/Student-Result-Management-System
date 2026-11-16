import json
import os
from student import Student

# The data folder and file are created if they do not exist.
folder = os.path.join(os.path.dirname(__file__), "data")
file_name = os.path.join(folder, "students.json")


def save_students(students):
    if not os.path.exists(folder):
        os.makedirs(folder)

    student_list = []

    for student in students:
        student_list.append(student.to_dictionary())

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(student_list, file, indent=4)


def load_students():
    if not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump([], file)
        return []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            student_list = json.load(file)

        students = []
        for details in student_list:
            students.append(Student.from_dictionary(details))

        return students

    except json.JSONDecodeError:
        print("The student data file is empty or has a problem.")
        return []
