import array as arr

a = arr.array('i', [0])
num = int(input("Enter number of elements : \t"))
for i in range(0, num):
    val = int(input("Enter %d element : "%(i+1)))
    a.insert(i, val)

flag = 0
i = 0
j = num - 1

while i <= num/2:
    if(a[i] == a[j]):
        i+=1
        j-=1
        continue
    else:
        flag = 1
        brea

if flag == 1:
    print("\nIts not a palindrome")
else:
    print("\nIts a palindrome")