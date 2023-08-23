import math
import numpy as np

xi = 0.01
xf = 2.0
e = math.e


def func(x):
    return (450/x)*(((1+x)**80) - 1) - 75000


for i in np.arange(xi, xf+0.01, 0.01):
    # print("fx0 = {}, fx1 = {}".format(func(i), func(i+1)))
    if func(i) < 0 < func(i + 0.01):
        x1 = i
        x0 = i + 0.01


ite = 0
x2a = x1
while True:

    fx0 = round(func(x0), 4)
    fx1 = round(func(x1), 4)
    x2 = round(x1 - ((fx1*(x0-x1))/(fx0-fx1)), 4)

    er = abs(x2-x2a)/x2
    x2a = x2
    print("i = {}, x0 = {}, x1 = {}, fx0 = {}, fx1 = {}, x2 = {}, er = {}".format(ite, x0, x1, fx0, fx1, x2, er))
    x0 = x1
    x1 = x2
    ite = ite + 1
    if abs(er) < 0.001:
        break

print("Tasa de interés = {}".format(x2))
print("Cuenta: {}".format(func(x2)+75000))