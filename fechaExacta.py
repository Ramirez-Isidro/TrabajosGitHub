actualidad = int(input("ingrese fecha actual, todo junto y sin simbolos de pormedio: "))
año_actual = actualidad // 10000
resto_1 = actualidad % 10000
mes_actual = resto_1 // 100
dia_actual = resto_1 % 100
nacimiento = int(input("ingrese fecha de nacimiento, todo junto y sin simbolos de pormedio: "))
año_nacimiento = nacimiento // 10000
resto_2 = nacimiento % 10000
mes_nacimiento = resto_2 // 100
dia_nacimiento = resto_2 % 100
edad1 = año_actual - año_nacimiento
if mes_nacimiento == mes_actual:
    if dia_actual >= dia_nacimiento:
        print("aca estoy viendo q pasa:",edad1)
    else:
         edad1 = edad1 -1
         print("tu edad es:",edad1)         
else:
    if mes_nacimiento > mes_actual:
        print("es correcto")
    else: 
        print("ano menos",edad1)
    

