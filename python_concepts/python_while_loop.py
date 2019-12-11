i = 1
while i <=5:
    print(i)
    if i == 3:
        print("Loop breaked")
        break
    i += 1
else:
    print("loop completed")



#With the continue statement we can stop the current iteration, and continue with the next:

x = 0
while x <= 5:
    x += 1
    if x == 3:
        continue
    print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")