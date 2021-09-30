from os import system
system('pip install sympy')
import sympy
from sympy import *
import math

# E[a] = a
# E[a * X] = a * E[X]

# Var[a] = 0
# Var[X] = E[X^2] - E[X]^2
# Var[a * (X^b)] = (a^b) * Var[X^b]

def expected_value(functions, n):
    ans = 0
    for f, bounds in functions:
        ans += integrate((x**n) * f, (x, bounds[0], bounds[1]))
    return ans

def variance(functions):
    return expected_value(functions, 2) - expected_value(functions, 1) ** 2

def variance_with_pdf(functions, e_x):
    return round(expected_value(functions, 2) - e_x ** 2, 2)

def variance_transformed(functions, e_x):
    return expected_value(functions, 4) - e_x ** 2

x = Symbol('x')

functions = [
    [2 * x / 3, [1, 2]]
]

print(4 * variance_transformed(functions, 5/2))