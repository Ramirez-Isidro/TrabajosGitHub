clave_correcta = "1234"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    clave = input("Ingresa clave de acceso: ")

    if clave == clave_correcta:
        print("Acceso correcto")
        break
    else:
        intentos += 1
        print(f"Clave incorrecta. Intento {intentos} de {max_intentos}")

if intentos == max_intentos:
    print("Tarjeta bloqueada")