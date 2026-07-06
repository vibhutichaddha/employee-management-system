from employee import Employee
class Developer(Employee):
    """Represents a developer employee."""
    BONUS_RATE=0.10
    def calculate_bonus(self):
        """Calculate developer bonus based on salary."""
        return self.salary * self.BONUS_RATE