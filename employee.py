from address import Address
from exceptions import InvalidSalaryError
class Employee:
    """Base class representing and employee."""
    def __init__(self, employee_id: int, name: str, salary: float, address: Address):
        self.employee_id = employee_id
        self.name = name
        self.__salary = 0.0
        self.salary=salary
        self.address = address
    @property
    def salary(self):
        """Return the employee salary."""
        return self.__salary
    @salary.setter
    def salary(self, value):
        """Validate and update the employee salary."""
        if value <= 0:
            raise InvalidSalaryError("Salary must be greater than 0.")
        self.__salary = value
    def calculate_bonus(self):
        """Calculate employee bonus"""
        return 0.0
    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}, Address: {self.address}"