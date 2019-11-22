
a = 1
b = 1.1
c = 'string'

print(a)
print(b)
print(c)
#input('press any key to continue')

x = y= z = 100
print(x, y, z)

p, q, r = 1, 1.1, 'string'

print(p, q, r)

  #print complete string from the index

#Global and local variable
var1 = "Global"


def func1():
    var1 = "Local"
    print("this is  local variable", var1)


def func2():
    print("this is global variable", var1)


func1()

func2()

#Global and local variable


def func3():
    global var2
    var2 = "Anurag"
    print("Inside the function func3", var2)


def func4():
    print("Inside function func4", var2)


func3()
func4()
