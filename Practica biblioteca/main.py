titulos = [0]*2
ejemplares = [0]*2

libros = 0
salir = False 

while salir == False:
    print("////////////Menú principal////////////")
    print("1. Cargar Titulos y ejemplares")
    print("2. Mostrar Catalogo Completo")
    print("3. Consultar disponibilidad")
    print("4. Titulos Agotados")
    print("5. Agregar un nuevo titulo")
    print("6. actualizar ejemplares (préstamo/devolución)")
    print("7. Salir")

    opcion = input("Ingresar opción: ")

    if opcion == "1":
        for x in range(len(titulos)):
            titulos[x] = str(input("Ingrese el nombre del titulo: "))

        for x in range (len(ejemplares)):
            ejemplares[x] = int(input(f"Ingrese el numero de ejemplares de {titulos[x]}: "))
    
    
    elif opcion == "2":
        for x in range(len(titulos)):
            print (titulos[x])
                                       
    
    elif opcion == "3":
        for x in range(len(ejemplares)):
            print (f"{titulos[x]} tiene {ejemplares[x]} ejemplares")
    
    elif opcion == "4":
        agotados = False 
        for x in range(len(titulos)):
            if ejemplares[x] == 0:
                print(f"Titulos Agotados: {titulos[x]}")
                agotados = True
        if not agotados:
            print("No hay títulos agotados")

    elif opcion == "5":
        for x in range(len(titulos)):
            if titulos[x] == 0:
                titulos[x] = str(input("Ingrese el nuevo libro: "))
                ejemplares[x] = int(input("Ingrese su cantidad de copias: "))
                libros == False
                break
            else:
              print ("Se a excedido la maxima cantidad de ejemplares")
              break
    elif opcion == "6":
        act = input("Ingrese el título a actualizar: ")
        for x in range(len(titulos)):
            if titulos[x] == act:
                accion = input("Escriba 'p' para préstamo o 'd' para devolución: ")
                if accion == "p":
                    if ejemplares[x] > 0:
                        ejemplares[x] -= 1
                        print("Préstamo realizado.")
                    else:
                        print("No hay ejemplares disponibles.")
                elif accion == "d":
                    ejemplares[x] += 1
                    print("Devolución realizada.")
                break
        else:
            print("El título no existe")
    elif opcion == "7":
        salir = True
        print("Saliendo...")
    else:
        print("Opción invalida")