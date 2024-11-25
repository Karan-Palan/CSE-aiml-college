# **A Minor Project Report**  
On  

**Employee Management System Using Python**

---

## **Bachelor of Technology**  
In  
**Computer Science and Engineering (AIML)**  

**2023-2027**  

By  
**Name – Karan Palan**  
**Registration Number – 23FE10CAI00523**  

Under the supervision of  
**Sanjay Kumar Tehariya**  

**School of Computer Science and Engineering**  
**Department of Artificial Intelligence and Machine Learning**  
**Manipal University Jaipur, Jaipur, Rajasthan, India**  

**SEP-OCT 2024**

---

## **Introduction**

The **Employee Management System (EMS)** is a crucial application in modern business environments. Its primary purpose is to streamline administrative processes by maintaining employee records, calculating salaries, and managing hierarchical structures within organizations. The EMS was developed as part of a minor project for the Bachelor of Technology program in Computer Science and Engineering (AIML) at Manipal University Jaipur.  

This project applies **Object-Oriented Programming (OOP)** principles to design a system that efficiently manages employee data. The EMS utilizes Python’s OOP features, demonstrating concepts such as **Abstraction**, **Encapsulation**, **Inheritance**, and **Polymorphism**.  

The EMS allows users to:  
- Add, update, remove, and view employee details.  
- Support multiple employee types, including General Employees, Managers, and Interns, with distinct attributes like bonuses and stipends.  
- Ensure data security using encapsulation and validations.  

This report outlines the system's logic, functionality, technical details, and Python code, accompanied by its corresponding output.  

---

## **How the Project Works**

### **Objective**

- Manage and store employee records securely.
- Implement salary calculations, considering specific attributes (e.g., bonuses for Managers and stipends for Interns).
- Demonstrate key OOP concepts in Python through an interactive system.

### **Core Workflow**

1. **Class Design**
   - Abstract and concrete classes are used to define and implement employee attributes and behaviors.
   - Specialized employee types (e.g., Manager, Intern) inherit from the base `Employee` class.

2. **Encapsulation**
   - Attributes like employee ID, name, age, and salary are private, with controlled access through getters and setters.

3. **Inheritance and Polymorphism**
   - Subclasses like `Manager` and `Intern` override methods such as `get_details` and `calculate_salary`.

4. **Employee Operations**
   - Add: Validates and adds an employee, ensuring no duplicate IDs.
   - Update: Modifies employee details while maintaining data integrity.
   - Remove: Deletes an employee, handling cases of non-existent IDs.

5. **Error Handling**
   - Ensures robustness by handling edge cases, such as invalid inputs, duplicate records, and operations on non-existent data.

---

## **Code Overview**

### **Code Structure**

1. **`employee.py`**  
   - Contains the abstract `AbstractEmployee` class and concrete `Employee` class.
   - Defines the `Manager` and `Intern` subclasses.

2. **`employee_management_system.py`**  
   - Manages employee records and provides functionalities like adding, updating, and removing employees.

3. **`main.py`**  
   - Demonstrates the EMS functionalities and showcases edge-case handling.

### **Key Features**

- **Encapsulation**:  
  Private attributes prevent unauthorized access, ensuring data security. For example:
  ```python
  def set_base_salary(self, base_salary):
      if base_salary >= 0:
          self.__base_salary = base_salary
      else:
          raise ValueError("Base salary cannot be negative.")
  ```

- **Polymorphism**:  
  Subclasses override methods to provide specific implementations. For instance:
  ```python
  def calculate_salary(self):
      return super().calculate_salary() + self.__bonus  # For Manager
  ```

- **Edge Case Handling**:  
  Handles cases like duplicate employee IDs and invalid updates.

---

## **Output**

### **During Execution:**
1. The system displays:
   - A list of all employees with their details.
   - Real-time updates after adding, updating, or removing employees.
   - Calculated total salaries for all employees.

2. Demonstrates edge-case handling, such as:
   - Adding an employee with a duplicate ID:
     ```
     ValueError: Employee with ID 1 already exists.
     ```
   - Attempting to update a non-existent employee:
     ```
     KeyError: No employee found with ID 999.
     ```

### **Sample Output:**
Adding employees:
```
Employee Alice added successfully.
Manager Bob added successfully.
Intern Charlie added successfully.
```

Calculating total salaries:
```
Total Salary of all employees: 150000
```

Removing an employee:
```
Employee Charlie removed successfully.
```

---

## **Conclusion**

The Employee Management System demonstrates a robust application of Object-Oriented Programming principles, showcasing the following:  

1. **Abstraction**: Abstract base classes define common behaviors while hiding implementation details.  
2. **Encapsulation**: Sensitive data is protected through private attributes and controlled access.  
3. **Inheritance**: Specialized classes extend and reuse common functionality from the base `Employee` class.  
4. **Polymorphism**: Method overriding allows for dynamic and flexible functionality.

The EMS is a valuable tool for automating employee management tasks, providing a scalable foundation for further enhancements. Future improvements could include integrating a database, developing a graphical user interface, or implementing advanced analytics for employee performance tracking.  

---
