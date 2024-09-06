#simple marks
a = int(input("enter your marks: "))

if(a>100):
    print("enter correct marks")

elif (a>90 and a<=100):
    print("you are the topper")
    
elif(a>=50 and a<90):
    print("you are good")
    
elif(a>=30 and a<50):
    print("you are passed")
    
else:
    print("you are fail")

#finding greater
a=input(("enter your number: "))
b=input(("enter your number: "))
c=input(("enter your number: "))
d=input(("enter your number: "))

if(a>b and a>c and a>d):
    print(f"{a} is greater")
elif(b>a and b>c and b>d):
    print(f"{b} is greater")
elif(c>a and c>d and c>b):
    print(f"{c} is greater")
elif(d>a and d>c and d>b):
    print(f"{d} is greater")
