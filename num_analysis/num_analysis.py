import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read in data
df = pd.read_csv('efield.t', delim_whitespace=True)

# plot data; first entire data set, then without time values
df.plot()
df.iloc[:,1:].plot()

# delete columns 'x' and 'z'
x = df[df.columns].var() > 0.0001
df = df[df.columns[x]]

# calculate fft of column 'y'
f = np.fft.fft(df['y'])
f = f.real

print(f)


#plt.show()
plt.figure()
plt.plot(f, label='FFT of y')
plt.legend()

#plt.show()

plt.savefig("fft.pdf")
