import numpy as np
import glob
import os

def f1(File):
	try:
		Ndata = np.loadtxt(File)
	except ValueError as err:
		contenu = ""
		Ndata = 0	
		print(int(str(err).split(" ")[-1]))
		n = int(str(err).split(" ")[-1])
		if n <= 3:
			n -= 1
		fichier = open(File,"r")
		N = 0
		for ligne in fichier:
			N+=1
			if not(N == n):
				contenu = contenu + str(ligne)
		fichier.close()
		fichier = open(File, 'w')
		fichier.write(contenu)
		fichier.close()
		return((Ndata,True))
		
	return((Ndata,False))
print("fichier")
fichier = "./"+str(input())
filename = fichier+"/Etalonnage.txt"
print("Etalonnage des données : \n Nom du fichier")
name = str(input())
Input = fichier+"/"+name+".txt"
Output = fichier+"/Out_"+name+".txt"

bol = True

while bol:
	out = f1(Input)
	Data,bol = out

bol = True

while bol:
	out = f1(filename)
	data,bol = out

Data = np.loadtxt(Input)

Byte = data[:,1:]
DByte = Data[:,1:]

MByte = Byte.mean(0)

MByte -= 1024/2
DByte -= 1024/2
Norm = np.linalg.norm(MByte)
DByte = ((DByte - MByte)/Norm)
MByte = (MByte/Norm)
Data[:,1:] = DByte

new = MByte.dot(DByte.T)

Data = np.vstack([Data.T,new]).T

np.savetxt(Output, Data)

Nlyse = (new^2)^(1/2)[900:]

P = 950*9/15
I = 0
Val = 0
Val2 = 0

for i in range(P):
	I += 1
	val = Nlyse[i*15:(i+1)*15].max()
	Val += val
	Val2 += val*val

print("Moyenne: "+str(Val/I)+"/n")
print("Incertitude: "+str((sqrt((Val*Val)-Val2))/I)+"/n")
