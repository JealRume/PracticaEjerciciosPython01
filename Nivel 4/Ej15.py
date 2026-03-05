#ejercicio 15
while True:
    try:
        SM = float(input("Ingrese su salario mensual: "))

        if SM < 1500000:
            print("Usted no paga impuestos")
            print ("su impuesto es: ", SM*0)
            print ("Su salario es:", SM-0)

        elif SM >= 1500000 and SM < 3000000:
            print("Usted paga", SM * 0.05)
            print ("su impuesto es: ", SM*0.05)
            print ("Su salario es:", SM-(SM*0.05))

        elif SM >= 3000000:
             print ("usted paga impuestos")
             print ("su impuesto es:", SM*0.10)
             print ("su salario es:", SM-(SM*0.10))


    except ValueError:
              print ("Error: Por favor ingrese un número válido para el salario mensual:")
        