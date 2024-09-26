class Employee:
    def details (self, name):
        self.name = name
        print(f"the name of the emoployee is {self.name}")
        
class Worker(Employee):
    def showDetails (self, language):
        self.language = language
        print(f"the language of the emoployee is {self.language}")
        
a = Employee()
a.details("sagar")

a= Worker()
a.showDetails("C++")

## multiple inheritance ###

class Employee:
    def details(self,name):
        self.name=name
        print(f"the name of the employee is {self.name}")
        
class Programmer:
    def coding(self,language):
        self.language = language
        
        print(f"the language of the programmerger is {self.language}")
        
class Details(Employee,Programmer):
    def __init__(self):
        print("inherited successfully")
        
### multilevel inheritance ###
        
class Employee:
    a = 2
    
class Programmer(Employee):
    b= 3
    
class Details(Programmer):
    c=4
    
a = Details()

print(a.a, a.b, a.c)

#usimg super 

class Employee:
    def __init__(self):
        print("run successfully")
        
class Programmer(Employee):
    def __init__(self):
        print("Programmer run successfully")
        
class Details(Programmer):
    
    def __init__(self):
        super().__init__()##only parent constructor will run
        print(" Details run successfully")
        

c = Details()

##class method concept

class Employee():
    a = 1
    
    @classmethod
    def show(cls):
        print(f"number = {cls.a}")
        
e = Employee()
e.a=45
e.show()

######### operator overloading #################


#double values
class Operations:
    def __init__(self,m,n):
        self.m = m
        self.n = n
    
    def __add__(self, num):
        self.num = num
        return self.m + num.n


a = Operations(10,5)
b = Operations(10,9)

c = a+b
print(c)

#####using single values############

class Operations:
    def __init__(self,n):
        self.n = n
    def __add__(self,num):
        return self.n+ num.n
    
a = Operations(5)
b= Operations(10)

print(a+b)

#creating a 2d vector class and creating a 3d vector class

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The two-dimensional vector is {self.i}i + {self.j}j")
        
class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
        
    def show(self):
        print(f"The three-dimensional vector is {self.i}i + {self.j}j + {self.k}k")
b= TwoDVector(1,3)
b.show()        
a = ThreeDVector(2,3,5)
a.show()

#inheriting and passing parent  class

class Animal:
    pass
    
    
class Pet(Animal):
    pass
    
class Dog(Pet):
    @staticmethod
    def bark():
        print("bark")
        
        
d = Dog
d.bark()

#salary increamnetal

class Employee():
    def __init__(self, salary, increament):
        self.salary = salary
        self.increament = increament
    
    @property
    def salaryAfterIncreament(self):
        return (self.salary +self.salary * (self.increament/100))
    
    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self, salary):
        self.increament = ((salary/self.salary)-1)*100
    
       
a = int(input("Salary: "))
b = float(input("increament: "))

e = Employee(a, b)

print(e.salaryAfterIncreament)
print(e.increament)



## printing single number
class Complex:
    def __init__(self,m,n):
        self.m = m
        self.n = n
    
    def __add__(self, num):
        self.num = num
        return print( f"{self.m + self.n}i")
    
    
a = Complex(1,5)

print(a+0)
      

##printing complex number

class Complex:
    def __init__(self,m,n):
        self.m = m
        self.n = n
    
    def __add__(self, num):
        self.num = num
        return f"your sum of complex numbers {self.m + num.m} + {self.n + num.n}i"

a = Complex(1,5)
b= Complex(2,5)

c = a+b
print(c)