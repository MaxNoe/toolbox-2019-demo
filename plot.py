import matplotlib.pyplot as pyplot
import numpy as np

x = np.linspace(0, 1, 100)
plt.plot(x, np.sin(x))
plt.savefig('test.pdf')