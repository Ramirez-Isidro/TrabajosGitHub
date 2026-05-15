equipoA = int(input("goles del primer equipo: "))
equipoB = int(input("goles del segundo equipo: "))
if equipoA == equipoB:
    print("no hay difencia de goles")
else:
    if equipoA > equipoB:
        goles1 = equipoA - equipoB
        print("difencia de goles:",goles1)
    else:
        goles2 = equipoB - equipoA
        print("difencia de goles:",goles2)
