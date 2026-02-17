
from util import generate_id

class Course:
    def __init__(self, name, credits, department_id):
        self.id = generate_id("CRS")
        self.name = name
        self.credits = credits
        self.department_id = department_id

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.credits} credits)"

