from enum import Enum


class NumberKey(Enum):
    COMPLEX = 0
    FRACTION = 1
    POLAR = 2


class Number:
    def __init__(self, key):
        self.key = key

    def read(self, array, i):
        pass

    def generate(self):
        pass

    def __str__(self):
        pass
