
# from abc import ABC, abstractmethod

# class Person(ABC):
#     def __init__(self, id, name, email, phone):
#         self.id = id
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def __str__(self):
#         return f"[{self.id}] {self.name} ({self.email})"

#     def update_contact_info1(self, email=None, phone=None):
#         if email:
#             self.email = email
#         if phone:
#             self.phone = phone

# new

from abc import ABC, abstractmethod
from notification import NotificationSystem

class Person(ABC):
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.email})"

    def update_contact_info1(self, email=None, phone=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        
        # Call notification after updating contact info
        self._notify_contact_info_updated()

    def _notify_contact_info_updated(self):
        """Notify person about contact information update"""

        NotificationSystem.send_email(
            self.email,
            "Contact Information Updated",
            f"Your contact information has been successfully updated. Email: {self.email}, Phone: {self.phone}"
        )


