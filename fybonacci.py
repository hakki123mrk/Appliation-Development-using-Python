def fybonacci(num):
    if num < 0:
        print("Invalid Number")
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fybonacci(num - 1) + fybonacci(num - 2)

print(fybonacci(int(input("Enter a number : "))))