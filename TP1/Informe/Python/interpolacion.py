# Interpolacion polinomica de curva k de nagaoka, eje x es l/D e y es k


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos
x = np.array([0.35, 0.4, 0.55, 1 ,1.5,2 , 3 ])
y = np.array([1.55, 1.95, 3, 6.75, 11, 15.1, 25])

# Interpolacion lineal
f = interp1d(x, y, kind='linear')


# Grafico
xnew = np.linspace(0.35, 3, num=1000, endpoint=True)
plt.plot(x, y, 'o', xnew, f(xnew), '-')
plt.legend(['Datos', 'Interpolacion'], loc='best')
plt.xlabel('l/D')
plt.ylabel('k')
plt.title('Interpolacion polinomica de curva k de nagaoka')
plt.grid()

plt.show()


