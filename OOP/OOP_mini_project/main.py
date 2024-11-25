from employee import Employee, Manager, Intern
from employee_management_system import EmployeeManagementSystem

def main():
    # Create an instance of EmployeeManagementSystem
    ems = EmployeeManagementSystem()

    try:
        emp1 = Employee(emp_id=1, name="Karan", age=18, department="HR", base_salary=50000)
        ems.add_employee(emp1)

        mgr1 = Manager(emp_id=2, name="Raghav", age=40, department="IT", base_salary=80000, bonus=10000)
        ems.add_employee(mgr1)

        intern1 = Intern(emp_id=3, name="Kavyaa", age=22, department="Marketing", base_salary=30000, stipend=5000)
        ems.add_employee(intern1)

        print("\nList of all employees:")
        ems.list_all_employees()

        ems.update_employee(1, department="Finance", base_salary=55000)

        total_salary = ems.calculate_total_salary()
        print(f"\nTotal Salary of all employees: {total_salary}")

        ems.remove_employee(3)

        print("\nList of all employees after removal:")
        ems.list_all_employees()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
