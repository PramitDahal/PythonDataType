'''
Q11.Write a Python program to insert a given string at the beginning of all items in a list.
num = [1,2,3,4]
string = "emp"
OUTPUT => ['emp1','emp2','emp3','emp4']
'''
num = [1, 2, 3, 4]
string = "emp"

print([f"{string}{i}" for i in num])
