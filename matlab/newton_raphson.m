function newton_raphson

M = ["Iteracion" "x0" "f(x0)" "f'(x0)" "x2" "Err"]
y = input("Ingresa la funcion a resolver: ", "s")
derivada = input("Ingresa la derivada de esta función: ", "s")
x0 = input("Ingresa tu valor inicial: ")
Er = input("Ingresa el error que quieres alcanzar: ")
iter = 0

N(1,1) = iter;
N(1,2) = x0;

x = x0;
fx0 = eval(y);
dx0 = eval(derivada);
N(1,3) =fx0;
N(1,4) =dx0;

x1 = x0 - (fx0/dx0);
N(1,5) = x1;

N(1,6) = 1;

N(1,1) = iter;
error = 1;
i = 1;

while error>Er
    iter = iter + 1;
    x0 = N(i,5);

    x = x0;
    fx0 = eval(y);
    dx0 = eval(derivada);

    x1 = x0 - (fx0/dx0);
    error = abs((x1 - x0)/x1);
    
    N(i+1,1) = iter;
    N(i+1,2) = x0;
    N(i+1,3) = fx0;
    N(i+1,4) = dx0;
    N(i+1,5) = x1;
    N(i+1,6) = error;

    i = i+1;
end

disp(M)
disp(N)

end