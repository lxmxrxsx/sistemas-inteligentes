import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-5, 5, 100)
y = 1.0 / (1.0 + np.exp(-x))


plt.plot(x, y)
plt.show()
