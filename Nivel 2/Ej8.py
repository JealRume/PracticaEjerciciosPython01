# Ejercicio 8
while True:
    try:
        NT1 = float(input ("Nota1:"))
        NT2 = float(input ("Nota2:"))
        NT3 = float(input ("Nota3:"))
        print ("El promedio es:", (NT1 + NT2 + NT3) / 3)
    except ValueError:
        print ("Error: Por favor ingrese números válidos:") 

