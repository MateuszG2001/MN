from math import *

def f1(x):
    #f(x) = x^11 + 4x^10 + 8x^9 - 6x^8 - 11x^7 + 24x^6 + 20x^5 - 28x^4 - 10x^3 + 10x^2 + 24x - 16
    return -16+x*(24+x*(10+x*(-10+x*(-28+x*(20+x*(24+x*(-11+x*(-6+x*(8+x*(4+x))))))))))

def f2(x):
    #f(x) = 9sin(2x) + 8sin(3x) - 7sin(4x) + 6cos(5x) - 5cos(6x) + 4cos(7x)
    return 9*sin(2*x)+8*sin(3*x)-7*sin(4*x)+6*cos(5*x)-5*cos(6*x)+4*cos(7*x)

def f3(x):
    # f(x) = 2^x +1
    return 2**x+1
