import random

class Unfair():
    def __init__(self):
        self._value = 0

    def random(self):
        self._value += 1
        return random.randint(1,self._value)
