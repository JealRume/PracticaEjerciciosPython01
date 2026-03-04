# Ejercicio 12
while True:
    try:
        nm1 = float(input("n1:"))
        nm2 = float(input("n2:"))

        if nm1 > nm2:
            print("El mayor es el primer numero")
        elif nm2 > nm1:
            print("El mayor es el segundo numero")
        else:
            print("Los dos numeros son iguales")
        break
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

    
    
