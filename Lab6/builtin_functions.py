#Ex1
from functools import reduce
def multiplied(numbers):
    result = reduce(lambda x, y: x* y, numbers)
    return result
print(multiplied([1, 2, 3, 4]))

#Ex2
def count_upper_lower_case_letters(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return upper_count, lower_count

input_string = "Hello World! 123"
upper, lower = count_upper_lower_case_letters(input_string)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")

#Ex3

def is_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

input_string = "A man, a plan, a canal, Panama!"
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

#Ex4
    
import time
import math

def delayed_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000)  # milliseconds to seconds
    return math.sqrt(number)

number = 25100
delay_ms = 2123
result = delayed_square_root(number, delay_ms)
print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

#Ex5

def all_elements_true(input_tuple):
    return all(input_tuple)

input_tuple = (True, True, False)
if all_elements_true(input_tuple):
    print("All elements in the tuple are True.")
else:
    print("Not all elements in the tuple are True.")
