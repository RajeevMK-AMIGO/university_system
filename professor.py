
from person import Person
from utils import generate_id

class Professor(Person):
    def __init__(self, name, email, phone, title, department_id):
        super().__init__(generate_id("PROF"), name, email, phone)
        self.title = title
        self.department_id = department_id

    def __str__(self):
        return super().__str__() + f" - {self.title}"
