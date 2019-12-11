#####################################
#  Adding  set of values to single  #
#     key                           #
#                                   #
#####################################
#TIP: if you have declared the list as an empty list and latter you are trying to assing the value to it,
# by list[1] =value this will not work as there is not index 0 in the list for this use append function to
#generate the list.

scorecard = {}
marks = []
print("Enter the number of students...")
number = int(input())
for x in range(1, number + 1):
    print("Enter the name of {} candidate".format(x))
    key = input()
    print("Enter the marks of english")
    marks.append(int(input()))
    print("Enter the marks of Hindi")
    marks.append(int(input()))
    print("Enter the marks of Maths")
    marks.append(int(input()))
    scorecard[key] = marks
    print(scorecard)
    if x != number:
        marks.clear()
print("Score card of class:")
print(scorecard)