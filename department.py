
from utils import generate_id

class Department:
    def __init__(self, name, head_id=None):
        self.id = generat_id("DEPT")
        self.name = name
        self.head_id = head_id

    def __str__(self):
        return f"{self.name} Department (Head: {self.head_id})"
    
    def set_head(self, professor_id):
        self.head_id = professor_id




