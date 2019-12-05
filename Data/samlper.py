from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# ell1 = Ellipse(xy = (0.0, 0.0), width = 4, height = 8, angle = 30.0, facecolor= 'yellow', alpha=0.3)
r = 2
cir1 = Circle(xy = (0.0, 0.0), radius=r, alpha=0.5)
# ax.add_patch(ell1)
ax.add_patch(cir1)

x, y = 0, 0
ax.plot(x, y, 'ro')

plt.axis('scaled')

plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length


import numpy as np
for i in range(500):
    ratio = np.random.random() * 360.0
    dis = (np.random.random()*(r**2))**(1/2)
    x = np.cos(ratio)*dis
    y = np.sin(ratio)*dis
    plt.scatter(x,y)


plt.show()