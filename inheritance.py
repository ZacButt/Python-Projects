
class User:
    name = 'No Name Provided'
    email = ' '
    password = 'abcdefg'
    account_number = 1

class Employee(User):
    base_pay = 11.00
    department = 'Cook'

class Customer(User):
    mailing_address = ' '
    mailing_list = True


#I Created my class "User"
#I inherited the traits of "User for my 2 other classes by putting it in parenthesis after the class
