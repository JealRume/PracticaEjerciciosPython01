#Ejercicio 19
while True: 
    try:
        User = input("usuario: ")
        Pass = input("contraseña: ") 
        if User == "admin" and Pass == "1234":
           print ("Welcome to the system!")
        else: 
           print ("Invalid username or password")
    except Exception as e:
        print ("Error:", e)