import numpy as np
import matplotlib.pyplot as pl
X = [1,2,3,4,5]
Y = [1,4,9,16,25]
pl.plot(X, Y)
pl.title('Grafica2')
pl.xlabel('anios')
pl.ylabel('novios y mascotas')
pl.savefig('temp.png')
pl.show()
