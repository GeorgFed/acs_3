import math
import random

from number import *
from point import *


class Polar(Number):
    def __init__(self):
        self.angle = 0
        self.endpoint = Point()

    def read(self, array):
        self.angle = int(array[0])
        self.endpoint.x = int(array[1])
        self.endpoint.y = int(array[2])
        return self

    def generate(self):
        self.angle = random.randint(0, 10000)
        self.endpoint.x = random.randint(0, 10000)
        self.endpoint.y = random.randint(0, 10000)
        return self

    def raw(self):
        return f'2 {self.angle} {self.endpoint.x} {self.endpoint.y}'

    def __str__(self):
        return f'Polar: angle = {self.angle}, x = {self.endpoint.x}, y = {self.endpoint.y}\n' \
               f'Real: {self.to_real()}'

    def to_real(self):
        return math.sqrt(self.endpoint.x ** 2 + self.endpoint.y ** 2)
