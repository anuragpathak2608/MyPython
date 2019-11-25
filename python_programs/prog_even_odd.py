'''find out the even and odd numbers counts'''

dictonary = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12)
even_counter = 0
odd_counter = 0

for x in dictonary:
    if x % 2:
        odd_counter += 1
    else:
        even_counter += 1
print("Total Number of Even number is %d \nTotal number of Odd  number is %d " %(even_counter, odd_counter))
