total = 0

precio = float(input("Ingrese el precio del producto (0 para cerrar caja): "))

while precio != 0:
    total += precio
    precio = float(input("Ingrese el precio del producto (0 para cerrar caja): "))

print("Total general de la venta:", total)