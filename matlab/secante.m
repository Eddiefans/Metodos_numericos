function secante

M = ["Iteración" "X0" "f(X0)" "x1" "f(X1)" "X2" "Error"];
y = input("Ingresa tu función a resolver:","s")
x0 = input("Ingresa tu valor de x0:")
x1 = input("Ingresa tu valor de x1:")
Erel = input("Ingres el error que quieres alcanzar:")
iteracion = 0;
error_calculado = 1;
N(1,1)= iteracion;
N(1,2) = x0;
N(1,4)= x1;

x=N(1,2);
Z = eval(y);
N(1,3)=Z;

x=N(1,4);
Z = eval(y);
N(1,5)=Z;

x2 = N(1,4)-(N(1,5)*(N(1,2)-N(1,4)))/(N(1,3)-N(1,5));
N(1,6)= x2;
N(1,7)= error_calculado


i = 2;
while error_calculado > Erel
iteracion = iteracion + 1;
N(i,1) = iteracion;

N(i,2) = N(i-1,4);
x = N(i,2);
Z = eval(y);
N(i,3)=Z;

N(i,4) = N(i-1,6);
x = N(i,4);
Z = eval(y);
N(i,5)=Z;

x2 = N(i,4)-(N(i,5)*(N(i,2)-N(i,4)))/(N(i,3)-N(i,5));
N(i,6)= x2;

error_calculado = abs((N(i,6)-N(i-1,6))/N(i,6));
N(i,7) = error_calculado

i = i+1
end

disp(M)
disp(N)



end