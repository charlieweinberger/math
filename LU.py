from matrix import *

def get_lu(a):

    u = a.rref(half=True)
    
    for i in range(-20, 20):
        for j in range(-20, 20):
            for k in range(-20, 20):
                l = Matrix([[1, 0, 0], [i, 1, 0], [j, k, 1]])
                lu = l.matrix_multiply(u)
                if a.elements == lu.elements:
                    # print('l:', l.elements)
                    # print('u:', u.elements)
                    return l, u

def get(matrix, col_num, row_num):
    l, u = get_lu(matrix)
    return {'l': l.elements[col_num-1][row_num-1], 'u': u.elements[col_num-1][row_num-1]}

matrix = Matrix([[-2, 3, 8], [0, 1, 2], [0, 6, 9]])
l, u = get_lu(matrix)
ans = get(matrix, 3, 2)['l'] * get(matrix, 3, 3)['u']
print(ans)