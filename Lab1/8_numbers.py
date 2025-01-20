x = 1 # int
y = 2.8 # float
z = 1j # complex
print(type(x))
print(type(y))
print(type(z))
x = 1
y = 627863786287
z = -2898019
print(type(x))
print(type(y))
print(type(z))

#float
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

#Float
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

#Complex
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
#Converting from one type to another
x = 1
y = 2.8
z = 1j
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
#Random number
import random
print(random.randrange(1, 10))