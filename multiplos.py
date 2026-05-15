n1 = int(input("ingrese un numero: "))
n2 = int(input("ingrese otro numero: "))
resto = n1 % n2
if resto == 0:
    print("los numeros son multiplos")
else:
    print("los numeros no son multiplos")