
class User:
    #Define the attributes of the class
    name = 'No Name Provided'
    email = ' '
    password = '1234abcd'
    account = 0
#"child" classes
class Employee(User):
    base_pay = 11.00
    department = 'General'

class Customer(User):
    mailing_address = ' '
    mailing_list = True
    
    

#Define the methods of the class
def login(self):
    entry_email = input("Enter your email: ")
    entry_password = input("Enter your password: ")
    if (entry_email == self.email and entry_password == self.password):
        print("Welcome back, {}!".format(self.name))
    else:
        print("You are not authorized for this page.")

def __init__(self, name, email, password, account):
    self.name = name
    self.email = email
    self.password = password
    self.account = account

