import math
#Ex1
degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print(f"Output radian: {radian:.6f}")

#Ex2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area = 1/2 * (base1 + base2) * height
print(f"Expected Output: {area}")

#Ex3
n = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))
area = (n * side_length**2) / (4 * math.tan(math.pi / n))
print(f"The area of the polygon is: {area}")

#Ex4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print(f"Expected Output: {area}")