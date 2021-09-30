from matrix import *
import math

# fix, expand to more matrices

def unit_of(elem, mod, operation):
        
    if type(elem) == list:
        matrix = Matrix(elem)
        elem = matrix.determinant()
    
    return math.gcd(elem, mod) == 1

for i in [[[3, 1], [1, 2]], [[math.sqrt(2), 1], [2, math.sqrt(2)]], [[0.5, -3], [-1, 6]]]:
    print(unit_of(i, 26, '+'))