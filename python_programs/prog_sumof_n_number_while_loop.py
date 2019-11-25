x = 1
sum = 0
while(x <= 10):
    print(x)
    sum = sum + x
    x = x + 1
else:
    print("\nSum =", sum)


i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i = i + 1

print("Exited by break...")
