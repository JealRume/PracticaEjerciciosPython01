# Ejercicio 1

while True:
    try:
        name = input ("Username:")
        print (f"Hola, {name} Welcome!")

    except ValueError: 
        print ("Error: Por favor ingrese un nombre válido:")    
    