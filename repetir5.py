numero = int(input("ingresa tu numero: "))
if numero <= 0:
    print("el numero debe ser mayor a 0.")
else:
    for i in range(1, numero + 1 ):
        resto = i%2
        if resto == 0:
            print(i)
    