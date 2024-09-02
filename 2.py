num1 = input ("enter first number: ")
num2 = input ("enter second number: ")
num3 = input ("enter third number: ")

if num1>num2 and num1>num3 :
    print("greatest number ", num1)
elif num2>num1 and num2>num3 :
    print("greatest number ", num2)
else : 
    print("greatest number ", num3)