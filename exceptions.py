class DuplicateEmployeeError(Exception):
    """Raised when a duplicate employee is found in the system."""
class InvalidSalaryError(Exception):
    """Raised when an invalid salary is provided for an employee."""
class EmployeeNotFoundError(Exception):
    """Raised when an employee is not found in the system."""
class InvalidMenuChoiceError(Exception):
    """Raised when an invalid menu choice is made in the application."""