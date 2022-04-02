'''
Q2. Write a Python program to get the frequency of the elements in a given list of lists.
[[1,2,3,2],[4,5,6,2],[7,8,9,5]]
Frequency of the elements in the said list of lists:
{1:1,2:3,3:1,4:1,5:2,6:1,7:1,8:1,9:1}
'''

numbers = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
frequency = {}

for number in numbers:

    for items in number:
        if items in frequency:
            frequency[items] += 1

        else:
            frequency[items] = 1
print(frequency)
