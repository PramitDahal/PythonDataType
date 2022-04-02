'''
Q5. Write  a Python program to remove all strings from a given list of tuples

Original list:[(100, 'Math'), (80, 'Math'), (90, 'Math'),(88, 'Science', 89), (90, 'Science', 92)]

Remove all strings from the said list of tuples:
[(100,), (80,), (90,), (88, 89), (90, 92)]

'''
mylist = [(100, 'Math'), (80, 'Math'), (90, 'Math'),
          (88, 'Science', 89), (90, 'Science', 92)]


output = [tuple([j for j in i if type(j) != str]) for i in mylist]
print(output)

# List comprehensions
