import math
import sympy as sp
X = sp.Symbol('x')

xi = 6
xf = 9
e = math.e

def func(x):
    return (math.pi/3)*(21*x**2-x**3) - 862.053

def func_(x):
    return sp.diff(func(X), X).subs(X, x)

for i in range(xi, xf+1):
    if func(i) < 0 < func(i + 1):
        x0 = i


ite = 0
x1a = x0
while True:

    fx0 = round(func(x0), 4)
    f_x0 = round(func_(x0), 4)
    x1 = round(x0 - (fx0/f_x0), 4)

    er = abs(x1-x1a)/x1
    x1a = x1
    print("i = {}, x0 = {}, fx0 = {}, f_x0 = {}, x1 = {}, er = {}".format(ite, x0, fx0, f_x0, x1, er))
    x0 = x1
    ite = ite + 1
    if er < 0.005:
        break

print("h = {}".format(x1))