
'''The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.'''
'''Which means if you have 2 List L1 and L2 and you have to mapp L1[0] to L2[0]'''

Name = ['Anurag', 'Anant', 'Pathak']
Roll_number = ['1', '2', '3']
Marks = ['70', '80', '90']

mapped = zip(Name, Roll_number, Marks)
mapped = set(mapped)
print("Mapped Results: ", mapped)

'''Unziping results back to individual list'''

Namez, Roll_numberz, Marksz = zip(*mapped)
print(Namez)
print(Roll_numberz)
print(Marksz)
