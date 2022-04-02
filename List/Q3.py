'''
Q3. Write a Python program to reverse a given list of lists.

Original List:
[['orange','red'],['green','blue'],['white','black','pink']]
Reverse said list of lists:
[['white','black','pink'],['green','blue'],['orange','red']]

Original list:
[[1,2,3,4],[0,2,4,5],[2,3,4,2,4]]
Reverse said list of list:
[[2,3,4,2,4],[0,2,4,5],[1,2,3,4]]
'''
mylist1 = [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
mylist1.reverse()
print(mylist1)

mylist2 = [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
mylist2.reverse()
print(mylist2)
