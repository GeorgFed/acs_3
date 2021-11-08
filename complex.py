import math

from number import *


class Complex(Number):
    def __init__(self):
        self.d = 0
        self.i = 0

    def read(self, array, i):
        self.d = int(array[i])
        self.i = int(array[i + 1])
        i += 2
        return i

    def __str__(self):
        return f'Complex: d = {self.d}, i = {self.i}\n' \
               f'Real: {self.to_real()}'

    def to_real(self):
        return math.sqrt(self.d ** 2 + self.i ** 2)
