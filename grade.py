
class Grade:
    def __init__(self, student_id, course_id, numeric_score):
        self.student_id = student_id
        self.course_id = course_id
        self.numeric_score = numeric_score
        self.letter_grade = self._calculate_letter_grade()

    def _calculate_letter_grade(self):
        if self.numeric_score >= 90: return 'A'
        elif self.numeric_score >= 80: return 'B'
        elif self.numeric_score >= 70: return 'C'
        elif self.numeric_score >= 60: return 'D'
        else: return 'F'

    def __str__(self):
        return f"Grade: {self.letter_grade} ({self.numeric_score})"
