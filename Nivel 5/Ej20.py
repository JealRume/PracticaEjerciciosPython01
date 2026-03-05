#Ejercicio 20
while True:
    try:
        Edad = int(input("Ingrese Edad:"))
        Estrato = int(input("Ingrese Estrato:"))
        if Edad > 18 and Edad <= 25 and Estrato  < 4:
            print ("Aplica para subsidio")
        else:
            print ("No aplica para subsidio")
    except ValueError:
        print("Por favor ingrese valores numéricos válidos.")
