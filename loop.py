#printing counting using for loop

for i in range (1, 10):
    print(i)

#printing counting using while loop

i=1

while(i<100):
    print(i)
    i=i+1

#printing letter multiple time
i=0
   
while(i<30):
    print("RAM")
    i=i+1


a = ["sagar", 1, 2.5,"gupta"]

i=0

#slicing using loop

while(i<=3):
    print(a[i])
    i=i+1

#traversing
while(i<len(a)):
    print(a[i])
    i=i+1

for i in range(len(a)):
    print(a[i])

#jumping after 5

for i in range(0, 100, 5):
    print(i)


#printing item of tuple
t = ("sagar", "gupta", 1, 2, 2.5)

for i in range(len(t)):
    print(t[i], type(t))

#pring each letter

a= "sagar"
for i in a:
    print(i)

#using else after printing item

l = ["sagar", "gupta", 1,2]

for i in range(len(l)):
    print(l[i])
else:
    print("done")


#break function

for i in range(0, 100):
    if(i==34):
        break
    print(i)

#continue function
    
for i in range(0, 100):
    if(i==50):
        continue
    print(i)

#traversing list and greeting item

n= int(input("enter your number: "))
for i in range(1, 11):
    print(f"{n}*{i} = ", n*i)

l = ["sagar", "suraj", "sunil", "bhanu","bahubali", "appe"]

for i in l:
    if (i.startswith("s")):
        print(f"{i} hello")


#printing table using while loop

n = int(input("enter your number: "))

i=1

while(i<11):
    print(f"{n} * {i} = ",n*i)
    i=i+1



#checking prime or not

n = int(input("enter your number: "))
flag = 1
for i in range(2, n):
    if(n%i==0):
        flag=0
   
if(flag==0):
    print("not a prime")
else:
    print("a prime")


#sum of n natural numbers

n = int(input("enter your number: "))

i = 1
sum =0
while (i<=n):
    sum=sum+i
    i=i+1

print(sum)


#factorial program

n = int(input("enter your number: "))
f=1
for i in range(1, n+1):
    f=f*i
    
print(f)

##star pattern

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    # Print spaces for left padding
    print(" " * (n - i), end="")
    
    # Print stars in odd numbers
    print("*" * (2 * i - 1))


'''
    *
   ***
  *****
 *******
**********

'''

################################################3

n = int(input("Enter the number: "))

for i in range (1, n+1):
    for j in range (1, i+1):
        print(" * ", end="")
    print("") 
    
'''

* 
* * 
* * * 
* * * * 
* * * * * 

'''   


#########################################################3

n = int(input("Enter the number: "))

for i in range(1, n+1):
    if(i==n or i==1):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n-2),end="")
        print("*", end="")
    print("")
    
    
"""
*****
*   *
*   *
*   *
*****"""


# opposite multiplication table

n= int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n}*{11-i} = ", (11-i)*n)
    
    
