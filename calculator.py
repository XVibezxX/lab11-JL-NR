import math
def square_root(a):
    math.sqrt(a)

def hypotenuse(a, b):
    math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Arguments for logarithm must be positive")
    else:
        return math.log(a,b)

def mul(a, b):
    return a*b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return b/a

def exp(a, b):
    return a**b
