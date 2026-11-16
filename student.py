class Student:
    # This class stores the details and scores of one student.

    def __init__(self, student_id, name, student_class, gender, date_of_birth):
        self.student_id = student_id
        self.name = name
        self.student_class = student_class
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.scores = {}
        self.date_entered = ""

    def add_score(self, subject, score):
        self.scores[subject] = score

    def get_total(self):
        total = 0
        for score in self.scores.values():
            total = total + score
        return total

    def get_average(self):
        if len(self.scores) == 0:
            return 0

        return self.get_total() / len(self.scores)

    def get_grade(self):
        average = self.get_average()

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

    def to_dictionary(self):
        # JSON files store dictionaries, so this changes the student to a dictionary.
        return {
            "student_id": self.student_id,
            "name": self.name,
            "student_class": self.student_class,
            "gender": self.gender,
            "date_of_birth": self.date_of_birth,
            "scores": self.scores,
            "date_entered": self.date_entered
        }

    @staticmethod
    def from_dictionary(details):
        # This changes the dictionary from the JSON file back into a Student object.
        student = Student(
            details["student_id"],
            details["name"],
            details["student_class"],
            details["gender"],
            details["date_of_birth"]
        )
        student.scores = details.get("scores", {})
        student.date_entered = details.get("date_entered", "")
        return student
