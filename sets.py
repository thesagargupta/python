# #empty set creation

# a = set()
# print(type(a))

# #creating a set

# s={"sagar", 1, 100, 20.6}

# print(s, type(s))

# s.add("kishan")

# print(s, type(s))

# print(len(s))

# #union and intersection

# s={"sagar", 1, 100, 20.5}
# d={"1", 40, 1, 20.5}

# print(s.union(d))
# print(s.intersection(d))

#disctionary of english and hindi

dict ={
    
  "fruit" : "फल", 
  "help" : "मदद",
  "vegetables" : "सब्ज़ी" 
    
}

word = input("enter the english meaning: ")
print(dict[word])