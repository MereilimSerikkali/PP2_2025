#              Python Variables

x = 5
y = "John"
print(x)
print(y)

x = 4 # x is the type of int
x = "Sally" # x is now of type str
print(x)

x = str(3)
y = int(3)
z = float(3)

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

#            Variable Names

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

"""
Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John
"""

myVariableName = "John" #Camel case
MyVariableName = "JOhn" #Pascal case
my_variable_name = "John" #Snake case

#     Assign Multiple Values

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#        Output variables
x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "AWESOME"
print(x, y, z)

# + operator with strings
x = "Python "
y = "is "
z = "awesome "
print(x + y + z)

# + operator with numbers
x = 5
y = 10
print(x + y)

#best way to output multiple variables with diff data types
x = 5
y = "John"
print(x, y)

#        Global Variables
x = "awesome"
def myFunc():
    print("Python is " + x)
myFunc()

x = "awesome"
def function():
    x = "fantastic"
    print("Python is " + x)
function()
print("Python is " + x)

def func():
    global x
    x = "fantastic"
func()
print("Python is " + x)

x = "awesome"
def my_func():
    global x 
    x = "fantastic"
my_func()
print("Python is " + x)

