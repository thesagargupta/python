#empty set creation

a = set()
print(type(a))

#creating a set

s={"sagar", 1, 100, 20.6}

print(s, type(s))

s.add("kishan")

print(s, type(s))

print(len(s))

#union and intersection

s={"sagar", 1, 100, 20.5}
d={"1", 40, 1, 20.5}

print(s.union(d))
print(s.intersection(d))

# disctionary of english and hindi

dict ={
    
  "fruit" : "फल", 
  "help" : "मदद",
  "vegetables" : "सब्ज़ी" 
    
}

word = input("enter the english meaning: ")
print(dict[word])


s= set()

a = input("enter the number: ")

s.add(int(a))

a = input("enter the number: ")

s.add(int(a))

a = input("enter the number: ")

s.add(int(a))

a = input("enter the number: ")

s.add(int(a))

a = input("enter the number: ")

s.add(int(a))

a = input("enter the number: ")

s.add(int(a))

a = input("enter the number: ")

s.add(int(a))

print(s, type(s))



# cheking set can have multiple value types

s= set()

a = input("enter the value: ")
s.add(a)

a= input("enter the value: ")
s.add(int(a))

print(s, type(s))

s= set()

s.add(20)
s.add(20.5)
s.add("sagar")

print(s, type(s))
print(len(s))

s=set()

s.add(20)
s.add(20.0)
s.add("20")

print(s, len(s))

d= {}

name = input(("enter your name: "))
subject = input(("enter your subject: "))
d.update({name:subject})

name = input(("enter your name: "))
subject = input(("enter your subject: "))
d.update({name:subject})

name = input(("enter your name: "))
subject = input(("enter your subject: "))
d.update({name:subject})

name = input(("enter your name: "))
subject = input(("enter your subject: "))
d.update({name:subject})

print(d,type(d))

print(d.get("subham"))

# d= {1, 2, 3, "sagar", [1,2]}// cant add list in a set

