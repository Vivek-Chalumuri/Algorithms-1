from math import *

def Karatsuba_Mult(X,Y):
	if X < 10 or Y < 10:
		return X*Y
	
	Base = 10
	
	n = max(len(str(X)),len(str(Y)))
	
	if n % 2 != 0:
		n -= 1
	
	m = n/2
	
	a , b = divmod(X,Base**m)
	c , d = divmod(Y,Base**m)
	
	ac = Karatsuba_Mult(a,c)
	bd = Karatsuba_Mult(b,d)
	k = Karatsuba_Mult(a+b,c+d) - ac - bd
	
	return (10**n * ac) + (10**m * k) + bd
