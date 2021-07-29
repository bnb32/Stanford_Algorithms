def mult(a,b):

    if (a<10) or (b<10):
        return a*b
    else:
        
        N=min((len(str(a)),len(str(b))))
        M=N//2
        
        a1 = int(str(a)[0:-M])
        a0 = int(str(a)[-M:])
        b1 = int(str(b)[0:-M])
        b0 = int(str(b)[-M:])

        z0 = mult(a0,b0)
        z2 = mult(a1,b1)
        z1 = mult((a1+a0),(b1+b0))
        
        return (z2*10**(2*M))+((z1-z2-z0)*10**M)+z0

a=3141592653589793238462643383279502884197169399375105820974944592
b=2718281828459045235360287471352662497757247093699959574966967627

print(mult(a,b))
