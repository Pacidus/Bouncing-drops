# -*- coding: utf-8 -*-

import numpy as np;
import matplotlib;
import matplotlib.pyplot as plt;
from matplotlib import rc
import pandas as pd
import seaborn as sns

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

Data = load("./Radius.txt");

X = Data[:];

sns.distplot(X, norm_hist=True ,bins=40,kde=False);
sns.kdeplot(X, bw=.05, shade=True, color="orange");
#plt.axvline(x=3.65175);
#plt.axvline(x=8.32);

x = [3.65,4,5,6,7,8,8.32,9];

plt.xticks(x,rotation=45)

set_xlabel(r'Diamètre en mm', fontsize=12)
#set_ylabel(r'Accélération en ${\gamma_m/g}$', fontsize=12)

grid(True);

plt.savefig('Radius.png', dpi=700);
show();
