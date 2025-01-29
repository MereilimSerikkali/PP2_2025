#Example1 
thisdict = {
    "brand" : "Ford",
    "model":"Mustang",
    "year": 1964
}
print(thisdict)

#Example2
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print(thisdict["brand"])

#Example3
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

#Example4
print(len(thisdict))

#Example5
thisdict = {
    "brand":"Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
    
}
#Example6
print(type(thisdict))

#Example7
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Example 8
thisdict = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964
}
x = thisdict["model"]

#Example 9
x = thisdict.get("model")

#Example10
x = thisdict.keys()

#Example11
car = {
    "brand": "Ford", 
    "model": "mustang",
    "year": 1964

}
x = car.keys()
print(x)
car["color"] = "white"
print(x)

#Example12
x = thisdict.values()

#Example13
car = {
    "brand":"Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)
car["year"] = 2020
print(x)

#Example 14
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year":1964
}
x = car.values()
print(x)
car["color"] = "red"
print(x)

#Example 15
x = thisdict.items()

#Example16
car = {
    "brand": "Ford",
    "model" : "Mustang",
    "year": 1964
}
x = car.items()
print(x)
car["year"] = 2020
print(x)

#Example 17
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
car["color"] = "red"
print(x)

#Example 18
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in thisdict dictionary")

#Example 19
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

#Example 20
thisdsct = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})

#Example 21
thisdict = {
    "brand": "Ford",
    "model": "MUstang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Example 22
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})

#Example 23
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

#Example 24
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

#Example 25
thisdict.clear()
print(thisdict)

#Example 26
for x in thisdict:
    print(x)

#Example27
for x in thisdict:
    print(thisdict[x])

#Example 28
for x in thisdict.values():
    print(x)

#Example 29
for x in thisdict.keys():
    print(x)

#Example 30
for x, y in thisdict.items():
    print(x, y)
    
#Example 31
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Example 32
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}    
mydict = dict(thisdict)
print(mydict)

#Example 33
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    }, 
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus", 
        "year" : 2011
    }
}
#Example 34
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year" : 2011
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

#Example 35
print(myfamily["child2"]["name"])

#Example 36
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ":", obj[y])
        