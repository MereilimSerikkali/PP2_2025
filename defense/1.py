import math
#class radius S
class Ploshad_kruga:
    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour
    def ploshad(self):
        return 3.14 * self.radius**2
    
red_circle = Ploshad_kruga(5)
print(red_circle.ploshad())