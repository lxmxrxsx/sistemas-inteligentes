import numpy as np

columns = np.array([[0], [1], [2], [3], [4]])
lines = np.array([np.arange(100)])

c = columns.dot(lines)
print(lines)
print(columns)
print(c)
