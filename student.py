
from person import Person
from tils import generate_id

class Student(Person):
    def __init__(self, name, email, phone, major, year):
        super().__init__(generate_id("STU"), name, email, phone)
        self.major = major
        self.year = year
        self.gpa = 0.0

    def __str__(self):
        return super().__str__() + f" - {self.major} ({self.year})"

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

