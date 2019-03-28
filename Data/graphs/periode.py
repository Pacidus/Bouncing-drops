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
X_error	= Data[:,1];
Y	= Data[:,2];
Y_error	= Data[:,3];

def func(x,a,b):
	return(a*x+b);

popt, pcov = curve_fit(func, X, Y, sigma = Y_error);
perr = np.sqrt(np.diag(pcov));

print(*popt,"+-",*perr)
x = np.linspace(0,X.max()+1,1000);
y = func(x,*popt);

set_ylabel(r'Période en s', fontsize=12)

set_xlabel(r'Diamètre en mm', fontsize=12)

error(X, Y, yerr=Y_error,xerr=X_error, fmt='.', ecolor='red',color='blue', capsize=2.5);

grid(True);

plt.savefig('period.png', dpi=700);

plt.plot(x,y,"gray",label=r"~\\ $a = %.3f \pm %.3f $ \\ $b = %.3f \pm %.3f$ \\$f(x) = a \times x + b$" %(popt[0],perr[0],popt[1],perr[1]));
error(X, Y, xerr=X_error, fmt='.', ecolor='red',color='blue', capsize=2.5);
plt.legend();
plt.savefig('period_fth.png', dpi=700);
show();
