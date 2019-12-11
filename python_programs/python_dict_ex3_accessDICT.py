dist = {}
print("Generate dictinlary: ")
for x in range(3):
    print("Enter Key:")
    key = input()
    print("Enter Value:")
    Value = input()
    dist[key] = Value

print("Generated Dict is")
print(dist)

#Read element from dictonary using get
shabdkosh = {1: 'a', 2: 'b', 3: 'c'}
print(shabdkosh.get(2))

#delete element from dictonary or deleting whole dictnary.
Dict = { 5 : 'Welcome',
         6 : 'To',
         7 : 'Geeks',
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
        'B' : {1 : 'Geeks', 2 : 'Life'}
       }

#delete element from pop
#Dict.pop(5)
#print(Dict)

#delete any arbitrary eletment from the dictonay using popitem()
#Dict.popitem()
print(Dict)

#deleting single element using del key word
#del Dict['A']
#del Dict[5]
print(Dict)

#Deleting the ke from nested dict.
del Dict['A'][3]
print(Dict)

#Returns all the values in list
print(Dict.values())
#Dict.clear()
print(Dict)
#print(Dict.Has_key('A'))

#https://www.geeksforgeeks.org/python-dictionary/