import numpy as np
f=lambda x:np.sin(10*x)

a,b,n=0,2*np.pi,4
h=(b-a)/n
x=np.linspace(a,b,n+1)
y=f(x)

T=(h/2)*(y[0]+2*sum(y[1:-1])+y[-1])
print(T)