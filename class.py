# creating a class and printing data
class employee:
    language = "py"
    salary = 120000
        
sagar = employee()
sagar.name= "Sagar"
print(sagar.name, sagar.language, sagar.salary)



## function creating in a class and printing data

class Employee:
    language = "python"
    salary = 120000
    def getInfo(self):
        print(f"the language of the employee {self.language}\n the salary of the employee {self.salary}")
    @staticmethod
    def hello():
        print("hello world")
    
sagar = Employee()

sagar.language = "C++"
sagar.salary = 15000000

print(sagar.language, sagar.salary)

sagar.getInfo()
sagar.hello()


## dender method , it runs automatically

class Employee:
    salary = 150000
    language = "pyhton"
    
    def __init__(self):
        print(f"salary of employee {self.salary}\n the language of employee {self.language}")
        
        
sagar = Employee()


#constructer

class Employee:
    salary=1200000
    name= "sagar"
    language = "python"
    
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary 
        self.language= language
        print(f"the name of the employee {self.name}\nthe language of employee {self.language}\n the salary of employee {self.salary}")
        
        
ed = Employee("sagar gupta", 1200000, "python")
print(ed.name, ed.salary, ed.language)

# using constructor
class Employee:
    company = "microsoft"
    
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        
sagar = Employee("sagar gupta", 1200000, "python")
print(sagar.name, sagar.salary, sagar.language,sagar.company)


#creating class for mathematical operations

class Calculator:
    def __init__(self,n):
        self.n=n
        
    def square(self):
        print(f"square of number : {self.n * self.n} ") 
    
    def cube(self):
        print(f"cube of number : {self.n * self.n * self.n} ")
        
    def root(self):
        print(f"root of number : {self.n ** 1/2}")
        
        
n = Calculator(4)
n.square()
n.cube()
n.root()       


###creating class for train bookings

import random
class Train:
    
    def __init__(self,trainNo):
        self.trainNo=trainNo
        self.fro="RXL"
        self.to="ANVT"
        
    def book(self):
        print(f"ticket is boocked from {self.fro} to {self.to} with Train Number: {self.trainNo}")
    
    def getStatus(self):
        print(f"Train number with {self.trainNo} running successfully, from {self.fro} to {self.to}.")
    
    def getFares(self):
        print(f"ticket price from with train number {self.trainNo}. {self.fro} to {self.to} is {random.randint(1200, 2000)}")
        
        
t = Train(15274)
t.getStatus()
t.getFares()
t.book()
