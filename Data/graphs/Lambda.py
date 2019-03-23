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

Data = load("./lambda_yohan.txt");

X	= Data[:,1];
Y	= Data[:,0];
X_error	= Data[:,2];

set_ylabel(r'Fréquence en Hz', fontsize=12)
set_xlabel(r'${F_\lambda}$ en mm', fontsize=12)

error(X, Y, xerr=X_error, fmt='.', ecolor='red',color='blue', capsize=2.5);

grid(True);
plt.savefig('lambda_f.png', dpi=700);

show();
