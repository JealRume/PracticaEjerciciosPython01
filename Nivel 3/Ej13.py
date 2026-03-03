# Ejercicio 13
PP = int(input("Precio del producto:"))
D10 = PP * 10/100
if PP > 100000: 
 print("El descuento es de:", D10)
 print("EL precio total es de:", PP - D10)
       
else:
 print("El descuento es de:", 0)
 print("EL precio total es de:", PP)
 