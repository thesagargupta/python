# avg function
def avg():
    a = int(input("enter your no.: "))
    b = int(input("enter your no.: "))
    c = int(input("enter your no.: "))
    print("Average: ",(a+b+c)/3)

avg()

def greet():
    a = input("enter your name: ")
    print("hello,",a)
    
greet()



def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
    
n = int(input("enter your number: "))
print(f"factorial of {n} = ",fact(n))


#to find great numbers

def grt(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c    
    
num1 = int(input("enter your number: "))
num2 = int(input("enter your number: "))
num3 = int(input("enter your number: "))

print("greatest ",grt(num1,num2,num3))

#to print F to C

def con(a):
    return (a- 32) * 5/9
    
c = int(input("enter temprature in F: "))
print("temprature: ",con(c))

#sum of n nantural numbers

def sum(n):
    if(n==1):
        return 1
    if(n==0):
        return 0
    return sum(n-1)+n

a = int(input("enter your number: "))
print("sum: ",sum(a))

#star pattern

def pattern(n):
    if(n==0):
        return
    print(" * " * n)
    pattern(n-1)
    
a= int(input("enter your number: "))

print("star pattern: ",pattern(a))


n = int(input("enter your number: "))

for i  in range(1, n+1):
    print(" * " * (n-i+1))
    


#inch to cm
    
def inch(n):
    return n * 2.54
    
    
    
n= int(input("enter your number: "))

print("your number in cm: ",inch(n))


#function for table
def mult(n):
    for i in range(1, 11):
        print(f"{n} * {i}: ",n*i)
    return "done"         
    
n =int(input("enter your number: "))
print(mult(n))


