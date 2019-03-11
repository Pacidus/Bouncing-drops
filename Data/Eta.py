"""Code pour etalonner (Et) les valeurs de l'accélération (a) envoyées par la carte Arduino."""

import numpy as np						####################
import os							# Nos importations #
import tkinter as tk						####################
from tkinter.filedialog import askopenfilename

def ask():
	root = tk.Tk();
	root.withdraw();
	
	print("Donées de références :");
	Ref = askopenfilename();
	print(Ref)

	print("Donées à étalonner :");
	Input = askopenfilename();
	print(Input)
	
	name = Input.split("/")[-1];
	name = name.split(".")[0];
	
	print("Sortie :");
	Chemin = Input.split("/");
	del Chemin[-1];
	chemin = "/".join(Chemin);
	Output = chemin+"/Out_"+name+".eta";
	
	print(Output);
	
	return((Ref,Input,Output));
	
def f1(chemin):
	try:
		Ndata = np.loadtxt(chemin);
	except ValueError as err:
		n = int(str(err).split(" ")[-1]);
		if n <= 3:
			n -= 1;		
		print("Erreur ligne ",n);
		Rexclude(n,chemin);
		return((False,True));
	return((Ndata,False));

def Rexclude(n,chemin):
	fichier = open(chemin,"r");
	
	N = 0;
	
	contenu = "";
	
	for ligne in fichier:
		N+=1;
		if not(N == n):
			contenu += str(ligne);
			
	fichier.close();
	
	fichier = open(chemin, 'w');
	fichier.write(contenu);
	fichier.close();
	
def Error(chemin):
	error = True;
	while error:
		data,error = f1(chemin);
	return(data);
	
def eta(Data,RData):
	Byte = Data[:,1:];
	RByte = Rdata[:,1:];

	Bg = RByte.mean(0);

	Bg -= 1024/2;
	Byte -= 1024/2;

	Vecg = np.linalg.norm(Bg);
	Axyz = ((Byte - Bg)/Vecg);
	Uz = (Bg/Vecg);

	Data[:,1:] = Axyz;

	Az = Uz.dot(Axyz.T);

	Data = np.vstack([Data.T,Az]).T;
	return(Data);

def Analyse(Nlyse):
	P = np.prod(Nlyse.shape)//15;
	Val = 0;
	Val2 = 0;

	for i in range(P):
		val = np.max(Nlyse[i*15:(i+1)*15]);
		Val += val;
		Val2 += val*val;
	s = (Val2/P)-((Val/P)*(Val/P));
	s = np.sqrt(s);
	return((Val/P,s));

Ref,Input,Output = ask();
Data = Error(Input);
Rdata = Error(Ref);
Data = eta(Data,Rdata);
np.savetxt(Output, Data);
Az = Data[:,4]	
Nlyse = np.abs(Az)[900:];
Moy,sig = Analyse(Nlyse);

print("\nMoyenne:",str(Moy)+"g")
print("incertitude:","±"+str(sig)+"g")
