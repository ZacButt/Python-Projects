
class EncapsulationClass:
    def __init__(self):
        self._protected_attribute = "This is a protected attribute"
        self.__private_attribute = "This is a private attribute"

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

    def access_encapsulated_data(self):
        # Accessing the protected attribute
        print("Accessing protected attribute:", self._protected_attribute)
        
        # Calling the protected method
        self._protected_method()

        # Accessing the private attribute
        print("Accessing private attribute:", self.__private_attribute)
        
        # Calling the private method
        self.__private_method()

# Creating an object of the EncapsulationClass
obj = EncapsulationClass()

# Accessing encapsulated data
obj.access_encapsulated_data()

# Trying to access private attribute and method directly (outside the class)
print("Trying to access private attribute directly:", obj.__private_attribute)
print("Trying to call private method directly:")
obj.__private_method()
