from matplotlib import pyplot as mp
from array import array
import numpy as np
a=input("Enter parameter A : ")
x=0.1#input("Enter initial condition : ")
n=input("Enter no. of iterations : ")
i=0
j=0
ar = []
ar1 = []
ar2=[]
ar3=[]
def Lm(i,a,x,n,j) :
	#for i in range(100):
	while(i<=1):	
		y = a*i*(1-i)
		ar.append(y)
		ar1.append(i)
		x=y
		i=i+0.005
	while(j<=1):	
		a = j
		ar2.append(a)
		ar3.append(j)
		j=j+0.005
	mp.plot(ar1,ar)
	mp.plot(ar2,ar3)
	mp.show()
Lm(i,a,x,n,j)
