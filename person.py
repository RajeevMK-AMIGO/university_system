
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.email})"

    def update_contact_info(self, email=None, phone=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
