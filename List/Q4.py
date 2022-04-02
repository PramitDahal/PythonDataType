'''
Q4. Write a Python program to get the unique values in a given list of lists.

Original list:
[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
Unique values of the said list of lists:
[0, 1, 2, 3, 4, 5, 7]

Original List:
[['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
Unique values of the said list of lists:
['h', 'g', 'l', 'k', 'a', 'b', 'd', 'e', 'c', 'j', 'i', 'y', 'n', 'v', 'x', 'z']

'''

mylist1 = [[1, 2, 3, 5], [2, 3, 5, 4], [
    0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]

unique1 = []

for numbers in mylist1:
    for items in numbers:
        if items not in unique1:
            unique1.append(items)
unique1.sort()
print(unique1)

mylist2 = [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'],
           ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
unique2 = []

for numbers2 in mylist2:
    for items2 in numbers2:
        if items2 not in unique2:
            unique2.append(items2)

print(unique2)
