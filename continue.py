numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
else:
    print("Inside else block")