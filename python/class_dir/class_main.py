from class_example import Employee, Developer, Manager

####
# Create
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
# print(Employee.num_of_emps)
####

####
# # Create from string with classmethod
# emp_str_1 = "John-Doe-70000"
# new_emp_1 = Employee.from_string(emp_str_1)
####

####
# # Create for SubClass
# dev_1 = Developer('Corey','Schafer', 50000, 'Python')
# dev_2 = Developer('Marina','Chefer', 30000, 'Python')
# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
####

####
# # Show Using method
# print(emp_1.fullname) # Employee.fullname(emp_1)
# print(dev_1.pay)
# print(dev_1.prog_lang)
# mgr_1.print_emps()
####

####
# # Change (Create Instance Variable) and show dict variable
# emp_1.raise_amount = 1.05 # If need change Class Variable use: Employee.raise_amount = 1.05
# print(Employee.__dict__)
# print(emp_1.__dict__)
# print(emp_2.__dict__)
####

####
# Change amount by classmethod
# Employee.set_raise_amt(1.10)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
####

####
# # Working with StaticMethod
# import datetime
# my_date = datetime.date(2020, 4, 26)
# print(Employee.is_workday(my_date))
####

####
# # Magic/Dunder Methods
# # __init__, __repr__, __str__ will use more often
# print(emp_1)
# print(emp_1 + emp_2)
# print(len(emp_1))
####

####
# # Using decorator
# ## Using Property decorator
# print(emp_1.email) 
# print(emp_1.fullname)
# ## Using setter
# emp_1.fullname = "Marina Chefer"
# print(emp_1.fullname)
# del emp_1.fullname
####