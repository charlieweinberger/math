from matrix import *

def dot_product(m1, m2): # only works for 1 vector
    dot_product = 0
    for index in range(len(m1)):
        dot_product += m1[index] * m2[index]
    return dot_product

def belongs_to_orthogonal_components(h, to_test):
    for test in to_test:
        if dot_product(test, h) == 0:
            print(to_test.index(test) + 1)    

def orthogonal_components(h): # doesnt work for some reason
    matrix = Matrix(h)
    new_matrix = matrix.transpose().rref()
    new_matrix.transpose()
    print(new_matrix.elements)

def add_sets(a, b):
    return [a[i] + b[i] for i in range(len(a))]

def set_scalar_mult(scalar, a):
    return [scalar * a[i] for i in range(len(a))]

matrix = Matrix([[1, -2, 0], [0, -2, 1], [0, 0, -1]])
matrix_2 = Matrix([[0, -6, 0], [6, 0, 0], [-2, 1, 0], [0, -1, 2]])
print(matrix_2.matrix_multiply(matrix).elements)