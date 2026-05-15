nota = float(input("ingresar nota: "))
while nota < 1 or nota > 10:
    nota= float(input("ingresar nota valida: "))
if nota > 6:
    print("el alumno esta aprobado.")
else:
    print("el alumno esta desaprobado.")