
class ParentClass:
    def parent_method(self):
        print("This is my parent classes method.")

class ChildClass1(ParentClass):
    def __init__(self, attribute1, attribute2):
        self.attribute1 = 1
        self.attribute2 = 2

    def parent_method(self):
        # Polymorphism: Overriding the parent method
        print("This is the child class 1 implementation of the parent method.")

    def child_method(self):
        print("This is a method specific to child class 1.")
        print("Attribute 1:", self.attribute1)
        print("Attribute 2:", self.attribute2)

class ChildClass2(ParentClass):
    def __init__(self, attribute3, attribute4):
        self.attribute3 = 3
        self.attribute4 = 4

    def parent_method(self):
        # Polymorphism: Overriding the parent method
        print("This is the child class 2 implementation of the parent method.")

    def child_method(self):
        print("This is a method specific to child class 2.")
        print("Attribute 3:", self.attribute3)
        print("Attribute 4:", self.attribute4)

# Creating objects of child classes
child1 = ChildClass1("Value 1", "Value 2")
child2 = ChildClass2("Value 3", "Value 4")

# Calling the polymorphic method on the objects
child1.parent_method()
child2.parent_method()

# Calling child-specific methods
child1.child_method()
child2.child_method()
