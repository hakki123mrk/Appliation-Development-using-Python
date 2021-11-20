principal = int(input("Enter the principal amount : "))
rateofinterest = int(input("Enter the rate of interest : "))
duration = int(input("Enter the duartion in years : "))

SI = (principal * rateofinterest * duration) / 100
print("Simple Interest is : ", format(SI))