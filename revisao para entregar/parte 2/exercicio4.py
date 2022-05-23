import numpy as np
from numpy.random import shuffle
from exercicio3 import getObjsFill

objs = getObjsFill()

shuffle(objs)

soma = np.sum([obj.area() for obj in objs])

print(soma)
