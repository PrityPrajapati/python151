# 81. Class Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

# 82. Class Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

    def circumference(self):
        return 2 * 3.14159 * self.radius

circle = Circle(4)
print("Area:", circle.area())
print("Circumference:", circle.circumference())

# 83. Class BankAccount
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")

    def check_balance(self):
        print(f"Balance: {self.balance}")

account = BankAccount()
account.deposit(100)
account.withdraw(50)
account.check_balance()

# 84. Class Student
class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Alice", 101, [85, 90, 78])
print("Average Grade:", student.average_grade())

# 85. Class Car and Inheritance
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def battery_info(self):
        return f"Battery size: {self.battery_size} kWh"

ecar = ElectricCar("Tesla", "Model S", 2022, 100)
print(ecar.description())
print(ecar.battery_info())

# 86. Class ComplexNumber
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)

# 87. Class Point
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

p1 = Point(0, 0)
p2 = Point(3, 4)
print("Distance:", p1.distance(p2))

# 88. Classmethod and Staticmethod
class Example:
    def instance_method(self):
        return "Instance method called", self

    @classmethod
    def class_method(cls):
        return "Class method called", cls

    @staticmethod
    def static_method():
        return "Static method called"

obj = Example()
print(obj.instance_method())
print(Example.class_method())
print(Example.static_method())

# 89. Property Decorators
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value
        else:
            raise ValueError("Name cannot be empty")

person = Person("John")
print(person.name)
person.name = "Alice"
print(person.name)

# 90. Class Employee with Inheritance
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        return f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display(self):
        return f"{super().display()}, Department: {self.department}"

mgr = Manager("Alice", 101, 90000, "HR")
print(mgr.display())
