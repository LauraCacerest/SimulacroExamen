# Escriba el codigo necesario para que al ejecutar python ejercicio2.py
# se cree una grafica con una funcion sinusoidal entre 0 y 2pi.

import numpy as np
import matplotlib.pyplot as plt 


x=np.linspace(0.0,2*np.pi)
y=np.sin(x)

plt.plot(x,y)
plt.show 



