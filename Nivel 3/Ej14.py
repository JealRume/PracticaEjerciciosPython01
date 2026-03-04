#Ejercicio 14
while True:
    try:
        TMP = float(input("Temperatura:"))
        if TMP<15:
            print ("Está haciendo frío")
        else:  
            print ("Está haciendo calor")
        break 
    except ValueError:
        print("Error: Por favor ingrese un número válido para la temperatura.")

