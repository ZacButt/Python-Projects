

from abc import ABC, abstractmethod

# Abstract class
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def regular_method(self):
        print("This is a regular method.")

# Child class
class ChildClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of the abstract method in the child class.")

# Creating an object of the ChildClass
obj = ChildClass()

# Calling the abstract method
obj.abstract_method()

# Calling the regular method from the parent class
obj.regular_method()
