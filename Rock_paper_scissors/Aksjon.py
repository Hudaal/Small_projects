"""Aksjons metoder, overloading"""

class Aksjon:
    def __init__(self, val):
        if isinstance(val, str):
            val = {'Stein': 0, 'Saks': 1, 'Papir': 2}[val]
        assert isinstance(val, int) & (val >= 0) & (val < 3)
        self.value = val

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return (3 + other.value - self.value) % 3 == 1

    def __str__(self):
        return {0: "Stein", 1: "Saks", 2: "Papir"}[self.value]
