from os import system
system('pip install sympy')
import sympy
from sympy import *
import math

def normal_vector_of_level_curve(f, init):
    g_x_point = diff(f, x).subs(x, init[0]).subs(y, init[1])
    g_y_point = diff(f, y).subs(x, init[0]).subs(y, init[1])
    mag = math.sqrt(g_x_point ** 2 + g_y_point ** 2)
    return [mag, g_x_point, g_y_point]

def normal_vector_of_level_surface(f, init):
    g_x_point = diff(f, x).subs(x, init[0]).subs(y, init[1]).subs(z, init[2])
    g_y_point = diff(f, y).subs(x, init[0]).subs(y, init[1]).subs(z, init[2])
    g_z_point = diff(f, z).subs(x, init[0]).subs(y, init[1]).subs(z, init[2])
    return [g_x_point, g_y_point, g_z_point]

def eqn_of_normal_line_of_curve(f, init):
    mag, g_x_point, g_y_point = normal_vector_of_level_curve(f, init)
    x1, y1 = sympy.Symbol('x1'), sympy.Symbol('y1')
    solve_for_x = solve(g_y_point * (x1 - init[0]) - g_x_point * (y1 - init[1]), x1)
    solve_for_y = solve(g_y_point * (x1 - init[0]) - g_x_point * (y1 - init[1]), y1)
    return solve_for_x, solve_for_y

def eqn_of_normal_line_of_surface(f, init):
    g_x_point, g_y_point, g_z_point = normal_vector_of_level_surface(f, init)
    x1, y1, z1 = sympy.Symbol('x1'), sympy.Symbol('y1'), sympy.Symbol('z1')
    return [[x1 - init[0], g_x_point], [y1 - init[1], g_y_point], [z1 - init[2], g_z_point]]

x, y, z = sympy.Symbol('x'), sympy.Symbol('y'), sympy.Symbol('z')

f = x**2 + ((y**2) / 9) + ((z**2) / 4) - 1
init = [0, 0, 2]

print(eqn_of_normal_line_of_surface(f, init))