
#https://www.w3resource.com/python/python-list.php good Documnet


'''this program is to demonstrate the use of list and inbuild fnction available for performing operations on list'''

'''this declres the blank list'''

blank_list = []
print(blank_list)

list1 = ['A', 'E', 'I', 'O', 'U']
india = ['I', 'LOVE', 'INDIA']
first_name = ['Anurag']
last_name = ['Pathak']
Mix = ['1', '2', 'a', 'e', 'i', 'o', '3', '4', '5', 'u']
print(Mix)
print(list1[0:])  #prints the complete list starting from 0
print(list1[3:])
print(list1[-3])        # when used '-ve' sign count from last starting with -1


#Lists Concatination:
print(first_name + last_name)

#list repetation,
print(first_name*2)

#looping through the list or itrating through the list
#for x in list1:
 #   print(x)

#updating the value in the list:
print(Mix[0])
Mix[0] = 0
print(Mix[0])

#Deleting the element from the list using del keyword.
print(Mix[0])
del Mix[0]
print(Mix[0])

#list opreations:
print(len(['1', '2', '3']))
print(len(list1))

#check if element is present in the list or not
if 'a' in Mix :
    print('True')
else:
    print('False')

#################################################3
'''List built in function'''

#compare two list:
L1 = ['1', '2', '3', '1']
L2 = ['1', '2', '3']
L3 = ['5', '4', '6']
#x = cmp(L1, L2)
print(len(L1))
print(max(Mix))
print(min(L1))


#L1.append('4')
print(L1)
#L1.append('100')
print(L1)

#print(L1.count('1'))

#Extends method is used to append another list into the other list.
print(L1)
#L1.extend(L2)
print(L1)

print(L1)
L1.append(L2)
print(L1)

for x in L1:
    print(x)
#diffrence between append and extend method of list --> Append will add as a single element at the end of the string  where as extend will add element by element.

print(L1.index('2'))    #Returns the lowest index in list that obj appears

print(L1.insert(0,'0')) # insert the element at the particular index
print(L1)


#Reverse the list and stores the result in the same list
L1.remove(L1[-1])
print(L1)

#list is as stack: this pop() method is used for poping up the last element from the list.. it is as good as delete last element.
#L1.pop()
#print(L1)

L1.reverse()
print(L1)


##############################################
#List sorting
print(L1)
L1.sort()
print(L1)
