"""
Text type: str
Numeric types: int, float, complex
Sequence types: list, tuple, range
Mapping type: dict
Set types: set, frozenset
Boolean type: bool
Binary types: bytes, bytearray, memoryview
None type: NoneType
"""
x = 5
print(type(x)) 
x = "Hello World" # str
x = 20 # int
x = 20.5 #float
x = 1j #complex
x = ["apple", "banana"] #list
x = ("apple", "banana") #tuple
x = {"name": "John", "age": 36} #dict
x = {"apple", "banana"} #set
x = range(6) #range
x = frozenset({"apple", "banana"}) #frozenset
x = True #bool
x = b"Hello" #bytes
x = bytearray(5)
x = memoryview(bytes(5)) #memoryview
x = None #NoneType

