import math

from number import *


class Fraction(Number):
    def __init__(self):
        self.numerator = 0
        self.denominator = 0

    def read(self, array, i):
        self.numerator = int(array[i])
        self.denominator = int(array[i + 1])
        i += 2
        return i

    def __str__(self):
        return f'Fraction: numerator = {self.numerator}, denominator = {self.denominator}\n' \
               f'Real: {self.to_real()}'

    def to_real(self):
        return self.numerator / self.denominator