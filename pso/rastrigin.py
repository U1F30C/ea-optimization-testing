
import math

class Rastrigin:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    RANGE = MAX_VALUE - MIN_VALUE

    def __init__(self):
        pass

    def f(self, chromosome):
        z = chromosome.size * 10
        for allel in chromosome:
            z += (allel**2-10*math.cos(2*math.pi*allel))
        return -z
