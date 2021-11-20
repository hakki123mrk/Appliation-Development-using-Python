def fact(num):
    if(num == 1):
        return 1
    else:
        return num * fact(num-1)

num = int(input("Enter a number : "))
fact = fact(num)
print("Factoria of", num, "is", fact)