name = input("Enter your name: ")
print ("good afternoon",name)
print (f"good afternoon, {name}")

nam = "sagar"
date = "03/09/024"

print(f"""
      Dear {name},
      you are selected
      {date}
      """)


letter = """Dear |name|
            you are selected
            |date|        """
            
print(letter.replace("|name|", "sagar").replace("|date|", "4/09/2024"))

#double spaces

name = "sagar is   good  boy"
print(name.find("  "))
name = "sagar is   good  boy"
print(name.find("g"))

#triming spaces
name = "sagar is  good  boy"
print(name.replace("  "," "))

#string are immutable

letter = "heelo,\n everyone!,\n my name is \" sagar\" "
print(letter)