# https://github.com/nickdevito22/lab10-ND-CZ
# Partner 1: Nicholas Devito
# Partner 2: Cynthia Zhang

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid arguments for logarithm.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b
