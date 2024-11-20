# Class is represnted in PascalCase. Object is an instance of a class
# Methods are functions inside classes
# Contructor is a special method whose code inside automatically gets excecuted when the object of that class is read for ex. __init__
# Advantage of OOP - Object is an instance of the class. Hence the variables and all other stuff can be stored uniquely
# Objects contain 2 things - Objects and data
# Nothing is truly private in python. 
# Private attribute __ and use getters and setters
# Ref var - variable in which object is stored
# Classes of objects are also mutable
# Static variable - value same for all objects. Hence static vaiables are initialized outside contructor, they are acessed using class name and not self
# To acess static methods, you do not need to pass the object
# Aggregation - has-a relationship between classes

class Atm:
    def __init__(self):
        
        self.__pin = ""
        self.__balance = 0

        self.menu()

    def menu(self):
        user_input = input("""
                            Hello, how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input== "2":
            self.deposit()
        elif user_input== "4":
            self.withdraw()
        elif user_input== "3":
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.__pin = input("Enter your pin")
        print("Pin set succesfully")

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.__balance = self.balance + amount
            print("Deposit sucessful")
        else:
            print("Invalid Pin")

    
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Operation Sucessful")
            else:
                print("Insufficient funds")
        else:
            print("invalid Pin")
        
    def check_balance(self):
        temp = input("Enter the pin")
        if temp == self.__pin:
            print(self.balance)
        else:
            print("invalid pin")
                
class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    
    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(self.num, self.den)
    
    def __sub__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(self.num, self.den)