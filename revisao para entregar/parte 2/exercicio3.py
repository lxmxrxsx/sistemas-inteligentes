import numpy as np
from numpy.random import randint
from exercicio1 import Quadrado, Triangulo
from exercicio2 import Circulo

objs = []

for i in range(20):
    objs.append(Quadrado(randint(1, 10)))

for i in range(20):
    objs.append(Triangulo(randint(1, 10), randint(1, 10)))

for i in range(20):
    objs.append(Circulo(randint(1, 10)))


def getObjsFill():
    objs = []

    for i in range(20):
        objs.append(Quadrado(randint(1, 10)))

    for i in range(20):
        objs.append(Triangulo(randint(1, 10), randint(1, 10)))

    for i in range(20):
        objs.append(Circulo(randint(1, 10)))

    return objs
