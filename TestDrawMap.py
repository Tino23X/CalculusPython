import numpy as np
import matplotlib.pyplot as plt

x = np.array(np.arange(-10, 10, 0.1))
y =  x**2

plt.figure(figsize=(5, 5))
plt.plot(x, y)
plt.show()