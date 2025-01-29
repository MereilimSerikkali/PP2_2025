#Example 1
mylist = ["apple", "banana" "cherry"]

#Example 2
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Example 3
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Example 4
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#Example 5
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#Example 6
list1 = ["abc", 34, True, 40, "male"]

#Example 7
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Example 8
thislist = list(("apple", "banana", "cherry"))
print(thislist)

#Example 9
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Example 10
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Example 11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Example 12
thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon", "mango "]
print(thislist[:4])

#Example 13
print(thislist[2:])

#Example 14
print(thislist[-4:-1])

#Example 15
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple is in the fruits list")

#Example 16
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

#Example 17
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Example 18
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Example 19
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Example 20
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Example 21
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Example 22
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Example 23
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Example 24
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Example 25
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Example 26
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Example 27
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Example 28
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Example 29
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Example 30
thislist = ["apple", "banana", "cherry"]
del thislist

#Example 31
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Example 32
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#Example 33
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#Example 34
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1 
    
#Example 35
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#Example 36
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

#Example 37
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Example 38
newlist = [x for x in fruits if x != "apple"]

#Example 39 
newlist = [x for x in fruits]

#Example 40
newlist = [x for x in range(10)]

#Example 41
newlist = [x for x in range (10) if x < 5]

#Example 42
newlist = [x.upper() for x in fruits]

#Example 43
newlist = ['hello' for x in fruits]

#Example 44 
newlist = [x if x != "banana" else "orange" for x in fruits]

#Example 45
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Example 46
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Example 47
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Example 48
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Example 49
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Example 50
thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.sort()
print(thislist)

#Example 51
thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Example 52 
thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Example 53
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Example 54
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Example 55
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Example 56
list1 = ["a", "b", "c"]
lis2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Example 57
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

#Example 58
list1 = ["a", "b", "c"]
lis2 = [1, 2, 3]
list1.extend(list2)
print(list1)

