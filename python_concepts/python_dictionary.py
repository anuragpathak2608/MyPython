'''
Dictionary is immutable
Dictionary in Python is an unordered collection of data values,
Dictionary holds key:value pair.
Each key-value pair in a Dictionary is separated by a colon :,
whereas each key is separated by a ‘comma’.
Keys of a Dictionary must be unique and of immutable data type such as Strings, Integers and tuples,
but the key-values can be repeated and be of any type.
Keys in a dictionary doesn’t allows Polymorphism.

a Dictionary can be created by placing sequence of elements within curly {} braces,
also be created by the built-in function dict().
Dictionary keys are case sensitive, same name but different cases of Key will be treated distinctly
'''

#CREATING AN EMPTY DISCT

dict = {}
print("This is empty dictonary...", dict)

#CREATING DICT WITH INTEGER KEY

dict = {1: "Anurag", 2: "Anant", 3: "Pathak"}
print(dict)

#CREATING DISCT WITH MIXED KEYS
dict = {1: "Anurag", "Anant": "2", 3: "Pathak"}
print(dict)

#Nested Dictionary:
city = {1: "US", 2: "UK", 3: {1: "India", 2: "Pakistan", 3: "shrilanka"}}

print(city[3])

######
#Accessing elements from a Dictionary
######
