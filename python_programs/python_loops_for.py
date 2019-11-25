'''For loop in python is used to traversl the list and other data structure  '''

Colors = ['Red', 'Green', 'Yellow', 'Blue', 'Green']
for color in Colors:
    print(color)


'''Python uses range() function for starting and incrementing the loop , Below is the syntax'''

# range(S-tarting_Index,Ending_Index, Increment_By)

# Run python loop from 1 to 10.

for x in range(1,10):
    print(x)

# Run loop to print only even numbers
print()
for x in range(0, 10, 2):
    print(x)
