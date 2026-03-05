# Ejercicio 18
while True:
        try: 
                ancho = float(input("Ingrese el ancho del cuarto:"))
                largo = float(input("Ingrese el largo del cuarto:"))
                Area = ancho * largo
                if Area < 12:
                 print (f"El area del cuarto es, {Area}cm así que este es pequeño")
                elif Area == 12 and Area < 20:
                 print (f"El area del cuarto es, {Area}cm así que este es mediano")
                else:
                 print (f"El area del cuarto es, {Area}cm así que este es grande")

        except ValueError:
                print("Por favor ingrese valores numéricos válidos.")
     