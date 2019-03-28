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

Data = load("./rayons_yohan.txt");

X1	= Data[0::2,0];
Y1	= Data[0::2,1];
Y_error1= Data[0::2,2];
X2	= Data[1::2,0];
Y2	= Data[1::2,1];
Y_error2= Data[1::2,2];

def func(x,b):
	return(0*x+b);

popt1, pcov1 = curve_fit(func, X1, Y1, sigma = Y_error1);
perr1 = np.sqrt(np.diag(pcov1));
popt2, pcov2 = curve_fit(func, X2, Y2, sigma = Y_error2);
perr2 = np.sqrt(np.diag(pcov2));

print(*popt1,"+-",*perr1)
x = np.linspace(0,8,1000);
y1 = func(x,*popt1);
y2 = func(x,*popt2);

set_ylabel(r'Diamètre des orbites en mm', fontsize=12)

set_xlabel(r'Mesure n°', fontsize=12)

error(X1, Y1, yerr=Y_error1, fmt='.', ecolor='red',color='blue', capsize=2.5);
error(X2, Y2, yerr=Y_error2, fmt='.', ecolor='red',color='blue', capsize=2.5);

plt.plot(x,y1,"--",label=r"$d_1 = %.3f \pm %.3f $" %(popt1[0],perr1[0]));
plt.plot(x,y2,"--",label=r"$d_2 = %.3f \pm %.3f $" %(popt2[0],perr2[0]));

plt.legend();
grid(True);

plt.savefig('rayon.png', dpi=700);
show();

