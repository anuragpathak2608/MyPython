var1 = 1+2j
var2 = 1
var3 = 'string'
var4 = 10.10
var5 = []
var6 = ()
var7 = {}


print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))
print(type(var6))
print(type(var7))

if type(var1) == int :
    print("Integer")
elif type(var1) == str:
    print("String")
elif type(var1) == bool:
    print("Boolean")
elif type(var1) == float:
    print("Float")
elif type(var1) == complex:
    print("Complex")
else:
    print("None of the above")

x = True
y = False

if (x and y):
    print('Both are true')
else:
    print('Either one is false')
list1 = [1, 2, 3]
a = 1
if a in list1:
    print("Preset:")
else:
    print("Not Present")
    