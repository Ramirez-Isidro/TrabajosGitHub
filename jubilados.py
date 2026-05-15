precio = float(input("precio del medicamento: "))
edad = int(input("edad del cliente: "))
resta = 100 - 40
descuento = resta /100
total = precio * descuento 
if edad >= 65:
    print("total a pagar, descuento aplicado:",total)
else:
    print("total a pagar, sin descuento:",precio)