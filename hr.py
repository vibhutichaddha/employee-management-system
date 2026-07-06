from employee import Employee
class HR(Employee):
    """Represents an HR employee."""
    BONUS_RATE=0.15
    def calculate_bonus(self):
        """Calculate HR bonus based on salary."""
        return self.salary * self.BONUS_RATE