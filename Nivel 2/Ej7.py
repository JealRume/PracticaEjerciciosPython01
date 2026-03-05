# Ejercicio 7
while True:
    try:
        HTS = int(input ("Horas Trabajadas:"))
        SPH = int(input ("Salario por hora:"))
        print ("La ganancia semanal es de:", {HTS * SPH})
    except ValueError:
        print ("Error: Por favor ingrese números válidos:")
