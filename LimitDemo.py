import numpy as np
import matplotlib.pyplot as plt
import sympy

x = np.array(np.linspace(-100, 100, 10000))
y = np.cos(x)  x

plt.figure(figsize=(12, 3))


plt.plot(x, y)

plt.axvline(x=0, linestyle='--')
plt.axhline(y=0, linestyle='--')

plt.show()

x1 = sympy.Symbol('x')
y1 = sympy.sin(x1)/x1

r = sympy.limit(y1, x1, 'oo')
print(f"function {y1} the limit is {r}")