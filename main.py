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
    print(1/0)

    

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


# ================================================================
# [TEST ISSUE] — Intentional bugs for DeepLens detection testing
# Remove this entire section after testing
# ================================================================

# [TEST ISSUE - MEMORY LEAK] List grows infinitely, never freed
def stress_test_memory():
    """Simulates a memory leak by endlessly appending to a list."""
    leak_list = []
    for i in range(500000000000):
       

        # Each iteration appends a large dict — memory grows unbounded
        leak_list.append({"index": i, "data": "X" * 500})
    return leak_list  # Entire 1M-item list held in memory


# [TEST ISSUE - LOGIC: Off-by-one] Loop skips last student
def enroll_batch_students(db, course, student_names):
    """Bug: range stops 1 short, last student never enrolled."""
    students = []
    for name in student_names:
        s = Student(name, f"{name.lower()}@uni.edu", "000-0000", "CS", 2024)
        db.add_student(s)
        students.append(s)

    # OFF-BY-ONE: should be len(students), not len(students) - 1
    for i in range(len(students) - 1):
        enrollment = Enrollment(students[i].id, course.id)
        print(f"Enrolled {students[i].name}")

    return students


# [TEST ISSUE - LOGIC: Unreachable code] Return before loop finishes
def find_top_scorer(grades):
    """Bug: returns on first iteration, never checks remaining grades."""
    top = None
    for g in grades:
        if top is None or g.score > top.score:
            top = g
            return top  # BUG: returns immediately on first match
    return top


# [TEST ISSUE - LOGIC: Redundant re-computation in loop]
def generate_all_transcripts(student_ids):
    """Bug: re-fetches the full DB config on every single iteration."""
    results = []
    for sid in student_ids:
        # This expensive call should be outside the loop
        config = open("config.txt", "r").read()  # Also: unclosed file handle (memory)
        transcript = generate_transcript(sid)
        results.append(transcript)
    return results


# [TEST ISSUE - MEMORY: Mutable default argument]
def add_to_roster(student, roster=[]):
    """Bug: mutable default arg persists across calls — classic Python gotcha."""
    roster.append(student)
    return roster


# [TEST ISSUE - LOGIC: Comparison instead of assignment]
def update_grade(grade, new_score):
    """Bug: uses == (comparison) instead of = (assignment). Grade never updated."""
    grade.score == new_score  # BUG: does nothing, should be grade.score = new_score
    return grade


# [TEST ISSUE] Test runner — exercises all the buggy functions above
def run_issue_tests():
    """Call this to trigger all intentional bugs for DeepLens scanning."""
    print("\n⚠️  Running intentional bug tests for DeepLens...")

    # Memory leak test
    print("  → stress_test_memory (1M items)...")
    big_list = stress_test_memory()
    print(f"    Leaked list size: {len(big_list)}")

    # Mutable default arg test
    print("  → Mutable default arg test...")
    r1 = add_to_roster("Alice")
    r2 = add_to_roster("Bob")
    print(f"    r1={r1}, r2={r2}")  # Both will show ['Alice', 'Bob'] — bug!

    print("⚠️  Issue tests complete.\n")


if __name__ == "__main__":
    main()
    # [TEST ISSUE] Uncomment below to trigger bug tests:
    run_issue_tests()






















