import sys      

print(sys.version)
print("Hello Welocme to python ")

if 5 < 2:
    print("Five is greater than two !")
else:
    print("nothing")

x = 5
y = "hello world"

print(str(x) + " " +y)

# This is a coment in python]

"""
This is a multiple line comments
"""
print(type(x))
print(type(y))

z = ["apple", "bananan", "mango"]
print(type(z))

j = ("apple", "bananan", "mango")

print(type(j))


c = range(5)
print(c)

x1 = {"email" : "example@email.com", "name":"Hasan"}
print(x1.keys())
print(x1.values())

print(x1["apple"])
print(x1["mango"])


print(list(x1.keys())[0])
print(list(x1.values())[0])

print(list(x1.items())[0])
