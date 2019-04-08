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

Data = load("./953G1");

X	= Data[:,1];
Y	= Data[:,2];

plot(X,Y);


Data = load("./953G2");

X	= Data[:,1];
Y	= Data[:,2];

plot(X,Y);

set_xlabel(r'x en mm', fontsize=12);
set_ylabel(r'y en mm', fontsize=12);

#plt.legend();
grid(True);
plt.savefig('Traj1.png', dpi=700);
show();
