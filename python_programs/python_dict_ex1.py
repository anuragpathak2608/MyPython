#####################################
# Adding elements to a Dictionary   #
#   Dict[Key] = ‘Value’             #
#                                   #
#####################################
score = {}
print("This dict is empty now: \n")
print(score)


print("Enter how many subjects you want to enter: ")
number = int(input())
for x in range(1, number+1):
    print("Enter subject Name :")
    sub = input()
    print("Enter Marks of  {}:".format(sub))
    marks = int(input())
    score[sub] = marks
print("Below is the your score card:")
print(score)

print("Enter the subject to know the marks")
subject = input()
print("You have scored %d marks in {}".format(subject) % (score[subject]))





