import matplotlib.pyplot as plt
import numpy as np
#creamos el vetor
x = np.arange(-5,5,0.05)
y = np.cos(x)
plt.plot(x,y,color="#ff0000")
#plt.grid(True)
plt.axhline(0)
plt.axvline(0)
plt.show()