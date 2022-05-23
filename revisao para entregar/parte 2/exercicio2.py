import numpy as np


class Circulo:
    raio = 0

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return np.pi*(self.raio**2)
