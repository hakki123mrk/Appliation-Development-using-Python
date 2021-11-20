num = int(input("Enter a number : \t"))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num ," is not a prime number")
else:
    print("Given number", num, " is a prime number")