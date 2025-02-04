#Ex1
class two_methods:
    def __init__(self):
        self.input_string = ""
    def getString(self):
        self.input_string = input("Enter a string: ")
    def printString(self):
        print(self.input_string.upper())
twoMethods = two_methods()
twoMethods.getString()
twoMethods.printString()
#Ex2
class Shape:
    class Square:

