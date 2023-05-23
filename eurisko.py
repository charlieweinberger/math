import math
import numpy as np

def calc_pinv(x, y):

    x_trans = x.transpose()
    x_trans_x = np.matmul(x_trans, x)
    x_trans_x_inv = np.linalg.inv(x_trans_x)
    pinv = np.matmul(x_trans_x_inv, x_trans)
    b = np.matmul(pinv, y)

    print(f"\nX^T = \n{x_trans}")
    print(f"\nX^T * X = \n{x_trans_x}")
    print(f"\n(X^T * X)^(-1) = \n{x_trans_x_inv}")
    print(f"\n(X^T * X)^(-1) * X^T = \n{pinv}")
    print(f"\n(X^T * X)^(-1) * X^T * y = \n{b}")

y = np.array([
    [math.log(1)],
    [math.log(5)],
    [math.log(3)]
])

x = np.array([
    [1, math.log(1)],
    [1, math.log(2)],
    [1, math.log(4)]
])

calc_pinv(x, y)