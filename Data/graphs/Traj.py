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

start = 15;

X1	= Data[start:,1];
Y1	= Data[start:,2];

plot(X1,Y1,'-o');


Data = load("./953G2");

X2	= Data[start:,1];
Y2	= Data[start:,2];

plot(X2,Y2,'-o');

plot((X2+X1)/2,(Y2+Y1)/2,'k-', label = "Centre de masse");

set_xlabel(r'x en mm', fontsize=12);
set_ylabel(r'y en mm', fontsize=12);

plt.legend();
grid(True);
plt.savefig('Traj1.png', dpi=700);

show();

X = X1-X2;
Y = Y1-Y2;
R = np.sqrt(X*X+Y*Y);
T = Data[start:,0];
T -= T[0]; 

plot(T,R,'-x');

set_xlabel(r'Temps en s', fontsize=12);
set_ylabel(r'Diamètre en mm', fontsize=12);
grid(True);
plt.savefig('Distraj1.png', dpi=700);

show();
##########################

T,X1,Y1 = load("./954G1", unpack = True);

plot(X1,Y1,'-o');


T, X2, Y2 = load("./954G2", unpack = True);

plot(X2,Y2,'-o');

set_xlabel(r'x en mm', fontsize=12);
set_ylabel(r'y en mm', fontsize=12);

plt.legend();
grid(True);

plt.savefig('Traj2.png', dpi=700);

show();

X = X1-X2;
Y = Y1-Y2;
R = np.sqrt(X*X+Y*Y);
T -= T[0]; 
grid(True);
plot(T,R,'-x');

set_xlabel(r'Temps en s', fontsize=12);
set_ylabel(r'Diamètre en mm', fontsize=12);
plt.legend();
plt.savefig('Distraj2.png', dpi=700);

show();

i = 15;
f = 200;

plot(X1[i:f],Y1[i:f],'-o');
plot(X2[i:f],Y2[i:f],'-o');

plot((X2[i:f]+X1[i:f])/2,(Y2[i:f]+Y1[i:f])/2,'k-', label = "Centre de masse");

set_xlabel(r'x en mm', fontsize=12);
set_ylabel(r'y en mm', fontsize=12);
grid(True);
plt.savefig('Trot.png', dpi=700);
show();
plt.legend();
plot(T[i:f]-T[i],R[i:f],'-x');

set_xlabel(r'Temps en s', fontsize=12);
set_ylabel(r'Diamètre en mm', fontsize=12);
grid(True);
plt.savefig('Distrot.png', dpi=700);
show();

i = -50;
f = -1;

plot(X1[i:f],Y1[i:f],'-o');
plot(X2[i:f],Y2[i:f],'-o');

plot((X2[i:f]+X1[i:f])/2,(Y2[i:f]+Y1[i:f])/2,'k-', label = "Centre de masse");

set_xlabel(r'x en mm', fontsize=12);
set_ylabel(r'y en mm', fontsize=12);
grid(True);
plt.legend();
plt.savefig('Straj.png', dpi=700);
show();

plot(T[i:f]-T[i],R[i:f],'-x');

set_xlabel(r'Temps en s', fontsize=12);
set_ylabel(r'Diamètre en mm', fontsize=12);
grid(True);
plt.savefig('Distraj.png', dpi=700);
show();
