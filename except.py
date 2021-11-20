import sys
list = ['b', 0, 2]
for entry in list:
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
    except ValueError:
        print('Unable to perform arithmatic operation on characters')
    except ZeroDivisionError:
        print('Unable to divide by zero')
    print("Next entry")
print("The result of", entry, "is", r)
