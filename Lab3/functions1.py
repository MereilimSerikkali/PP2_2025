import math
import random
#Ex1
def ounces(grams):
    return 28.3495231 * int(grams)
#Ex2
def c(f):
    return (5/9) * (f - 32)
#Ex3
def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if( 4* rabbits + 2 * chickens) == numlegs:
            return chickens, rabbits
    return None
#Ex4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
#Ex5
def permutations(s, prefix = ""):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            permutations(s[:i] + s[i + 1:], prefix + s[i])
#Ex 6
def reverse(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])
#Ex7
def has_33(nums):
    for i in range(len(nums - 1)):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
        return False
#Ex 8 
def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                reutrn True
    return False
#Ex9
def sphere_volume(radius):
    return (4/3) * math.pi * (radius **3)
#Ex10
def unique_elements(lst):
    uinque_list = []
    for item in lst:
        if item not in uinque_list:
            uinque_list.append(item)
    return uinque_list
#Ex11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
#Ex12
def histogram(lst):
    for num in lst:
        print('*' * num)
#Ex13
def guess_the_num():
    name = input("Hello! What's your name ?\n")
    print(f"Well, {name}, I am thinking of a num between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0
    while True:
        guess = int(input("Take a guess. \n"))
        guesses +=1 
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses")
            break
print(grams_to_ounces(100))
print(fahrenheit_to_centigrade(98.6))
print(solve(35, 94))
print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(permutations("abc"))
print(reverse_sentence("We are ready"))
print(has_33([1, 3, 3]))
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(sphere_volume(5))
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
print(is_palindrome("madam"))
histogram([4, 9, 7])
guess_the_number()        
