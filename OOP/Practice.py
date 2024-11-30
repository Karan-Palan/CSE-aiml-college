age = 20
price = 20.14
first_name = 'Karan'
name = input("What's your name")
print(age)
# input is taken in string
birth_year = int(input("Enter your birth year"))
# .find , .upper - does not change the original string
# if you use /, you get float and if you use // you get int
# and- if both true, or - if one true

# Basic Atm system with OOP

class Atm:
    def __init__(self):
        self.__pin = ""
        self.balance = 0

        self.menu()

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if type(new_pin) ==str:
            self.__pin = new_pin
            print("Pin changed")
        else:
            print("Please enter a string")

    def menu(self):
        user_input = input("""
            Hello, how would you like to proceed?
            1. Enter 1 to create __pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to exit        
        """)

        if user_input == "1":
            self.create___pin
        if user_input == "2":
            self.deposit
        if user_input == "3":
            self.withdraw
        if user_input == "4":
            self.check_balance
        if user_input == "5":
            print("Exit Sucessfull")

    def create___pin(self):
        self.__pin = input("Enter your __pin")
        print("__pin set sucessfully")

    def deposit(self):
        temp = input("Enter your __pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
            print("Deposit sucessful")
        else:
            print("Invalid __pin")

    def withdraw(self):
        temp = input("Enter your __pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance - amount
            print("Withdrawal sucessful")
        else:
            print("Invalid __pin")

    def check_balance(self):
        temp = input("Enter your __pin")
        if temp == self.__pin:
            print(self.balance)
        else:
            ("Wrong __pin")

# Creating your own data type
class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self,other):
        temp_num = self.num *other.den + other.num * self.den
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num, temp_den)
    

# Aggregation

class Customer:
    def __init__(self,name,gender,address):
        self.name= name
        self.gender = gender
        self.address = address
        
        
    
class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state
        
add = Address("Mumbai", 400080, "MH")
cust = Customer("Karan", "Male", add)

# Inheritance

class User:
    def login(self):
        pass
    
class Student(User):
    def enroll(self):
        pass
    
    
Karan = Student()

Karan.login

# Polymorphism

class Geometry:
    # This code will not work in python. Method overloading
    def area (self,radius):
        return 3.14*radius*radius
    def area (self,l,b):
        return l*b
    
    # This can be done
    def area (self, a, b=0):
        if b == 0:
            print("Circle: ", 3.14*a*a)
        else:
            print("Rectangle: ", a*b)
    
obj = Geometry()
obj.area(4)
