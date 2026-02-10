
import re
import uuid
from datetime import datetime

def generate_id(prefix: str) -> str:
    """Generates a unique ID with a given prefix."""
    unique_suffix = uuid.uuid4().hex[:8]
    return f"{prefix}_{unique_suffix}"

def validate_email(email: str) -> bool:
    """Validates an email address using regex."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def format_date(date_obj: datetime) -> str:
    """Formats a datetime object to a standard string format."""
    return date_obj.strftime("%Y-%m-%d %H:%M:%S")
