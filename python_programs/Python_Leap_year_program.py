try:
    print("Enter the year you want to check: -")
    year = int(input())      #by default your input function will take the value in string format)
    print(type(year))       # this will give yuo the type of the variable
    print(year)
except ValueError:
    print('please enter valid input, only numbers are allowed')
    exit(1)

if year%400 == 0:
    print('this is leap yeaer..')
elif year%4 == 0:
    print('this is a leap year')
elif year%100 == 0:
    print('this is not a leap year')
else:
    print('Not a leap year...')
