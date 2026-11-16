import os


def make_student_report(student):
    report = ""
    report += "==========================================\n"
    report += "             STUDENT REPORT CARD\n"
    report += "==========================================\n"
    report += "Student ID: " + student.student_id + "\n"
    report += "Name: " + student.name + "\n"
    report += "Class: " + student.student_class + "\n"
    report += "Gender: " + student.gender + "\n"
    report += "Date of Birth: " + student.date_of_birth + "\n"
    report += "------------------------------------------\n"
    report += "SUBJECT SCORES\n"

    if len(student.scores) == 0:
        report += "No scores have been entered.\n"
    else:
        for subject, score in student.scores.items():
            report += subject + ": " + str(score) + "\n"

    report += "------------------------------------------\n"
    report += "Total: " + str(round(student.get_total(), 2)) + "\n"
    report += "Average: " + str(round(student.get_average(), 2)) + "\n"

    if len(student.scores) > 0:
        report += "Grade: " + student.get_grade() + "\n"
    else:
        report += "Grade: Not available\n"

    report += "Date Result Entered: " + student.date_entered + "\n"
    report += "==========================================\n"
    return report


def make_class_report(students):
    report = ""
    report += "===============================================\n"
    report += "              CLASS RESULT REPORT\n"
    report += "===============================================\n"

    if len(students) == 0:
        report += "There are no registered students.\n"
        return report

    # Sort students from the highest average to the lowest average.
    sorted_students = sorted(students, key=lambda item: item.get_average(), reverse=True)

    for student in sorted_students:
        if len(student.scores) > 0:
            grade = student.get_grade()
        else:
            grade = "N/A"

        report += student.student_id + " - " + student.name
        report += " | Total: " + str(round(student.get_total(), 2))
        report += " | Average: " + str(round(student.get_average(), 2))
        report += " | Grade: " + grade + "\n"

    averages = []
    all_scores = []

    for student in students:
        if len(student.scores) > 0:
            averages.append(student.get_average())
            all_scores.extend(student.scores.values())

    if len(averages) > 0:
        highest_score = max(all_scores)
        lowest_score = min(all_scores)
        class_average = sum(averages) / len(averages)
        highest_average = max(averages)
        lowest_average = min(averages)

        report += "-----------------------------------------------\n"
        report += "Highest Score: " + str(round(highest_score, 2)) + "\n"
        report += "Lowest Score: " + str(round(lowest_score, 2)) + "\n"
        report += "Class Average: " + str(round(class_average, 2)) + "\n"
        report += "Highest Student Average: " + str(round(highest_average, 2)) + "\n"
        report += "Lowest Student Average: " + str(round(lowest_average, 2)) + "\n"

    report += "===============================================\n"
    return report


def save_report(report, file_name):
    report_folder = os.path.join(os.path.dirname(__file__), "reports")

    if not os.path.exists(report_folder):
        os.makedirs(report_folder)

    path = os.path.join(report_folder, file_name)
    report_file = None

    try:
        report_file = open(path, "w", encoding="utf-8")
        report_file.write(report)
    except OSError as error:
        print("The report could not be saved:", error)
        return None
    else:
        return path
    finally:
        if report_file is not None:
            report_file.close()
