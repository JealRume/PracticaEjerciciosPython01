# Ejercicio 9
while True:
    try:
        AC = float(input("Ingrese el radio de circuito:"))
        Area = (AC * AC * 3.1416)
        print ("El area del ciurcuito es:", {Area})
    except ValueError:
        print ("Error: Por favor ingrese un número válido:")
