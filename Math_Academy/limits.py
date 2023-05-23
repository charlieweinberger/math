from os import system
system('pip install sympy')
import sympy
from sympy import *
import math

class Sigma:
    def __init__(self, low_board, high_bound, x, expression):
        self.low_board = low_board
        self.high_board = high_board
        self.x = x
        self.expression = expression
        self.state = None
        
def nth_term_test(x, expression):
    lim = limit(expression, x, oo)
    if lim != 0:
        return 'diverges'
    return 'no conclusion'

def integral_test(x, expression, bounds=(-oo, oo)):
    # If f(n) is a positive, continuous, and decreasing function for x >= 1
    integral = integrate(expression, (x, bounds[0], bounds[1]))
    if type(integral) in [sympy.core.numbers.NegativeInfinity, sympy.core.numbers.Infinity]:
        return 'diverges'
    return 'converges'

def test(x, expression):
    print(nth_term_test(x, expression))
    print(integral_test(x, expression))

x = symbols('x')
test(x, ((-1) ** x) / math.sqrt(x))

def p_series_test(p):
    if p > 1:
        print('series is convergent')
    else:
        print('series is divergent')

def comparison_test_for_convergence(a, b, expression_a, expression_b):
    
    # if expression_a > 0 and expression_b > 0 and if expression_a <= expression_b for all n:
    # n_val = 
    # a_n = expression_a.subs(n, n_val)
    # b_n = expression_b.subs(n, n_val)
    # if a_n > 0 and b_n > 0 and a_n <= b_n:

        # if expression_b converges:
            # expression_a converges
    pass

def comparison_test_for_divergence(n, expression_a, expression_b):
    # if expression_a > 0 and expression_b > 0 and if expression_a >= expression_b for all n:
    
    # n_val = 
    # a_n = expression_a.subs(n, n_val)
    # b_n = expression_b.subs(n, n_val)
    # if a_n > 0 and b_n > 0 and a_n >= b_n:

        # if expression_b diverges:
            # expression_a diverges
    pass

def limit_comparison_test(n, expression_a, expression_b):
    # if expression_a > 0 and expression_b > 0:
        lim = limit(expression_a / expression_b, n, oo)
        if lim > 0 and type(lim) != sympy.core.numbers.NegativeInfinity:
            print('a_n and b_n have same state')

# x = symbols('x')
# expression = sin(x)/x
# nth_term_test(x, expression)
# integral_test(x, expression, (-oo, 1))

# p_series_test(p)

# n = symbols('x')
# expression_a = sin(n)
# expression_b = sin(n)
# comparison_test_for_convergence(n, expression_a, expression_b)
# comparison_test_for_divergence(n, expression_a, expression_b)
# limit_comparison_test(n, expression_a, expression_b)
# limit_comparison_test(n, expression_a, expression_b)