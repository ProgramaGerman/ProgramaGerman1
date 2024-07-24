from math import sin, cos
from src.Taylor import taylor_polynomial
from src.Taylor2 import polinomio_taylor
from src.Intregral_Riemman import integralRiemman
from src.IntegralTrapecio import Integraltrapecio
from src.newtonRaphson import newtonRapshon,df
from src.biseccion import biseccion


def test_biseccion():
    #Prueba del metodo de Biseccion
    a = 1
    b = 0
    Es = 0.002
    Ni = 8
    func = lambda x: sin(x)-x
    resultado = biseccion(func,a,b,Es,Ni)



def test_newton_raphson():
    #Prueba del metodo de newton Raphson
    func = lambda x: pow(x,2)
    xo = 2
    Er = 0.002 
    N = 4
    resultado = newtonRapshon(func,df,xo,Er,N)
    assert resultado



#Polinomio de Taylor
def test_taylor():
    #Primera forma 
    y = lambda x: pow(x,2) + cos(x)  # Puedes cambiar esta función por la que desees
    x0 = 0  # Punto alrededor del cual se expande el polinomio
    grado = 5  # Grado del polinomio de Taylor

    taylor = polinomio_taylor(y, x0, grado)
    assert taylor



def test_taylor2():
    #Segunda forma mas, solo que mas corta
    y = lambda x: pow(x,2) + cos(x)
    resultado = taylor_polynomial(y,0,3)


def test_Integral_Riemman():
    #Integracion por el metodo de Riemman
    f = lambda x: sin(x)
    a = 0
    b = 1
    n = 4
    resultado = integralRiemman(a,b,f,n)
    assert resultado


def test_integral_trapecio():
    #Integracion por el metodo del Trapecio
    f = lambda x: sin(x) + 1
    a = 0
    b = 1
    n = 4
    resultado = Integraltrapecio(f,a,b,n)
    assert resultado
    
    