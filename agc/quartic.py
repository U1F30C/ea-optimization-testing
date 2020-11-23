
import math

class Quartic:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    RANGE = MAX_VALUE - MIN_VALUE

    def __init__(self):
        pass

    def f(self, chromosome):
        z = 0
        i = 1
        for allel in chromosome:
            z += i*allel**4
            i += 1
        return -z
