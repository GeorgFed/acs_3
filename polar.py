import math

from number import *
from point import *

class Complex(Number):
    def __init__(self):
        self.angle = 0
        self.endpoint = Point()

    def read(self, array, i):
        self.angle = int(array[i])
        self.endpoint.x = int(array[i + 1])
        self.endpoint.y = int(array[i + 2])
        i += 3
        return i

    def __str__(self):
        return f'Polar: angle = {self.angle}, x = {self.endpoint.x}, y = {self.endpoint.y}\n' \
               f'Real: {self.to_real()}'

    def to_real(self):
        return math.sqrt(self.endpoint.x**2 + self.endpoint.y**2)