def ingresar_precios():
    """Se encarga exclusivamente de la recolección de datos de la caja."""
    total = 0
    while True:
        precio = float(input("Ingrese el precio del producto (0 para cerrar caja): "))
        if precio == 0:
            break
        total += precio
    return total

def calcular_iva(subtotal, iva_ingresado):
    """Función pura: solo calcula. No sabe qué es una consola, un input o un print."""
    return subtotal + (subtotal * iva_ingresado / 100)

# PROGRAMA:

# 1. total de la caja
subtotal = ingresar_precios()
print(f"Subtotal acumulado: ${subtotal:.2f}")

# 2. IVA 
iva_ingresado = float(input("Ingrese el porcentaje de IVA (ejemplo: 21 para 21%): "))

# 3. Calculo del total usando la función 
total_final = calcular_iva(subtotal, iva_ingresado)

# 4. resultado final
print(f"Total con IVA: ${total_final:.2f}")