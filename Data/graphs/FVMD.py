# -*- coding: utf-8 -*-

import numpy as np;
import matplotlib;
import matplotlib.pyplot as plt;
from matplotlib import rc

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

Data = load("./Frontièremort.txt");

X	= Data[:,0];
X_error	= Data[:,1];
Y	= Data[:,2];
Y_error	= Data[:,3];
error(X, Y, xerr=X_error, yerr=Y_error, fmt='.', ecolor='red',color='blue', capsize=2.5);

Data = load("./FrontièreSD.txt");

X	= Data[:,0];
X_error	= Data[:,1];
Y	= Data[:,2];
Y_error	= Data[:,3];
error(X, Y, xerr=X_error, yerr=Y_error, fmt='x', ecolor='gray',color='black', capsize=2.5);


set_xlabel(r'Accélération en ${\gamma_m/g}$', fontsize=12);
set_ylabel(r'Diamètre en mm', fontsize=12);


grid(True);
plt.savefig('Frontière.png', dpi=700);
show();
