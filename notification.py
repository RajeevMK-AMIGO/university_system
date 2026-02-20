
class NotificationSystem:
    @staticmethod
    def sendemail(to_email: str, subject: str, body: str):
        """Simulates sending an email."""
        print(f"--- EMAIL NOTIFICATION ---")
        print(f"To: {to_email}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        print("--------------------------")

    @staticmethod
    def send_sms(to_phone: str, message: str):
        """Simulates sending an SMS."""
        print(f"--- SMS NOTIFICATION ---")
        print(f"To: {to_phone}")
        print(f"Message: {message}")
        print("------------------------")



