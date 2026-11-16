# Student Result Management System

## Introduction

This is my Python practical project. It is a simple program that can be used to keep student details and their examination scores.

I used Python to create the program. I also used a JSON file to save student information so that the records will still be available when the program is opened again.

## Features

1. Register a student.
2. View all registered students.
3. Search for a student by ID or name.
4. Update student details.
5. Delete a student.
6. Enter scores for five subjects.
7. Update a subject score.
8. Calculate total, average and grade.
9. Print an individual report card.
10. View class results and statistics, including the highest score, lowest score and class average.
11. Sort students by average or name.
12. Save student records in a JSON file.

## Subjects

- English
- Mathematics
- Biology
- Chemistry
- Physics

## Grade system

- 70 to 100 = A
- 60 to 69 = B
- 50 to 59 = C
- 45 to 49 = D
- 0 to 44 = F

## How to run the program

1. Download and extract the project folder.
2. Open the folder in Visual Studio Code.
3. Open the terminal.
4. Type `python main.py` and press Enter.
5. Follow the menu displayed on the screen.

If `python` does not work on Windows, try `py main.py`.

## Files in the project

- `main.py` contains the main menu and program functions.
- `student.py` contains the Student class.
- `results.py` contains result calculation functions.
- `storage.py` saves and loads student records.
- `reports.py` creates student and class reports.
- `data/students.json` stores the student records.

## Python concepts used

The project demonstrates variables, strings, numbers, lists, tuples, dictionaries, if/elif/else statements, for and while loops, functions with parameters and return values, sorting, exception handling (try/except/else/finally), file handling, JSON, modules and Object-Oriented Programming through the Student class. It also uses Python's datetime module to record when scores are entered.

## Note

This is a command-line project created for learning and practising Python programming.
