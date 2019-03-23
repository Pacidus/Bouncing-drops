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

Data = load("./fc.txt");

X	= Data[:,0];
Y	= Data[:,1];
Y_error	= Data[:,2];

set_xlabel(r'Fréquence en Hz', fontsize=12)
set_ylabel(r'Accélération en ${\gamma_m/g}$', fontsize=12)

error(X, Y, yerr=Y_error, fmt='.', ecolor='red',color='blue', capsize=2.5);

grid(True);
plt.savefig('faradsquare.png', dpi=700);

show();
