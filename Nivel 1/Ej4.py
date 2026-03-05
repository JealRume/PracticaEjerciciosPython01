# Ejercicio 4
while True:
    try:
        materia = input ("Materia fav:")
        print (f"Elegiste {materia} buena eleccion!")
    except ValueError:
        print ("Error: Por favor ingrese una materia válida:")  