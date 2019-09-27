import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
plt.plot(x, np.sin(x), 'r', label='sin')
plt.plot(x, np.cos(x), 'b', label='cos')
plt.legend()
plt.savefig('test.pdf')
