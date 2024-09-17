#reading content from a file
a = open("hello.txt")
data=a.read()
print(data)
a.close()


str = "hello how are you"
a = open("file.txt", "w")
a.write(str)
print(a)
a.close()

# printing lines of a file
f= open("file.txt")
lines = f.readlines()
print(lines, type(lines))
f.close()



##printing line of a file
f = open("file.txt")
line = f.readline()

while(line != ""):
    line = f.readline()
    print(line,type(line))

f.close()

#writing into a file
str = "\nhey !!!"

a  = open("file.txt", "a")

a.write(str)

print(a)
a.close()
 
#reading the file
with open("file.txt") as a:
    a.read()
    print(a)

#closing file manually and finding text

a = open("poem.txt")
c=a.read()
if("twinkle" in c):
    print("twinkle is present")
else:
    print("twinkle is not present")

a.close()

#finding text in file and closing automatically   
with open("poem.txt") as a:
    c=a.read()
    if("twinkle" in c):
        print("twinkle is present")
    else:
        print("twinkle is not present")


###letters replace from file

str= "donkey"

with open("letter.txt") as l:
    data=l.read()
    if("donkey" in data):
                            
        data = data.replace(str,"####")
        with open("letter.txt", "w") as l:
            l.write(data)
    else:
        print("missing")

####letters replace from file
str= ["donkey", "bad", "dirty"]

with open("letter.txt") as l:
    data=l.read()
    if("donkey" in data):
        for word in str:                    
            data = data.replace(word,"####")
            with open("letter.txt", "w") as l:
                l.write(data)
    else:
        print("missing")

##table generator
def tablegenrator(n):
    table = ""
    for i in range(1,11):
        table = table + f"{n}*{i}= {n*i}\n"
            
    with open(f"tables/table{n}.txt", "w") as l:        
        l.write(str(table))  
        
for i in range(2, 21):
    tablegenrator(i)


#finding the data and line number
with open("log.txt") as l:
    data = l.readlines()
    
lineno = 1 
 
for i in data:
    if("python" in i):
        print(f"Python is present in {lineno}")
        break
    lineno += 1
else:
    print("python is not present") 

# creating new file and copying data from existing file

with open("log.txt") as l:
    data = l.read()

with open("copy.txt", "w") as f:
    f.write(data)
   
##checking file idecntial is or not
    
with open("copy.txt") as c:
    data=c.read()
    
with open("log.txt") as f:
    data2=f.read()
    
if(data==data2):
    print("identical")
else:
    print("different")