#--------------------SIMPLE CALCULATOR--------------------#
print("--------------------SIMPLE CALCULATOR--------------------\n")
num1= float(input("enter number 1:\n"))
num2= float (input("enter number 2:\n")) 

print("choose the opreation give below\n")
print("add, subtract, multiply, divide\n")
opreation=input("Enter the opreation:\n").lower()

def calculate(num1,num2,operation):
    if operation == 'add':
        return num1+num2
    elif opreation=='subtract':
        return num1-num2
    elif operation == 'multiply':
        return num1*num2
    elif operation == 'divide':
        if num2!=0:
            return num1/num2
        else:
            return "error! Divison by zero"
    else:
        return "invalid opreation!"
    
result=calculate(num1,num2,opreation)
print(f"the result of {opreation} {num1} {num2} is {result}")