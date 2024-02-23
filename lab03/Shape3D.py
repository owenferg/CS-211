'''Owen Ferguson
Lab03 Shape3D 1-24-2024'''

import math

class Shape3D:  
    def __init__(self):
        raise NotImplementedError("Abstract class cannot be instantiated")

    def volume(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def area(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")
    
    def print_info(self):
        print(f'Area: {self.area()} Volume: {self.volume()}')

class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = float(radius)
        self.height = float(height)
        self.area()
        
    def volume(self) -> float:
        return math.pi * self.radius**2 * self.height
    
    def area(self) -> float:
        return 2 * math.pi * self.radius**2 + 2 * math.pi * self.radius * self.height
        
class Cuboid(Shape3D):
    def __init__(self, width, length, height):
        self.width = float(width)
        self.length = float(length)
        self.height = float(height)

    def volume(self) -> float:
        return self.width * self.length * self.height
    
    def area(self) -> float:
        return 2 * self.width * self.length + 2 * self.width * self.height + 2 * self.length * self.height
    
class Cube(Cuboid):
    def __init__(self, width):
        self.width = width
        self.length = width
        self.height = width