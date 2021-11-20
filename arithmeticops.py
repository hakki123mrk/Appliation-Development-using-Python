num1 = int(input("Enter first number : "))
num2  = int(input("Enter second number : "))

op = input("Enter the operation : ")

if(op == '+'):
    print("%d + %d = %d"%(num1, num2,num1 + num2))
elif(op == '-'):
    print("%d - %d = %d"%(num1, num2,num1 - num2))
elif(op == '*'):
    print("%d x %d = %d"%(num1, num2,num1 * num2))
elif(op == '/'):
    print("%d / %d = %d"%(num1, num2,num1 / num2))
elif(op == '%'):
    print("%d mod %d = %d"%(num1, num2,num1 % num2))
else:
    print("Not a valid operator")