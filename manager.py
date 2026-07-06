from employee import Employee
class Manager(Employee):
    """Represents a manager employee."""
    BONUS_RATE=0.20
    def calculate_bonus(self):
        """Calculate manager bonus based on salary."""
        return self.salary * self.BONUS_RATE