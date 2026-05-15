contador = 0
contador2 = 0
for i in range (1 , 101):
    contador = 0
    for j in range(1 , i + 1):
        dato = i % j
        if dato == 0:
            contador = contador + 1
    if contador == 2:
        contador2 = contador2 +1
print("total de primos:", contador2)
