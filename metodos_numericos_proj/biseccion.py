import math

xi = 0
xf = 5
e = math.e


def func(x):
    return x**2 + e**(2*x) - 4


for i in range(xi, xf+1):
    if func(i) < 0 < func(i + 1):
        x0 = i
        x1 = i + 1

xm = x1
ite = 0
while True:

    xma = xm
    xm = round((x0+x1)/2, 4)
    fxm = round(func(xm), 4)
    er = abs(xma-xm)/xm

    print("i = {}, x0 = {}, x1 = {}, xm = {}, fxm = {}, er = {}".format(ite, x0, x1, xm, fxm, er))
    if fxm > 0:
        x1 = xm
    else:
        x0 = xm
    ite = ite + 1
    if er < 0.0010:
        break

print("Coordenadas donde cortan:")
print("x = {}, y = {}".format(xm, e**(xm)))