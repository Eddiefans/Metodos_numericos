def fx(y, z):
    return (8 + y - 3*z)/12

def fy(x, z):
    return (-51 - x + 4*z)/7

def fz(x, y):
    return (62 -4*x + 4*y)/9


x, y, z, i = 0, 0, 0, 0

print("\n\nMétodo de Jacobi")
while True:
    xa = x
    ya = y
    za = z
    print("Iteración = {}, x = {}, y = {}, z = {}".format(i, x, y, z))
    
    x = round(fx(ya, za), 4)
    y = round(fy(xa, za), 4)
    z = round(fz(xa, ya), 4)
    
    erx = abs(x-xa)/x
    ery = abs(y-ya)/y
    erz = abs(z-za)/z
    
    i += 1
    
    if (erx < 0.003) and (ery < 0.003) and (erz < 0.003):
        break
    
    
print("Iteración = {}, x = {}, y = {}, z = {}".format(i, x, y, z))
print("Errores: x = {}, y = {}, z = {}".format(erx, ery, erz))


x, y, z, i = 0, 0, 0, 0

print("\n\nMétodo de Gauss-Seidel")
while True:
    xa = x
    ya = y
    za = z
    print("Iteración = {}, x = {}, y = {}, z = {}".format(i, x, y, z))
    
    x = round(fx(ya, za), 4)
    y = round(fy(x, za), 4)
    z = round(fz(x, y), 4)
    
    erx = abs(x-xa)/x
    ery = abs(y-ya)/y
    erz = abs(z-za)/z
    
    i += 1
    
    if (erx < 0.003) and (ery < 0.003) and (erz < 0.003):
        break
    
    
print("Iteración = {}, x = {}, y = {}, z = {}".format(i, x, y, z))
print("Errores: x = {}, y = {}, z = {}".format(erx, ery, erz))