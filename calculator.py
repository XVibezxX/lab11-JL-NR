import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        return ZeroDivisionError
    else:
        return a / b

def logarithm(a, b):
    return math.log(a,b)

def exponent(a, b):
    return a ** b


