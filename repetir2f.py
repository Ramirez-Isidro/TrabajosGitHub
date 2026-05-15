numero = int(input("ingresar numero: "))
contador = 0
for i in range(1 , numero + 1):
    dato = numero % i
    if dato == 0:
        contador = contador + 1
if contador == 2:
    print("el numero es primo")
else:
    print("el numero no es primo")