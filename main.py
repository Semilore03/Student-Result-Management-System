from datetime import datetime, date
from student import Student
from storage import save_students, load_students
from reports import make_student_report, make_class_report, save_report

# These are the five subjects used in the project.
# A tuple is used because the five subject names are fixed for this project.
subjects = ("English", "Mathematics", "Biology", "Chemistry", "Physics")


def find_student(students, student_id):
    for student in students:
        if student.student_id.lower() == student_id.lower():
            return student
    return None


def register_student(students):
    print("\n--- REGISTER STUDENT ---")
    student_id = input("Enter student ID: ").strip()

    if find_student(students, student_id) is not None:
        print("This student ID already exists.")
        return

    name = input("Enter full name: ").strip()
    student_class = input("Enter class/form: ").strip()
    gender = input("Enter gender: ").strip()

    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date_of_birth, "%Y-%m-%d")
    except ValueError:
        print("Please enter the date in YYYY-MM-DD format.")
        return

    if name == "" or student_class == "" or gender == "":
        print("Please fill in all the details.")
        return

    new_student = Student(student_id, name, student_class, gender, date_of_birth)
    students.append(new_student)
    save_students(students)
    print("Student registered successfully.")


def view_students(students):
    print("\n--- ALL STUDENTS ---")

    if len(students) == 0:
        print("No students have been registered.")
    else:
        for student in students:
            print("ID:", student.student_id)
            print("Name:", student.name)
            print("Class:", student.student_class)
            print("Gender:", student.gender)
            print("------------------------")


def search_student(students):
    search_value = input("Enter student ID or name: ").lower()
    found = False

    for student in students:
        if (search_value in student.student_id.lower()
                or search_value in student.name.lower()):
            print(make_student_report(student))
            found = True

    if found is False:
        print("Student not found.")


def update_student(students):
    student_id = input("Enter the student ID to update: ")
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    print("Press Enter if you do not want to change a detail.")
    name = input("New name (" + student.name + "): ")
    student_class = input("New class (" + student.student_class + "): ")
    gender = input("New gender (" + student.gender + "): ")
    dob = input("New date of birth (" + student.date_of_birth + "): ")

    if name != "":
        student.name = name
    if student_class != "":
        student.student_class = student_class
    if gender != "":
        student.gender = gender

    if dob != "":
        try:
            datetime.strptime(dob, "%Y-%m-%d")
            student.date_of_birth = dob
        except ValueError:
            print("Invalid date. The other changes will still be saved.")

    save_students(students)
    print("Student details updated.")


def delete_student(students):
    student_id = input("Enter the student ID to delete: ")
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    answer = input("Are you sure you want to delete this student? (yes/no): ")

    if answer.lower() == "yes":
        students.remove(student)
        save_students(students)
        print("Student deleted.")
    else:
        print("Delete cancelled.")


def enter_scores(students):
    student_id = input("Enter student ID: ")
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    print("Enter each score from 0 to 100.")

    for subject in subjects:
        while True:
            try:
                score = float(input(subject + " score: "))

                if score >= 0 and score <= 100:
                    student.add_score(subject, score)
                    break
                else:
                    print("Score must be between 0 and 100.")

            except ValueError:
                print("Please enter a number.")

    student.date_entered = date.today().isoformat()
    save_students(students)
    print("Scores saved successfully.")


def update_score(students):
    student_id = input("Enter student ID: ")
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    print("Subjects:", subjects)
    subject = input("Enter the subject name: ")

    if subject not in subjects:
        print("Subject not found.")
        return

    while True:
        try:
            score = float(input("Enter the new score: "))

            if score >= 0 and score <= 100:
                student.add_score(subject, score)
                student.date_entered = date.today().isoformat()
                save_students(students)
                print("Score updated.")
                break
            else:
                print("Score must be between 0 and 100.")

        except ValueError:
            print("Please enter a number.")


def view_report_card(students):
    student_id = input("Enter student ID: ")
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    report = make_student_report(student)
    print(report)

    answer = input("Do you want to save this report? (yes/no): ")
    if answer.lower() == "yes":
        file_name = "report_" + student.student_id + ".txt"
        path = save_report(report, file_name)
        print("Report saved in:", path)


def view_class_report(students):
    report = make_class_report(students)
    print(report)

    answer = input("Do you want to save the class report? (yes/no): ")
    if answer.lower() == "yes":
        path = save_report(report, "class_report.txt")
        print("Report saved in:", path)


def sort_students(students):
    print("1. Sort by average score")
    print("2. Sort by name")
    choice = input("Choose an option: ")

    if choice == "1":
        sorted_students = sorted(
            students,
            key=lambda student: student.get_average(),
            reverse=True
        )
    elif choice == "2":
        sorted_students = sorted(
            students,
            key=lambda student: student.name.lower()
        )
    else:
        print("Invalid choice.")
        return

    for student in sorted_students:
        print(student.name, "-", round(student.get_average(), 2))


def show_menu():
    print("\n======================================")
    print("     STUDENT RESULT MANAGEMENT SYSTEM")
    print("======================================")
    print("1. Register a student")
    print("2. View all students")
    print("3. Search for a student")
    print("4. Update student details")
    print("5. Delete a student")
    print("6. Enter student scores")
    print("7. Update a subject score")
    print("8. View student report card")
    print("9. View class report and statistics")
    print("10. Sort students")
    print("0. Exit")
    print("======================================")


def main():
    students = load_students()
    print("Welcome to the Student Result Management System!")
    print(len(students), "student record(s) loaded.")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            register_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            enter_scores(students)
        elif choice == "7":
            update_score(students)
        elif choice == "8":
            view_report_card(students)
        elif choice == "9":
            view_class_report(students)
        elif choice == "10":
            sort_students(students)
        elif choice == "0":
            save_students(students)
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
