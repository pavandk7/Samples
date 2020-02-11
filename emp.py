class Employee():
    name = 'pavan'
    age = 24
    raise_amount = 2.06

    def fun(self,designation):
        self.designation = designation
    
    def __init__(self,salary):
        self.name = Employee.name
        self.age = Employee.age
        self.salary = salary

    def get_hike(self):
        self.salary = int(self.salary * self.raise_amount) # we can provide Employee.raise_amount as well #

    
#************************************************************
       
employee = Employee(25000)  #instance of the class

employee.fun('team-lead')

##print(Employee.name)
print(employee.name)
print(employee.age)
print(employee.designation)
print(employee.salary)
employee.get_hike()
print(employee.salary)


print(employee.__dict__)
