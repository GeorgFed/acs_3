import math
import random

from number import *


class Complex(Number):
    def __init__(self):
        self.d = 0
        self.i = 0

    def read(self, array):
        self.d = int(array[0])
        self.i = int(array[1])
        return self

    def generate(self):
        self.d = random.randint(0, 10000)
        self.i = random.randint(0, 10000)
        return self

    def raw(self):
        return f'0 {self.d} {self.i}'

    def __str__(self):
        return f'Complex: d = {self.d}, i = {self.i}\n' \
               f'Real: {self.to_real()}'

    def to_real(self):
        return math.sqrt(self.d ** 2 + self.i ** 2)
