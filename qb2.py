list1 = []
list2 = []
list_add = []
x= int(input('Enter number of elements in list 1: '))
print('Enter elements: ')
for i in range(x):
    list1.append(int(input()))
y= int(input('Enter number of elements in list 2: '))
print('Enter elements: ')
for i in range(y):
    list2.append(int(input()))
small = len(list1) if (len(list1) < len(list2))else len(list2)
for i in range(small):
    list_add.append(list1[i] + list2[i])
print(list1)
print("+")
print(list2)
print(list_add)
