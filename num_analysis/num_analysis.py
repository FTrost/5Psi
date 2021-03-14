import numpy as np

f = open("efield.t", "r")
#arr = np.array(f.read())

x = list(f.read())

#print(f.read())
#print(arr)
#print(arr.dtype)
print(x)

data = np.array(x, dtype=np.float)

#print(arr)

#x = np.loadtxt('efield.t')

f.close()
