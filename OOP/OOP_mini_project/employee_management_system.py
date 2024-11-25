from employee import Employee, Manager, Intern

class EmployeeManagementSystem:
    """
    Employee Management System to manage employees.
    Demonstrates usage of classes, objects, inheritance, polymorphism, etc.
    """
    
    def __init__(self):
        # Dictionary to store employees with emp_id as key
        self.__employees = {}

    def add_employee(self, employee):
        """
        Adds an employee to the system.
        Handles edge case of duplicate emp_id.
        """
        if employee.get_emp_id() in self.__employees:
            raise ValueError(f"Employee with ID {employee.get_emp_id()} already exists.")
        self.__employees[employee.get_emp_id()] = employee
        print(f"Employee {employee.get_name()} added successfully.")

    def remove_employee(self, emp_id):
        """
        Removes an employee from the system.
        Handles edge case of non-existent emp_id.
        """
        if emp_id in self.__employees:
            removed_employee = self.__employees.pop(emp_id)
            print(f"Employee {removed_employee.get_name()} removed successfully.")
        else:
            raise KeyError(f"No employee found with ID {emp_id}.")

    def update_employee(self, emp_id, **kwargs):
        """
        Updates employee details.
        Handles edge cases like non-existent emp_id and invalid attributes.
        """
        if emp_id not in self.__employees:
            raise KeyError(f"No employee found with ID {emp_id}.")

        employee = self.__employees[emp_id]

        for key, value in kwargs.items():
            if key == 'name':
                employee._Employee__name = value
            elif key == 'age':
                employee.set_age(value)
            elif key == 'department':
                employee.set_department(value)
            elif key == 'base_salary':
                employee.set_base_salary(value)
            elif isinstance(employee, Manager) and key == 'bonus':
                employee.set_bonus(value)
            elif isinstance(employee, Intern) and key == 'stipend':
                employee.set_stipend(value)
            else:
                raise AttributeError(f"Invalid attribute '{key}' for employee type.")

        print(f"Employee {employee.get_name()} updated successfully.")

    def get_employee_details(self, emp_id):
        """
        Retrieves details of a specific employee.
        Handles edge case of non-existent emp_id.
        """
        if emp_id in self.__employees:
            return self.__employees[emp_id].get_details()
        else:
            raise KeyError(f"No employee found with ID {emp_id}.")

    def calculate_total_salary(self):
        """
        Calculates the total salary of all employees.
        """
        total = 0
        for employee in self.__employees.values():
            total += employee.calculate_salary()
        return total

    def list_all_employees(self):
        """
        Lists details of all employees.
        """
        if not self.__employees:
            print("No employees in the system.")
        else:
            for emp_id, employee in self.__employees.items():
                print(employee.get_details())
