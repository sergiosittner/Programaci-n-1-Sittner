from paquete.edad import verificar_acceso as verif
edad = int(input("ingrese su edad: "))
acceso1 = verif(edad)
if acceso1 == True:
    print("usted es mayor de edad")
if acceso1 == False:
    print("usted es menor de edad")
