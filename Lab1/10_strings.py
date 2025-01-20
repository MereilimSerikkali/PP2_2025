# PYTHON STRINGS
print("Hello")
print('Hello')
print("It's alright")
#quotes inside quotes
print("He is called 'Johnny'")
print('He is called "Johnny"')
#Assign string to a variable
a = "Hello"
print(a)
#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Strings are arrays
a = "Hello, World!"
print(a[1])
#Looping through letters
for x in "banana":
    print(x)
a = "Hello, World!"
print(len(a))
#Check String
txt = "The best things in life are free!"
print("free in txt")
if "free" in txt:
    print("Yes, 'free' is present")
print("expensive not in txt")
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")
# SLICING STRINGS
b = "Hello, World!"
print(b[:5])
print(b[2:])
print(b[-5:-2])
#MODIFY STRINGS
print(b.upper())
print(b.lower()) 
print(b.strip())
print(b.replace("H", "J"))
print(b.split(",")) #returns ['Hello', 'World!']
#STRING CONCATENATION
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)
#FORMAT
age = 36
txt = f"My name is John, I am {age}"
print(txt)
price = 59
txt = f"The price is {price} dollars"
print(txt)
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20*59} dollars"
print(txt)
#ESCAPE CHARACTERS
txt = "we are the so-called \"Vikings\" from the north."
#STRING METHODS
"""capitalize()
casefold()
center()
count()
encode()
endswith()
expandtabs()
find()
format()
format_map()
index()
isalnum()
isalpha()
isascii()
isdecimal()
isdigit()
isidentifier()
islower()
isnumeric()
isprintable()
isspace()
istitle()
isupper()
join()
!just()
lower()
lstrip()
maketrans()
partition()
replace()
rfind()
rindex()
rjust()
rpartition()
rsplit()
rstrip()
splitlines()
startswith()
strip()
swapcase()
title()
translate()
upper()
zfill()
"""

    