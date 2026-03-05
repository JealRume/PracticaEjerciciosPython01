# Ejercicio 5
while True:
    try:
        nm1 = int(input ("#1:"))
        nm2 = int(input ("#2:"))
        print ("la suma es:",{nm1 + nm2})
        print ("la resta es:",{nm1 - nm2})
        print ("la multiplicacion es:",{nm1 * nm2})
        print ("la division es:",{nm1 / nm2})
    except ValueError:
        print ("Error: Por favor ingrese números válidos:")