import math
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
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2
square = Square(5)
print("Area:" square.area())
#Ex3
class Rectangle(Shape):
    def __init__ (self, length, width):
        self.length = lengthself.width
    def area(self):
        return self.length * self.width
rectangle = Rectangle(4, 6)
print("Area", rectangle.area())
#Ex4
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(Self, other_point):
        return math.sqrt((self.x - other_point.x) **2 + (self.y - other_point.y) **2)
point1 = Point(1, 2)
point2= Point(4, 6)
point1.show()
point2.show()
print("Distance equals to", point.dist(point2))
#Ex5
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("INsufficient funds")
        else:
            self.balance -= amount 
            print(f"Withdrew {amount}. New balance: {self.balance}")
account = Account("Merei", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)
#Ex6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
#Ex7
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 18]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)
