import copy
spam = ['A', 'B', 'C', 'D']
temp = [[21,31, 41, 51], 21, 31, 51, 41]
cheese = copy.copy(spam)
jam = copy.deepcopy(temp)
cheese[1] = 42
print(spam)
print(cheese)
print(temp)
print(jam)