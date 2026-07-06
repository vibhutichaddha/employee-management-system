from dataclasses import dataclass
@dataclass
class Address:
    """Represents an employee address."""
    city: str
    state: str
    country: str
    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}"