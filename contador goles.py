contador = 0
inicio = input("¿Empezó el partido? (si/no): ")
if inicio == "si":
    partido_en_curso = True
    print("Sistema de goles activo. (Escribe 'gol' para sumar o 'fin' para terminar)")

    while partido_en_curso:
        accion = input("¿Qué sucedió? (gol / nada / fin): ")
        if accion == "gol":
            contador += 1
            print(f"¡GOOOOL! Marcador actual: {contador}")
        
        elif accion == "fin":
            partido_en_curso = False
        else:
            print(f"El juego sigue... Marcador: {contador}")

    print("---")
    print(f"PARTIDO FINALIZADO. Resultado total: {contador} goles.")

else:
    print("Esperando a que empiece el partido...")