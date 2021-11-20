def add(num1, num2):
    print("%d + %d = %d"%(num1, num2, num1+num2))

def sub(num1, num2):
    print("%d - %d = %d"%(num1, num2,num1 - num2))

def mul(num1, num2):
    print("%d x %d = %d"%(num1, num2,num1 * num2))

def div(num1, num2):
    print("%d / %d = %d"%(num1, num2,num1 / num2))

def mod(num1, num2):
    print("%d mod %d = %d"%(num1, num2,num1 % num2))




num1 = int(input("Enter first number : "))
num2  = int(input("Enter second number : "))
op = input("Enter the operation : ")

if(op == '+'):
    add(num1, num2)
elif(op == '-'):
    sub(num1, num2)
elif(op == '*'):
    mul(num1, num2)
elif(op == '/'):
    div(num1, num2)
elif(op == '%'):
    mod(num1, num2)
else:
    print("Not a valid operator")