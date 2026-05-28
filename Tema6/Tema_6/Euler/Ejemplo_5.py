def euler(f,x0,y0,h,n):

    x=x0
    y=y0

    for i in range(n):

        y=y+h*f(x,y)
        x=x+h

        print(x,y)

euler(lambda x,y:x**2+y,0,0,0.2,3)
