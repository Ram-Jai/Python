# Find Nth largest element in Python
from collections import OrderedDict 
    
n = int(input('Enter the number of elements in the list: \n'))
a = [int(input()) for _ in range(n)]
print("The original list is ",a)

a_new = list(set(a))
a_new = list(OrderedDict.fromkeys(a))
print('The new list after the duplicates are removed is ',a_new)

a_new.sort()
print('The sorted list is {} with a length of {}'.format(a_new, len(a_new)))

k = int(input('Enter the Nth largest element you want to find: \n'))
print('The value is ',a_new[k-1])
