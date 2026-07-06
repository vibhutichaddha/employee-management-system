# Employee Management System
## Project Description
The employee management system is a menu friven python application developed using OOP concepts.
The system manages employee records and supports different employee types such as Developer, Manager and HR. It demonstrates core Python concepts including inheritance, polymorphism, encapsulation, properties, dataclasses, object association and exception handling.
Employee records are stored in a list of objects during program execution. No database or file storage is used.
## Features
-Add employee
-Search employee by ID
-Update employee salary
-Delete employee
-Display all employees
-Calculate Bonus based on employee type
## OOP Concepts Used
- Inheritance
- Polymorphism
- Method Overriding 
- Encapsulation
- Private Attributes
- Property Decorators
- Object Association
- Dataclasses
## Project Structure
employee_management/
|
|__main.py
|__employee.py
|__developer.py
|__manager.py
|__hr.py
|__address.py
|__exceptions.py
|__README.md
## Class Structure
### Employee
The 'Employee' class is the base class for all employee types.
Salary is implemented as a private attribute and validated using '@property' decorator.
### Developer
The 'Developer' class inherits from 'Employee' class and overrides the 'calculate_bonus()' method.
### Manager
The 'Manager' class inherits from 'Employee' class and provides its own implementation of the 'calculate_bonus()' method.
### Address
The 'Address' class is created using '@dataclass' and is associated with each employee object.
## Exception Handling 
The application handles the following errors:
- Duplicate employee ID
- Invalid salary
- Employee Not Found
- Invalid Menu Choice
## Execution steps
1. Clone the repository
2. Navigate the project directory
3. Ensure Python 3.12 or above is downloaded
4. Run the 'main.py' file using: 'python3 main.py'
5. Select the required option from the menu
6. Follow the on-screen instructions to add, search, update, delete or display employees and calculate employee bonuses.
## Requirements
- Python 3.12 or above
- Linux 
## Author
Vibhuti Chaddha
