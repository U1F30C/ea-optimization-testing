class Sphere:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    RANGE = MAX_VALUE - MIN_VALUE
    def __init__(self):
        pass
    def f(self, chromosome):
        z = 0
        for allel in chromosome:
            z += allel**2
        return -z
