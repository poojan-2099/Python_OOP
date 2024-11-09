# OOP is paradigm that uses "objects" to model real-world entinties.
# a. Classes and Objects
#   Class: A blueprint for creating objects. It defines attribtus and functions
#   Object: An instance of a class

# class Employee:
#     def __init__(self, name, employee_id):
#         self.name =name
#         self.employee_id = employee_id

#     def display_info(self):
#         print(f"Name: {self.name}, ID:{self.employee_id}")
# #creating objects
# emp1 = Employee("Arun", 101)
# emp2 = Employee("Bala", 102)

# emp1.display_info()
# emp2.display_info()

# b. Encapsulation: is the bundling of data and methods that operate on that data within a single unit(class). It involves restricting access tp certain components.
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number   # Public attribute
#         self.__balance = balance               # Private attribute
    
#     def deposit(self, amount):
#         self.__balance += amount
    
#     def __apply_fee(self):                    # Private Method
#         self.__balance -= 5
    
#     def get_balance(self):
#         self.__apply_fee()
#         return self.__balance
# account = BankAccount("123456789", 1000)
# account.deposit(500)
# print("Balance:", account.get_balance())

# c. Inheritance :Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class), promoting code reusability.
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
    
#     def start_engine(self):
#         print(f"My {self.make} {self.model} Engine started")

# class Car(Vehicle):                         # inherting from vehice
#     def __init__(self, make, model, doors):
#         super().__init__(make, model)
#         self.doors = doors
    
#     def open_trunk(self):
#         print("Trunk Opened")

# my_car = Car("Toyota", "Corolla", 4)
# my_car.start_engine()      # Inherited method
# my_car.open_trunk()        # Method from Car class

# d.Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables methods to be used in different ways.
# class Shape:
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         from math import pi
#         return pi * self.radius ** 2

# # Usage
# shapes = [Rectangle(3, 4), Circle(5)]

# for shape in shapes:
#     print("Area:", shape.area())

# e. Abstraction: It involves creating simple interface for complex systems, exposing only essential features

# from abc import ABC, abstractmethod

# class DataProcessor(ABC):
#     @abstractmethod
#     def process(self, data):
#         pass

# class CSVDataPRocessor(DataProcessor):
#     def process(self, data):
#         print("Processing CSV data")

# class JSONDataProcessor(DataProcessor):
#     def process(self, data):
#         print("Processing JSON Data")

# processors = [CSVDataPRocessor(), JSONDataProcessor()]

# for processor in processors:
#     processor.process(None)

# 2> Advanced OOP concepts

# a.magic mehtod(dunder method) allow customization of behavior for built-in operations.
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):              # Overloading the '+' operator
#         return Vector(self.x + other.x, self.y + other.y)

#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"

# # Usage
# v1 = Vector(2, 3)
# v2 = Vector(4, 5)
# v3 = v1 + v2
# print(v3)


# b. Class and Static Methods
# Class Methods: Methods that have access to the class object (cls) rather than the instance.
# Static Methods: Methods that do not access instance or class data.
# class Employee:
#     num_employee = 0 

#     def __init__(self, name):
#         self.name = name
#         Employee.num_employee += 1

#     @classmethod
#     def get_num_employee(cls):
#         return cls.num_employee
    
#     @staticmethod
#     def is_valid_employee_id(empoyee_id):
#         return isinstance(empoyee_id, int) and empoyee_id>0

# emp1 = Employee("Arun")
# emp2 = Employee("Bala")


# print("Total Employees:", Employee.get_num_employees())
# print("Is valid ID:", Employee.is_valid_employee_id(101))

# c. Decorators can modify or enhance method in classes
# def authorize(func):
#     def wrapper(*args, **kwargs):
#         # Authorization logic (simplified)
#         user_authorized = True
#         if user_authorized:
#             return func(*args, **kwargs)
#         else:
#             print("Access denied")
#     return wrapper

# class DataService:
#     @authorize
#     def get_data(self):
#         print("Data fetched successfully")

# # Usage
# service = DataService()
# service.get_data()


# => Real lif AI project exapmple practicefrom abc import ABC, abstractmethod
from abc import ABC, abstractmethod
class DataLoader(ABC):
    @abstractmethod
    def load_data(self):
        pass

class Preprocessor(ABC):
    @abstractmethod
    def preprocess(self, data):
        pass

class Model(ABC):
    @abstractmethod
    def train(self, data):
        pass

class CSVLoader(DataLoader):
    def load_data(self):
        print("Loading data from CSV")
        # Load CSV data
        return "raw_data"

class DataPreprocessor(Preprocessor):
    def preprocess(self, data):
        print("Preprocessing data")
        # Data cleaning and transformation
        return "processed_data"

class NeuralNetworkModel(Model):
    def train(self, data):
        print("Training neural network model")
        # Training logic
        return "trained_model"

# Coordinating the pipeline
class AIPipeline:
    def __init__(self, loader, preprocessor, model):
        self.loader = loader
        self.preprocessor = preprocessor
        self.model = model

    def run(self):
        data = self.loader.load_data()
        data = self.preprocessor.preprocess(data)
        model = self.model.train(data)
        print("Pipeline completed")
        return model

# Usage
pipeline = AIPipeline(CSVLoader(), DataPreprocessor(), NeuralNetworkModel())
trained_model = pipeline.run()


# . Best Practices and Advanced Topics
# a. Design Patterns
# Familiarity with design patterns enhances code quality.

# Singleton Pattern: Ensures a class has only one instance.
# Factory Pattern: Creates objects without specifying the exact class.
# Observer Pattern: Implements a subscription mechanism.
# Example of Singleton Pattern:


class SingletonMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}

# Usage
config1 = Configuration()
config2 = Configuration()
print(config1 is config2)  # True

# The SingletonMeta metaclass ensures only one instance of Configuration exists.


# b. SOLID Principles
# Adhering to SOLID principles leads to robust software design.

# S: Single Responsibility Principle
# O: Open/Closed Principle
# L: Liskov Substitution Principle
# I: Interface Segregation Principle
# D: Dependency Inversion Principle
# Applying Open/Closed Principle:


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount):
        print(f"Paying {amount} using credit card")

class PayPalProcessor(PaymentProcessor):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal")

# Adding a new payment method without modifying existing code
class BitcoinProcessor(PaymentProcessor):
    def pay(self, amount):
        print(f"Paying {amount} using Bitcoin")

# The system is open to extension (adding new payment methods) but closed to modification of existing classes.
