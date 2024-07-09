from math import sin
def integralRiemman(a,b,f,n):
	area = 0
	h = (b - a)/n

	for i in range(n):
		area += f(a+i*h)*h
	return area

f = lambda x: sin(x)

a = 0
b = 1
n = 4

print(integralRiemman(a,b,f,n))