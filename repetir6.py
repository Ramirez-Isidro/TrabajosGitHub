mayor = None
while True:
    numero = int(input("Ingresá un número positivo (negativo para terminar): "))
    if numero < 0:
        break
    if mayor is None or numero > mayor:
        mayor = numero
if mayor is not None:
    print("El número máximo ingresado fue:", mayor)
else:
    print("No se ingresaron números positivos.")