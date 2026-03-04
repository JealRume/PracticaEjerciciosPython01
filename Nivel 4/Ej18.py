while True: 
    try:
        ancho = float(input("Ancho:"))
        largo = float(input("Largo:"))
        if ancho > largo:
            Area = ancho * largo
        