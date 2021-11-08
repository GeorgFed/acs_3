import math
import random

from number import *


class Fraction(Number):
    def __init__(self):
        self.numerator = 0
        self.denominator = 0

    def read(self, array):
        self.numerator = int(array[0])
        self.denominator = int(array[1])
        return self

    def generate(self):
        self.numerator = random.randint(0, 10000)
        self.denominator = random.randint(0, 10000)
        return self

    def raw(self):
        return f'1 {self.numerator} {self.denominator}'

    def __str__(self):
        return f'Fraction: numerator = {self.numerator}, denominator = {self.denominator}\n' \
               f'Real: {self.to_real()}'

    def to_real(self):
        return self.numerator / self.denominator
