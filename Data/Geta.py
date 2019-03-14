"""Code pour obtenir (Get) les valeurs de l'accélération (a) envoyées par la carte Arduino."""

import serial						####################
from time import time					# Nos importations #
							####################

def Read():
	serial_port = '/dev/ttyACM0';			#Le port sur lequel est branchée l'Arduino
	baud_rate = 115200; 				#Dans le code arduino, Serial.begin(baud_rate)
	ser = serial.Serial(serial_port, baud_rate);	#ser est le port série

	print("Prise de donées : \n Nom du fichier");	##############################################
	write_to_file_path = str(input())+".txt";	# On récupère le chemin et le nom du fichier #
	output_file = open(write_to_file_path, "w+");	##############################################

	data = [];					#liste des donées
	times = [];					#liste du temps
	
	Apdata = data.append;				#fonction append in data
	Aptimes = times.append;				#fonction append in times
	
	Sread = ser.readline;				#fonction serial read line
	
	print("Temps de captation (en secondes)");	##################################################
	Dt = float(input());				# On recupère le temps de prise de donées voulue # 
	t0 = time();					##################################################
	tmax = t0+Dt;
	fline = time();
	while fline < tmax:				#Pour la periode voulue 
		fline = time();				#On récupère la valeur du temps
		Apdata(Sread());			#On stocke les valeurs envoyées par l'arduino
		Aptimes(fline);				#On stocke la valeur du temps

	n = 0;						#On initialise le nombre d'erreur à 0
	Wrinfile = output_file.write;			#fonction write in file
	
	for i in range(len(data)):			#Pour toutes les valeurs stockées
		try:					#On essaie (il peut y avoir des erreurs)
			val = data[i].decode("utf-8");	#On decode la valeur binaire de data -> str 
			dt = str(times[i]-t0);		#On calcul la valeur du temps écoulé à cet instant
			Wrinfile(dt+" "+val);		#On l'écrit dans le fichier
		except:					#Si il y as une erreur
			n += 1;				#On rajoute +1 à notre compteur
			
	print("Nombre d'erreur : "+str(n));		#On print le nombre d'erreur 

	f = (len(times)-n)/(times[-1]-times[0]);	#On calcul la fréquence
	pms = str(1000/f);				#On calcul la periode en ms

	print(f," Hz -> "+pms+" ms");			#On affiche la fréquence d'aquisition et la periode
	return();

Read();							#On lance le code
