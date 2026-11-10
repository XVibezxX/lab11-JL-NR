import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Divide by zero")
    else:
        return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Arguments for logarithm must be positive")
    else:
        return math.log(a,b)

def exponent(a, b):
    return a ** b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return b/a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Arguments for logarithm must be positive")
    return math.log(b, a)

def exp(a, b):
    return a**b

def square_root(a):
    math.sqrt(a)
def hypotenuse(a, b):
    math.hypot(a, b)
