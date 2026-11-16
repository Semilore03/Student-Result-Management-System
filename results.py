# Functions used for calculating and displaying student results.

def calculate_total(scores):
    total = 0
    for score in scores.values():
        total = total + score
    return total


def calculate_average(scores):
    if len(scores) == 0:
        return 0

    total = calculate_total(scores)
    average = total / len(scores)
    return average


def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    else:
        return "F"
