import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(0, 10, 0.5)
y = np.arange(0, 10, 0.5)
z1 = np.power(x, 0.25) + np.power(y, 0.25)
z2 = np.power(x, 2) - np.power(y, 2)
z3 = 2 * x + 3 * y
z4 = np.power(x, 2) + np.power(y, 2)
z5 = 2 + 2 * x + 2 * y - np.power(x, 2) - np.power(y, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z1, label='z1')
ax.plot(x, y, z2, label='z2')
ax.plot(x, y, z3, label='z3')
ax.plot(x, y, z4, label='z4')
ax.plot(x, y, z5, label='z5')
ax.set_xlabel('x')
ax.set_xlabel('y')
ax.set_xlabel('z')
plt.legend()
plt.show()
