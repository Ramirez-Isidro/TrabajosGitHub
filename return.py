def aplicar_iva(precio_base):
    impuesto = precio_base * 0.21
    precio_final = precio_base + impuesto
    return precio_final # Devolvemos el total para usarlo afuera
monto = float(input("Ingrese el precio del producto: $"))
total_a_cobrar = aplicar_iva(monto)
print(f"El precio final con IVA es: ${total_a_cobrar:.2f}")