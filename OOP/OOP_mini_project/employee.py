from abc import ABC, abstractmethod

# ------------------------ Abstraction ------------------------

class AbstractEmployee(ABC):
    """
    Abstract base class to define the interface for Employee.
    This class uses abstraction to hide implementation details.
    """
    
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass

# ------------------------ Encapsulation ------------------------

class Employee(AbstractEmployee):
    """
    Employee class representing a general employee.
    Demonstrates encapsulation by using private attributes.
    """
    
    def __init__(self, emp_id, name, age, department, base_salary):
        self.__emp_id = emp_id        # Private attribute
        self.__name = name            # Private attribute
        self.__age = age              # Private attribute
        self.__department = department# Private attribute
        self.__base_salary = base_salary # Private attribute

    # Getter methods to access private attributes
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_department(self):
        return self.__department

    def get_base_salary(self):
        return self.__base_salary

    # Setter methods to modify private attributes with validation
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive.")

    def set_department(self, department):
        self.__department = department

    def set_base_salary(self, base_salary):
        if base_salary >= 0:
            self.__base_salary = base_salary
        else:
            raise ValueError("Base salary cannot be negative.")

    def get_details(self):
        """
        Implementation of abstract method to return employee details.
        """
        return f"ID: {self.__emp_id}, Name: {self.__name}, Age: {self.__age}, " \
               f"Department: {self.__department}, Base Salary: {self.__base_salary}"

    def calculate_salary(self):
        """
        Calculates salary. For a general employee, it's just the base salary.
        """
        return self.__base_salary

# ------------------------ Inheritance and Polymorphism ------------------------

class Manager(Employee):
    """
    Manager class inheriting from Employee.
    Demonstrates inheritance and polymorphism by overriding methods.
    """
    
    def __init__(self, emp_id, name, age, department, base_salary, bonus):
        super().__init__(emp_id, name, age, department, base_salary)
        self.__bonus = bonus  # Private attribute specific to Manager

    # Getter and Setter for bonus
    def get_bonus(self):
        return self.__bonus

    def set_bonus(self, bonus):
        if bonus >= 0:
            self.__bonus = bonus
        else:
            raise ValueError("Bonus cannot be negative.")

    def get_details(self):
        """
        Overridden method to include bonus information.
        """
        base_details = super().get_details()
        return f"{base_details}, Bonus: {self.__bonus}"

    def calculate_salary(self):
        """
        Overridden method to include bonus in salary calculation.
        """
        return super().calculate_salary() + self.__bonus

class Intern(Employee):
    """
    Intern class inheriting from Employee.
    Demonstrates polymorphism by overriding methods differently.
    """
    
    def __init__(self, emp_id, name, age, department, base_salary, stipend):
        super().__init__(emp_id, name, age, department, base_salary)
        self.__stipend = stipend  # Private attribute specific to Intern

    # Getter and Setter for stipend
    def get_stipend(self):
        return self.__stipend

    def set_stipend(self, stipend):
        if stipend >= 0:
            self.__stipend = stipend
        else:
            raise ValueError("Stipend cannot be negative.")

    def get_details(self):
        """
        Overridden method to include stipend information.
        """
        base_details = super().get_details()
        return f"{base_details}, Stipend: {self.__stipend}"

    def calculate_salary(self):
        """
        Overridden method to include stipend instead of bonus.
        """
        return super().calculate_salary() + self.__stipend
