import pandas as pd
import numpy as np
data=pd.read_table('Complete_TAVG_daily.txt', sep='\s+', comment='%')
#print(data)
ar=data.values
tfix= lambda t : t+0.6
a=tfix(5)
i=1
r=0
d=0
while i>0:
	if r==6:
		d=r
	if d!=0:
		print(d)
		break
	r=r+1
 

