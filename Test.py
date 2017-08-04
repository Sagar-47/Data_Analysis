import pandas as pd
import array as arr
import numpy as np
import matplotlib.pyplot as plt
f=pd.read_table('Complete_TAVG_daily.txt', sep='\s+',comment='%')
#dt=np.dtype([])
#print(f)
ar=f.values 
#ar1=f.values['Anomaly']
#print ar1
tfix= lambda t : t + 8.68
vtfix=np.vectorize(tfix)
ncolumn = vtfix(ar[:,5])
reshapencolumn= np.reshape(ncolumn, (ncolumn.size,1))
fnew=np.append(ar,reshapencolumn,axis=1)
x=reshapencolumn
plt.xlabel('Temperature')
plt.ylabel('No. of days')
plt.title('Temperature Variaion of Entire set of Years')
plt.hist(fnew, bins=500, histtype='bar')
plt.show()