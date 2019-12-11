'''
python language do not have switch case we will use python dict for this
'''


print("****Menu****")
print("1. Addition")
print("2. Multiplication")
print("3. Substraction")
print("4. Division")

print("Enter your choise: ")
input_text = int(input())

print("Enter number 1:")
num1 = int(input())

print("Enter number 2:")
num2 = int(input())

dist = {1 : num1 + num2, 2: num1 * num2, 3: num1 - num2, 4: num1/num2}

#print(dist)
print("Result of your operation is %d " %dist[input_text])