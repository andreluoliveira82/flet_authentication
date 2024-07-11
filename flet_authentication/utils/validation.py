
import re

#Here we will have a class for validation

class Validation():
    """_summary_
    """
    def __init__(self) -> None:
        pass


    def is_valid_email(self, email):
        """_summary_
        """
        if email == "":
            return False
        else:
            # regular expression to valid email
            pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
            return re.match(pattern, email) is not None


    def is_valid_password(self, password: str) -> bool:
        """Checks whether the entered password is a valid password

        Args:
            password (str): an string password to validate

        Returns:
            bool: returns False if failed or True if password is validated
        """
        if len(password) < 6:
            return False
        elif not any(c.isdigit() for c in password):
            return False
        elif not re.search("[@_!#$%^&*()<>?/\\|}{~:}]", password):
            return False
        return True