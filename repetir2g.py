numero = int(input("igresar numero mistico: "))
suma = 0
for i in range (1 , numero):
    dato = numero % i
    if dato == 0:
        suma = suma + i
if suma == numero :
    print("el numero es perfecto")
else:
    print("el numero no es perfecto")