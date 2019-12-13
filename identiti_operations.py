'''
1. Using identity operators we can check memory location of objects
'''

a = 10
b = 10
c = a

l = [1,2,3]
l2 = l

if a is not c : print('IS')
# print(' L id is :', id(l))
# print(' L2 id is :', id(l2))

# if l is l2 : print('IS')