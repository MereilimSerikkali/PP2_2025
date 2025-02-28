import re
#Ex1
example = ["merei", "apple", "banana", "pear", "chocolate"]
new_list = []
def task_1(list_of_strings):
    regex = 'ab*'
    for name in list_of_strings:
        result = re.search(regex, name)
        new_list = []
        if result:
            new_list.append(name)
            return new_list

print("needed strings: ", task_1(example))
print("*************************")
#Ex2
example = ["mereiabb", "apple", "banana", "pear", "chocolate"]
def task_2(list_of_strings):
    regex = 'ab{2,3}'
    for name in list_of_strings:
        new_list = []
        result = re.search(regex, name)
        if result:
            new_list.append(name)
            return new_list
print("needed strings: ", task_2(example))

# Ex3
example = ["abc_def", "hello_world", "test_case", "exampleText"]
def task_3(list_of_strings):
    regex = '[a-z]+_[a-z]+'
    new_list = []
    for name in list_of_strings:
        result = re.search(regex, name)
        if result:
            new_list.append(name)
    return new_list

print("needed strings: ", task_3(example))
print("*************************")

# Ex4
example = ["Hello", "World", "Python", "testCase"]
def task_4(list_of_strings):
    regex = '[A-Z][a-z]+'
    new_list = []
    for name in list_of_strings:
        result = re.search(regex, name)
        if result:
            new_list.append(name)
    return new_list

print("needed strings: ", task_4(example))
print("*************************")

# Ex5
example = ["a123b", "testb", "a_test_b", "abc"]
def task_5(list_of_strings):
    regex = 'a.*b$'
    new_list = []
    for name in list_of_strings:
        result = re.search(regex, name)
        if result:
            new_list.append(name)
    return new_list

print("needed strings: ", task_5(example))
print("*************************")

# Ex6
example = ["Hello, world. How are you?", "Test, example. Data here"]
def task_6(list_of_strings):
    regex = '[ ,.]'
    new_list = []
    for name in list_of_strings:
        new_list.append(re.sub(regex, ":", name))
    return new_list

print("modified strings: ", task_6(example))
print("*************************")

# Ex7
example = ["hello_world", "snake_case_example", "convert_me"]
def task_7(list_of_strings):
    new_list = []
    for name in list_of_strings:
        new_list.append("".join(word.capitalize() for word in name.split("_")))
    return new_list

print("converted strings: ", task_7(example))
print("*************************")

# Ex8
example = ["HelloWorldTest", "CamelCaseString", "PythonCode"]
def task_8(list_of_strings):
    regex = '(?=[A-Z])'
    new_list = []
    for name in list_of_strings:
        new_list.append(re.split(regex, name))
    return new_list

print("split strings: ", task_8(example))
print("*************************")

# Ex9
example = ["HelloWorldTest", "InsertSpacesHere", "PythonCode"]
def task_9(list_of_strings):
    regex = '(?<!^)(?=[A-Z])'
    new_list = []
    for name in list_of_strings:
        new_list.append(re.sub(regex, " ", name))
    return new_list

print("modified strings: ", task_9(example))
print("*************************")

# Ex10
example = ["HelloWorldTest", "CamelCaseString", "ConvertMe"]
def task_10(list_of_strings):
    regex = '([a-z])([A-Z])'
    new_list = []
    for name in list_of_strings:
        new_list.append(re.sub(regex, r'\1_\2', name).lower())
    return new_list

print("converted strings: ", task_10(example))
print("*************************")
