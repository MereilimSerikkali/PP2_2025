#Example 1
mytuple = ("apple", "banana", "cherry")

#Example2 
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Example3
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Example4
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Example5
thistuple = ("apple",)
print(type(thistuple))
#NOt a tuple
thistuple = ("apple")
print(type(thistuple))

#Example6
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 2, 3, 4, 5)
tuple3 = (True, False, False)

#Example7
tuple1 = ("abc", 34, True, 40, "male")

#Example8
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Example9
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#Example10
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Example11
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Example12
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Example13
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#Example14
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Example15
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Example16
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, apple is in the fruits tuple")

#Example17
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Example18
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Example19
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#Example20
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#Example21
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #Causing error

#Example22
fruits = ("apple", "banana", "cherry")

#Example23
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits 
print(green)
print(yellow)
print(red)

#Example24
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#Example25
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#Example 26
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

#Example27
thistuple = ("apple", "banana", "cherry")
for i in range (len(thistuple)):
    print(thistuple[i])
    
#Example28
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

#Example29
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple2)

#Example30
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
    