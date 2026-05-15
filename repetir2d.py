numero = int(input("igresar numero mistico: "))
for i in range(1, 11):
        dato = numero % i
        if dato == 0:
                print(f"el numero {numero} es divisible por {i}")
