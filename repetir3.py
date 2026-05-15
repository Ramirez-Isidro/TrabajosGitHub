numero = int(input("Ingresá un número del 1 al 10: "))

# Validar rango
if numero < 1 or numero > 10:
    print("El número debe estar entre 1 y 10.")
else:
    print(f"\nTabla del {numero}:\n")
    
    # Bucle del 1 al 10
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
