from os import system
system('pip install sympy')
import sympy
from sympy import *
import math

def first_few_terms(expr):

    string = ''
    for i in range(4):
        expr_i = expr.subs(n, i)
        diff = sympy.diff(expr_i)
        string += ' + ' + str(diff)

    return string[3:]

def general_term(expr):
    return sympy.diff(expr, x)

def radius_of_convergence(expr):
    expr_1 = expr.subs(n, n + 1)
    l = limit(expr_1 / expr, n, oo)
    return abs(solve(l - 1, x)[0])

x = sympy.Symbol('x')
n = sympy.Symbol('n')
expr = (2*x) ** n

print(radius_of_convergence(expr))