'''Program to identify and print 2 consicative elements in list'''

l1 = [1, 1, 2, 2, 3, 4, 5, 5, 7, 5]
zipped = zip(l1[:], l1[1:])

for x, y in zipped:
    if x == y:
        print(x, y)

