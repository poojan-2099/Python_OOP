# OOP is paradigm that uses "objects" to model real-world entinties.
# a. Classes and Objects
#   Class: A blueprint for creating objects. It defines attribtus and functions
#   Object: An instance of a class

class Employee:
    def __init__(self, name, employee_id):
        self.name =name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Name: {self.name}, ID:{self.employee_id}")
#creating objects
emp1 = Employee("Arun", 101)
emp2 = Employee("Bala", 102)

emp1.display_info()
emp2.display_info()
