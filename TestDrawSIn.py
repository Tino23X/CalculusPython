import numpy as np
import matplotlib.pyplot as plt

x = np.array(np.linspace(-2*np.pi, 2*np.pi, 100))
y =  np.cos(x)

plt.figure(figsize=(5, 5))


plt.plot(x, y)

plt.axvline(x=0, linestyle='--')
plt.axhline(y=0, linestyle='--')

plt.show()