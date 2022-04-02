'''
Q1. Write a python program to sum a specific column of a list in a given list of lists.
Original list of lists:
[[1,2,3,2],[4,5,6,2],[7,8,9,5]]
Sum: 1st column of the said list of lists: 12
sum: 2nd column of the said list of lists: 15
Sum: 4th column of the said list of lists: 9
'''


mylist = [[1, 2, 3, 2],
          [4, 5, 6, 2],
          [7, 8, 9, 5]]
z = 1
sum = 0
for x in range(4):
    for y in mylist:
        sum += y[x]
    if(z != 3):
        print(f"Sum: {z}st column of the said list of lists: {sum}")
    z += 1
    sum = 0


""" def addcol(mylist, a):
    result = sum(b[a] for b in mylist)
    return result

mylist = [[1, 2, 3, 2],
          [4, 5, 6, 2],
          [7, 8, 9, 5]]

column = 0
print(addcol(mylist, column))

column = 1
print(addcol(mylist, column))


column = 3
print(addcol(mylist, column))
 """
