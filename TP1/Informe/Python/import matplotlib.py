import matplotlib.pyplot as plt
import numpy as np

# Generar datos
x = np.logspace(0, 1, 10000)
y = (1/(1 + 0.9 * (1/(2*x)) - 0.02 * (1/(2*x))*(1/(2*x)))) * np.pi * np.pi * x 

# Graficar los datos
plt.plot(x, y) 

# Etiquetar los ejes
plt.xlabel('L/D')
plt.ylabel('Factor de nagaoka K')

# Mostrar la gráfica
plt.show()
