import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

Data = "output1.txt"
XY = np.loadtxt(Data)

X = XY[::,0]
Y = XY[::,4]

def func(x,a, c):
	return 100000000000*a*np.cos(80*2*3.14*x + 0.1*c)

plt.plot(X, Y, 'b-', label='data')

popt, pcov = curve_fit(func, X, Y)
plt.plot(X, func(X, *popt), 'r-',label='fit: a=%f,c=%f' % tuple(popt))
plt.legend()
plt.show()


