import numpy
from numpy import array, linalg

terms = 2

while True:
    n = 5
    x1 = [0.25, 0.75, 1.25, 1.5, 2]
    fx = [-0.23, -0.33, 0.7, 1.88, 6]


    x2 = list(map(lambda x: pow(x, 2), x1))
    xfx = [x1[i] * fx[i] for i in range(len(x1))]
    y_ = sum(fx)/n

    a = array([[]])
    results = array([])
    for i in range(0, terms):
        if i == 0:
            a = numpy.append(a, [[n]], axis = 1)
            for j in range(0, terms-1):
                a = numpy.append(a, [[sum(list(map(lambda x: pow(x, j+1), x1)))]], axis = 1)
        else:
            aux = array([])
            for j in range(i, terms + i):
                aux = numpy.append(aux, [sum(list(map(lambda x: pow(x, j), x1)))])
            a = numpy.append(a, [aux], axis = 0)
        results = numpy.append(results, [sum([(x1[k]**i) * fx[k] for k in range(len(x1))])])

    a = linalg.solve(a, results)

    def y(a, xr):
        yr = 0
        for i in range(0, len(a)):
            yr = yr + round(a[i], 4)*(xr**i)

        return round(yr, 4)


    yt = ""
    for i in range(0, len(a)):
        if i == 0:
            yt = yt + str(round(a[i], 4))
        else:
            yt = yt + " + " + str(str(round(a[i], 4))) + "x^" + str(i)

    ynueva = []
    sr = []
    st = []
    for i in range(0, n):
        ynueva.append(y(a, x1[i]))
        sr.append(round((ynueva[-1]-fx[i])**2, 4))
        st.append(round((y_-fx[i])**2, 4))

    print("Terminos: {}".format(terms))
    print(yt)
    print("{:<5}| {:<5}| {:<6}| {:<7}| {:<7}| {:<7}| {:<6}".format("x", "f(x)", "x^2", "f(x)x", "ynueva", "sr", "st"))
    for i in range(0, n):
        print("{:<5} {:<6} {:<7} {:<8} {:<8} {:<8} {:<7}".format(x1[i], fx[i], x2[i], xfx[i], ynueva[i], sr[i], st[i]))
    r = round(((abs(sum(st)-sum(sr))/sum(st))**(1/2))*100, 2)
    print("r = {}%".format(r))
    print("\n\n")
    if r > 90:
        break
    else:
        terms = terms + 1



