import numpy as np

filename = "Etalonnage.txt"
output = "output.txt"
Output = "output1.txt"

data = np.loadtxt(filename)
Data = np.loadtxt(output)

Byte = data[:,1:]
DByte = Data[:,1:]

MByte = Byte.mean(0)

MByte -= 1023/2
DByte -= 1023/2

DByte = (DByte / np.linalg.norm(MByte))*-9.81

Data[:,1:] = DByte

np.savetxt(Output, Data)
