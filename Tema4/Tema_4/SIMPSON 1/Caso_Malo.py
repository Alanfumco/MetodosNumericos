import numpy as np
f=lambda x:np.log(x+1)

a,b,n=0,2,4
h=(b-a)/n
x=np.linspace(a,b,n+1)
y=f(x)

S=(h/3)*(y[0]+4*sum(y[1:-1:2])+2*sum(y[2:-2:2])+y[-1])
print(S)