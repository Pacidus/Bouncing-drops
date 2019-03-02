#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
from struct import unpack
from time import time
import numpy as np

def Read():
	serial_port = '/dev/ttyACM0';
	baud_rate = 115200; #In arduino, Serial.begin(baud_rate)
	ser = serial.Serial(serial_port, baud_rate)

	print("Prise de donées : \n Nom du fichier")
	write_to_file_path = str(input())+".txt";
	output_file = open(write_to_file_path, "w+")

	data = []
	times = []
	
	Apdata = data.append
	Aptimes = times.append
	
	Sread = ser.readline
	print("temps de caption")
	Dt = float(input())
	fline = time()	
	t0 = time()
	tm = t0+Dt
	
	while fline < tm:
		fline = time()
		Apdata(Sread())
		Aptimes(fline)

	n = 0

	for i in range(len(data)):
		try:
			output_file.write(str(times[i]-t0)+" "+data[i].decode("utf-8"))
		except:
			n += 1
					
	print("Nombre d'erreur : "+str(n))

	print(str(len(times)/(times[-1]-times[0]))+" Hz -> "+str((times[-1]-times[0])*1000/len(times))+" ms")

	
Read()
