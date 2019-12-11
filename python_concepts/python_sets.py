'''
A Set is an unordered collection data type and unindexed
It is iterable, mutable, and has no duplicate elements.

Frozen Sets Frozen sets are immutable objects that only support methods and operators

'''
#sets in python
set = {'a', '1', 'b', '2', '3', 4}
set1 = {1, 2, 3, 4}
#list in python
list = ['a', 'b', 'c', 'd']

#dict in python
dict = {'key': "value", 1: "1", "Anurag": 1}

#print(set)
#print(list)
#print(dict)

#Check if the element is preent in the set
if '3' in set:
    print("Yes")
else:
    print("No")

#print the elements of the list
#for x in set:
    #print(x)

## Add single item to the set
print(set)
print("Enter Element to add:")
#x = input()
#set.add(x)
print(set)

#Add multiple elemet at a time
print(set)
#set.update(['Anurag', 'Anant', 'Pathak'])
print(set)

# find the length of the set
print("Len of the set is %d" % (len(set)))

print("Length of the list is %d" % (len(list)))

print("lent of dict is %d" %(len(dict)))

# remove element from the set
print(set)
set.remove('3')
print(set)

# remove element by discard method "Discard will not thorw the error if the ele to remove is not there"
#where as the remove will give error if element is not present
print(set)
set.discard('3')

#pop will remove last element from the set, which when used will remove any random element as set is un ordered
# pop returns the value of removed element.
print(set)
print(set.pop())
print(set)

#del key word will delete the set completly
#del set
#print(set)

#unioun to merge two sets
#set3 = set.union(set1)
#print(set, set1, set3 )

# update to merge two sets
set1.update(set)
print(set1)

#| to merge two sets
set3 = set | set1
print(set3)
print(set3)

#find out intersection of the sets
set3 = set.intersection(set1)
print(set3)

#find out the differnce
set3 = set.difference(set1)
print(set3)
Set3 = set - set1
print(set3)
#https://www.w3schools.com/python/python_sets.asp