import numpy as np
import matplotlib.pyplot as plt
X = [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
Y = [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,3]
plt.plot(X, Y)
plt.grid(True)
plt.title('Grafica')
plt.xlabel('anios')
plt.ylabel('novios y mascotas')
plt.savefig('temp.png')
plt.show()
