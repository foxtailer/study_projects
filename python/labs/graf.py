'''
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(10, 0, -0.1)
plt.plot(x, x**2 +7)
plt.show()
'''
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, np.sin(x), x, np.cos(x), x, -x, x, x**2)
plt.grid(True)
plt.show()
"""
'''
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
t = np.arange(-10, 11, 1)

 #subplot 1
sp = plt.subplot(221)
plt.plot(x, np.sin(x))
plt.title(r'$\sin(x)$')
plt.grid(True)

#subplot 2
sp = plt.subplot(222)
plt.plot(x, np.cos(x), 'g')
plt.axis('equal')
plt.grid(True)
plt.title(r'$\cos(x)$')

#subplot 3
sp = plt.subplot(223)
plt.plot(x, x**2, t, t**2, 'ro')
plt.title(r'$x^2$')

#subplot 4
sp = plt.subplot(224)
plt.plot(x, x)
sp.spines['left'].set_position('center')
sp.spines['bottom'].set_position('center')
plt.title(r'$x$')

plt.show()

'''

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
ax = axes3d.Axes3D(plt.figure())
i = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(i, i)
Z = X**2 - Y**2
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
plt.show()
