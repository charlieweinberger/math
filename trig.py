import math
from matrix import *

def image(v, rad):
    r = Matrix([[math.cos(rad), -math.sin(rad)], [math.sin(rad), math.cos(rad)]])
    return r.matrix_multiply(v).elements

v = Matrix([[-3], [-1]])
rad = -math.pi/3
img = image(v, rad)
print(img)