'''
Q8. Write a Python function that takes two lists and returns True if they have at least one common member.
a = [1,2,3,4,5]
b = [5,6,7,8,9]

output => True

a = [1,2,3,4,5]
b = [6,7,8,9]

output => None


'''


def func(list1, list2):
    for a in list1:
        for b in list2:
            if a == b:
                result = True
                return result


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(func(a, b))

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9]
print(func(x, y))
