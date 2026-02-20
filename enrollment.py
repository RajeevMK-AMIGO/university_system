
from utils import generate_id, format_date
from datetime import datetime
from database import Database
from notification import NotificationSystem

class Enrollment:
    def __init__(self, student_id, course_id):
        self.id = generate_id("ENR")
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = datetime.now()
        self.grade = None
        
        self.db = Database()
        self._register()

    def _register(self):
        # Notify student about enrollment
        student = self.db.get_student(self.student_id)
        course = self.db.get_course(self.course_id)
        
        if student and course:
            NotificationSystem.send_email(
                student.email, 
                "Course Enrollment", 
                f"You have been enrolled in {course.name}."
            )
            self.db.add_enrollment(self)
        else:
            print("Error: Student or Course not found.")

    def assign_grade(self, grade):
        self.grade = grade
        # Calculate new GPA for student (Mock implementation)
        print(f"Grade {grade.letter_grade} assigned to enrollment {self.id}")

    def __str__(self):
        return f"Enrollment [{self.id}] - Student: {self.student_id}, Course: {self.course_id}, Date: {format_date(self.enrollment_date)}"





