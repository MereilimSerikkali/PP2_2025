#Ex1
def squares(N):
    for i in range(N + 1):
        yield i ** 2

# Example:
N = 5
for square in squares(N):
    print(square)

#Ex2
def even_numbers_upto(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Example:
n = int(input("Enter a number: "))
even_numbers = even_numbers_upto(n)
print(", ".join(map(str, even_numbers)))

#EX3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example:
n = 50
for num in divisible_by_3_and_4(n):
    print(num)
#Ex4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Example:
a, b = 3, 7
for square in squares(a, b):
    print(square)
    
#EX5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Example:
n = 10
for num in countdown(n):
    print(num)