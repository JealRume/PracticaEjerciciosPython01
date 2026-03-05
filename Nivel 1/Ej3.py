# Ejercicio 3
while True:
     try:
          name2 = input ("User2:")
          age = input ("Age:")
          print (f"Your name is {name2} and you are {age} years old")
          
     
     except ValueError: 
          print ("Error: Por favor ingrese un nombre y una edad válidos:")