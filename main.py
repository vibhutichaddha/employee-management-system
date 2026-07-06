from address import Address
from developer import Developer
from exceptions import (DuplicateEmployeeError, EmployeeNotFoundError, InvalidMenuChoiceError, InvalidSalaryError)
from hr import HR
from manager import Manager
employees = []
def find_employee(employee_id):
    """Find and return an employee by ID."""
    for emp in employees:
        if emp.employee_id == employee_id:
            return emp
    raise EmployeeNotFoundError(f"Employee with ID {employee_id} not found.")
def validate_duplicate_id(employee_id):
    """Check for duplicate employee ID."""
    for emp in employees:
        if emp.employee_id == employee_id:
            raise DuplicateEmployeeError(f"Employee with ID {employee_id} already exists.")
def create_employee(employee_type, employee_id, name, salary, address):
    """Create and return an employee object based on type."""
    employee_classes = {
        "1": Manager,
        "2": Developer,
        "3": HR
    }
    employee_class = employee_classes.get(employee_type)
    if employee_class is None:
        raise InvalidMenuChoiceError("Invalid employee type choice.")
    return employee_class(employee_id, name, salary, address)
def add_employee():
    """Add a new employee:"""
    employee_id=int(input("Enter Employee ID: "))
    validate_duplicate_id(employee_id)
    name=input("Enter Employee Name: ").strip()
    salary=int(input("Enter Employee Salary: "))
    city=input("Enter City: ").strip()
    state=input("Enter State: ").strip()
    country=input("Enter Country: ").strip()
    address=Address(city=city, state=state, country=country)
    print ("\n Employee Types")
    print ("1. Manager")
    print ("2. Developer")
    print ("3. HR")
    employee_type=input("Select Employee Type (1-3): ").strip()
    employee=create_employee(employee_type, employee_id, name, salary, address)
    employees.append(employee)
    print("\nEmployee added successfully")
def search_employee():
    """Search for an employee by ID and display details."""
    employee_id=int(input("Enter Employee ID to search: "))
    employee=find_employee(employee_id)
    print("\nEmployee Details:")
    print(employee)
def update_employee_salary():
    """Update the salary of an existing employee."""
    employee_id=int(input("Enter Employee ID to update salary: "))
    employee=find_employee(employee_id)
    new_salary=float(input("Enter new salary: "))
    employee.salary=new_salary
    print("\nSalary updated successfully.")
def delete_employee():
    """Delete an employee by ID."""
    employee_id=int(input("Enter Employee ID to delete: "))
    employee=find_employee(employee_id)
    employees.remove(employee)
    print("\nEmployee deleted successfully.")
def display_all_employees():
    """Display details of all employees."""
    if not employees:
        print("\nNo employees found.")
        return
    print("\nAll Employees:")
    for emp in employees:
        print(emp)
def calculate_employee_bonus():
    """Calculate and display the bonus for an employee."""
    employee_id=int(input("Enter Employee ID to calculate bonus: "))
    employee=find_employee(employee_id)
    bonus=employee.calculate_bonus()
    print(f"\nEmployee: {employee.name}")
    print(f"Employee Type: {type(employee).__name__}")
    print(f"Bonus: {bonus:2f}")
def display_menu():
    """Display the main menu and handle user choices."""
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Search Employee by ID")
    print("3. Update Employee Salary")
    print("4. Delete Employee")
    print("5. Display All Employees")
    print("6. Calculate Employee Bonus")
    print("7. Exit")
def process_menu_choice(choice):
    """Process the selected menu option."""
    menu_actions={
        "1":add_employee,
        "2":search_employee,
        "3":update_employee_salary,
        "4":delete_employee,
        "5":display_all_employees,
        "6":calculate_employee_bonus
    }
    action=menu_actions.get(choice)
    if action is None:
        raise InvalidMenuChoiceError("Please select a valid Menu Option")
    action()
def main():
    """Run the employee management system"""
    while True:
        display_menu()
        choice=input("\nEnter your choice:").strip()
        if choice == "7":
            print("\nExiting Employee Management System")
            break
        try:
            process_menu_choice(choice)
        except DuplicateEmployeeError as error:
            print(f"\nError:{error}")
        except InvalidSalaryError as error:
            print(f"\nError:{error}")
        except EmployeeNotFoundError as error:
            print(f"\nError:{error}")
        except InvalidMenuChoiceError as error:
            print(f"\nError:{error}")
        except ValueError:
            print(f"\nError: Please enter a valid numeric value.")
if __name__ == "__main__":
    main()