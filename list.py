list = [1, 2, 3, 4, 5, 6, 7] 
print(len(list))
for i in list:
    print(i)
list.insert(8, 11)
for i in range(0, len(list)):
    print(list[i])
print(len(list))
list.append(15)
for i in range(0, len(list)):
    print(list[i])
print(list)
abc = list
list.append(31)
print(abc)



