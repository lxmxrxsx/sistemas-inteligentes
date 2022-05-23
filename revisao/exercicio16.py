import numpy as np


def replaceEvenNumbers(list):
    print(list)


list = np.array([1, 2, 3, 4, 5, 6, 7, 8])
list = np.where(list % 2 == 0, -1, list)
print(list)
