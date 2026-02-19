from database import Database
from department import Department
from professor import Professor
from course import Course
from student import Student
from enrollment import Enrollment
from grade import Grade
from report_generator import generate_transcript
from utils import generate_id

def main():
    print("Initializing University System...")
    db = Database()

    # 1. Create Department
    cs_dept = Department("Computer Science")
    db.add_department(cs_dept)
    print(f"Created {cs_dept}")

    # 2. Create Professor
    prof_turing = Professor("Alan Turing", "alan@uni.edu", "555-0100", "Dr.", cs_dept.id)
    db.add_professor(prof_turing)
    cs_dept.set_head(prof_turing.id)
    print(f"Created {prof_turing}")

    # 3. Create Course
    algo_course = Course("Algorithms", 4, cs_dept.id)
    db.add_course(algo_course)
    print(f"Created {algo_course}")

    # 4. Create Student
    student_alice = Student("Alice Smith", "alice@uni.edu", "555-0200", "CS", 2024)
    db.add_student(student_alice)
    print(f"Created {student_alice}")

    # 5. Enroll Student
    enrollment = Enrollment(student_alice.id, algo_course.id)
    print(f"Enrolled: {enrollment}")

    # 6. Assign Grade
    grade = Grade(student_alice.id, algo_course.id, 92)
    enrollment.assign_grade(grade)
    print(f"Assigned Grade: {grade}")

    # 7. Generate Transcript
    print("\nGenerating Transcript...")
    print(generate_transcript(student_alice.id))

if __name__ == "__main__":
    main()
