from random import randrange, uniform
import random
from math import exp

def NumAleatorio2():
    aleatorio = random.uniform(0,1)
    return (aleatorio)

def NumAleatorio():
    k = 2
    eps = 5
    e = 2.7182

    x = uniform(0, 180)
    x = x/1000

    y = (eps**k * x**(k-1) * e**(-eps * x)) / 1
    y = 2*y/3.65

    
    return(y)

NumAleatorio2()