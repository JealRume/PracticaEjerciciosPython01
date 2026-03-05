# Ejercicio 6
while True:
    try:
         pp = int(input("Precio del producto:"))
         IVA = pp * 19/100
         print (f"El Iva es de: {IVA}")
         print (f"El precio del producto es:{pp + IVA}")


    except ValueError as e:
         print (f"Error: Por favor ingrese un precio válido: {e}")
