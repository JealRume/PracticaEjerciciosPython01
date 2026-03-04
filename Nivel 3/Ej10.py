while True:
    try:
        Age = int(input("Edad usuario:"))
        if Age >= 18:
            print("El usuario es mayor de edad")
        else:
            print("El usuario es menor de edad")
        break
    except ValueError:
        print("Error: Por favor ingrese un número entero para la edad.")
