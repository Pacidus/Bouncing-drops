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

Data = load("./periode_yohan.txt");

X	= Data[:,0];
Y	= Data[:,2];
X_error	= Data[:,1];
Y_error	= Data[:,3];

def func(x,a):
	return(a*x);

popt, pcov = curve_fit(func, X, Y);

print(*popt,"+-",*pcov[0]);

x = np.linspace(0,X.max()+1,1000);
y = func(x,*popt);

set_ylabel(r'Période en s', fontsize=12)

set_xlabel(r'Diamètre en mm', fontsize=12)

error(X, Y, yerr=Y_error,xerr=X_error, fmt='.', ecolor='red',color='blue', capsize=2.5);

grid(True);

plt.savefig('period.png', dpi=700);

plt.plot(x,y,"gray");
error(X, Y, xerr=X_error, fmt='.', ecolor='red',color='blue', capsize=2.5);

plt.savefig('period_fth.png', dpi=700);

show();
