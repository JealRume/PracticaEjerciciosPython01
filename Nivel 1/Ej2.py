# Ejercicio 2
while True: 
    try:
         city = input ("Ciudad de nacimiento:")
         print (f"Eres de: {city}")
        
    except ValueError: 
             print ("Error: Por favor ingrese una ciudad válida:")