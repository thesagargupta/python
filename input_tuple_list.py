#inserting in the list

fruits = []

f1=input("enter your fruit name: ")
fruits.append(f1)
f2=input("enter your fruit name: ")
fruits.append(f2)
f3=input("enter your fruit name: ")
fruits.append(f3)
f4=input("enter your fruit name: ")
fruits.append(f4)
f5=input("enter your fruit name: ")
fruits.append(f5)
f6=input("enter your fruit name: ")
fruits.append(f6)
f7=input("enter your fruit name: ")
fruits.append(f7)


print(fruits)

#storing and sorting marks

marks= []

m1= int(input("enter the marks: "))
marks.append(m1)

m2=int(input("enter the marks: "))
marks.append(m2)

m3=int(input("enter the marks: "))
marks.append(m3)

m5=int(input("enter the marks: "))
marks.append(m5)

m5=int(input("enter the marks: "))
marks.append(m5)

m6=int(input("enter the marks: "))
marks.append(m6)

print(marks)

marks.sort()
print(marks)


#program that check a tuple cant be changed

a = ("sagar", "rohit", 2.5, 2, True) 

print(a)

# a[2]="33" #TypeError: 'tuple' object does not support item assignment

#a.append("dj") #AttributeError: 'tuple' object has no attribute 'append'

#sum of list

a=[1,2,3,4]

print(sum(a))

#counting the number

a=(1,3,3,5,3,5,3)

print(a.count(3))