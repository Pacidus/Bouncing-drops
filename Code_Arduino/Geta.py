##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed 
import serial
from time import time 

serial_port = '/dev/ttyACM0';
baud_rate = 115200; #In arduino, Serial.begin(baud_rate)
write_to_file_path = "output.txt";

output_file = open(write_to_file_path, "w+")
ser = serial.Serial(serial_port, baud_rate)
t0 = time()
while 1==1:
	line = ser.readline();
	fline = str(time() - t0)
	line = line.decode("utf-8") #ser.readline returns a binary, convert to string
	output_file.write(fline+" "+line);
