total = int(input("ingresar monto de su plan: "))
cuotas = int(input("ingresar cantidad de cuotas: "))
if cuotas < 1 or cuotas > 12:
    print("el numero de cuotas de estar entre 1 y 12.")
else:
    
    # Bucle del 1 al 12
    for i in range(1, cuotas+1):
        dato = total / cuotas
        print(f"cuota numero {i} = {dato}")
