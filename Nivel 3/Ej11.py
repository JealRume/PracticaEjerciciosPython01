# Ejercicio 11
while True:
    try: 
        nota = int(input("Digite su nota:"))
        if   nota>= 60:
            print("El estudiante aprobó")
        else: 
            print ("El estudiante No aprobó")
        break
    except ValueError:
        print("Error: Por favor ingrese un número entero para la nota.")

