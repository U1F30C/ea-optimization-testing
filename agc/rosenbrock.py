import math


class Rosenbrock:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    RANGE = MAX_VALUE - MIN_VALUE

    def __init__(self):
        pass

    def f(self, chromosome):
        z = 0
        i = 0
        while i < (chromosome.size - 1):
            allel = chromosome[i]
            secondAllel = chromosome[i + 1]
            z += (100 * (secondAllel - allel**2)**2 + (allel - 1)**2)
            i += 1
        return -z
