'''
Q6. Write a Python program to count the number of strings where the string lenght is 2 or more and the first and last characters
are the same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result: 2

'''

mylist = ['abc', 'xyz', 'aba', '1221']

count = 0
for items in mylist:
    if(items[0] == items[-1] and len(items) >= 2):
        count += 1
print(count)
