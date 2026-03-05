# Ejercicio 16  
while True:
    try:

         NT1 = float(input("ingrese 1N: "))
         NT2 = float(input("ingrese 2N: "))
         NT3 = float(input("ingrese 3N: "))

         prom = (NT1 + NT2 + NT3) / 3

         if prom >= 59:
            print("El estudiante aprobó con un promedio de", prom)
         elif prom < 56:
            print("El estudiante no aprobó con un promedio de", prom)
         else:
            print("El estudiante está en recuperación con un promedio de", prom)
    
    except ValueError:
             print("Error: Por favor ingrese un número válido para las notas.")
