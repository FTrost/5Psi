import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('efield.t', delim_whitespace=True)

x = df[df.columns].var() > 0.0001

df = df[df.columns[x]]

#print(df)

f = np.fft.fft(df['y'])

#print(f)

#plt.figure()
#df['y'].plot()
#f.plot()

plt.plot(f)

plt.show()
