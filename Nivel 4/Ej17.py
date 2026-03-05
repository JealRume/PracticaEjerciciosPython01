#Ejercicio 17

while True:
    try:
        KMR = float(input("Kilometros rec:"))
        TIEMPO = float(input("cuanto tiempo se demoró en minutos:"))

        if TIEMPO < 10:
            print ("el valor de la carrera es 5000")
        else: 
            print ("el valor de la carrera es:", 800 * KMR)

    except ValueError:
        print("Error: Por favor ingrese un número válido.")
