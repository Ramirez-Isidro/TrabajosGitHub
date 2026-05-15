# Pedir cantidad de notas
cantidad = int(input("¿Cuántas notas querés cargar?: "))

suma = 0

# Validación básica
if cantidad <= 0:
    print("La cantidad debe ser mayor a 0.")
else:
    # Bucle para cargar notas
    for i in range(1, cantidad + 1 ):
        nota = float(input(f"Ingresá la nota {i}: "))
        suma += nota

    # Calcular promedio
    promedio = suma / cantidad

    print(f"\nEl promedio es: {promedio}")