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


s1 =   int(input("enter your marks: "))
s2 =   int(input("enter your marks: "))
s3 =   int(input("enter your marks: "))
s4 =   int(input("enter your marks: "))
s5 =   int(input("enter your marks: "))

# if(s1<33):
#     print("fail you does not score in s1")
# if(s2<33):
#     print("fail you does not score in s2")
# if(s3<33):
#     print("fail you does not score in s3")
# if(s4<33):
#     print("fail you does not score in s4")
# if(s5<33):
#     print("fail you does not score in s5")
  
    
p = 100*((s1+s2+s3+s4+s5)/500)
print(p)
if(p>=40 and s1<33 and s2<33 and s3<33 and s4<33 and s5<33):
    print("pass")
else:
    print("fail")

#spam filtering

m1 = "hello contact me"
m2 = "dm for fun"
m3 = "make money"
m4 = "you are winner and you will get a car"
m5 = "buy now"

msg = input("enter your message: ")

if((m1 in msg) or (m2 in msg) or (m3 in msg) or (m4 in msg) or (m5 in msg)):
    print("spam message")
else:
    print("not a spam")

#username len checking

un = input("enter your user name: ")

if(len(un)<10):
    print("very short user name")
else:
    print("please go ahed")


#finding name in the list

a =["sagar", "mohit", "suraj", "sandeep"]

print(a, type(a))

chk = input("enter the name: ")

if(chk in a):
    print("available")
else:
    print("not available")


#grading system

num = int(input("enter your number: "))

if(num>90 and num<=100):
    print("your grade is EX")
elif(num>80 and num<=90):
    print("your grade is A")
elif(num>70 and num<=80):
    print("your grade is B")
elif(num>60 and num<=70):
    print("your grade is C")
elif(num>50 and num<=60):
    print("your grade is D")
else:
    print(" your grade is F")

#post checker

post = input("enter your post: ")

if ("sagar".lower() in post.lower()):
    print("this talking about you")
else:
    print("not talking about you")