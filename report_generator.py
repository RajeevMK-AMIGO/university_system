
from database import Database

def generate_transcript(student_id):
    db = Database()
    student = db.get_student(student_id)
    if not student:
        return "Student not found."

    enrollments = db.get_enrollments_for_student(student_id)
    report = f"TRANSCRIPT FOR {student.name}\n"
    report += "-"*35 + "\n"
    for enrollment in enrollments:
        grade_str = enrollment.grade.letter_grade if enrollment.grade else "N/A"
        course = db.get_course(enrollment.course_id)
        report += f"{course.name}: {grade_str}\n"
    report += "-"*30 + "\n"
    return report


