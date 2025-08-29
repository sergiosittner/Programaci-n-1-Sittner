def mostrar_atracciones () ->int:
    atraccion=int(input("Zoologico [1]\nParque acuatico [2]\nPaseo de juegos [3]\nZona arcade [4]\nIngrese la atracción: "))
    return atraccion


def edad_minima(atraccion: int)->int:
    match atraccion:
        case 1:
            return 5
        case 2:
            return 12
        case 3:
            return 2
        case 4:
            return 15
        case _:
            print ("opción incorrecta")
    

def puede_subir (edad: int, edad_permitida:int)->bool:
    if edad >= edad_permitida:
        return True
    else:
        return False

def calcular_precio (atraccion1: int)->int:
    if atraccion1 == 1:
        return 1200
    elif atraccion1 == 2:
        return 1500
    elif atraccion1 == 3:
        return 300
    elif atraccion1 == 4:
        return 800


def registrar_visita (atraccion1: int, precio: int, puede_subir: int )->int:
    if puede_subir == True:
        if atraccion1 == 1:
            elegida = "Zoologico"
            if puede_subir == True:
                decision = int(input(f"usted cumple con la edad suficiente para el/la {elegida}, el valor por cada entrada es de {precio} pesos\n¿Cuantos boletos desea comprar? "))
                if decision >= 3:
                    precio_total = (precio * decision) * 0.90
                    return precio_total
                else:
                    precio_total = precio * decision
                    return precio_total

        elif atraccion1 == 2:
            elegida = "Parque acuatico"
            if puede_subir == True:
                decision = int(input(f"usted cumple con la edad suficiente para el/la {elegida}, el valor por cada entrada es de {precio} pesos\n¿Cuantos boletos desea comprar? "))
                if decision >= 3:
                    precio_total = (precio * decision) * 0.90
                    return precio_total
                else:
                    precio_total = precio * decision
                    return precio_total
            elif puede_subir == False:
                print("lo sentimos, no cumple con la edad suficiente para entrar en el/al {elegida}")

        elif atraccion1 == 3:
            elegida = "Paseo de juegos"
            if puede_subir == True:
                decision = int(input(f"usted cumple con la edad suficiente para el/la {elegida}, el valor por cada entrada es de {precio} pesos\n¿Cuantos boletos desea comprar? "))
                if decision >= 3:
                    precio_total = (precio * decision) * 0.90
                    return precio_total
                
                else:
                    precio_total = precio * decision
                    return precio_total

        elif atraccion1 == 4:
            elegida == "Zona arcade"
            if puede_subir == True:
                decision = int(input(f"usted cumple con la edad suficiente para el/la {elegida}, el valor por cada entrada es de {precio} pesos\n¿Cuantos boletos desea comprar? "))
                if decision >= 3:
                    precio_total = (precio * decision) * 0.90
                    return precio_total
                else:
                    precio_total = precio * decision
                    return precio_total




    
    