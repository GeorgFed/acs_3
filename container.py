from complex import *
from polar import *
from fraction import *


class Container:
    def __init__(self):
        self.storage = []

    def __str__(self):
        result = ['Container:', f'Number of elements: {len(self.storage)}', 'Elements:']
        for i in range(len(self.storage)):
            result.append(f'{i}: {str(self.storage[i])}')
        return '\n'.join(result)

    def generate_test(self):
        result = []
        for number in self.storage:
            result.append(number.raw())
        return '\n'.join(result)

    def print(self):
        print(str(self))

    def test_write(self, filename: str):
        with open(file=filename, mode='w') as file:
            file.write(self.generate_test())

    def write(self, filename: str):
        with open(file=filename, mode='w') as file:
            file.write(str(self))

    def generate(self, amount):
        for i in range(amount):
            if i % 3 == 0:
                self.generate_polar()
            elif i % 3 == 1:
                self.generate_complex()
            else:
                self.generate_fraction()

    def read(self, filepath: str):
        with open(file=filepath, mode='r') as file:
            while True:
                line = file.readline()
                print(line)
                if not line:
                    return
                if line[0] == '0':
                    self.add_complex(line[1:])
                if line[0] == '1':
                    self.add_fraction(line[1:])
                if line[0] == '2':
                    self.add_polar(line[1:])

    def add_polar(self, line: str):
        polar = Polar()
        self.storage.append(polar.read(line.split()))

    def generate_polar(self):
        polar = Polar()
        self.storage.append(polar.generate())

    def add_complex(self, line: str):
        complex_number = Complex()
        self.storage.append(complex_number.read(line.split()))

    def generate_complex(self):
        complex_number = Complex()
        self.storage.append(complex_number.generate())

    def add_fraction(self, line: str):
        fraction = Fraction()
        self.storage.append(fraction.read(line.split()))

    def generate_fraction(self):
        fraction = Fraction()
        self.storage.append(fraction.generate())

    def sort(self):
        for i in range(len(self.storage) - 1):
            max_index = i
            for j in range(i + 1, len(self.storage)):
                if self.storage[j].to_real() > self.storage[max_index].to_real():
                    max_index = j
            self.storage[max_index], self.storage[i] = self.storage[i], self.storage[max_index]
