'''
Q9.Write a python program to check whether two list are circularly identical.
list1 = [10,10,0,0,10]
list2 = [10,10,10,0,0]
list3 = [1,10,10,0,0]
Output:
Compare list1 and list2: True
Compare list1 and list3: False
'''
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
a = ' '.join(map(str, list1*2))
# print(a)
b = ' '.join(map(str, list2))
# print(b)
print("Compare list1 and list2: ")
print(b in a)

c = ' '.join(map(str, list3))
# print(c)
print("Compare list1 and list3: ")
print(c in a)
