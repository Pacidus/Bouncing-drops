# -*- coding: utf-8 -*-

import numpy as np;
import matplotlib;
import matplotlib.pyplot as plt;
from matplotlib import rc
from scipy.optimize import curve_fit

rc('font',**{'family':'serif','serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

matplotlib.rcParams['text.usetex'] = True;
matplotlib.rcParams['text.latex.unicode'] = True;

load = np.loadtxt;

plot = plt.plot;

error = plt.errorbar;

xlabel = plt.xlabel;

ylabel = plt.ylabel;

show = plt.show;

set_xlabel = plt.xlabel;

set_ylabel = plt.ylabel;

grid = plt.grid;

Data = load("./lambda_yohan.txt");

X	= Data[:,1];
Y	= Data[:,0];
X_error	= Data[:,2];

def func(x):
	DPI = 2*np.pi;
	g = 9.81;
	Lambda = x*10**-3;
	rho = 950;
	sig = 20.7*10**-3;
	return((2/DPI)*np.sqrt((DPI*g/Lambda)+((sig*(DPI**3)))/(rho*Lambda**3)));

#popt, pcov = curve_fit(func, X, Y,bounds=(0, 1));

#print(*popt,"+-",*pcov[0]);

x = np.linspace(4,19.5,1000);
y = func(x);

set_ylabel(r'Fréquence en Hz', fontsize=12)

set_xlabel(r'${\lambda_F}$ en mm', fontsize=12)

error(X, Y, xerr=X_error, fmt='.', ecolor='red',color='blue', capsize=2.5);

grid(True);

plt.savefig('lambda_fexp.png', dpi=700);

plt.plot(x,y,"k--", label = r'$\frac{1}{\pi}\sqrt{}$');

plt.savefig('lambda_fth.png', dpi=700);

show();
