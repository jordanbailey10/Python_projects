#Parent Class User
class EmployeeLogin:
    name = "Jordan"
    email = "JordanBailey10@gmail.com"
    password = "cheddar"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcom back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")
#Child Class Employee
class Employee(EmployeeLogin):
    base_pay = 20.00
    department = "Packaging"
    pin_number = "1228"

# This is the same method in the parent class "User"
#The difference is that instead of using entry password, we're using entry_pin.
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")
#The following code invodes the methods inside each class for User and Employee

customer = EmployeeLogin()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
