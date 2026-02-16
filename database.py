
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.students = {}
        self.professors = {}
        self.courses = {}
        self.departments = {}
        self.enrollments = []

    def add_student1(self, student):
        self.students[student.id] = student

    def get_student(self, student_id):
        return self.students.get(student_id)

    def add_professor(self, professor):
        self.professors[professor.id] = professor

    def get_professor(self, professor_id):
        return self.professors.get(professor_id)

    def add_department(self, department):
        self.departments[department.id] = department
    
    def get_department(self, department_id):
        return self.departments.get(department_id)

    def add_course(self, course):
        self.courses[course.id] = course

    def get_course(self, course_id):
        return self.courses.get(course_id)

    def add_enrollment(self, enrollment):
        self.enrollments.append(enrollment)

    def get_enrollments_for_student(self, student_id):
        return [e for e in self.enrollments if e.student_id == student_id]

    def get_enrollments_for_course(self, course_id):
        return [e for e in self.enrollments if e.course_id == course_id]





