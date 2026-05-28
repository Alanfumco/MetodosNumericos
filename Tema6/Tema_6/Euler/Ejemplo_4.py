def euler(f,x0,y0,h,n):

    x=x0
    y=y0

    for i in range(n):

        y=y+h*f(x,y)
        x=x+h

        print(x,y)

euler(lambda x,y:y-x**2,0,1,0.1,3)
