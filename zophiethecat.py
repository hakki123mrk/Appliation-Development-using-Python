name = input("Enter a string : ")
repstr = input("Enter the string to be replaced : ")
newstr = input("Enter a new String : ")
print(name.replace(repstr, newstr))
temp = name.split(' ')
for i in range(0, len(temp)):
    if(temp[i] == repstr):
        temp[i] = newstr
print(*temp)