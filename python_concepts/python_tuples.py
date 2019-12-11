"""
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists
the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

"""

"""
List []                     can contains duplicate, mutable 
Tuple ()                    Same as list , imutable, used where requiment is value shouls not get change
dict {key : "Value"}        key should be unique. 
set ()                      can no contains 

"""

tuple1 = ()
tupele2 = (1, 2, 3, 4, 5)
tupele3 = (4, 5, 6, 7, 8)
tuple4 = (tupele2, tupele3)
print(tupele2)
print(tuple4)
print(tupele2 + tupele3)

#tupples are immutable so you can not add vaulue to it

# vut you can delete entier tuple by del key word as belwo

#del tupele2
#print(tupele2)


#slicing of tupele is similar to list
print(tupele2[0:])


thistuple = ("apple",)
print(type(thistuple))

tupleI = (1)
print(type(tupleI))

if 1 in tupele2:
    print("yes")
else:
    print("no")