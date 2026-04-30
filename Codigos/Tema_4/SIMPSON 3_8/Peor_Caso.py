import numpy as np
f=lambda x:np.sin(15*x)

a,b,n=0,3,3
h=(b-a)/n
x=np.linspace(a,b,n+1)
y=f(x)

S=(3*h/8)*(y[0]+3*y[1]+3*y[2]+y[3])
print(S)